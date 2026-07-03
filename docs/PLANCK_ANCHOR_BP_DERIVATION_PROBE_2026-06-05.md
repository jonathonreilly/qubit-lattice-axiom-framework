# Planck-Anchor (BP) Derivation Probe

**Date:** 2026-06-05
**Type:** meta
**Claim type:** meta
**Status:** frontier-probe synthesis; no theorem promotion and no audit-status
claim. Source-note proposal; pipeline-derived `effective_status` is set only
after independent audit review.
**Authority role:** records a frontier attack on whether the named open bridge
premise **(BP)** of the Planck conditional-completion packet derives from the
framework baseline plus the retained gravity chain, thereby closing the Planck
anchor `a = l_P`. The probe lands a precise **characterization of (BP) as a
genuine dimensionful import**, supported by an explicit free-fermion
holographic/area-law computation. It does not retag any existing audit row,
modify any theorem, or set any audit status.
**Primary runner:** [`scripts/frontier_planck_anchor_bp_derivation_probe.py`](../scripts/frontier_planck_anchor_bp_derivation_probe.py)
**Cache:** [`logs/runner-cache/frontier_planck_anchor_bp_derivation_probe.txt`](../logs/runner-cache/frontier_planck_anchor_bp_derivation_probe.txt)

## Authority disclaimer

This is a source-note proposal. Pipeline-derived status is generated only after
the independent audit lane reviews the claim, dependency chain, and runner.
This note does not promote any source theorem note, does not retag any audit
row, does not modify any theorem, and does not set or predict an audit outcome.
Status authority is the independent audit lane only.

## The question

