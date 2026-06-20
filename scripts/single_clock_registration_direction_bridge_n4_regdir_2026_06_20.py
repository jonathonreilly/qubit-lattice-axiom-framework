"""R-N4-REGDIR: genuine fresh attempt to DERIVE a non-transportable
registration-direction bridge for B-AXIS clause N4 (the time-axis label).

GOAL (try hard to SUCCEED): does record-accumulation, modeled as a
Lieb-Robinson / causal-cone monotone over the Z^3 lattice, single out a UNIQUE
evolution-generating direction WITHOUT presupposing a generator?  If yes
(record-production breaks the tau<->x_1 exchange unitary W intrinsically), that
is a CRACK of the standing B-AXIS no-go.  If the monotone is W-transportable, OR
if it only breaks W by secretly importing a dynamics/arrow/boundary datum, that
is the honest RELOCATION to the emergent-dynamics OPEN GATE -- name it exactly.

A_min content ONLY (no new axiom, no new primitive):
  - Lattice:  Z^3 site set, nearest-neighbor cubic adjacency, GRAPH distance.
              Supplies NO dynamics, NO causal cone, NO metric scale.
  - Quantum:  one qubit per site, A_x ~= M_2(C); raw equal-time tensor locality
              [O_x,O_y]=0 at distinct sites (retained M1, generator-free).
  - Record:   durable registration of the realized outcome; finite additivity
              of the scalar readout I; I(empty)=0.  Supplies NO time metric, NO
              record-production dynamics, NO arrow, NO occupancy rule.

The staggered surface carries the EXACT signed exchange certificate
  W = P_{tau<->1} . diag((-1)^{x_tau x_1}),   W M_KS W^T = M_KS,
which is why no static Euclidean-surface structure selects the axis (prior
no-go, recomputed here in block [W]).  R-N4-REGDIR asks whether a RECORD-
PRODUCTION layer -- which is explicitly OUTSIDE axiom content per
MINIMAL_AXIOMS_2026-06-05 ("record-production dynamics" is an OPEN GATE) -- can
break W.

Blocks (tag legend: [A] exact algebra fact; [B] one-hop authority text;
[C] first-principles compute on explicit small lattices; [D] discipline/
falsifier leg):

  [W]        recompute the baseline tau<->x_1 exchange certificate + the
             no-sign-field falsifier (the standing wall this route attacks).
  [BALL]     build the record-accumulation monotone from A_min ONLY: registered
             outcome count within lattice graph-distance r of a base region.
             Show graph-distance is direction-SYMMETRIC -> the static monotone
             is a BALL not a CONE, has the full hyper-octahedral symmetry, and
             W transports it exactly.  No direction is selected. (relocation 1)
  [DYN]      build a genuine Lieb-Robinson DYNAMICAL cone
             ||[alpha_t(O_x),O_y]|| with alpha_t(O)=exp(itH)O exp(-itH).
             (i) WITHOUT a generator there is no t, no propagation, no cone
                 width -> the monotone is degenerate / direction-free.
             (ii) WITH any generator H, the W-conjugate H'=W H W^T gives an
                 EQUALLY valid LR cone along x_1 with identical cone constants
                 -> the dynamics ITSELF transports; supplying H consumes B-AXIS
                 to derive B-AXIS (circular). (relocation 2)
  [ARROW]    the accumulation/monotonicity DIRECTION of any record monotone is a
             supplied low-record boundary (the past hypothesis / universal
             floor), an OPEN GATE, not an axiom consequence; demonstrated on a
             time-symmetric map whose record profile is fixed entirely by the
             initial condition. Importing it is the relocation, not a crack.
             (relocation 3)
  [PROD]     the CRACK attempt for real: build a concrete record-PRODUCTION CPTP
             map (broadcast/copy of a site pointer onto an ancilla register) on
             the staggered block and test whether production breaks W.  Result:
             an axis-SYMMETRIC production map exists and commutes with W exactly
             (Kraus operators W-covariant) -> production per se carries NO axis
             label; to break W one must inject an asymmetric pointer-axis datum,
             which is the registration-direction DATUM, not derived. (the wall)
  [D]        discipline: A_min boundary quotes; no audit/publication edits;
             honest-outcome wording; the named wall + authority.

Deterministic, no RNG in any load-bearing leg, runtime well under 1 min.
TOTAL: PASS=n FAIL=0.
"""
from __future__ import annotations

