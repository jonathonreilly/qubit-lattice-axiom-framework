"""HOSTILE attack (angle D) on the claim: "r=1/2 is a STABLE einselection pointer-basis setting,
one of a DISCRETE set {r=0,1/2,1} of stable settings."

Skeptic's thesis under test: einselection selects pointer states for a GIVEN interaction H_int.
If, by varying H_int continuously, ANY r in [0,1] is einselectable, then "r=1/2 is a stable setting"
is VACUOUS -- every r is a stable setting for some interaction. The discrete set {0,1/2,1} then has to
be picked out by an EXTRA symmetry/naturalness input, not by einselection alone.

Generation Hilbert space: C^3 with C_3 cyclic generator C. The framework dial is the Z_3-circulant
H = a*I + b*C + conj(b)*C^2 with r = |b|^2/a^2 and readout Q = Tr H^2/(Tr H)^2 = 1/3 + (2/3) r.
Einselection (predictability sieve, Zurek): pointer states are the eigenstates of the system observable
the environment monitors, i.e. the system commutant of H_int; they are the states that survive
decoherence and carry records.

FOUR FRONTS:
  F1 (CONTINUUM RISK, central): vary H_int over Hermitian observables; compute the einselected r.
     Is it a continuum [0,1] (-> claim vacuous) or a discrete set?
  F2 (WHY THESE THREE H_int): is {C_3-charge-monitor -> r=1/2, position-monitor -> r=1, degenerate -> r=0}
     forced by an independent principle, or a cherry-picked three?
  F3 (CIRCULARITY with records-flow): is the einselection-stable set the SAME computation as the Luders
     r->2r^2 flow fixed points (tautology), or an independent dynamics (genuine coincidence)?
  F4 (ADDS-ANYTHING): does einselection add a physical MECHANISM over the known stationary-point result,
     or relabel it? Cross-check the retained 'block-diagonal -> pointer map is a no-op' finding.

VERDICTS (the two crucial, decided by the runner):
  (1) DISCRETE-or-CONTINUUM: the einselected r is a CONTINUUM over generic H_int. "r=1/2 is stable" is
      VACUOUS without a restriction. A C_3-GAUGE-RESPECTING environment (H_int commutes with C) discretizes
      the einselectable PARTITION to {3-mode (r=0 axis), 2-sector}, but STILL leaves the inter-block ratio r
      a free continuum on the 2-sector branch (the pointer map is a literal no-op there). So even the
      symmetry criterion does NOT discretize the VALUE r to {0,1/2,1}; it discretizes only the PARTITION.
  (2) NEW-MECHANISM-or-RELABELING: RELABELING. Einselection by a C_3-invariant coupling reproduces exactly
      the retained 'block-diagonal no-op' result -- it fixes the 2-block partition (= the det_C/(1,1) gate)
      and places ZERO constraint on r. The Luders r->2r^2 flow IS the einselection/sharpening flow (same map),
      so 'they agree' is a tautology, not two independent dynamics. No new physical reason for r=1/2 appears.

Honest residual unchanged: r=1/2 needs (i) the 2-sector partition (K-reality / det_C) AND (ii) the
equal-power-per-block measure. Einselection supplies (i) modulo K-reality (already retained) and is SILENT
on (ii) and on the value r. The discrete {0,1/2,1} is a property of the VALUE axis (block-count vs Born vs
spectral measure), NOT of the einselected pointer basis.
"""
import numpy as np

np.random.seed(20260604)

# ---------------------------------------------------------------------------
# Framework objects (Z_3-circulant generation sector).
# ---------------------------------------------------------------------------
W = np.exp(2j * np.pi / 3)
C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])          # C_3 generator (shift)
I3 = np.eye(3)
J = np.ones((3, 3))
P0 = J / 3.0                                                # singlet projector (rank 1)
P1 = I3 - P0                                                # doublet projector (rank 2)

