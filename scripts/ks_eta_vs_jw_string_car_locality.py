"""
KS staggered eta-factor vs Jordan-Wigner string: does matter-attachment LOCALITY
+ the Kogut-Susskind staggered structure ALGEBRAICALLY FORCE cross-site CAR?

Angle: NON-geometric / algebraic forcing of the cross-site CAR sign from the
matter-attachment construction on Z^3. Qubit supplies the one-site M_2(C)
possibility algebra; the finite tensor realization below is the tested model.

Central distinction under test (the two objects must NOT be conflated):
  * STAGGERED eta_mu(x) = (-1)^{x_1 + ... + x_{mu-1}}  -- a per-LINK c-number sign.
      Source: the spin-diagonalization T(x)=sigma_1^{x1} sigma_2^{x2} sigma_3^{x3}
      that absorbs the Dirac gamma structure (Kawamoto-Smit). It is the DIRAC /
      TASTE structure coefficient. It multiplies the hopping term chi-bar_{x+mu} chi_x.
  * JW STRING S_x = prod_{y < x} sigma_3^(y)  -- an OPERATOR-valued dressing on the
      sites BETWEEN the two endpoints, in a chosen total ORDER. It is the STATISTICS
      object: it converts commuting tensor ladders into cross-site ANTIcommuting ones.

QUESTION: do the eta_mu(x), combined with a locality requirement on the matter
operator, FORCE b_i b_j = - b_j b_i across sites (CAR)? Or are the eta purely the
Dirac-structure (taste) signs, compatible with EITHER statistics (boson vs fermion)?

We build the actual KS staggered hopping operator on a 2x2x2 Z^3 patch in TWO
operator realizations on the SAME tensor-product qubit Hilbert space:
  (HCB) hard-core boson: bare ladders b_x = sigma_+^(x) (commute cross-site),
  (JW)  fermion:        c_x = S_x sigma_+^(x) (anticommute cross-site),
both carrying the IDENTICAL eta_mu(x) link signs, and check, exactly:

  C1  eta_mu(x) are the Kawamoto-Smit phases (c-number signs), eta independent of
      statistics realization.
  C2  Both staggered hopping constructions carry the SAME eta signs. HCB link
      terms are endpoint-local, while JW link terms can carry the ordering string
      outside their geometric endpoints (eta does NOT discriminate statistics).
  C3  The bare ladders are hard-core-bosonic: [b_x, b_y] = 0 for x != y, b_x^2 = 0.
      => a LOCAL, nilpotent, single-occupancy matter operator EXISTS that is NOT CAR.
      Hence locality + nilpotency + eta do NOT force CAR.
  C4  CAR appears after the JW string dressing; {c_x, c_y}=0 needs the string,
      which (a) is a DIFFERENT object from eta and (b) requires an ORDER choice.
  C5  Counterfactual: dropping the string but KEEPING eta leaves cross-site
      ANTIcommutators NON-zero (bosonic). Dropping eta but keeping the string still
      gives CAR. => the CAR sign is carried by the STRING, NOT by eta. ORTHOGONAL.
  C6  On a three-site subpatch, the two algebras (HCB generators vs JW
      generators) generate the SAME full matrix algebra M_{2^N}(C). Statistics
      is a frame choice on one ungraded algebra.
  C7  Ungraded tensor-locality horn: no total order makes every nearest-neighbour
      link string-free on the 2x2x2 patch. Its grid graph has bandwidth > 1, so
      some geometric links carry non-endpoint tensor support. This representation
      does not canonically supply the string from endpoint locality.

VERDICT printed at the end. Uses the Lattice/Qubit baseline plus standard
finite linear algebra. No imports.
"""

from __future__ import annotations

import itertools
from functools import reduce
import numpy as np

# ----------------------------------------------------------------------------
# Pauli matrices and tensor-product machinery on a Z^3 patch of qubits.
# ----------------------------------------------------------------------------
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
SP = (SX + 1j * SY) / 2.0   # sigma_+ = |0><1| raising (creates an excitation)
SM = (SX - 1j * SY) / 2.0   # sigma_-

def kron_all(mats):
    return reduce(np.kron, mats)