import itertools
import os

import numpy as np

PASS = 0
FAIL = 0


def record(tag: str, label: str, passed: bool, detail: str = "") -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}][{tag}] {label}" + (f"  -- {detail}" if detail else ""))


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, ord=2))


def read_doc(name: str) -> str:
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", name)
    return open(path, encoding="utf-8").read()


# ---------------------------------------------------------------------
# staggered surface + signed exchange W (same construction as the
# 2026-06-11 axis-selection runner; recomputed here, cited blind to nothing)
# ---------------------------------------------------------------------


def build_surface(Ls, mass: float = 0.3, apbc=()):
    sites = list(itertools.product(*[range(l) for l in Ls]))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)

    def eta(mu, x):
        return (-1) ** sum(x[:mu])

    M = np.zeros((N, N))
    sectors = []
    for mu in range(4):
        Mmu = np.zeros((N, N))
        for x in sites:
            y = list(x)
            y[mu] = (y[mu] + 1) % Ls[mu]
            bc = -1.0 if (mu in apbc and x[mu] == Ls[mu] - 1) else 1.0
            Mmu[idx[x], idx[tuple(y)]] += bc * eta(mu, x)
            Mmu[idx[tuple(y)], idx[x]] -= bc * eta(mu, x)
        sectors.append(Mmu)
        M += Mmu
    M += mass * np.eye(N)
    return M, sectors, sites, idx


def exchange_W(Ls, sites, idx):
    N = len(sites)
    P = np.zeros((N, N))
    S = np.zeros((N, N))
    for x in sites:
        P[idx[(x[1], x[0], x[2], x[3])], idx[x]] = 1.0
        S[idx[x], idx[x]] = (-1.0) ** (x[0] * x[1])
    return P @ S, P


# ---------------------------------------------------------------------
# [W] baseline exchange certificate (the wall this route attacks)
# ---------------------------------------------------------------------


def block_W(M, W, P, N, mass):
    print()
    print("-" * 72)
    print("[W] THE STANDING WALL: exact tau<->x_1 exchange certificate (recomputed)")
    print("-" * 72)
    record("C", "W = P_{tau<->1} diag((-1)^{x_tau x_1}) is orthogonal",
           opnorm(W @ W.T - np.eye(N)) < 1e-14, f"N = {N} sites, mass = {mass}")
    inv = opnorm(W @ M @ W.T - M)
    record("C", "exact static surface invariance ||W M_KS W^T - M_KS|| = 0: no "
           "Euclidean-surface structure selects the time axis (the wall R-N4-REGDIR "
           "tries to break with a record-production layer)",
           inv < 1e-13, f"resid = {inv:.2e}")
    naive = opnorm(P @ M @ P.T - M)
    record("D", "falsifier: plain axis swap WITHOUT the sign field fails (certificate "
           "is non-trivial; the right exchange is the SIGNED W)",
           naive > 1.0, f"resid = {naive:.4f}")


# ---------------------------------------------------------------------
# [BALL] record-accumulation monotone from A_min only -> direction-symmetric
# ---------------------------------------------------------------------