The framework takes exactly one dimensionful reference (Buckingham-Pi): the
scale-reference primitive `a^{-1} = M_Pl`
([`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md),
registered in `axiom_premise_nodes.json` with explicit owner approval). The
candidate route to *derive* that ruler — rather than declare it — is the
conditional Planck-completion packet
([`PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24.md`](PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24.md)),
which packages the conditional algebraic implication

```text
PREMISE (BP):  the primitive one-step substrate boundary/worldtube count IS
               the microscopic carrier of the standard gravitational
               area/action (Bekenstein-Hawking) density.

CONSEQUENCE:   with c_cell = Tr((I_16/16) P_A) = 1/4 and the same-surface
               density match c_cell/a^2 = 1/(4 l_P^2), algebra gives a/l_P = 1.
```

The conditional implication `(BP) => a/l_P = 1` is exact. **(BP) is unaudited
(not a no-go).** This probe asks the frontier question:

> Does (BP) derive from Lattice + Quantum + Record and the retained
> gravity chain? Concretely, does the `Z^3` + record structure holographically
> reproduce `S = A/(4 l_P^2)` natively — supplying the Bekenstein-Hawking `1/4`
> and forcing `a = l_P` — or does the boundary-to-BH-carrier identification
> need an external dimensionful input?

## Verified ledger context (origin/main, 2026-06-05)

The probe was built against the live audit ledger. The load-bearing statuses:

| Row | `effective_status` |
|---|---|
| `GRAVITY_CLEAN_DERIVATION_NOTE` (conditional weak-field IF-chain, `G_kernel = 1/(4 pi)`) | **retained_bounded** |
| `BH_QUARTER_WALD_NEWTON_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10` (the algebra `4 G c = 1`) | **retained** (`audited_clean`) |
| `AREA_LAW_MAJORANA_CAR_FOCK_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-09` | **retained** (`audited_clean`) |
| `PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24` | unaudited |
| `PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25` (`c_cell = 1/4`) | unaudited |
| `PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM_NOTE_2026-04-24` | unaudited |
| `BH_QUARTER_WALD_NOETHER_FRAMEWORK_CARRIER_THEOREM_NOTE_2026-04-29` (`S_BH = A/4`, consumes (BP)+Wald) | unaudited |
| `AREA_LAW_QUARTER_BROADER_NO_GO_NOTE_2026-04-25` (`c_Widom <= 1/6`) | unaudited |
| `AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25` (`c_Widom = 1/4` via CIP) | unaudited |

**Key observation:** the only *retained* objects in the BH/area-law
neighborhood are (i) the conditional weak-field gravity IF-chain whose physical
output is the **bare** Green coefficient `G_kernel = 1/(4 pi)`, and (ii) a
**pure rational-algebra** identity `4 G c = 1` on abstract symbols that consumes
no physics. Every object that actually attaches the number `1/4` to a
gravitational area density (the coframe carrier, the boundary-density
extension, the Wald-Noether composition) is unaudited and explicitly carries
(BP) as a named open premise.

## The probe and its findings

The runner performs the holographic/area-law computation native to `Z^3` and
isolates exactly where (BP) enters. Five independent angles, all PASS
(`SUMMARY: PASS=17 FAIL=0`).

### (A) The action-side `1/4` is a counting trace, not an entropy

`P_A` is built explicitly as the rank-4 Hamming-weight-one diagonal projector
on `C^16 = C^2_t (x) C^2_x (x) C^2_y (x) C^2_z`. Then

```text
c_cell = Tr((I_16/16) P_A) = 4/16 = 1/4     (exact)
```

is an **occupation / counting** expectation value. It is **not** a von Neumann
entanglement entropy: the source-free state's own entropy is `log 16`, the
reduced entropy of any one tensor factor is `log 2`, and neither equals `1/4`.
Identifying the counting trace `c_cell` with the Bekenstein-Hawking *entropy*
density per unit area is therefore a **change of category** (count -> entropy
density). The algebra does not perform that step; (BP) is exactly that step.

### (B) The native `Z^3` free-fermion entanglement coefficient is NOT `1/4`

The runner computes the entanglement entropy of the gapless half-filled
free-fermion chain (the boundary theory of a `Z^3` Dirac sea) directly from the
one-body correlation matrix `C_ij = <c_i^dag c_j>` via the Peschel formula
`S_A = -sum_k [n_k log n_k + (1-n_k) log(1-n_k)]`, with no assumed coefficient.
Across `L = 64 ... 2048` the discrete log-derivative of `S(L)` converges to the
free-Dirac-fermion central charge:

```text
c_eff(L=2048) = 1.0026      ->  leading area coefficient c/6 = 0.1671
```

This is **an octave below** the Bekenstein-Hawking `1/4`. The probe's value was
cross-checked independently (recorded in this note's commit, not in the runner):
the **periodic** chain (two cuts) gives slope `c/3 = 0.3333 => c = 1.0000`, and
the **open** chain residual `S - (1/6) log(2L/pi)` converges to the known
non-universal boundary constant (`~0.362`) — both are textbook Calabrese-Cardy
checks confirming the leading coefficient is exactly `1/6`, not `1/4`. This
agrees with the retained-neighborhood Widom no-go: the simple-fiber class is
bounded by `c_Widom <= 1/6`, and the half-filled cubic `Z^3` carrier sits at
`~0.105`. **No native single-band `Z^3` entanglement carrier yields `1/4`.** The
known `c_Widom = 1/4` carrier
([`AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM`](AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md))
reaches it only via an average crossing number of exactly `3`, which is itself a
separate, unaudited carrier-identification premise (CIP). So the entanglement
side does not supply the BH `1/4` for free either.

### (C) The retained `4 G c = 1` algebra does not pin `(c, G) = (1/4, 1)`

The only retained BH-quarter object
([`BH_QUARTER_WALD_NEWTON_COEFFICIENT_NARROW_THEOREM`](BH_QUARTER_WALD_NEWTON_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10.md))
is the polynomial equivalence `S_Wald(c,A) = A c` equals `S_BH(G,A) = A/(4G)`
for all `A` iff `4 G c = 1`. The constraint is a hyperbola: `(1/4,1)`,
`(1/2,1/2)`, `(1,1/4)` all satisfy it. Selecting the physical point `(1/4, 1)`
needs **two** extra inputs the algebra does not provide: `c = c_cell = 1/4`
(the coframe counting coefficient) **and** the gravitational normalization
`G_lat = 1`. The retained gravity chain on its own gives the **bare**
`G_kernel = 1/(4 pi) ~ 0.0796`, not `G_lat = 1`; plugging the bare kernel into
`4 G c` with `c = 1/4` gives `1/(4 pi) != 1` — inconsistent. The missing `4 pi`
carrier normalization (solid angle of a 2-sphere) is supplied by (BP), not by
the bare Green kernel.

### (D) Dimensional analysis: (BP) is the single dimensionful ruler

`c_cell` and `G_kernel` are dimensionless (a rank ratio and a lattice Green
coefficient). The only length-dimensionful symbols are the lattice spacing `a`
and the Planck length `l_P`. The match `c_cell/a^2 = 1/(4 l_P^2)` is an equality
of two `[length]^{-2}` area-densities; it is dimensionally consistent **only**
once the substrate boundary-count density `c_cell/a^2` is *identified* with the
gravitational BH entropy density `1/(4 l_P^2)` — and that identification is (BP).

By Buckingham-Pi, a dimensionful number (`a` measured against a fixed physical
`l_P`) cannot be produced by purely dimensionless structure. The framework
baseline (Lattice + Quantum + Record) is dimensionless except for the single
ruler `[a]`. So **some** dimensionful input is irreducibly required to relate
`a` to physical `l_P`. (BP) is exactly that input: it pins the ruler by
declaring the substrate boundary count to be the BH area carrier. This is
**the same content** as the scale-reference primitive (one dimensionful ruler),
re-expressed physically. Hence (BP) is not derivable from Lattice + Quantum + Record plus retained
gravity — it *is* the ruler choice, in physical clothing.

### (E) Record-native holographic attempt

Record gives boundary records — one classical bit per recorded boundary
edge — which is an **area-law-shaped count**. But the maximal record entropy per
boundary plaquette is `log 2 ~ 0.693` nats, not `1/4`, and even granting an
area-law *form* from records, the *coefficient* `1/4` is not fixed by counting
bits. It would require identifying the record-bit count with the BH entropy and
fixing the per-bit weight — again (BP)-type content plus a normalization. The
record structure supplies an area-law **candidate**, not the BH
**normalization**.

## Verdict

**BP-IS-GENUINE-IMPORT.** The Planck anchor `a = l_P` does **not** close from
Lattice + Quantum + Record + the retained gravity chain alone.

- The conditional implication `(BP) => a/l_P = 1` is exact algebra (re-verified).
- But every native route to the antecedent fails to supply the
  Bekenstein-Hawking `1/4` *as a gravitational area-entropy density*:
  - the action-side `1/4` is a counting trace, not an entropy (A);
  - the native `Z^3` entanglement coefficient is `1/6` (single cut) / `~0.105`
    (3D cubic), an octave below `1/4` (B);
  - the only retained BH-quarter algebra (`4 G c = 1`) leaves a hyperbola of
    solutions and needs `G_lat = 1`, which the bare retained `G_kernel = 1/(4 pi)`
    does not supply (C);
  - dimensional analysis shows (BP) is the **single dimensionful ruler**,
    equivalent to the already-recorded scale-reference primitive (D);
  - the record structure gives an area-law form but not the `1/4` normalization
    (E).

(BP) is therefore precisely the one Buckingham-Pi dimensionful identification —
the boundary-count `<->` BH-area-carrier bridge — and it coincides with the
scale-reference primitive `a^{-1} = M_Pl` rather than reducing it to a theorem.
This is a clean negative characterization: it does not bound any lane (the
scale-reference primitive is already an approved framework primitive carrying
zero dimensionless content), and it does not foreclose future structural work.

## What this opens (not closes)

The probe sharpens *what a genuine derivation of (BP) would have to do*, which
is a strictly more constrained target than before. Any future route to (BP)
must do **all** of:

1. produce the Bekenstein-Hawking `1/4` as a true area-**entropy** density
   (not a counting trace and not the `1/6` free-fermion coefficient);
2. supply the `4 pi` carrier normalization that turns the bare retained
   `G_kernel = 1/(4 pi)` into `G_lat = 1` on the same surface;
3. do (1)-(2) **without** importing a dimensionful comparator — i.e. produce a
   dimensionful match from a route that is not itself the scale-reference ruler.

Item (3) is the crux the dimensional analysis exposes: by Buckingham-Pi any
such route must either (a) introduce a *second, independent* dimensionful
structure inside the baseline (which the current three axioms do not contain),
or (b) be a relabeling of the same single ruler. The probe does not claim this
is impossible; it pins the obstruction to exactly that dimensional gap, so the
search space for (BP) is now well-posed: find a baseline-native dimensionful
structure distinct from the spacing ruler, or show the count `<->` entropy
identification follows from a derived, not merely supplied, horizon-sector area law
whose per-face coefficient is provably the `16`-state event-cell count *and*
provably an entropy. The gapped-horizon / topological-sector carrier route
listed in
[`AREA_LAW_COEFFICIENT_GAP_NOTE.md`](AREA_LAW_COEFFICIENT_GAP_NOTE.md)
remains the most compatible open direction; it still needs a new
carrier-identification theorem rather than another area-law probe.

## Cited authorities (informational, NON-load-bearing)

This is a meta synthesis note; its content is the runner's exact linear-algebra
and free-fermion computation plus the dimensional bookkeeping. The references
below are informational pointers to the live authority chain, not load-bearing
proof inputs:

- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
- [`PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24.md`](PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24.md)
- [`PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md`](PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md)
- [`PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM_NOTE_2026-04-24.md`](PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM_NOTE_2026-04-24.md)
- [`BH_QUARTER_WALD_NOETHER_FRAMEWORK_CARRIER_THEOREM_NOTE_2026-04-29.md`](BH_QUARTER_WALD_NOETHER_FRAMEWORK_CARRIER_THEOREM_NOTE_2026-04-29.md)
- [`BH_QUARTER_WALD_NEWTON_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10.md`](BH_QUARTER_WALD_NEWTON_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10.md)
- [`GRAVITY_CLEAN_DERIVATION_NOTE.md`](GRAVITY_CLEAN_DERIVATION_NOTE.md)
- [`AREA_LAW_QUARTER_BROADER_NO_GO_NOTE_2026-04-25.md`](AREA_LAW_QUARTER_BROADER_NO_GO_NOTE_2026-04-25.md)
- [`AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md`](AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md)
- [`AREA_LAW_COEFFICIENT_GAP_NOTE.md`](AREA_LAW_COEFFICIENT_GAP_NOTE.md)
- [`AXIOM_FIRST_BEKENSTEIN_BOUND_THEOREM_NOTE_2026-05-01.md`](AXIOM_FIRST_BEKENSTEIN_BOUND_THEOREM_NOTE_2026-05-01.md)

## Forbidden-imports check

- No PDG / observed `G_Newton`, `l_P_obs`, or `S_BH_obs` consumed. The symbol
  `l_P` appears only as an abstract dimensional placeholder in the same-surface
  match; no decimal value enters.
- No literature numerical comparator consumed.
- No fitted selector consumed.
- No new axiom or framework primitive proposed. The probe's conclusion is that
  (BP) coincides with the **already-approved** scale-reference primitive; it
  introduces nothing new.
- The free-fermion Peschel/Calabrese-Cardy entanglement method is standard
  mathematical background (used in parallel, as in the cited area-law runners),
  not a new framework axiom.

## Verification

```bash
python3 scripts/frontier_planck_anchor_bp_derivation_probe.py
```

Expected: `SUMMARY: PASS=17  FAIL=0`. Audit status is set only by the
independent audit lane.