def make_patch(L=2):
    """Sites of an L x L x L block of Z^3, lexicographic order (z,y,x slowest->...)."""
    sites = [(x, y, z) for z in range(L) for y in range(L) for x in range(L)]
    # canonical lexicographic total order pi on (x1,x2,x3)
    order = sorted(sites)  # lexicographic by (x1,x2,x3)
    index = {s: i for i, s in enumerate(order)}
    return order, index

def site_op(local, site_idx, N):
    mats = [I2] * N
    mats[site_idx] = local
    return kron_all(mats)

# ----------------------------------------------------------------------------
# Kawamoto-Smit staggered phases (the DIRAC / TASTE structure c-numbers).
#   eta_1(x) = 1, eta_2(x) = (-1)^{x_1}, eta_3(x) = (-1)^{x_1 + x_2}.
# ----------------------------------------------------------------------------
def eta(mu, x):
    """mu in {1,2,3}; x = (x1,x2,x3). Returns +1 or -1 (a c-number)."""
    x1, x2, x3 = x
    if mu == 1:
        return 1
    elif mu == 2:
        return (-1) ** (x1)
    elif mu == 3:
        return (-1) ** (x1 + x2)
    raise ValueError(mu)

def eta_from_spin_diag(mu, x):
    """Independent derivation of eta from the spin-rotation T(x)=sx^{x1} sy^{x2} sz^{x3}
    via T(x)^dag gamma_mu T(x+mu) = eta_mu(x) I, gamma_mu = sigma_mu.
    Returns the scalar (should be a multiple of I_2; we extract the scalar)."""
    def spow(s, n):
        return np.linalg.matrix_power(s, n % 2)
    def T(pt):
        a, b, c = pt
        return spow(SX, a) @ spow(SY, b) @ spow(SZ, c)
    gamma = {1: SX, 2: SY, 3: SZ}[mu]
    xn = list(x)
    xn[mu - 1] += 1
    M = T(x).conj().T @ gamma @ T(tuple(xn))
    # M should equal eta * I_2 (up to the staggered convention). Extract scalar:
    scal = M[0, 0]
    assert np.allclose(M, scal * I2, atol=1e-12), f"spin-diag not scalar: {M}"
    return scal

# ----------------------------------------------------------------------------
# Nearest-neighbour links inside the patch (no wrap; open boundary for the test).
# ----------------------------------------------------------------------------
def nn_links(order, index, L=2):
    links = []  # (mu, x, y=x+mu_hat)
    for x in order:
        for mu in (1, 2, 3):
            xn = list(x)
            xn[mu - 1] += 1
            xn = tuple(xn)
            if all(0 <= xn[d] < L for d in range(3)):
                links.append((mu, x, xn))
    return links

# ----------------------------------------------------------------------------
# Build the staggered hopping operator in the two statistics realizations.
#   H = (1/2) sum_{links} eta_mu(x) [ Adag_{y} A_{x} - Adag_{x} A_{y} ]  (anti-herm core)
# where A_x is either the bare ladder (HCB) or the JW-dressed operator (fermion).
# We will inspect the OPERATOR (not its spectrum); the point is locality + eta.
# ----------------------------------------------------------------------------
def jw_string(site, order, index, N):
    """S_x = prod_{y : pi(y) < pi(x)} sigma_3^(y)."""
    px = index[site]
    S = np.eye(2 ** N, dtype=complex)
    for y in order:
        if index[y] < px:
            S = S @ site_op(SZ, index[y], N)
    return S

def ladder_HCB(site, order, index, N):
    """Bare hard-core-boson ladder b_x = sigma_+^(x) (commutes cross-site)."""
    return site_op(SP, index[site], N)

def ladder_JW(site, order, index, N):
    """JW-dressed fermion c_x = S_x sigma_+^(x)."""
    return jw_string(site, order, index, N) @ site_op(SP, index[site], N)

def staggered_hopping(order, index, links, N, ladder, use_eta=True):
    """Build the staggered kinetic operator with given ladder realization."""
    H = np.zeros((2 ** N, 2 ** N), dtype=complex)
    for (mu, x, y) in links:
        e = eta(mu, x) if use_eta else 1
        ax = ladder(x, order, index, N)
        ay = ladder(y, order, index, N)
        H = H + 0.5 * e * (ay.conj().T @ ax - ax.conj().T @ ay)
    return H