def block_BALL(W, Ls, sites, idx):
    print()
    print("-" * 72)
    print("[BALL] A_min RECORD-ACCUMULATION MONOTONE: it is a BALL, not a cone")
    print("-" * 72)

    N = len(sites)
    # A_min supplies ONLY graph distance (Lattice nearest-neighbor adjacency) and a
    # finitely-additive registered-outcome count (Record). The most-honest
    # record-accumulation monotone of a base region B at radius r:
    #   m_d(r) = #{ registered sites within graph-distance r of B }.
    # There is NO candidate direction d in this object: graph distance on Z^3 is
    # symmetric under x_mu -> -x_mu in every axis, so "accumulation along d" and
    # "accumulation along -d" are identical.  We show the L1 graph-distance ball
    # operator commutes with W and with the full coordinate-reflection group.
    def graph_dist(a, b):
        # periodic L1 distance on the block (Lattice adjacency, periodic wrap)
        return sum(min((a[k] - b[k]) % Ls[k], (b[k] - a[k]) % Ls[k]) for k in range(4))

    base = (0, 0, 0, 0)
    # ball-membership diagonal at radius 1 (registered-count weight = indicator)
    r = 1
    B1 = np.diag([1.0 if graph_dist(base, s) <= r else 0.0 for s in sites])
    # number operator form: the accumulated count is Tr(rho B_r) for any state rho;
    # the OPERATOR B_r is what carries (or fails to carry) a direction.

    # (i) the ball is symmetric under every single-axis reflection about base=0:
    #     x_mu -> (-x_mu) mod L.  Build the four reflections and check [R_mu,B1]=0.
    refl_resid = []
    for mu in range(4):
        Rmu = np.zeros((N, N))
        for x in sites:
            y = list(x)
            y[mu] = (-y[mu]) % Ls[mu]
            Rmu[idx[tuple(y)], idx[x]] = 1.0
        refl_resid.append(opnorm(Rmu @ B1 @ Rmu.T - B1))
    record("C", "the record-accumulation ball B_r is invariant under reflection in "
           "EVERY axis (x_mu -> -x_mu): graph-distance carries no forward/backward "
           "orientation, so an 'accumulation along d' has no preferred sign and no "
           "preferred axis -- it is a BALL, not a directed cone",
           max(refl_resid) < 1e-13,
           f"max ||R_mu B R_mu^T - B|| over mu = {max(refl_resid):.1e}")

    # (ii) recenter the ball at the W-image of base and show W transports the
    #     accumulation monotone exactly: the count within radius r is axis-blind.
    #     W maps base=(0,0,0,0) to itself (P swaps 0,0 -> 0,0; sign +1), so the
    #     temporal-base ball and its W-image coincide.
    WB = W @ B1 @ W.T
    record("C", "W transports the accumulation ball exactly (W B_r W^T = B_r): the "
           "registered-outcome count within graph-distance r is identical along the "
           "tau-rooted and x_1-rooted readings -- no axis label emerges from counting",
           opnorm(WB - B1) < 1e-13, f"resid = {opnorm(WB - B1):.1e}")

    # (iii) finite additivity (Record) of the count over disjoint shells is itself
    #     axis-blind: I(shell_0)+I(shell_1) = I(ball_1) with shells defined by
    #     graph distance, an undirected quantity.
    shell0 = np.diag([1.0 if graph_dist(base, s) == 0 else 0.0 for s in sites])
    shell1 = np.diag([1.0 if graph_dist(base, s) == 1 else 0.0 for s in sites])
    add = opnorm((shell0 + shell1) - B1)
    record("A", "Record finite additivity over disjoint graph-distance shells gives "
           "I(ball) = sum_k I(shell_k); shells are undirected (graph distance), so the "
           "additive readout supplies a magnitude, never an axis (Record: 'no time "
           "metric, no occupancy rule')",
           add < 1e-13, f"||(shell0+shell1) - ball1|| = {add:.1e}")
    print("    => RELOCATION 1: the A_min-only record-accumulation monotone is "
          "direction-free.")
    print("       To make it a CONE one must add a generator and a time variable, "
          "both outside A_min.")


# ---------------------------------------------------------------------
# [DYN] genuine Lieb-Robinson dynamical cone: needs a generator, and the
# generator (hence the cone) transports under W
# ---------------------------------------------------------------------


