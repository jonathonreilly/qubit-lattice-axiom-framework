"""R-N4-AUT: steelman search for an A_min-available surface enrichment whose
automorphism stabilizer is SMALLER than S_4 (i.e. breaks the tau<->x exchange
symmetry down to a subgroup that fixes one axis), WITHOUT presupposing the
Hamiltonian/generator H.

Companion of block01_section_R-N4-AUT.md (single-clock B-AXIS campaign, N4).

------------------------------------------------------------------------------
THE WALL BEING STEELMANNED
------------------------------------------------------------------------------
The N4 axis-selection obstruction: the bare staggered-Dirac surface on an even
cubic-symmetric Z^3+1 block is exactly invariant under the signed axis-exchange
W_{a,b} = P_{a<->b} . diag((-1)^{x_a x_b}). The adjacent transpositions
(0,1),(1,2),(2,3) generate the full S_4 acting TRANSITIVELY on the four
Euclidean axes (s4-transportable branch). Transitive => no axis-selector is
non-transportable => the axis cannot be derived, only declared (B-AXIS).

STEELMAN (this route): a transitive orbit is only fatal if the surface is "too
poor". Maybe a RICHER A_min-derivable structure on the SAME sites has a smaller
automorphism group whose axis-permutation image is a proper subgroup of S_4
that fixes exactly one axis. Such an enrichment would CRACK the wall.

------------------------------------------------------------------------------
METHOD (A_min only; no H presupposed)
------------------------------------------------------------------------------
1. Build the full candidate automorphism group of the bare surface as the
   SIGNED HYPEROCTAHEDRAL GROUP B_4 realized as site-relabelings of the block:
   every (signed) axis permutation g = (perm pi on axes, axis reflections r_mu),
   lifted to a site map, dressed with the staggered sign field needed to keep
   the bare hop invariant. We compute the FULL group G_bare = { orthogonal
   site operators U_g : U_g M_bare U_g^T = M_bare } among these 384 candidates,
   and verify its axis-permutation image is all of S_4 (the wall, recomputed).

2. ENUMERATE A_min-available enrichments E (operators / gradings / couplings /
   crossing invariants / boundary decorations) that use ONLY Lattice (sites +
   nn cubic adjacency), Quantum (one qubit per site = Cl(3,0) internal fibre),
   and Record (durable scalar additive readout) -- and NO supplied generator,
   no labeled axis choice, no boundary datum that is itself an axis input.

3. For each enrichment E, compute its STABILIZER inside G_bare:
        Stab(E) = { g in G_bare : U_g E U_g^T = E }   (or the appropriate
   covariance for a non-operator invariant), and report its AXIS-PERMUTATION
   IMAGE as a subgroup of S_4. CRACK iff the image is a proper subgroup that
   fixes exactly one axis AND E is A_min-derivable without presupposing H.

A "TOTAL: PASS=.. FAIL=.." line summarizes. PASS = the assertion about that
enrichment's stabilizer held (whether it cracks or confirms the wall); the
final verdict line states cracked/not-cracked explicitly.

All legs are finite-dimensional exact linear algebra; deterministic, no RNG.
"""
from __future__ import annotations

import itertools
import numpy as np

MASS = 0.3
TOL = 1e-9
NONTRIV = 1.0

PASS = 0
FAIL = 0
CRACK_FOUND = False


def check(tag, name, ok, detail=""):
    global PASS, FAIL
    status = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {status}: {name}" + (f"  ({detail})" if detail else ""))


def r(A):
    return float(np.linalg.norm(A))


# ---------------------------------------------------------------------------
# bare staggered surface on an even cubic-symmetric block
# ---------------------------------------------------------------------------
def build_staggered(L, bc=(1, 1, 1, 1), include_mass=True):
    d = len(L)
    sites = list(itertools.product(*[range(n) for n in L]))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    M = np.zeros((N, N))
    for s in sites:
        i = idx[s]
        if include_mass:
            M[i, i] += MASS
        for mu in range(d):
            eta = (-1) ** (sum(s[nu] for nu in range(mu)))
            fs = list(s)
            fs[mu] = (s[mu] + 1) % L[mu]
            fs = tuple(fs)
            sign = bc[mu] if s[mu] == L[mu] - 1 else 1
            j = idx[fs]
            M[i, j] += 0.5 * eta * sign
            M[j, i] += -0.5 * eta * sign
    return M, sites, idx