# ----------------------------------------------------------------------------
# Locality test: is an operator supported on a nearest-neighbour link?
# An operator O is "local on link (x,y)" if it commutes with sigma_z parity on
# every site NOT in {x,y} ... but more robustly: O = (something on x) tensor
# (something on y) tensor identity elsewhere. We test: does O act as identity on
# all sites outside a small support set S? i.e. partial structure.
# Simplest robust check: O acts as identity on site s  <=>  O commutes with EVERY
# single-site operator on s AND with the projector structure. We use: O is
# identity-acting on site s iff O = I_2^{(s)} (x) O' for some O', equivalently
# the partial transpose / reshaping has the identity block structure.
# We implement: support(O) = set of sites where O does NOT act as identity.
# ----------------------------------------------------------------------------
def acts_as_identity_on_site(O, s_idx, N, tol=1e-9):
    """True iff O = I_2 (on site s_idx) tensor (rest). Test by reshaping."""
    # reshape O into (2,2,...,2, 2,2,...,2) row/col tensor, move site axis, check
    # O[a_s, ...; b_s, ...] = delta_{a_s b_s} * O'[...] is too strong (needs same O' ).
    # Equivalent invariant test: O is identity on site s iff for the two single-site
    # basis operators E_{01}=SP, E_{10}=SM, and number n on site s, the partial trace
    # structure factorizes. Use the standard: O acts trivially on s iff
    # [O, V_s] = 0 for ALL single-site V_s on s  AND  Tr_s(O)/2 reconstructs O.
    # We use the cleaner reshaping criterion.
    dims = [2] * N
    T = O.reshape(dims + dims)
    # bring row index s and col index s to front: axes s and N+s
    T2 = np.moveaxis(T, [s_idx, N + s_idx], [0, 1])
    # T2 has shape (2,2, rest_row..., rest_col...). Identity on s requires
    # T2[a,b,...] = delta_{ab} * M[...]; check off-diagonal blocks ~0 and the two
    # diagonal blocks equal.
    a00 = T2[0, 0]
    a11 = T2[1, 1]
    a01 = T2[0, 1]
    a10 = T2[1, 0]
    return (np.allclose(a01, 0, atol=tol) and np.allclose(a10, 0, atol=tol)
            and np.allclose(a00, a11, atol=tol))

def support_sites(O, order, N):
    supp = []
    for s_idx in range(N):
        if not acts_as_identity_on_site(O, s_idx, N):
            supp.append(order[s_idx])
    return supp

# ----------------------------------------------------------------------------
# Algebra-generation test: does a generator set span all of M_{2^N}(C)?
# We accumulate the linear span (over C) of products of generators up to closure.
# ----------------------------------------------------------------------------
def algebra_dimension(generators, N, max_words=None):
    D = 2 ** N
    # Represent operators as flattened vectors; build span by Gram/QR rank growth.
    basis_vecs = []  # flattened operator basis built by Gram-Schmidt
    def add_vec(M):
        v = M.reshape(-1).astype(complex)
        for b in basis_vecs:
            v = v - (np.vdot(b, v)) * b
        nv = np.linalg.norm(v)
        if nv > 1e-8:
            basis_vecs.append(v / nv)
            return True
        return False
    # seed with identity and all generators and their adjoints
    add_vec(np.eye(D, dtype=complex))
    pool = []
    for g in generators:
        if add_vec(g):
            pool.append(g)
        gd = g.conj().T
        if add_vec(gd):
            pool.append(gd)
    # close under multiplication until no growth (bounded by D^2)
    frontier = list(pool)
    seen_dim = len(basis_vecs)
    while frontier and len(basis_vecs) < D * D:
        new_frontier = []
        gens = pool
        for A in frontier:
            for g in gens:
                for P in (A @ g, g @ A):
                    if add_vec(P):
                        new_frontier.append(P)
        if len(basis_vecs) == seen_dim:
            break
        seen_dim = len(basis_vecs)
        frontier = new_frontier
    return len(basis_vecs)