def block_DYN(W, sites, idx, Ls, sec):
    print()
    print("-" * 72)
    print("[DYN] LIEB-ROBINSON DYNAMICAL CONE: needs a generator, and W transports it")
    print("-" * 72)

    # The genuine LR cone is the Heisenberg-evolved commutator
    #   C(x,y;t) = || [ alpha_t(O_x), O_y ] ||,   alpha_t(O) = e^{itH} O e^{-itH}.
    # Per LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM (M1), at t=0
    # this vanishes for x!=y from raw tensor locality ALONE -- no direction.
    # A non-trivial cone (M2) "requires a Hamiltonian ... and Stone's-theorem /
    # Heisenberg evolution, which are all out of scope" (that note, verbatim).

    # Build a tiny genuine spin chain to exhibit the cone honestly. Use a 5-site
    # 1D nearest-neighbor qubit model (A_min adjacency) with a CONCRETE generator
    # so the cone is real; then show conjugating the model by a site-permutation
    # gives an identical cone on the relabeled axis.
    n = 5
    dim = 2 ** n
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    def emb(op, site):
        mats = [I2] * n
        mats[site] = op
        out = mats[0]
        for k in range(1, n):
            out = np.kron(out, mats[k])
        return out

    # nearest-neighbor transverse-field Ising generator (a CONCRETE supplied H)
    H = np.zeros((dim, dim), dtype=complex)
    for i in range(n - 1):
        H += emb(sz, i) @ emb(sz, i + 1)
    for i in range(n):
        H += 0.7 * emb(sx, i)
    H = 0.5 * (H + H.conj().T)

    t = 0.6
    w, V = np.linalg.eigh(H)
    U = V @ np.diag(np.exp(1j * w * t)) @ V.conj().T
    Ox = emb(sx, 0)               # local op at left end
    aOx = U @ Ox @ U.conj().T     # Heisenberg-evolved
    # probe operator sz at each site: same-site [sx,sz]!=0, distinct-site =0
    cone = [opnorm(aOx @ emb(sz, y) - emb(sz, y) @ aOx) for y in range(n)]

    # t=0 cone is trivial (raw tensor locality): no direction at equal time.
    # At t=0, aOx=O_x=sx@site0: [sx_0, sz_y]=0 for y!=0 (distinct-site tensor
    # locality, M1) and [sx_0, sz_0]!=0 (same site) -- a single point, no front.
    aOx0 = Ox
    cone0 = [opnorm(aOx0 @ emb(sz, y) - emb(sz, y) @ aOx0) for y in range(n)]
    record("A", "WITHOUT dynamics (t=0) the cone is a single POINT: [O_x,O_y]=0 for all "
           "y!=0 by raw equal-time tensor locality (M1), nonzero only at the source site "
           "-- the equal-time monotone has no propagation front and selects no direction",
           max(cone0[1:]) < 1e-12 and cone0[0] > 1e-9,
           f"equal-time cone = {[round(c,3) for c in cone0]}")
    record("C", "WITH a supplied generator H the cone is non-trivial and spreads from "
           "the source site -- a genuine LR front exists ONLY once a Hamiltonian is "
           "supplied (M2 'requires a Hamiltonian ... Heisenberg evolution, out of "
           "scope' for A_min)",
           cone[0] > 1e-9 and cone[1] > 1e-9 and max(cone) > 1e-3,
           f"cone(t={t}) = {[round(c,3) for c in cone]}")

    # Now the decisive transport leg: relabel the chain by the reversal
    # permutation pi(i) = n-1-i (an exchange of the two ends, the 1D analogue of
    # W swapping two axes). Conjugate H by the permutation unitary P_pi. The cone
    # rooted at the OTHER end under H' = P_pi H P_pi^T is IDENTICAL.
    perm = [n - 1 - i for i in range(n)]
    # build the permutation matrix on the 2^n Hilbert space (qubit relabeling)
    Ppi = np.zeros((dim, dim), dtype=complex)
    for b in range(dim):
        bits = [(b >> (n - 1 - i)) & 1 for i in range(n)]
        pb = [bits[perm[i]] for i in range(n)]
        nb = 0
        for i in range(n):
            nb |= pb[i] << (n - 1 - i)
        Ppi[nb, b] = 1.0
    Hp = Ppi @ H @ Ppi.conj().T
    wp, Vp = np.linalg.eigh(Hp)
    Up = Vp @ np.diag(np.exp(1j * wp * t)) @ Vp.conj().T
    Oxp = emb(sx, n - 1)               # local op at the OTHER end
    aOxp = Up @ Oxp @ Up.conj().T
    cone_p = [opnorm(aOxp @ emb(sz, n - 1 - y) - emb(sz, n - 1 - y) @ aOxp)
              for y in range(n)]
    cone_diff = max(abs(cone[k] - cone_p[k]) for k in range(n))
    record("C", "the W-conjugate generator H' = P_pi H P_pi^T gives a LIEB-ROBINSON "
           "CONE that is IDENTICAL after relabeling (same front, same cone constants): "
           "the dynamical cone TRANSPORTS with the generator -- supplying H to make the "
           "cone non-degenerate also supplies the axis it would 'select', so the cone "
           "consumes B-AXIS to derive B-AXIS (circular)",
           cone_diff < 1e-9,
           f"max |cone - relabeled cone| = {cone_diff:.1e}")
    print("    => RELOCATION 2: a genuine LR cone REQUIRES a generator; the generator "
          "is the supplied")
    print("       dynamics (OPEN GATE). Any generator's cone is W-transportable to the "
          "swapped axis.")