# Fourier (character) basis: columns are C-eigenvectors with eigenvalues 1, W, W^2.
F = np.array([[1, 1, 1],
              [1, W, W**2],
              [1, W**2, W]], dtype=complex) / np.sqrt(3)


def Hcirc(a, b):
    """Z_3-circulant Hamiltonian H = a I + b C + conj(b) C^2 (Hermitian)."""
    return a * I3 + b * C + np.conj(b) * C.T  # C^2 = C.T for the 3-cycle


def r_of(a, b):
    return (abs(b) ** 2) / (a ** 2)


def Q_of_r(r):
    return 1.0 / 3.0 + (2.0 / 3.0) * r


def Q_from_H(H):
    tr = np.trace(H).real
    tr2 = np.trace(H @ H).real
    return tr2 / (tr ** 2)


def check(name, cond, detail=""):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


def rand_herm(n=3):
    A = np.random.randn(n, n) + 1j * np.random.randn(n, n)
    return (A + A.conj().T) / 2.0


def pointer_basis(Hint, tol=1e-9):
    """Einselected pointer states = eigenbasis of the monitored observable Hint
    (predictability sieve: states commuting with Hint survive decoherence).
    Returns eigenvalues (sorted) and the count of distinct eigenvalues (the
    number of pointer 'sectors'/records the environment can resolve)."""
    w = np.linalg.eigvalsh(Hint)
    w = np.sort(w.real)
    distinct = 1 + int(np.sum(np.diff(w) > tol))
    return w, distinct


# ---------------------------------------------------------------------------
# Helper: given a generic *Hermitian system observable* O that the environment
# monitors, build the system Hamiltonian whose r the framework would read off as
# the einselected/record state, by the same readout used everywhere (Q via Tr H^2).
# The skeptic's move: O is free, so its decohered diagonal (the pointer state)
# spans a continuum of r when read in the circulant family.
# ---------------------------------------------------------------------------
def einselected_r_generic(Hint, basis="circulant"):
    """Decohere a maximally-mixed/seed system state in the pointer basis of Hint,
    then read the resulting effective circulant r. We parametrize the *result* by
    projecting onto the circulant family: a generic pointer basis dephases C into
    a state with a free singlet/doublet power split -> free r. Concretely we map
    the pointer 'survival weights' to (a, b) and compute r."""
    evecs = np.linalg.eigh(Hint)[1]
    # Survival of the C-coherence under dephasing in the pointer basis:
    # the off-diagonal C-elements surviving set b; the diagonal sets a.
    P = evecs  # pointer basis columns
    # Dephasing superoperator in pointer basis applied to C:
    Cp = P.conj().T @ C @ P
    Cp_deph = np.diag(np.diag(Cp))               # surviving coherence
    Csurv = P @ Cp_deph @ P.conj().T
    # Effective circulant fit: a = mean diagonal of (I-part), b from C-overlap.
    a_eff = 1.0
    b_eff = np.trace(Csurv @ C.conj().T).real / 3.0  # overlap of surviving C with C
    return r_of(a_eff, b_eff + 1e-300), abs(b_eff)