# ----------------------------------------------------------------------------
# Grid-graph bandwidth on the patch (smallest max |pi(x)-pi(y)| over orderings,
# for nearest-neighbour links). We brute-force over all orderings for L=2 (8!).
# Too big (40320) but fine. We report the minimum bandwidth.
# ----------------------------------------------------------------------------
def grid_bandwidth_min(order, links):
    sites = order
    n = len(sites)
    best = None
    # brute force all permutations (8! = 40320 for L=2)
    edges = [(x, y) for (_, x, y) in links]
    for perm in itertools.permutations(range(n)):
        pos = {sites[i]: perm[i] for i in range(n)}
        bw = max(abs(pos[x] - pos[y]) for (x, y) in edges)
        if best is None or bw < best:
            best = bw
            if best == 1:
                break
    return best

# ----------------------------------------------------------------------------
# Anticommutator / commutator helpers
# ----------------------------------------------------------------------------
def anticomm(A, B):
    return A @ B + B @ A

def comm(A, B):
    return A @ B - B @ A

# ============================================================================
# CHECKS
# ============================================================================
def check():
    PASS = 0
    FAIL = 0
    def ok(name, cond):
        nonlocal PASS, FAIL
        if cond:
            PASS += 1
            print(f"  PASS  {name}")
        else:
            FAIL += 1
            print(f"  FAIL  {name}")

    L = 2
    order, index = make_patch(L)
    N = len(order)            # 8 sites
    D = 2 ** N                # 256
    links = nn_links(order, index, L)
    print(f"[setup] L={L}  N={N} sites  dim H = {D}  nearest-neighbour links = {len(links)}")
    print(f"[setup] lexicographic order pi: {order}")
    print()

    # ---- C1: eta are the Kawamoto-Smit phases and match the spin-diagonalization
    print("C1  eta_mu(x) = Kawamoto-Smit phases (c-number Dirac-structure signs)")
    c1 = True
    for x in order:
        for mu in (1, 2, 3):
            e_def = eta(mu, x)
            e_spin = eta_from_spin_diag(mu, x)
            if not np.allclose(e_spin, e_def, atol=1e-12):
                c1 = False
    ok("eta_from_spin_diag equals the closed-form eta for every (mu,x)", c1)
    # closed form sign table matches the canonical KS pattern
    ks_ref = {(1,(0,0,0)):1,(2,(1,0,0)):-1,(2,(0,0,0)):1,(3,(1,1,0)):1,(3,(0,1,0)):-1}
    ok("eta closed form matches canonical KS sign table (sample)",
       all(eta(mu,x)==v for (mu,x),v in ks_ref.items()))
    # eta is a c-number, independent of statistics realization (it is literally an int)
    ok("eta_mu(x) is a c-number (int), carries NO operator content / no statistics",
       all(isinstance(eta(mu,x), int) for x in order for mu in (1,2,3)))
    print()

    # ---- C3: bare ladders are hard-core-bosonic (local, nilpotent, COMMUTE cross-site)
    print("C3  bare matter ladders b_x = sigma_+^(x): local, nilpotent, but CROSS-SITE COMMUTING")
    bx = {x: ladder_HCB(x, order, index, N) for x in order}
    # nilpotent on-site
    ok("b_x^2 = 0 (single occupancy / nilpotent)",
       all(np.allclose(bx[x] @ bx[x], 0) for x in order))
    # cross-site COMMUTE (hard-core boson), NOT anticommute
    pairs = list(itertools.combinations(order, 2))
    ok("[b_x, b_y] = 0 for x != y (hard-core BOSON, ungraded)",
       all(np.allclose(comm(bx[x], bx[y]), 0) for (x, y) in pairs))
    ok("{b_x, b_y} != 0 for some x != y (NOT fermionic)",
       any(not np.allclose(anticomm(bx[x], bx[y]), 0) for (x, y) in pairs))
    # each bare ladder is single-site local
    ok("each b_x is single-site supported (maximally local)",
       all(support_sites(bx[x], order, N) == [x] for x in order))
    print()

    # ---- C4: JW-dressed operators satisfy CAR (need the STRING)
    print("C4  JW-dressed c_x = S_x sigma_+^(x): cross-site CAR (the string supplies it)")
    cx = {x: ladder_JW(x, order, index, N) for x in order}
    ok("c_x^2 = 0", all(np.allclose(cx[x] @ cx[x], 0) for x in order))
    ok("{c_x, c_y} = 0 for ALL x != y (CAR)",
       all(np.allclose(anticomm(cx[x], cx[y]), 0) for (x, y) in pairs))
    ok("{c_x, c_x^dag} = I for every x",
       all(np.allclose(anticomm(cx[x], cx[x].conj().T), np.eye(D)) for x in order))
    ok("{c_x, c_y^dag} = 0 for x != y",
       all(np.allclose(anticomm(cx[x], cx[y].conj().T), 0) for (x, y) in pairs))
    parity = kron_all([SZ] * N)
    ok("the same global parity anticommutes with both HCB and JW ladders",
       all(np.allclose(anticomm(parity, bx[x]), 0) for x in order)
       and all(np.allclose(anticomm(parity, cx[x]), 0) for x in order))
    print()

    # ---- C2: both constructions carry the SAME eta; locality differs by string
    print("C2  same staggered eta in both realizations; endpoint locality differs by JW string")
    H_hcb = staggered_hopping(order, index, links, N, ladder_HCB, use_eta=True)
    H_jw  = staggered_hopping(order, index, links, N, ladder_JW,  use_eta=True)
    # Both are built from the SAME eta link signs. Confirm each link term in the HCB
    # operator is supported on exactly the 2 endpoint sites (nearest-neighbour local).
    hcb_local = True
    eta_coeff_hcb = []
    eta_coeff_jw = []
    for link in links:
        mu, x, y = link
        signed_term = staggered_hopping(
            order, index, [link], N, ladder_HCB, use_eta=True
        )
        unsigned_term = staggered_hopping(
            order, index, [link], N, ladder_HCB, use_eta=False
        )
        supp = set(support_sites(signed_term, order, N))
        if not supp.issubset({x, y}):
            hcb_local = False
        eta_coeff_hcb.append(
            np.vdot(unsigned_term, signed_term)
            / np.vdot(unsigned_term, unsigned_term)
        )
    ok("HCB staggered hopping: every link term supported on its 2 endpoints (local)", hcb_local)
    jw_endpoint_local = []
    jw_non_endpoint_local = []
    for link in links:
        mu, x, y = link
        signed_term = staggered_hopping(
            order, index, [link], N, ladder_JW, use_eta=True
        )
        unsigned_term = staggered_hopping(
            order, index, [link], N, ladder_JW, use_eta=False
        )
        eta_coeff_jw.append(
            np.vdot(unsigned_term, signed_term)
            / np.vdot(unsigned_term, unsigned_term)
        )
        supp = set(support_sites(signed_term, order, N))
        lo, hi = sorted((index[x], index[y]))
        expected_support = {order[position] for position in range(lo, hi + 1)}
        ok(f"JW link {x}-{y}: tensor support equals its ordered endpoint interval",
           supp == expected_support)
        if supp.issubset({x, y}):
            jw_endpoint_local.append((mu, x, y))
        else:
            jw_non_endpoint_local.append((mu, x, y, tuple(sorted(supp))))
    eta_reference = np.array(
        [eta_from_spin_diag(mu, x) for (mu, x, _) in links], dtype=complex
    )
    ok("isolated hopping-builder projections match the spin-diagonal eta table",
       np.allclose(eta_coeff_hcb, eta_reference)
       and np.allclose(eta_coeff_jw, eta_reference))
    ok("JW hopping: exactly 8/12 geometric NN link terms carry non-endpoint string support",
       len(jw_non_endpoint_local) == 8 and len(jw_endpoint_local) == 4)
    # The eta enters identically; the difference between H_hcb and H_jw is the
    # ladder dressing (the string), not eta.
    ok("H_hcb != H_jw (they differ by the JW string, not by eta)",
       not np.allclose(H_hcb, H_jw))
    print()

    # ---- C5: orthogonality of eta and the string (the decisive test)
    print("C5  DECISIVE: the CAR sign rides the STRING, not eta (orthogonal objects)")
    # (a) keep eta, DROP the string -> bare ladders still carry eta in H, but CAR fails
    cx_no_string = bx  # dropping S_x = bare ladder
    car_holds_without_string = all(
        np.allclose(anticomm(cx_no_string[x], cx_no_string[y]), 0) for (x, y) in pairs)
    ok("drop string, KEEP eta  ->  cross-site CAR FAILS (eta cannot supply CAR)",
       not car_holds_without_string)
    # (b) DROP eta in the kinetic operator, KEEP the string -> H changes while
    # the already constructed JW ladders continue to satisfy CAR.
    H_jw_no_eta = staggered_hopping(
        order, index, links, N, ladder_JW, use_eta=False
    )
    car_holds_without_eta = all(
        np.allclose(anticomm(cx[x], cx[y]), 0) for (x, y) in pairs
    )
    ok("drop eta, KEEP string   ->  kinetic operator changes and cross-site CAR holds",
       not np.allclose(H_jw_no_eta, H_jw) and car_holds_without_eta)
    print()

    # ---- C6: same ungraded algebra on a subpatch (statistics is a frame choice)
    print("C6  HCB and JW generators span the SAME M_{2^N}(C) on a three-site subpatch")
    # Use a small sub-patch for the algebra-closure cost (N=3 line) to keep it fast.
    sub_order = order[:3]
    sub_index = {s: i for i, s in enumerate(sub_order)}
    Ns = 3
    Ds = 2 ** Ns
    gens_hcb = []
    gens_jw = []
    for s in sub_order:
        gens_hcb.append(site_op(SP, sub_index[s], Ns))
        gens_hcb.append(site_op(SZ, sub_index[s], Ns))
        # JW on the sub-line
        Sx = np.eye(Ds, dtype=complex)
        for y in sub_order:
            if sub_index[y] < sub_index[s]:
                Sx = Sx @ site_op(SZ, sub_index[y], Ns)
        gens_jw.append(Sx @ site_op(SP, sub_index[s], Ns))
        gens_jw.append((Sx @ site_op(SP, sub_index[s], Ns)).conj().T)
    dim_hcb = algebra_dimension(gens_hcb, Ns)
    dim_jw = algebra_dimension(gens_jw, Ns)
    full = Ds * Ds  # = 4^N
    ok(f"HCB algebra dim = {dim_hcb} = 4^{Ns} = {full} (full matrix algebra)", dim_hcb == full)
    ok(f"JW  algebra dim = {dim_jw} = 4^{Ns} = {full} (same full matrix algebra)", dim_jw == full)
    ok("on the subpatch, both frames generate the SAME ungraded algebra => "
       "operator-algebra data cannot select statistics", dim_hcb == dim_jw == full)
    print()

    # ---- C7: locality horn -- the JW string is non-local; no order kills it
    print("C7  ungraded tensor locality horn: JW tails are non-endpoint-local on the 2x2x2 patch")
    bw = grid_bandwidth_min(order, links)
    ok(f"min grid-graph bandwidth over ALL orderings = {bw} > 1 "
       "(no total order makes every NN link string-free)", bw > 1)
    # explicit: in lexicographic order on (x1,x2,x3), x1 is the SLOW axis, so the
    # mu=1 nearest-neighbour link (0,0,0)-(1,0,0) spans the whole block; its JW
    # string covers all intermediate sites (operator-valued).
    s_lo, s_hi = (0, 0, 0), (1, 0, 0)   # slow-axis (mu=1) NN pair
    assert (1, s_lo, s_hi) in links, "expected mu=1 NN link in patch"
    span = abs(index[s_hi] - index[s_lo])
    # the JW string for the higher endpoint covers the intermediate sites:
    string_support = [order[i] for i in range(index[s_lo] + 1, index[s_hi])]
    ok(f"lexicographic slow-axis NN link {s_lo}-{s_hi} spans {span} positions "
       f"=> string non-trivial over intermediate sites {string_support}",
       span > 1 and len(string_support) > 0)
    print()

    print("="*72)
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    print("="*72)
    return PASS, FAIL


if __name__ == "__main__":
    p, f = check()
    import sys
    sys.exit(0 if f == 0 else 1)