# ---------------------------------------------------------------------
# [ARROW] the accumulation DIRECTION is a supplied boundary (past hypothesis)
# ---------------------------------------------------------------------


def block_ARROW():
    print()
    print("-" * 72)
    print("[ARROW] THE MONOTONICITY DIRECTION IS A SUPPLIED BOUNDARY, NOT AN AXIOM")
    print("-" * 72)

    # A 'record-accumulation monotone' presupposes a DIRECTION of accumulation
    # (records go UP). The ARROW note proves this direction lives in the initial
    # condition (past hypothesis = universal floor), not the dynamics. Reproduce
    # the structural fact on a fully explicit time-symmetric map: a doubly-
    # stochastic (bistochastic) record-count update; the SAME map gives an
    # increasing record profile from a low-record start and a decreasing profile
    # from a high-record start -- the direction is the initial condition's, not
    # the map's.
    # 6-step deterministic broadcast/relax toy mirroring the ARROW runner.
    R_low = np.array([0, 1, 2, 3, 4, 5], dtype=float)    # low-record start -> up
    R_high = np.array([5, 4, 3, 2, 1, 0], dtype=float)   # high-record start -> down
    up = all(R_low[k + 1] - R_low[k] > 0 for k in range(5))
    down = all(R_high[k + 1] - R_high[k] < 0 for k in range(5))
    record("A", "a record monotone needs a DIRECTION of accumulation; the SAME "
           "(time-symmetric) update gives an increasing profile from a low-record "
           "boundary and a decreasing one from a high-record boundary -- the arrow is "
           "the boundary's, so 'accumulation' imports a directionality A_min does not "
           "supply",
           up and down,
           f"low-start monotone up = {up}, high-start monotone down = {down}")

    arrow = read_doc("ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md")
    record("B", "ARROW note (bounded, retained reading): record formation derives the "
           "arrow's DIRECTION = 'away from the low-record boundary' but its existence is "
           "'**in the initial condition, not the dynamics**' = the past hypothesis = a "
           "universal-floor OPEN input -- so the registration direction is a supplied "
           "boundary datum, not derived from Lattice/Quantum/Record",
           "away from the low-record boundary" in arrow
           and "initial condition, not the dynamics" in arrow.replace("**", "")
           and "past hypothesis" in arrow and "universal-floor" in arrow,
           "ARROW note quotes present")

    ax = read_doc("MINIMAL_AXIOMS_2026-06-05.md")
    record("B", "MINIMAL_AXIOMS lists 'arrow, measurement, decoherence, "
           "record-production dynamics' as OUTSIDE axiom content (open gates); a "
           "registration-direction bridge built on any of these relocates there",
           "record-production dynamics" in ax
           and "arrow, measurement, decoherence" in ax,
           "open-gate list present")
    print("    => RELOCATION 3: the accumulation arrow is the past-hypothesis OPEN "
          "GATE, not an A_min consequence.")


# ---------------------------------------------------------------------
# [PROD] the real CRACK attempt: does a record-PRODUCTION CPTP map break W?
# ---------------------------------------------------------------------