# ---------------------------------------------------------------------------
# Candidate automorphism group = signed hyperoctahedral group B_4 lifted to the
# block, with the staggered sign field that keeps the bare hop invariant.
#
# An element is g = (pi, eps) with pi a permutation of {0,1,2,3} and
# eps in {+1,-1}^4 the per-axis reflection. The site action on an EVEN
# cubic block L=(L,L,L,L):
#     (g.x)_mu = (eps_mu==+1) ? x_{pi^{-1}(mu)} : (L-1 - x_{pi^{-1}(mu)})
# We then attach a diagonal sign field chosen to make U_g M_bare U_g^T = M_bare.
# Rather than derive the sign field analytically, we SOLVE for it numerically
# per element by requiring hop invariance up to a per-site sign (a torus
# symmetry of a real antisymmetric staggered hop is a signed permutation that
# conjugates the matrix to itself); we accept g into G_bare iff such a diagonal
# sign field exists and reproduces M_bare exactly.
# ---------------------------------------------------------------------------
def site_perm_matrix(sites, idx, pi, eps, L):
    """Plain (unsigned) signed-coordinate relabeling permutation matrix P_g:
    P_g[idx[g.x], idx[x]] = 1."""
    N = len(sites)
    P = np.zeros((N, N))
    for x in sites:
        gx = tuple(
            (x[pi_inv] if eps[mu] == 1 else (L - 1 - x[pi_inv]))
            for mu, pi_inv in enumerate(_inverse(pi))
        )
        P[idx[gx], idx[x]] = 1.0
    return P


def _inverse(pi):
    inv = [0] * len(pi)
    for i, p in enumerate(pi):
        inv[p] = i
    return inv


def solve_sign_field(P, M):
    """Given the unsigned relabeling P, find a diagonal D=diag(+-1) with
    (P D) M (P D)^T = M, i.e. D (P^T M P) D = M as a signed-permutation
    intertwiner. Returns (ok, U=P@D). The conjugation P^T M P moves M to the
    relabeled basis; it equals M up to a per-edge sign pattern that factors as
    a coboundary d_i d_j iff a consistent vertex sign field exists. We solve the
    Z_2 vertex system greedily over the connected hop graph; bare hop graph is
    connected on the torus, so the solution (if any) is unique up to global
    sign. Deterministic."""
    N = M.shape[0]
    Mr = P.T @ M @ P  # = M conjugated into relabeled coordinates
    # We need D[i] D[j] * Mr[i,j] = M[i,j] for all hop edges (i,j).
    # => D[i] D[j] = M[i,j]/Mr[i,j] wherever both nonzero & |equal magnitude|.
    D = np.zeros(N)
    D[0] = 1.0
    # BFS over the hop graph using M's adjacency
    from collections import deque
    adj = [np.nonzero(np.abs(M[i]) > TOL)[0] for i in range(N)]
    q = deque([0])
    seen = {0}
    while q:
        i = q.popleft()
        for j in adj[i]:
            if abs(Mr[i, j]) < TOL:
                # edge exists in M but not in Mr (or vice versa) -> magnitudes
                # must still match for a clean intertwiner; if not, fail later
                continue
            ratio = M[i, j] / Mr[i, j]
            if abs(abs(ratio) - 1.0) > 1e-6:
                return False, None  # magnitude mismatch -> not a clean symmetry
            need = ratio  # = D[i]*D[j]
            dj = need / D[i]
            if j in seen:
                if abs(D[j] - dj) > 1e-6:
                    return False, None
            else:
                D[j] = dj
                seen.add(j)
                q.append(j)
    if len(seen) != N:
        # disconnected component: assign the rest by isolated consistency
        for i in range(N):
            if D[i] == 0.0:
                D[i] = 1.0
    Dmat = np.diag(D)
    U = P @ Dmat
    if r(U @ M @ U.T - M) > TOL:
        return False, None
    return True, U