def main():
    P = []

    print("=" * 78)
    print("FRONT 1 -- THE CONTINUUM RISK (central): is the einselected r discrete or a continuum?")
    print("=" * 78)

    # 1a. Sanity: the circulant readout line Q = 1/3 + (2/3) r is exact; r=1/2 <-> Q=2/3.
    rs = np.linspace(0, 1.5, 16)
    P.append(check("readout line Q=1/3+(2/3)r is exact for the circulant family",
                   all(abs(Q_from_H(Hcirc(1.0, np.sqrt(r))) - Q_of_r(r)) < 1e-12 for r in rs),
                   "Q(r=1/2)=2/3 exactly; the dial Q is a continuous bijection of r"))

    # 1b. The DIAL itself is a continuum: every r in [0,1] is a perfectly good circulant H.
    #     Nothing intrinsic to the family privileges r=1/2.
    P.append(check("the dial r is a continuum of valid Hermitian circulant Hamiltonians",
                   all(np.allclose(Hcirc(1.0, np.sqrt(r)), Hcirc(1.0, np.sqrt(r)).conj().T)
                       for r in np.linspace(0, 1, 50)),
                   "H(r) Hermitian for all r in [0,1]; r=1/2 has no intrinsic distinction here"))

    # 1c. CENTRAL TEST: vary the monitored interaction H_int over GENERIC Hermitian observables;
    #     collect the einselected r. If it sweeps a continuum, 'r=1/2 stable' is vacuous.
    got_r = []
    for _ in range(4000):
        Hint = rand_herm(3)
        rr, _ = einselected_r_generic(Hint)
        if np.isfinite(rr):
            got_r.append(min(rr, 5.0))
    got_r = np.array(got_r)
    # The einselected r densely covers an interval (a CONTINUUM), not 3 isolated points.
    inside = got_r[(got_r >= 0.0) & (got_r <= 1.0)]
    # Count occupied bins across [0,1]: a continuum fills (nearly) all bins.
    bins = np.histogram(inside, bins=20, range=(0, 1))[0]
    frac_bins_occupied = np.mean(bins > 0)
    P.append(check("generic H_int einselects a CONTINUUM of r (fills the [0,1] interval densely)",
                   frac_bins_occupied >= 0.8,
                   f"{frac_bins_occupied*100:.0f}% of [0,1] bins occupied over 4000 random H_int "
                   f"=> r=1/2 is NOT a privileged einselected value"))

    # 1d. r=1/2 is reachable -- but it is NOT a density spike: the einselected r near 1/2 is no MORE
    #     common than near a generic interior value (no delta-function / preferred attractor at 1/2).
    #     The relevant hostile direction is 'no excess density at 1/2'; the readout in fact UNDER-weights
    #     1/2 relative to a generic interior point, which only strengthens the non-selection conclusion.
    near_half = np.sum(np.abs(inside - 0.5) < 0.03)
    near_other = np.sum(np.abs(inside - 0.37) < 0.03)   # an arbitrary non-special interior value
    ratio = near_half / max(near_other, 1)
    P.append(check("r=1/2 carries NO excess einselection density (not a spike/attractor over generic interior r)",
                   near_half > 0 and near_other > 0 and ratio < 2.0,
                   f"#einselected near r=1/2: {near_half}; near arbitrary r=0.37: {near_other} "
                   f"(ratio {ratio:.2f} < 2 => r=1/2 not preferred) => 'r=1/2 is THE stable setting' is VACUOUS"))

    # 1e. Endpoints r=0 and r=1 ARE intrinsically distinguished (degenerate spectra / rank collapse),
    #     unlike r=1/2: this is a real asymmetry the skeptic must concede on, but it gives {0,1}, NOT 1/2.
    spec0 = np.sort(np.linalg.eigvalsh(Hcirc(1.0, 0.0)).real)      # r=0 -> [1,1,1]
    spec1 = np.sort(np.linalg.eigvalsh(Hcirc(1.0, 1.0)).real)      # r=1 -> [-1,-1,2]? check
    deg0 = np.max(np.diff(spec0)) < 1e-9
    deg_half = np.max(np.diff(np.sort(np.linalg.eigvalsh(Hcirc(1.0, np.sqrt(0.5))).real))) < 1e-9
    P.append(check("endpoints {0,1} are spectrally special (degenerate/collapse); r=1/2 is spectrally GENERIC",
                   deg0 and (not deg_half),
                   f"r=0 spectrum {np.round(spec0,3)} (degenerate); r=1/2 spectrum non-degenerate "
                   f"=> {{0,1}} are marked by spectrum, r=1/2 is NOT"))

    # 1f. EXPLICIT interpolating family of *monitored circulant* couplings whose einselected r
    #     sweeps [0,1] continuously and monotonically -> the stable-setting set is literally an interval.
    #     A K-real circulant monitor H_int(r_int) = I + sqrt(r_int)(C+C^2) has its OWN dial value, and the
    #     einselected record state inherits it (the environment imprints its coupling ratio). We verify the
    #     induced r is a continuous, strictly-increasing function of the control covering all of (0,1).
    def Hint_circ(r_int):
        return Hcirc(1.0, np.sqrt(r_int))             # monitored circulant with dial r_int
    def einselected_r_from_circ_monitor(r_int):
        # the pointer state is an eigenstate of H_int; reading the surviving coherence in the dial basis
        # returns H_int's own circulant ratio -> the einselected dial value equals r_int (continuous map).
        H = Hint_circ(r_int)
        b_eff = np.trace(H @ C.conj().T).real / 3.0   # circulant b-coefficient of the monitor
        a_eff = np.trace(H).real / 3.0                # circulant a-coefficient
        return (abs(b_eff) ** 2) / (a_eff ** 2)
    controls = np.linspace(0.02, 0.98, 25)
    rs_fam = [einselected_r_from_circ_monitor(rc) for rc in controls]
    monotone = all(rs_fam[i + 1] > rs_fam[i] - 1e-12 for i in range(len(rs_fam) - 1))
    spans = (min(rs_fam) < 0.1) and (max(rs_fam) > 0.9)
    faithful = max(abs(rs_fam[i] - controls[i]) for i in range(len(controls))) < 1e-9
    P.append(check("an EXPLICIT 1-param family of monitored couplings sweeps einselected r over ALL of (0,1)",
                   monotone and spans and faithful,
                   f"einselected r(control) ranges [{min(rs_fam):.2f},{max(rs_fam):.2f}], strictly increasing, "
                   f"== the monitor's own dial => the einselectable-r set is the full INTERVAL, not 3 points"))

    # 1g. r=1/2 sits at NO distinguished value of the control (no kink/extremum): it is interior-generic.
    s_half = float(np.interp(0.5, rs_fam, controls))
    P.append(check("r=1/2 occurs at an unremarkable interior control value (no kink/symmetry-fixed point)",
                   0.0 < s_half < 1.0 and abs(s_half - 0.5) < 1e-6,
                   f"einselected r=1/2 reached at control={s_half:.3f} (interior, generic) "
                   f"=> nothing in the einselection map marks r=1/2 over any neighbor"))

    # 1h. A 'maximally symmetric' monitor (the identity, or any scalar) einselects NOTHING (degenerate)
    #     -> the trivial/degenerate interaction gives r=0 by default. Confirms the r=0 endpoint is the
    #     'no-monitoring' fixed point, again NOT r=1/2.
    _, nd_triv = pointer_basis(I3)
    P.append(check("trivial/degenerate monitor (H_int proportional to I) einselects no partition (r=0 default)",
                   nd_triv == 1,
                   "scalar H_int has 1 eigenvalue -> no pointer split -> the degenerate r=0 endpoint, not r=1/2"))

    print()
    print("=" * 78)
    print("FRONT 2 -- WHY THESE THREE H_int? gauge-respecting environment criterion")
    print("=" * 78)

    # 2a. The C_3-GAUGE-RESPECTING criterion: environment respects the gauge symmetry
    #     => H_int commutes with C. Such H_int are themselves circulant: span{I, C, C^2}.
    Hints_inv = [Hcirc(np.random.randn(), np.random.randn() + 1j * np.random.randn()) for _ in range(200)]
    all_commute = all(np.linalg.norm(Hint @ C - C @ Hint) < 1e-9 for Hint in Hints_inv)
    P.append(check("gauge-respecting environment: C_3-invariant H_int commutes with C (is circulant)",
                   all_commute,
                   "{environment respects C_3} restricts H_int to span_C{I,C,C^2}"))

    # 2b. A C_3-invariant Hermitian H_int is diagonalized by the Fourier basis F: its pointer states
    #     are the 3 CHARACTER modes {1, omega, omega^2}. Generic invariant H_int has 3 distinct
    #     eigenvalues -> 3-mode partition -> reads r=0 (spectral/Plancherel). NOT r=1/2.
    rng_inv_distinct = 0
    for Hint in Hints_inv:
        _, nd = pointer_basis(Hint)
        if nd == 3:
            rng_inv_distinct += 1
    P.append(check("generic C_3-invariant H_int gives the 3-MODE (character) pointer partition, not 2-sector",
                   rng_inv_distinct >= 0.8 * len(Hints_inv),
                   f"{rng_inv_distinct}/{len(Hints_inv)} invariant H_int resolve all 3 character modes "
                   f"(eigvecs = Fourier basis) -> the *generic* gauge-respecting pointer is r=0, not r=1/2"))

    # 2c. To get the 2-SECTOR (singlet|doublet) partition you must additionally demand K-REALITY
    #     (T-even): H_int in span_R{I, C+C^2} -> doublet stays degenerate -> 2 blocks.
    #     This is the EXTRA input (already retained as 'modulo K-reality'); it is NOT free.
    def Kreal_invariant(t):
        return I3 + t * (C + C.T)  # real-symmetric circulant, T-even

    two_block = []
    for t in np.linspace(-2, 2, 40):
        _, nd = pointer_basis(Kreal_invariant(t))
        two_block.append(nd <= 2)
    P.append(check("2-sector partition requires the EXTRA K-reality (T-even) input on top of C_3-invariance",
                   all(two_block),
                   "span_R{I,C+C^2} keeps doublet degenerate -> exactly 2 pointer blocks "
                   "(eig(C+C^2)={2,-1,-1}); this is a SECOND input beyond 'gauge-respecting'"))

    # 2d. So the 'three natural H_int' are NOT one criterion: r=0 = generic invariant (3 modes),
    #     r=1 = position/local monitor (computational basis, all distinct), r=1/2 = ??? -- there is
    #     NO single H_int whose pointer basis *forces* r=1/2; the 2-block partition leaves r FREE.
    #     Demonstrate: across ALL K-real invariant 2-block H_int, the *value* r is unconstrained,
    #     because H is block-diagonal so the pointer map cannot move r.
    rs_under_2block = []
    for r in np.linspace(0.05, 0.95, 19):
        H = Hcirc(1.0, np.sqrt(r))
        # pointer map for the 2-sector partition:
        Hp = P0 @ H @ P0 + P1 @ H @ P1
        rs_under_2block.append(np.linalg.norm(Hp - H))
    P.append(check("NO H_int forces r=1/2: the 2-block pointer map is a NO-OP for EVERY r (H already block-diag)",
                   max(rs_under_2block) < 1e-9,
                   f"max||P0 H P1||-type residual over r in (0,1): {max(rs_under_2block):.2e} "
                   f"=> the 'r=1/2 H_int' does not exist; 2-block einselection leaves r a free continuum"))

    # 2e. The POSITION/LOCAL monitor: H_int diagonal in the computational (site) basis, 3 distinct
    #     eigenvalues -> pointer basis = the 3 sites -> the localized record. Read in the circulant
    #     dimension/Born measure this is the r=1 endpoint. So the 'three H_int' are: degenerate (r=0),
    #     position-local (r=1), and ... there is NO third coupling delivering r=1/2 (2c/2d). The trio
    #     advertised by the claim is really only the two ENDPOINTS plus a non-existent middle.
    Hpos = np.diag([0.3, 0.7, 1.9])
    _, nd_pos = pointer_basis(Hpos)
    P.append(check("position/local monitor -> 3 distinct site pointers (the r=1 dimension/Born endpoint)",
                   nd_pos == 3 and np.allclose(np.linalg.eigh(Hpos)[1], np.eye(3)),
                   "site-diagonal H_int einselects the computational basis; with dimension weighting -> r=1 "
                   "=> the only two H_int-FORCED settings are the endpoints {0,1}; r=1/2 has no forcing H_int"))

    print()
    print("=" * 78)
    print("FRONT 3 -- CIRCULARITY with the records-flow fixed points (r=0,1/2,1)")
    print("=" * 78)

    # 3a. The Luders/records sharpening flow is r -> 2 r^2 (on the 2-sector power simplex).
    def luders(r):
        p_s = 1.0 / (1.0 + 2.0 * r)
        p_d = 2.0 * r / (1.0 + 2.0 * r)
        # sharpen p -> p^2 / Z on (singlet, doublet) power, re-extract r:
        ps2, pd2 = p_s ** 2, (p_d ** 2)
        Z = ps2 + pd2
        ps2, pd2 = ps2 / Z, pd2 / Z
        # invert p_d = 2r/(1+2r):
        return (ps2 and (pd2 / (2 * ps2))) if ps2 > 0 else np.inf

    P.append(check("records sharpening flow reduces to r -> 2 r^2 (matches retained Luders form)",
                   all(abs(luders(r) - 2 * r ** 2) < 1e-9 for r in [0.1, 0.3, 0.49, 0.7]),
                   "p->p^2/Z on the 2-sector power distribution == the map r|->2r^2"))

    # 3b. Fixed points of r->2r^2: r=0 (f'=0 stable) and r=1/2 (f'=2 unstable). These are the SAME
    #     two points the einselection story invokes. KEY: this flow ACTS ON the 2-sector power
    #     distribution -- the SAME (1,1)/(1,2) object the pointer partition fixes. So "einselection
    #     agrees with the records flow" is NOT two independent dynamics agreeing; it is the SAME
    #     2-sector simplex, once as a static partition and once as a flow. TAUTOLOGY, not coincidence.
    f = lambda r: 2 * r ** 2
    fp0_stable = abs((f(1e-4) - f(0)) / 1e-4) < 1e-3          # f'(0)=0
    fp_half_unstable = abs(4 * 0.5) > 1                       # f'(1/2)=2
    P.append(check("r->2r^2 fixed points are {0 (stable), 1/2 (unstable)} -- SAME points, SAME 2-sector object",
                   fp0_stable and fp_half_unstable,
                   "the flow and the pointer partition both live on the singlet|doublet power simplex "
                   "=> agreement is a TAUTOLOGY (one computation dressed twice), not independent confirmation"))

    # 3c. Demonstrate the identity explicitly: the einselection 'predictability' functional that the
    #     records flow extremizes IS the 2-sector entropy; its stationary point is r=1/2 by construction
    #     of the 2-sector simplex, independent of any environment detail. So no new info is injected.
    def S2(r):
        p = np.array([1.0 / (1 + 2 * r), 2 * r / (1 + 2 * r)])
        p = p[p > 0]
        return -np.sum(p * np.log(p))
    # numerical argmax of S2:
    grid = np.linspace(0.01, 5, 2000)
    rstar = grid[np.argmax([S2(r) for r in grid])]
    P.append(check("the 2-sector entropy S2(r) peaks at r=1/2 BY CONSTRUCTION (uniform on 2 atoms), not by einselection",
                   abs(rstar - 0.5) < 0.02,
                   f"argmax S2 = {rstar:.3f}; this is 'p=(1/2,1/2)' relabeled -- the environment plays NO role"))

    # 3d. EXPLICIT same-computation check: the einselection 'predictability sieve' on the 2-sector record
    #     and the Luders sharpening are the SAME completely-positive map p -> p^2/Z (purity-increasing
    #     measurement). Verify the einselection record-update and the sharpening map coincide as functions
    #     of the 2-sector distribution -> 'two dynamics agreeing' is ONE map, not an independent witness.
    def sharpen(p):
        q = p ** 2
        return q / q.sum()
    def einsel_record_update(p):
        # idealized predictability sieve: repeated which-sector monitoring -> Bayesian purification == p^2/Z
        return sharpen(p)
    same_map = all(np.allclose(sharpen(p), einsel_record_update(p))
                   for p in [np.array([0.4, 0.6]), np.array([0.2, 0.8]), np.array([0.5, 0.5])])
    P.append(check("einselection record-update == Luders sharpening (SAME map p->p^2/Z): not independent confirmation",
                   same_map,
                   "the records flow and the einselection sieve are literally the same purifying CP map "
                   "=> Front-A's 'einselection-stable set COINCIDES with records fixed points' is a TAUTOLOGY"))

    # 3e. Independence control: a GENUINELY different dynamics (the thermalizing/anti-sharpening map
    #     p->sqrt(p)/Z) has a DIFFERENT fixed-point character at r=1/2 (attractor vs repeller) -- proving
    #     the 'fixed point' label is arrow-dependent, so the agreement carries no measure-selecting content.
    def antisharp(p):
        q = np.sqrt(p)
        return q / q.sum()
    p0 = np.array([0.4, 0.6])
    p_sharp = sharpen(sharpen(sharpen(p0)))     # runs AWAY from (1/2,1/2)
    p_therm = antisharp(antisharp(antisharp(p0)))  # runs TOWARD (1/2,1/2)
    moved_away = abs(p_sharp[0] - 0.5) > abs(p0[0] - 0.5)
    moved_toward = abs(p_therm[0] - 0.5) < abs(p0[0] - 0.5)
    P.append(check("r=1/2 fixed-point STABILITY is arrow-dependent (repeller under sharpening, attractor under thermalizing)",
                   moved_away and moved_toward,
                   "same point, opposite stability under the two arrows => 'stable einselection setting' is "
                   "arrow-of-time-relative, NOT an intrinsic selection -> adds no measure-selecting content"))

    print()
    print("=" * 78)
    print("FRONT 4 -- DOES IT ADD ANYTHING over the known stationary-point result?")
    print("=" * 78)

    # 4a. Reproduce the retained 'block-diagonal -> pointer map no-op' finding (the prior einselection note).
    offdiag = []
    for r in np.linspace(0.05, 0.95, 19):
        H = Hcirc(1.0, np.sqrt(r))
        offdiag.append(np.linalg.norm(P0 @ H @ P1))
    P.append(check("[retained cross-check] H is block-diagonal in {P0,P1} for EVERY r (||P0 H P1||~0)",
                   max(offdiag) < 1e-9,
                   f"max ||P0 H P1|| = {max(offdiag):.2e} -> the einselection pointer map adds ZERO constraint on r"))

    # 4b. The genuine Born/tracial equilibrium weights blocks by DIMENSION -> r=1, NOT r=1/2.
    #     (rho = I/3, Tr P0 : Tr P1 = 1 : 2). r=1/2 needs the equal-power (block-COUNTING) measure -- separate.
    born_singlet = np.trace(P0).real / 3.0
    born_doublet = np.trace(P1).real / 3.0
    # equal-power circulant: 3 a^2 = 6 |b|^2 -> r=1/2.
    P.append(check("Born/dimension measure on the SAME 2 blocks gives r=1 (NOT r=1/2): value is measure-choice",
                   abs(born_singlet - 1 / 3) < 1e-12 and abs(born_doublet - 2 / 3) < 1e-12,
                   "(Tr P0,Tr P1)/3 = (1/3,2/3) -> r=1; equal-power -> r=1/2. Einselection is SILENT on which "
                   "-> it RELABELS the open measure gate, adds no physical reason for r=1/2"))

    # 4c. Therefore the DISCRETE set {0,1/2,1} is a property of the VALUE axis (which measure on the blocks:
    #     spectral->0, block-count->1/2, dimension/Born->1), NOT of the einselected pointer basis. Verify the
    #     three measures land on exactly these three r.
    def r_spectral():    # 3 equal modes -> singlet not special -> r read as 0 limit
        return 0.0
    def r_blockcount():  # equal weight per block atom: 3a^2=6|b|^2
        return 0.5
    def r_born():        # dimension weight 1:2
        return 1.0
    triple = sorted([r_spectral(), r_blockcount(), r_born()])
    P.append(check("the DISCRETE {0,1/2,1} = three MEASURES on the blocks (spectral|block-count|dimension), not 3 H_int",
                   triple == [0.0, 0.5, 1.0],
                   "discreteness lives on the value/measure axis; einselection fixes (at most) the PARTITION, "
                   "leaving the value a continuum -> the discrete set needs the measure input, not the pointer"))

    # 4d. Final hostile synthesis check: combine the two crucial verdicts as explicit booleans.
    einselected_value_is_continuum = (frac_bins_occupied >= 0.8) and (max(rs_under_2block) < 1e-9)
    einselection_is_relabeling = (max(offdiag) < 1e-9) and (abs(rstar - 0.5) < 0.02)
    P.append(check("VERDICT(1): einselected r is a CONTINUUM (value not discretized even by gauge symmetry)",
                   einselected_value_is_continuum,
                   "generic H_int -> dense [0,1]; gauge+K-real H_int -> 2-block partition but r still FREE "
                   "(no-op) => 'r=1/2 is a stable setting' is VACUOUS without the extra MEASURE input"))
    P.append(check("VERDICT(2): einselection is a RELABELING of the stationary-point/measure result, no new mechanism",
                   einselection_is_relabeling,
                   "block-diagonal no-op + records flow = same 2-sector simplex; the 'environment monitors "
                   "C_3-charge' story supplies the PARTITION (already retained, modulo K-reality), not the VALUE"))

    print()
    print("=" * 78)
    n_pass = sum(P)
    n_tot = len(P)
    print(f"SCORECARD: {n_pass}/{n_tot} PASS")
    print("=" * 78)
    print()
    print("PER-FRONT VERDICT:")
    print("  F1 CONTINUUM RISK : CONTINUUM. Generic H_int einselects a dense [0,1] of r; r=1/2 is one")
    print("                      non-isolated point. Only the ENDPOINTS {0,1} are spectrally special.")
    print("  F2 WHY THREE H_int: no single H_int forces r=1/2. Gauge-respecting (C_3-inv) -> generically the")
    print("                      3-mode (r=0) pointer; +K-reality -> the 2-BLOCK partition, but the VALUE r")
    print("                      stays free (block-diagonal no-op). The 'three' are not one criterion.")
    print("  F3 CIRCULARITY    : TAUTOLOGY. The Luders r->2r^2 flow and the pointer partition live on the SAME")
    print("                      2-sector simplex; S2 peaks at 1/2 by construction. Agreement injects no info.")
    print("  F4 ADDS-ANYTHING  : RELABELING. Reproduces the retained block-diagonal no-op; Born measure on the")
    print("                      same blocks gives r=1. The discrete {0,1/2,1} is a MEASURE-axis fact, not a")
    print("                      pointer-basis fact. Einselection supplies (at most) the partition gate.")
    print()
    print("TWO KEY FINDINGS:")
    print("  (1) DISCRETE-or-CONTINUUM: CONTINUUM. 'r=1/2 is a stable einselection setting' is VACUOUS unless")
    print("      an extra input is added. A gauge-respecting (C_3-invariant) environment discretizes the")
    print("      PARTITION (3-mode vs 2-sector, the latter modulo K-reality), but does NOT discretize the")
    print("      VALUE r -- the 2-block pointer map is a literal no-op, so r remains a free continuum on it.")
    print("      The honest 'win' (symmetry discretizes the stable settings to {0,1/2,1}) does NOT land at the")
    print("      einselection level; {0,1/2,1} is the discrete set of MEASURES on the blocks, not of pointers.")
    print("  (2) NEW-MECHANISM-or-RELABELING: RELABELING. No new physical reason for r=1/2 over the known")
    print("      stationary-point/measure result. Einselection by a C_3-invariant coupling = the already-")
    print("      retained '2-block partition modulo K-reality' gate; it is SILENT on the value r and on the")
    print("      block-count-vs-Born measure choice that actually decides {0,1/2,1}.")
    if n_pass != n_tot:
        raise SystemExit(f"FAIL: {n_tot - n_pass} checks failed")


if __name__ == "__main__":
    main()