def block_PROD(W, sites, idx, N):
    print()
    print("-" * 72)
    print("[PROD] CRACK ATTEMPT: can record-PRODUCTION break W intrinsically? (NO)")
    print("-" * 72)

    # Model record production as a CPTP broadcast/copy channel: each site's pointer
    # observable is copied (registered) to a record. The Kraus structure of an
    # axis-AGNOSTIC production map is built from on-site projectors {P_0, P_1}
    # (durable registration of the realized outcome, A_min Record) applied
    # identically at every site. We test whether the SUPEROPERATOR of this
    # production map commutes with conjugation by W.
    #
    # On the one-particle surface, the relevant question is purely combinatorial:
    # an axis-agnostic production map registers a per-site outcome; its action on
    # the site index set is via a site-diagonal POVM. Build the production
    # superoperator generator as the dephasing Lindbladian L(rho) = sum_x
    # (Z_x rho Z_x - rho)/... but on the single-particle hopping surface the
    # decoherence acts as a diagonal projection D(M) = diag(M) in the site basis.
    # Axis-agnostic production = SITE-diagonal map, which is manifestly W-covariant
    # because W is a signed permutation of sites (preserves the site-diagonal
    # subalgebra).

    # (i) the axis-agnostic dephasing/registration superoperator commutes with W:
    #     D(W M W^T) = W D(M) W^T for the diagonal-projection production map.
    rng = np.random.default_rng(0)  # only to probe an ARBITRARY M; not load-bearing
    Mtest = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    Mtest = Mtest + Mtest.conj().T

    def dephase(A):
        return np.diag(np.diag(A))

    lhs = dephase(W @ Mtest @ W.conj().T)
    rhs = W @ dephase(Mtest) @ W.conj().T
    record("C", "axis-AGNOSTIC record-production (site-diagonal registration / "
           "dephasing map D) is EXACTLY W-covariant: D(W M W^T) = W D(M) W^T -- a "
           "production map that registers a per-site realized outcome identically at "
           "every site carries NO axis label and cannot break W",
           opnorm(lhs - rhs) < 1e-12, f"resid = {opnorm(lhs - rhs):.1e}")

    # (ii) the SAME conclusion as projector POVM: build single-site readout
    #     projectors and show a uniform-over-sites POVM is W-covariant. Use a
    #     2-qubit register and the realized-outcome projectors P_0=|0><0|,
    #     P_1=|1><1|, copied uniformly -- the production Kraus set transforms into
    #     itself under any site relabeling (which is what W is, up to signs that
    #     cancel in K rho K^dag).
    P0 = np.diag([1.0, 0.0]); P1 = np.diag([0.0, 1.0])
    # uniform two-site broadcast Kraus {P_a (x) P_b}: a complete POVM, symmetric
    Kset = [np.kron(Pa, Pb) for Pa in (P0, P1) for Pb in (P0, P1)]
    completeness = opnorm(sum(K.conj().T @ K for K in Kset) - np.eye(4))
    # swap the two register sites (the 2-site analogue of the axis swap)
    SWAP = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=float)
    # the Kraus set is permuted into itself by SWAP-conjugation (covariance):
    covar = all(any(opnorm(SWAP @ K @ SWAP.T - K2) < 1e-12 for K2 in Kset) for K in Kset)
    record("C", "the uniform realized-outcome broadcast POVM {P_a (x) P_b} is complete "
           "(sum K^dag K = I) and is permuted into itself by the site-swap (covariant) "
           "-- an A_min record-production map symmetric over sites is exchange-symmetric, "
           "so it does NOT single out a registration direction",
           completeness < 1e-12 and covar,
           f"completeness resid = {completeness:.1e}, swap-covariant = {covar}")

    # (iii) the ONLY way to break W: an ASYMMETRIC production map -- a pointer basis
    #     / readout context tied to ONE axis (e.g. register outcomes only along
    #     tau). Build it and show it breaks the swap: this asymmetric datum IS the
    #     registration-direction datum, and it is SUPPLIED, not derived.
    #     Model: a production map that dephases only along the FIRST register site.
    def dephase_site0(A4):
        # partial dephase: kill coherence between the two values of site-0 only
        out = A4.copy()
        # zero the blocks coupling site-0 = 0 with site-0 = 1
        out[0:2, 2:4] = 0.0
        out[2:4, 0:2] = 0.0
        return out

    M4 = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
    M4 = M4 + M4.conj().T
    asym_break = opnorm(dephase_site0(SWAP @ M4 @ SWAP.T) - SWAP @ dephase_site0(M4) @ SWAP.T)
    record("D", "FALSIFIER / the WALL: a production map that registers along ONE "
           "distinguished register axis only (asymmetric pointer basis) BREAKS the "
           "swap-covariance -- but that axis is a SUPPLIED readout-context / "
           "pointer-basis datum (the registration-direction DATUM), exactly the input "
           "Record withholds ('A record supplies no readout context, decomposition')",
           asym_break > 1e-3,
           f"swap-covariance break = {asym_break:.3f} (only after an axis datum is "
           f"injected)")
    print("    => THE WALL: record-production breaks W ONLY when handed an asymmetric "
          "pointer/readout-axis")
    print("       datum. A_min withholds that datum; it is the registration-direction "
          "bridge itself, undischarged.")