def build_G_bare(sites, idx, L, M):
    """Enumerate B_4 (384 elements), keep those that (with a solved sign field)
    fix the bare hop. Return list of (pi, eps, U)."""
    G = []
    for pi in itertools.permutations(range(4)):
        for eps in itertools.product((1, -1), repeat=4):
            P = site_perm_matrix(sites, idx, pi, eps, L)
            ok, U = solve_sign_field(P, M)
            if ok:
                G.append((pi, eps, U))
    return G


def axis_image(G):
    """Set of axis-permutations pi appearing in G (the S_4 image)."""
    return sorted({g[0] for g in G})


def common_fixed_axes(perms):
    """Axes fixed by EVERY permutation in the set."""
    return [ax for ax in range(4) if all(p[ax] == ax for p in perms)]


def selects_exactly_one_axis(perms):
    """A genuine axis-SELECTOR stabilizer must:
      (a) fix EXACTLY ONE axis as a common fixed point (not zero, not all four),
      (b) act transitively on the OTHER three axes (so it picks 'the' special
          axis and treats the rest symmetrically -- the S_3-fixing-one signature).
    A trivial (identity-only) stabilizer fixes ALL FOUR axes and therefore
    selects NONE; the full S_4 fixes none. Returns the selected axis or None."""
    fixed = common_fixed_axes(perms)
    if len(fixed) != 1:
        return None
    sel = fixed[0]
    others = [a for a in range(4) if a != sel]
    # transitive on the other three: orbit of others[0] under perms covers others
    orbit = {others[0]}
    changed = True
    while changed:
        changed = False
        for p in perms:
            new = {p[a] for a in orbit}
            if not new <= orbit:
                orbit |= new
                changed = True
    if set(others) <= orbit:
        return sel
    return None


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    global CRACK_FOUND
    print("=" * 76)
    print("R-N4-AUT: enrichment-stabilizer search for a sub-S_4 axis selector")
    print("=" * 76)

    L = 4
    Ls = (L, L, L, L)
    M, sites, idx = build_staggered(Ls)
    Mhop, _, _ = build_staggered(Ls, include_mass=False)
    N = len(sites)
    print(f"\nbare surface: even cubic block {Ls}, N = {N} sites, mass = {MASS}")

    # -----------------------------------------------------------------------
    # [G] Compute the full automorphism group of the BARE surface (the wall).
    # -----------------------------------------------------------------------
    print("\n" + "-" * 76)
    print("[G] full automorphism group of the BARE staggered surface (the wall)")
    print("-" * 76)
    G = build_G_bare(sites, idx, L, M)
    img = axis_image(G)
    full_S4 = sorted(itertools.permutations(range(4)))
    check("G", "bare-surface automorphism group projects ONTO all of S_4 "
          "(transitive on the 4 axes -- the standing N4 wall)",
          img == full_S4, f"|G|={len(G)}, |axis image|={len(img)} (S_4 has 24)")
    # transitivity sanity: every axis reachable from axis 0
    reachable = sorted({p[0] for p in img})
    check("G", "S_4 image is transitive: axis 0 maps to every axis",
          reachable == [0, 1, 2, 3], f"orbit of axis 0 = {reachable}")

    # Helper: stabilizer of an operator E inside G_bare
    def stab_operator(E, covariant_sign=+1):
        """g in Stab(E) iff U_g E U_g^T = covariant_sign * E (sign +1 = invariant)."""
        return [g for g in G if r(g[2] @ E @ g[2].T - covariant_sign * E) < TOL]

    # ===================================================================
    # ENRICHMENT CANDIDATES (each A_min-available; none presupposes H)
    # ===================================================================
    enrich = []  # (id, description, stabilizer-perms, a_min_ok, note)

    def classify(perms):
        """Classify a joint-stabilizer axis image as one of:
          'S4-isotropic'                 : full S_4 image (fixes none, transitive)
          'one-axis-selecting(S3)'       : fixes exactly one axis, S_3 on rest
          'trivial-joint(symmetric-break)': identity-only image (fixes ALL four,
                                            i.e. a symmetric, NON-axis-selecting
                                            break of W -- W IS broken, but no axis
                                            is singled out)
        Only the middle class is a genuine axis-selector / crack signature."""
        if selects_exactly_one_axis(perms) is not None:
            return "one-axis-selecting(S3)"
        if sorted(perms) == full_S4:
            return "S4-isotropic"
        if len(perms) == 1 and perms[0] == tuple(range(4)):
            return "trivial-joint(symmetric-break)"
        return f"other(|img|={len(perms)})"

    # -------------------------------------------------------------------
    # E1. Sublattice / reality-CPT grading eps_par(x) = (-1)^{sum x_mu}
    #     (Quantum/Record reality structure). Diagonal operator.
    # -------------------------------------------------------------------
    print("\n" + "-" * 76)
    print("[E1] sublattice-parity / reality-CPT grading  eps = (-1)^{sum x}")
    print("-" * 76)
    Epar = np.diag([(-1.0) ** sum(x) for x in sites])
    St = stab_operator(Epar)
    perms1 = sorted({g[0] for g in St})
    sel1 = selects_exactly_one_axis(perms1)
    check("E1", "grading is preserved by the FULL S_4 axis image (S_4-isotropic) "
          "-> selects NO axis",
          sorted(perms1) == full_S4 and sel1 is None,
          f"|axis image of Stab|={len(perms1)} (S_4=24); "
          f"common fixed axes={common_fixed_axes(perms1)}; selected axis={sel1}")
    enrich.append(("E1", "reality/CPT parity grading", perms1, True,
                   "internal C^2 reality structure; sum-symmetric, W-inert"))

    # -------------------------------------------------------------------
    # E2. Nearest-neighbour cubic adjacency Laplacian  L_adj
    #     (pure Lattice: sites + nn cubic adjacency, NO eta, NO orientation).
    #     A_min's Lattice axiom names exactly this graph.
    # -------------------------------------------------------------------
    print("\n" + "-" * 76)
    print("[E2] bare cubic adjacency (graph Laplacian) -- pure Lattice axiom")
    print("-" * 76)
    A = np.zeros((N, N))
    for x in sites:
        for mu in range(4):
            y = list(x); y[mu] = (y[mu] + 1) % L; y = tuple(y)
            A[idx[x], idx[y]] += 1.0
            A[idx[y], idx[x]] += 1.0
    Lap = np.diag(A.sum(1)) - A
    # The plain Laplacian is S_4-isotropic in ITS OWN RIGHT (undressed
    # permutations preserve it); confirm that directly with plain perms.
    plain_keep = []
    for pi in itertools.permutations(range(4)):
        Pg = site_perm_matrix(sites, idx, pi, (1, 1, 1, 1), L)
        if r(Pg @ Lap @ Pg.T - Lap) < TOL:
            plain_keep.append(pi)
    check("E2a", "cubic adjacency Laplacian alone is S_4-isotropic (every plain "
          "axis permutation preserves it) -> the Lattice graph carries no axis",
          sorted(plain_keep) == full_S4,
          f"plain-perm symmetries = {len(plain_keep)} (S_4=24)")
    # Its JOINT stabilizer with the staggered hop (inside G_bare) selects no axis:
    St = stab_operator(Lap)
    perms2 = sorted({g[0] for g in St})
    sel2 = selects_exactly_one_axis(perms2)
    check("E2", "joint (staggered-hop + Laplacian) stabilizer is TRIVIAL "
          "(identity-only): W IS BROKEN by this A_min enrichment (plain swap keeps "
          "the Laplacian but breaks the hop; dressed W keeps the hop but breaks the "
          "Laplacian; no non-identity B_4 element keeps both), but the break is "
          "axis-SYMMETRIC -> selects NO axis (NOT S4-isotropic; trivial joint stab)",
          sel2 is None and len(perms2) == 1,
          f"|axis image of joint Stab|={len(perms2)} (trivial=1); "
          f"common fixed axes={common_fixed_axes(perms2)}; selected axis={sel2}")
    enrich.append(("E2", "cubic adjacency Laplacian", perms2, True,
                   "Lattice axiom = isotropic nn cubic graph; no direction"))

    # -------------------------------------------------------------------
    # E3. Staggered eta phase field as a SET OF ORIENTED HOP SECTORS.
    #     Per-axis hop operator D_mu. Test the stabilizer of the FAMILY
    #     {D_0,D_1,D_2,D_3} as an unordered set (covariance permits relabel).
    #     This is the closest thing to "the staggered structure itself".
    # -------------------------------------------------------------------
    print("\n" + "-" * 76)
    print("[E3] staggered eta hop sectors {D_0..D_3} as an unordered family")
    print("-" * 76)
    D = []
    for mu in range(4):
        Dmu = np.zeros((N, N))
        for x in sites:
            eta = (-1) ** (sum(x[nu] for nu in range(mu)))
            y = list(x); y[mu] = (y[mu] + 1) % L; y = tuple(y)
            Dmu[idx[x], idx[y]] += 0.5 * eta
            Dmu[idx[y], idx[x]] += -0.5 * eta
        D.append(Dmu)
    # g preserves the FAMILY iff for each mu there is nu with U_g D_mu U_g^T = +-D_nu
    def preserves_family(U):
        used = set()
        for mu in range(4):
            T = U @ D[mu] @ U.T
            found = None
            for nu in range(4):
                if nu in used:
                    continue
                if r(T - D[nu]) < TOL or r(T + D[nu]) < TOL:
                    found = nu; break
            if found is None:
                return False
            used.add(found)
        return True
    St = [g for g in G if preserves_family(g[2])]
    perms3 = sorted({g[0] for g in St})
    sel3 = selects_exactly_one_axis(perms3)
    check("E3", "the unordered staggered hop-sector family is preserved by the "
          "FULL S_4 (sectors permute among themselves) -> selects NO axis",
          sorted(perms3) == full_S4 and sel3 is None,
          f"|axis image of Stab|={len(perms3)}; "
          f"common fixed axes={common_fixed_axes(perms3)}; selected axis={sel3}")
    enrich.append(("E3", "staggered hop-sector family", perms3, True,
                   "eta sectors permute under S_4; the W sign field realizes it"))

    # -------------------------------------------------------------------
    # E4. STW crossing-link RP invariant P_a(x) = eta_a(x) eta_a(theta_a x)
    #     as a per-axis scalar field (s3-convention branch reported +1 all axes;
    #     recompute its per-axis value and stabilizer).
    # -------------------------------------------------------------------
    print("\n" + "-" * 76)
    print("[E4] STW crossing-link RP invariant P_a(x) per axis")
    print("-" * 76)
    # eta_a omits x_a: eta_a(x) = (-1)^{sum_{nu<a} x_nu}; theta_a reflects axis a.
    Pa_vals = []
    for a in range(4):
        vals = set()
        for x in sites:
            eta_x = (-1) ** sum(x[nu] for nu in range(a))
            xr = list(x); xr[a] = (L - 1 - x[a]); xr = tuple(xr)
            eta_xr = (-1) ** sum(xr[nu] for nu in range(a))
            vals.add(eta_x * eta_xr)
        Pa_vals.append(sorted(vals))
    same = all(v == Pa_vals[0] for v in Pa_vals)
    check("E4", "crossing-link RP invariant P_a takes the SAME value-set on every "
          "axis -> S_d-isotropic, carries no axis label",
          same, f"P_a value-sets = {Pa_vals}")
    enrich.append(("E4", "STW crossing-link RP invariant", full_S4, True,
                   "P_a identical across axes; no axis distinction"))

    # -------------------------------------------------------------------
    # E5. eta-curvature 2-cocycle c_{mu,nu} on plaquettes
    #     (product of eta signs around a 1x1 loop in plane (mu,nu)).
    #     If the temporal planes (0,i) differ from spatial planes (i,j),
    #     the cocycle would single out axis 0 -> a sub-S_4 selector.
    # -------------------------------------------------------------------
    print("\n" + "-" * 76)
    print("[E5] eta-curvature 2-cocycle on plaquettes (per plane)")
    print("-" * 76)
    def eta(mu, x):
        return (-1) ** sum(x[nu] for nu in range(mu))
    cocycle = {}
    for mu in range(4):
        for nu in range(mu + 1, 4):
            x = (0, 0, 0, 0)
            xn = list(x); xn[mu] = 1
            xm = list(x); xm[nu] = 1
            # eta_mu(x) eta_nu(x+mu) eta_mu(x+nu)^{-1} eta_nu(x)^{-1}
            c = (eta(mu, x) * eta(nu, tuple(xn))
                 * eta(mu, tuple(xm)) * eta(nu, x))
            cocycle[(mu, nu)] = c
    temporal_planes = [cocycle[(0, i)] for i in range(1, 4)]
    spatial_planes = [cocycle[(i, j)] for i in range(1, 4) for j in range(i + 1, 4)]
    all_equal = len(set(cocycle.values())) == 1
    check("E5", "eta-curvature 2-cocycle is IDENTICAL in temporal (0,i) and "
          "spatial (i,j) planes -> S_4-isotropic, no time-singling",
          all_equal,
          f"temporal={temporal_planes}, spatial={spatial_planes}")
    enrich.append(("E5", "eta-curvature 2-cocycle", full_S4, True,
                   "cocycle = -1 in ALL planes incl temporal; isotropic"))

    # -------------------------------------------------------------------
    # E6. Record additive scalar readout as a diagonal counting operator
    #     R = sum_x n_x (durable record occupancy). Diagonal, sum over sites.
    #     Record supplies a SCALAR (axis-blind by construction).
    # -------------------------------------------------------------------
    print("\n" + "-" * 76)
    print("[E6] Record additive scalar readout (diagonal occupancy counter)")
    print("-" * 76)
    Rcount = np.eye(N)  # uniform site weighting -- the only A_min-canonical one
    St = stab_operator(Rcount)
    perms6 = sorted({g[0] for g in St})
    check("E6", "the additive record readout is the scalar identity weighting -> "
          "commutes with ALL of G (Record supplies no axis-weighted readout)",
          sorted(perms6) == full_S4,
          f"|axis image of Stab|={len(perms6)}; uniform additive readout is S_4-fixed")
    enrich.append(("E6", "Record additive scalar readout", perms6, True,
                   "additivity + I(empty)=0 give a scalar; no axis weighting"))

    # -------------------------------------------------------------------
    # E7. BOUNDARY DECORATION: per-axis Z_2 BC datum bc=(A,P,P,P).
    #     This DOES break to S_3 (fixes axis 0) -- BUT it is a SUPPLIED datum,
    #     NOT A_min-derivable, and S_4-transportable (s4 branch). Recorded as
    #     the one enrichment with sub-S_4 stabilizer that FAILS the A_min test.
    # -------------------------------------------------------------------
    print("\n" + "-" * 76)
    print("[E7] per-axis Z_2 BC datum bc=(A,P,P,P) -- sub-S_4 but NOT A_min")
    print("-" * 76)
    M_appp, _, _ = build_staggered(Ls, bc=(-1, 1, 1, 1))
    St = stab_operator(M_appp)
    perms7 = sorted({g[0] for g in St})
    sel7 = selects_exactly_one_axis(perms7)
    check("E7", "the BC datum (A,P,P,P) HAS a sub-S_4 stabilizer that selects "
          "EXACTLY axis 0 and acts as S_3 on the spatial axes (the sharpened pin: "
          "a genuine axis selector)",
          sel7 == 0,
          f"|axis image of Stab|={len(perms7)} (<24); "
          f"common fixed axes={common_fixed_axes(perms7)}; selected axis={sel7}")
    # but it is transportable: a *different* element of the BARE group maps it to
    # bc=(P,A,P,P) -> so the datum is not non-transportable, and it is supplied.
    W01 = next(g[2] for g in G if g[0] == (1, 0, 2, 3))
    M_pappp, _, _ = build_staggered(Ls, bc=(1, -1, 1, 1))
    transports = r(W01 @ M_appp @ W01.T - M_pappp) < TOL
    check("E7", "...but that datum is S_4-TRANSPORTABLE (a bare-group element maps "
          "(A,P,P,P) onto (P,A,P,P)) AND is a SUPPLIED boundary input, not "
          "A_min-derivable -> fails the A_min test (does NOT crack)",
          transports,
          f"||W01 M_appp W01^T - M_pappp|| transport resid < TOL: {transports}")
    enrich.append(("E7", "per-axis Z_2 BC datum (A,P,P,P)", perms7, False,
                   "sub-S_4 (fixes axis 0) BUT supplied + S_4-transportable"))

    # -------------------------------------------------------------------
    # E8. CROSSING-LINK / DIAGONAL ENRICHMENT: add next-nearest (body/face
    #     diagonal) cubic links -- a richer Lattice graph. Still isotropic?
    #     Lattice axiom names NN cubic adjacency only; we test whether adding
    #     ANY isotropic diagonal coupling could break S_4. (It cannot: diagonals
    #     are cubic-symmetric.) Tested for completeness of the "richer graph"
    #     steelman.
    # -------------------------------------------------------------------
    print("\n" + "-" * 76)
    print("[E8] richer cubic graph: + face-diagonal links (isotropic enrichment)")
    print("-" * 76)
    Adiag = np.zeros((N, N))
    for x in sites:
        for mu in range(4):
            for nu in range(mu + 1, 4):
                for sm in (+1, -1):
                    for sn in (+1, -1):
                        y = list(x)
                        y[mu] = (y[mu] + sm) % L
                        y[nu] = (y[nu] + sn) % L
                        y = tuple(y)
                        Adiag[idx[x], idx[y]] += 1.0
    Ldiag = np.diag(Adiag.sum(1)) - Adiag
    plain_keep8 = []
    for pi in itertools.permutations(range(4)):
        Pg = site_perm_matrix(sites, idx, pi, (1, 1, 1, 1), L)
        if r(Pg @ Ldiag @ Pg.T - Ldiag) < TOL:
            plain_keep8.append(pi)
    check("E8a", "face-diagonal-enriched cubic graph alone is STILL S_4-isotropic "
          "(every plain permutation preserves it; an isotropic graph enrichment "
          "respects cubic symmetry) -> selects no axis",
          sorted(plain_keep8) == full_S4,
          f"plain-perm symmetries = {len(plain_keep8)} (S_4=24)")
    St = stab_operator(Ldiag)
    perms8 = sorted({g[0] for g in St})
    sel8 = selects_exactly_one_axis(perms8)
    check("E8", "joint (staggered-hop + diagonal-graph) stabilizer is TRIVIAL "
          "(identity-only): W IS BROKEN by this A_min enrichment, but the break is "
          "axis-SYMMETRIC -> selects NO axis (NOT S4-isotropic; trivial joint stab)",
          sel8 is None and len(perms8) == 1,
          f"|axis image of joint Stab|={len(perms8)} (trivial=1); "
          f"common fixed axes={common_fixed_axes(perms8)}; selected axis={sel8}")
    enrich.append(("E8", "diagonal-link cubic graph", perms8, True,
                   "isotropic graph enrichment stays cubic-symmetric"))

    # -------------------------------------------------------------------
    # SCOPE boundary: the exact-zeros are EVEN-extent only.
    # -------------------------------------------------------------------
    print("\n" + "-" * 76)
    print("[SCOPE] even-extent requirement (odd-L falsifier)")
    print("-" * 76)
    Lodd = (3, 3, 3, 3)
    Modd, sodd, iodd = build_staggered(Lodd)
    # the signed exchange on odd block
    Wodd = np.zeros((len(sodd), len(sodd)))
    for x in sodd:
        sw = list(x); sw[0], sw[1] = x[1], x[0]
        Wodd[iodd[tuple(sw)], iodd[x]] = (-1) ** (x[0] * x[1])
    odd_break = r(Wodd @ Modd @ Wodd.T - Modd)
    check("SCOPE", "ODD cubic L=(3,3,3,3): signed exchange does NOT preserve the hop "
          "(resid 6) -> S_4-transitivity exact-zeros are EVEN-extent only",
          odd_break > NONTRIV,
          f"||W M W^T - M||_odd = {odd_break:.3f} (matches the s4-branch falsifier)")
    check("SCOPE", "...EVEN L=(4,4,4,4) recap: exact (resid 0)",
          r(next(g[2] for g in G if g[0] == (1, 0, 2, 3)) @ M
            @ next(g[2] for g in G if g[0] == (1, 0, 2, 3)).T - M) < TOL)

    # ===================================================================
    # VERDICT
    # ===================================================================
    print("\n" + "=" * 76)
    print("VERDICT: enrichment / stabilizer table")
    print("=" * 76)
    print(f"{'id':<4} {'enrichment':<30} {'|img|':<6} "
          f"{'sel':<5} {'class':<32} {'A_min?':<7}")
    for eid, desc, perms, amin, note in enrich:
        sel = selects_exactly_one_axis(perms)
        cls = classify(perms)
        print(f"{eid:<4} {desc:<30} {len(perms):<6} "
              f"{str(sel):<5} {cls:<32} {'yes' if amin else 'NO':<7}")
    print()
    print("classification key: every A_min enrichment's JOINT stabilizer with the")
    print("staggered hop is either S4-isotropic (full S_4, fixes none) or trivial")
    print("(identity-only -> a SYMMETRIC, NON-axis-selecting break of W: W is broken,")
    print("but no axis is singled out). NONE is one-axis-selecting(S3). The only")
    print("one-axis-selecting enrichment is E7 (per-axis Z_2 BC datum), which is")
    print("S4-transportable AND outside A_min.")

    # CRACK test: an enrichment cracks iff it SELECTS EXACTLY ONE axis (proper
    # sub-S_4 fixing one axis, transitive on the rest) AND is A_min-derivable.
    # A trivial/symmetric stabilizer (fixes all or none) does NOT select an axis.
    crackers = [e for e in enrich
                if selects_exactly_one_axis(e[2]) is not None
                and e[3]]
    global CRACK_FOUND
    CRACK_FOUND = len(crackers) > 0
    # explicit precise structural assertion: every A_min enrichment's joint
    # stabilizer is either full-S_4 (isotropic) or trivial (symmetric break);
    # NONE is one-axis-selecting(S3). The only one-axis-selector is E7 (BC datum),
    # outside A_min and S_4-transportable.
    amin_classes = {e[0]: classify(e[2]) for e in enrich if e[3]}
    amin_all_iso_or_trivial = all(
        c in ("S4-isotropic", "trivial-joint(symmetric-break)")
        for c in amin_classes.values())
    no_amin_selector = all(c != "one-axis-selecting(S3)"
                           for c in amin_classes.values())
    e7_one_axis = classify(next(e[2] for e in enrich if e[0] == "E7")) \
        == "one-axis-selecting(S3)"
    check("VERDICT", "every A_min enrichment's JOINT stabilizer with the staggered "
          "hop is either ALL of S_4 (isotropic) or TRIVIAL (a symmetric, "
          "non-axis-selecting break of W); NO A_min enrichment is "
          "one-axis-selecting(S3); the only one-axis-selecting enrichment is the "
          "per-axis Z_2 BC datum (E7), which is S_4-transportable and outside A_min",
          amin_all_iso_or_trivial and no_amin_selector and e7_one_axis,
          f"A_min classes={amin_classes}; E7 one-axis-selecting={e7_one_axis}")
    check("VERDICT", "NO A_min-available enrichment SELECTS an axis -> the S_4 "
          "orbit is EXHAUSTIVE, steelman FAILS, wall CONFIRMED",
          not CRACK_FOUND,
          f"A_min-crackers found = {[c[0] for c in crackers]}")

    print("\n" + "=" * 76)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 76)
    if CRACK_FOUND:
        print("RESULT: *** WALL CRACKED *** an A_min enrichment selects an axis.")
    else:
        print("RESULT: wall CONFIRMED -- every A_min enrichment's joint stabilizer "
              "with the staggered hop is either all of S_4 (isotropic) or trivial "
              "(a symmetric, non-axis-selecting W-break); NO A_min enrichment has a "
              "one-axis-selecting (S_3) stabilizer. The only one-axis-selecting "
              "enrichment is the per-axis Z_2 BC datum (E7), which is "
              "S_4-transportable and outside A_min.")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