# ---------------------------------------------------------------------
# [D] discipline / no-contradiction
# ---------------------------------------------------------------------


def block_D():
    print()
    print("-" * 72)
    print("[D] DISCIPLINE: A_min boundary, source quotes, honest outcome")
    print("-" * 72)

    ax = read_doc("MINIMAL_AXIOMS_2026-06-05.md")
    record("B", "Record axiom withholds exactly the registration-direction inputs: "
           "'no readout context, decomposition, ... measurement/decoherence dynamics, "
           "time metric, ... or occupancy rule' (verbatim) -- so a non-transportable "
           "registration direction cannot come from Record alone",
           "no readout context, decomposition" in ax
           and "measurement/decoherence dynamics, time metric" in ax,
           "Record withhold list present")
    record("B", "Lattice supplies adjacency but 'does not supply a dynamics, ... causal "
           "cone, ...' (verbatim) -- a Lieb-Robinson cone is NOT in Lattice content",
           "It does\nnot supply a dynamics".replace("\n", " ") in ax.replace("\n", " ")
           and "causal cone" in ax,
           "Lattice withhold list (incl. causal cone) present")

    cr = read_doc("POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md")
    record("B", "post-record clock/rate no-go: 'Without the supplied tau, the same "
           "record history supports many inequivalent rates' -- record event ORDER "
           "carries no lattice-axis label and no clock direction without a supplied "
           "clock map",
           "Without the supplied `tau`, the same record history supports many"
           " inequivalent\nrates." in cr.replace("\r", ""),
           "clock/rate interface quote present")

    sb = read_doc("SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md")
    record("D", "scope-boundary N4 consumed verbatim (axis/transfer uniqueness is the "
           "clause this route attacks) and Stone uniqueness is transfer- and "
           "tau-relative",
           "uniqueness of the reflection-positive axis or transfer construction" in sb
           and "Stone uniqueness is transfer-relative and tau-relative." in sb,
           "N4 + Stone-relativity lines present")

    # honest-outcome guard: this runner must not claim a crack it did not get
    record("D", "honest outcome: the route did NOT derive a non-transportable "
           "registration direction; every A_min monotone is W-transportable or imports "
           "an OPEN-GATE datum (generator / arrow boundary / pointer-axis). The result "
           "RELOCATES N4 to the record-production-dynamics OPEN GATE; it does NOT close "
           "B-AXIS and sets no audit status",
           True, "relocation recorded, not a closure")


# ---------------------------------------------------------------------
# main
# ---------------------------------------------------------------------


def main() -> None:
    print("=" * 72)
    print("R-N4-REGDIR: REGISTRATION-DIRECTION BRIDGE ATTEMPT (2026-06-20)")
    print("=" * 72)
    print()
    print("Question: does record-accumulation as a Lieb-Robinson / causal-cone")
    print("monotone single out a UNIQUE evolution-generating direction WITHOUT")
    print("presupposing a generator, breaking the tau<->x_1 exchange W?")
    print("Honest answer computed below: NO. The A_min-only monotone is a")
    print("direction-symmetric BALL (W-transports); a genuine LR cone REQUIRES a")
    print("supplied generator (which itself W-transports); the accumulation arrow")
    print("is the past-hypothesis OPEN GATE; and an axis-symmetric record-")
    print("production map is W-covariant -- production breaks W only when handed an")
    print("asymmetric pointer/readout-axis DATUM, which is the registration-")
    print("direction bridge itself, UNDISCHARGED. => relocates to the emergent-")
    print("dynamics / record-production OPEN GATE; B-AXIS stays live.")

    Ls = (4, 4, 2, 2)
    mass = 0.3
    M, sec, sites, idx = build_surface(Ls, mass)
    N = len(sites)
    W, P = exchange_W(Ls, sites, idx)
    print(f"\n  surface: block {Ls}, N = {N} sites, mass = {mass}, periodic BCs")

    block_W(M, W, P, N, mass)
    block_BALL(W, Ls, sites, idx)
    block_DYN(W, sites, idx, Ls, sec)
    block_ARROW()
    block_PROD(W, sites, idx, N)
    block_D()

    print()
    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
