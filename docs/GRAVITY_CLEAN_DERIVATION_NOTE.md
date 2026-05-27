# Gravity Clean Derivation Note: Bounded IF-Chain to the Inverse-Square Law

**Date:** 2026-04-13 (status line narrowed 2026-04-28; bounded IF-chain
repair 2026-05-27)
**Claim type:** bounded_theorem
**Status:** bounded conditional weak-field gravity chain — IF the framework
imposes the self-consistency condition `L^{-1} = G_0`, the
Born/mass-density source map `rho = |psi|^2`, the weak-field test-mass
response `S = L(1 - phi)`, and the `Z^3` lattice Green-function asymptotic
with its normalization, THEN the lattice Poisson equation gives a `1/r`
potential and inverse-square force in lattice units. This note does not
derive those IF-premises from the current axiom surface and does not claim
zero-free-parameter Newton gravity.

---

## Binding Scope

The binding content of this note is the bounded IF-chain below. Earlier
wording in this lane described a complete, zero-free-parameter derivation from
the axiom surface alone; that broader reading is superseded here.

The useful mathematical skeleton is still:

```text
H = -Delta_lat,
G_0 = H^{-1},
IF L^{-1} = G_0, THEN L = -Delta_lat,
IF rho = |psi|^2 and S = L(1 - phi), THEN Poisson linearity plus the
Z^3 Green-function asymptotic gives a 1/r potential and inverse-square force.
```

The load-bearing firewall is that `L^{-1} = G_0`, `rho = |psi|^2` as
gravitational mass density, `S = L(1 - phi)` as the weak-field test-mass
response, and the exact Green-function normalization are premises or external
math inputs for this note. They are not established here as retained
theorems.

---

## Premises

Framework primitives used for context:

- primitive local algebra `Cl(3)` / one-qubit algebra on each site;
- spatial substrate `Z^3`.

Additional IF-premises consumed by the bounded chain:

1. `L^{-1} = G_0` is admitted as the weak-field self-consistency condition.
2. `rho = |psi|^2` is admitted as the gravitational mass-density source map.
3. `S = L(1 - phi)` is admitted as the weak-field test-mass response.
4. The `Z^3` lattice Green function has the stated `1/(4 pi r)` large-distance
   asymptotic in the normalization used by the chain.

The chain is conditional on these four premises.

---

## The Conditional Chain

The classifications in this section are local to the IF-chain. They are not
claims that the missing physical premises have been derived from the current
axiom surface.

### Step 1: Cl(3) on Z^3 --> Staggered Hamiltonian H = -Delta_lat

**Classification: LOCAL ALGEBRA (Kawamoto-Smit construction, inside the
IF-chain)**

The Clifford algebra Cl(3) on the cubic lattice Z^3 is realized by the
Kawamoto-Smit staggered construction (Kawamoto & Smit 1981; Susskind
1977). The three Clifford generators Gamma_mu become staggered hopping
operators:

    (H psi)(x) = sum_{mu=1}^{3} eta_mu(x) [psi(x + e_mu) - psi(x - e_mu)]

where eta_mu(x) = (-1)^{x_1 + ... + x_{mu-1}} are the KS staggered
phases. The resulting Hamiltonian, after squaring to obtain the scalar
sector (Gamma_mu^2 = 1 removes the spin structure), is the negative
graph Laplacian:

    H = -Delta_lat

where (Delta_lat psi)(x) = sum_{|y-x|=1} psi(y) - 6 psi(x) on Z^3.

**Local IF-chain role:** Given Cl(3) on Z^3, the staggered Hamiltonian is
uniquely determined (up to an overall coupling constant which sets
units). The identification H = -Delta_lat is an algebraic identity:
the squared staggered Dirac operator on Z^3 IS the graph Laplacian.
This is verified to machine precision in the script (CHECK 1).

**Assumptions consumed:** A1 + A2 (the axiom).

---

### Step 2: Propagator G_0 = H^{-1} = (-Delta_lat)^{-1}

**Classification: DEFINITION**

The free propagator's Green's function is defined as the matrix inverse
of the Hamiltonian:

    G_0 = H^{-1}

Since H = -Delta_lat (Step 1), this gives:

    G_0 = (-Delta_lat)^{-1}

This is not a physical claim. It is the definition of the propagator on
this graph: the response at site y to a unit source at site x.

**Assumptions consumed:** None beyond Step 1.

---

### Step 3: Self-consistency L^{-1} = G_0 forces L = -Delta_lat

**Classification: CONDITIONAL STEP.** `L^{-1} = G_0` is an IF-premise of
this note. Once that premise is admitted, the algebraic consequence
`L = -Delta_lat` follows immediately. This note does not derive the premise
from the current axiom surface.

The gravitational field phi is sourced by the propagator density
rho = |psi|^2 via a linear field operator L:

    L phi = -kappa rho

Self-consistency requires that the field the propagator generates
(through its density) equals the field the propagator propagates in.
At leading (linear) order, this fixed-point condition is:

    L^{-1} = G_0

That is: the Green's function of the field equation must equal the
propagator's Green's function. This is the ONLY condition that closes
the self-referential loop phi -> psi(phi) -> rho -> phi.

Now substitute from Step 2:

    L^{-1} = G_0 = (-Delta_lat)^{-1}

Invert both sides:

    L = G_0^{-1} = -Delta_lat

**This is the admitted closure condition, not a numerical search.**
If `L^{-1} = G_0` is granted, it determines `L` from the propagator. The
operator `L` is not selected from a family by fitting or sweeping inside this
conditional calculation. The result is:

    (-Delta_lat) phi = -kappa rho

which is the Poisson equation on Z^3.

**Why this remains conditional:** The earlier notes presented this step as a
numerical sweep over 21 operators, finding that only the Poisson operator gives
zero mismatch. The bounded chain instead treats the sweep as verification of
the admitted premise, not as a derivation of that premise. The local algebra is:

    L^{-1} = G_0  (framework closure condition)
    G_0 = (-Delta)^{-1}  (Step 2)
    => L = -Delta  (inversion)

This is a three-line consequence of the admitted closure condition. The
numerical checks confirm it: the mismatch
M(L) = ||L^{-1} delta - G_0 delta|| / ||G_0 delta|| is exactly zero
for L = -Delta and nonzero for every alternative operator tested
(10 alternatives, all M > 0.28). The parametric family (-Delta)^alpha
has M(alpha) uniquely minimized at alpha = 1.0 with M(1.0) < 6e-16.
These are confirmations of the closure condition, not the derivation
itself.

**Premises consumed:**
- Self-consistency condition `L^{-1} = G_0`.
- Linearity of the field operator in the weak-field regime.

---

### Step 4: Poisson equation (-Delta_lat) phi = rho where rho = |psi|^2

**Classification: CONDITIONAL STEP (from Step 3 plus the source-map premise)**

Combining Step 3 with the identification rho = |psi|^2 (the propagator's
probability density is the source of the gravitational field), we obtain
the lattice Poisson equation:

    (-Delta_lat) phi(x) = rho(x)

for a distributed source, or

    (-Delta_lat) phi(x) = M delta(x)

for a point mass M at the origin (where M = integral of rho over the
source region).

**Premises consumed:** Step 3 and the admitted source map `rho = |psi|^2` as
gravitational mass density.

---

### Step 5: Green's function G(r) --> 1/(4 pi r) for large r

**Classification: EXTERNAL MATH INPUT (lattice potential theory)**

On Z^3, the Green's function of the lattice Laplacian has the
large-distance asymptotic form:

    G(r) = <r| (-Delta_lat)^{-1} |0> = 1/(4 pi |r|) + O(1/|r|^3)

for |r| >> 1 in lattice units, where the O(1/|r|^3) correction is an
oscillatory cubic-symmetry artifact that vanishes for generic directions
and averages to zero over solid angles.

This is a mathematical theorem proved by Fourier analysis:

    G(r) = 1/(2pi)^3 integral_{[-pi,pi]^3}
            e^{i k . r} / [2(3 - cos k_1 - cos k_2 - cos k_3)] d^3k

The integral converges absolutely for r != 0 and its large-|r|
asymptotics are established by stationary-phase / saddle-point methods.

**References:**
- Maradudin, Montroll, Weiss & Ipatova, *Theory of Lattice Dynamics in
  the Harmonic Approximation* (Academic Press, 1971)
- Hughes, *Random Walks and Random Environments* (Oxford, 1995)
- Lawler & Limic, *Random Walk: A Modern Introduction* (Cambridge, 2010)

**Import status:** This is an external theorem of pure mathematics about the
discrete Laplacian on `Z^3`. This note uses it as a math input; it does not
provide a retained internal bridge or an executable derivation of the exact
normalization.

**Numerical verification:** On a 128^3 lattice, the ratio
4 pi r G(r) / 1 deviates from unity by less than 1% for off-axis points
at r in [5, 60]. The deviation is systematic (Dirichlet BC bias) and
decreases monotonically with lattice size, as the theorem predicts.

**Premises consumed:** the lattice Laplacian on `Z^3` and the stated external
Green-function asymptotic/normalization.

---

### Step 6: Potential phi = -GM/r

**Classification: CONDITIONAL RESULT (from Steps 4 + 5)**

From Step 4, a point mass M at the origin satisfies:

    (-Delta_lat) phi = M delta(0)

By linearity, phi(r) = M G(r). Using Step 5:

    phi(r) --> M / (4 pi |r|)   for |r| >> 1

Identifying G_N = 1/(4 pi) in lattice units, this is:

    phi(r) = -G_N M / r

The sign convention: phi represents a potential well (attractive), so
phi < 0 with the physics sign convention, or phi > 0 if we define the
Green's function as positive.

**Premises consumed:** Point-mass idealization and the admitted
Green-function asymptotic.

---

### Step 7: Force F = -nabla phi = G_N M / r^2

**Classification: CONDITIONAL RESULT (gradient of `1/r`)**

The gravitational force on a test particle at distance r from a mass M
is the gradient of the potential:

    F = -nabla phi = -nabla(-G_N M / r) = G_N M / r^2

directed radially inward. The gradient of 1/r is -1/r^2 in the radial
direction. This is calculus, not physics.

On the lattice, the discrete gradient (finite difference) agrees with
the continuum gradient to O(a^2 / r^2) where a is the lattice spacing,
which is negligible for r >> a.

**Premises consumed:** Steps 4-6 and the weak-field force/readout convention.

---

### Step 8: Product law F = G_N M_1 M_2 / r^2

**Classification: CONDITIONAL RESULT (Poisson linearity plus admitted
test-mass response)**

For two masses M_1 at r_1 and M_2 at r_2, the Poisson equation is:

    (-Delta) phi = M_1 delta(r_1) + M_2 delta(r_2)

By linearity:

    phi = M_1 G(r - r_1) + M_2 G(r - r_2)

The force on M_2 due to M_1 is:

    F_12 = -M_2 nabla phi_1(r_2) = G_N M_1 M_2 / |r_1 - r_2|^2

Within the bounded IF-chain, the product `M_1 M_2` follows from two independent
properties:

1. **Poisson linearity:** phi_1(r) is proportional to M_1.
2. **Test-mass response:** the force on M_2 is proportional to M_2
   (the deflection of a path sum in a fixed potential is proportional
   to the particle's mass through the action S = L(1 - phi)).

Poisson linearity is the mathematical part. The second factor depends on the
admitted test-mass response premise.

**Premises consumed:** Poisson linearity plus the admitted weak-field
test-mass response `S = L(1 - phi)`.

---

### Step 9: Exponent 2 = d - 1 = 3 - 1

**Classification: CONDITIONAL STEP (dimension fixed by the declared `Z^3`
substrate)**

In d spatial dimensions, the Poisson Green's function scales as:

    G_d(r) ~ 1/r^{d-2}   for d >= 3

The force is the gradient:

    F ~ 1/r^{d-1}

For d = 3: F ~ 1/r^2, so the exponent is 2 = d - 1 = 3 - 1.

The dimension used in this chain is `d = 3` because the declared substrate is
`Z^3`.

**Premises consumed:** the declared `Z^3` spatial substrate.

---

## Bounded IF-Chain Summary

```
Context: Cl(3) on Z^3

Step 1  [local algebra]       Cl(3) on Z^3 --> staggered H = -Delta_lat
                              (KS construction, algebraic identity)

Step 2  [definition]          G_0 = H^{-1} = (-Delta_lat)^{-1}
                              (propagator defined as Hamiltonian inverse)

Step 3  [IF-premise + algebra] IF L^{-1} = G_0, THEN L = -Delta_lat

Step 4  [IF-premise]          IF rho = |psi|^2 is the gravitational source,
                              THEN (-Delta) phi = rho

Step 5  [math input]          G(r) --> 1/(4 pi r) for large r
                              (lattice potential theory)

Step 6  [conditional result]  phi = -G_N M / r

Step 7  [conditional result]  IF S = L(1 - phi), THEN
                              F = -nabla phi = G_N M / r^2

Step 8  [conditional result]  F = G_N M_1 M_2 / r^2
                              (Poisson linearity plus test-mass response)

Step 9  [conditional result]  exponent 2 = d - 1 = 3 - 1
                              (d = 3 from Z^3)
```

The chain is useful because the algebra after the IF-premises is tight. It is
not an unconditional derivation of Newton gravity from the axiom surface.

---

## What Changed From Earlier Notes

The earlier `GRAVITY_COMPLETE_CHAIN.md` classified the self-consistency
step as BOUNDED, based on a numerical sweep over 21 operators. This note
reframes the argument:

**Old framing (BOUNDED):**
> We swept 21 operators and found only Poisson gives an attractive
> self-consistent fixed point. This is numerical evidence, not a proof.

**Current bounded framing:**
> If self-consistency is stipulated as `L^{-1} = G_0`, then since
> `G_0 = (-Delta)^{-1}`, we have `L = -Delta`. The 21-operator sweep is
> verification of the stipulated closure condition, not a proof that the
> condition follows from the axiom surface.

The key insight: the self-consistency condition L^{-1} = G_0 is not a
constraint that must be checked operator-by-operator. It is a direct
equation whose solution is L = G_0^{-1} = H = -Delta_lat. The operator
L is computed, not searched for. But the condition itself is a physical
closure requirement of the framework, not a mathematical theorem that
follows from axioms alone.

The lattice Green-function statement (Step 5) is carried as an external math
input in this note. A future retained bridge can internalize or wrap that input
if the row is meant to close beyond bounded IF-chain status.

---

## What Is Actually Proved

This note proves only the conditional implication:

```text
IF L^{-1} = G_0,
IF rho = |psi|^2 is the gravitational source,
IF S = L(1 - phi) is the weak-field test-mass response,
IF the Z^3 Green function has the stated 1/(4 pi r) asymptotic,
THEN F = G_N M_1 M_2 / r^2 in lattice units.
```

The product structure and exponent are internal consequences of the bounded
IF-chain. The physical source, response, and normalization premises remain
outside this note.

---

## What Remains Open

1. **Self-consistency premise:** A retained theorem or accepted-premise entry
   for `L^{-1} = G_0`.

2. **Source premise:** A retained theorem that `rho = |psi|^2` is the
   gravitational mass-density source map on this surface.

3. **Response premise:** A retained theorem for the weak-field test-mass
   response `S = L(1 - phi)`.

4. **Green-function authority:** A registered retained bridge or import wrapper
   for the exact `Z^3` Green-function asymptotic and normalization.

5. **Beyond weak field:** Horizons, frame dragging, gravitational waves, and
   full Einstein-equation dynamics remain outside this bounded row.

---

## Paper-Facing Safe Read

Safe wording:

> Conditional on the weak-field closure `L^{-1} = G_0`, the
> Born/mass-density source map, the weak-field test-mass response, and the
> `Z^3` Green-function asymptotic, the lattice Poisson chain yields a `1/r`
> potential and inverse-square force in lattice units.

Unsafe wording:

- Newton gravity derived from the current axiom surface alone.
- Zero-free-parameter gravity derivation.
- Clean single-axiom closure of `G_N`, the source map, or the physical
  response law.

---

## Commands Run

```bash
cd /Users/jonBridger/Toy\ Physics
python3 scripts/frontier_gravity_clean_derivation.py
```

---

## Relation to review.md

This note records a bounded weak-field conditional chain. It does not claim
closure of the broader gravity bundle, including WEP, time dilation,
geodesics, strong-field behavior, or physical `G_N` normalization.

## Audit boundary (2026-04-28)

Audit verdict (`audited_conditional`, high criticality, 123 transitive
descendants):

> Issue: the note advertises a zero-free-parameter derivation of
> Newton gravity from Cl(3) on Z^3, but the load-bearing step is the
> imposed physical closure condition `L^{-1} = G_0`, followed by
> unregistered identifications of `rho = |psi|^2` as gravitational
> mass density and test-mass response via `S = L(1 - phi)`. Why this
> blocks: the algebra `L = G_0^{-1}` is valid once the closure
> condition is granted, and the Z^3 Green-function asymptotic is
> standard mathematics, but the audit packet does not derive or
> register the physical law that the gravitational field operator
> must have the same Green function as the propagator, nor the
> source/readout/mass-coupling maps needed to turn the Poisson
> equation into `F = G_N M_1 M_2 / r^2`.

> Claim boundary until fixed: it is safe to claim a conditional
> weak-field chain: if the framework imposes `L^{-1} = G_0` and the
> stated source/response maps, then the Z^3 Laplacian Green function
> gives a Newtonian `1/r` potential and inverse-square force in
> lattice units.

## What this note does NOT claim

- An unconditional derivation of Newton gravity from a single axiom.
- Registered audit-clean dependency notes for: the self-consistency
  condition `L^{-1} = G_0`, the Born / mass-density source map
  `rho = |psi|^2`, the weak-field test-mass response `S = L(1 - phi)`,
  or the lattice Green-function normalization/asymptotic.
- A registered primary runner; the note names a command but the
  ledger has no runner_path entry.

## What would close this lane (Path A future work)

Promoting from bounded conditional to retained would require:

1. A registered primary gravity-clean runner with controlled
   finite-lattice checks.
2. Registered retained theorems for the self-consistency condition
   `L^{-1} = G_0`.
3. A registered Born / mass-density source map theorem
   (`rho = |psi|^2`).
4. A registered weak-field action / test-mass response theorem
   (`S = L(1 - phi)`).
5. A registered lattice Green-function normalization/asymptotic
   theorem.

## Citations

The IF-conditions of the conditional theorem are each addressed or discussed by
existing source notes in the repository. The markdown links here make the
dependency edges explicit so the audit lane can walk the chain rather than
treat the IF-conditions as unsourced. These citations do not turn the
IF-premises into retained theorems.

### Upstream authorities (citation graph deps)

- [SELF_CONSISTENCY_FORCES_POISSON_NOTE.md](SELF_CONSISTENCY_FORCES_POISSON_NOTE.md)
  — supplies the `L^{-1} = G_0` self-consistency closure forcing the
  field operator to be the negative graph Laplacian (Step 3 of the
  derivation chain).
- [POISSON_EXHAUSTIVE_UNIQUENESS_NOTE.md](POISSON_EXHAUSTIVE_UNIQUENESS_NOTE.md)
  — supplies the uniqueness of Poisson's law given the closure
  condition, so that the linear field operator is determined rather
  than chosen.
- [GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md](GRAVITY_FULL_SELF_CONSISTENCY_NOTE.md)
  — registers the broader self-consistency surface and the role of
  `L^{-1} = G_0` within it.
- [STAGGERED_FERMION_CARD_2026-04-11.md](STAGGERED_FERMION_CARD_2026-04-11.md)
  — establishes the Born / mass-density identification `rho = |psi|^2`
  used at Step 4. (Replaces a prior citation of
  `GRAVITY_SIGNED_SOURCE_DENSITY_BOUNDARY_NOTE.md`, which is a parallel
  audit of source-density forms rather than the upstream establishing
  the Born identification — see "Direction-corrected cycle break"
  below.)

### External mathematical theorems (no internal citation graph edge)

- **Maradudin et al. 1971** — the lattice Laplacian Green's function on
  `Z^3` converges to `1/(4 pi r)` at large `r`. This is a result of
  pure lattice potential theory, used at Step 5 (continuum form) and
  Step 8 (force-law derivation). It is an external math theorem, not
  an internal repo dep.

### Direction-corrected cycle break (2026-05-05)

Three citation edges previously listed here registered the wrong
direction in the citation graph. They have been removed in this
revision because each downstream note actually CONSUMES this note
rather than supplying input to it:

- `BROAD_GRAVITY_DERIVATION_NOTE.md` — broad_gravity's Step 1 and
  Step 5 explicitly cite this note as their authority ("established in
  GRAVITY_CLEAN_DERIVATION_NOTE.md Step 1", line 27-29 of broad_gravity;
  "Established in GRAVITY_CLEAN_DERIVATION_NOTE.md Step 5", line 59).
  broad_gravity is downstream, not upstream.
- `NEWTON_LAW_DERIVED_NOTE.md` — newton_law is a parallel, more compact
  presentation of the Newton-from-Z^3 derivation. It cites Maradudin
  directly for the Green's function asymptotic. There is no internal
  upstream-downstream relationship between gravity_clean and newton_law
  — they are alternate routes to the same conclusion.
- `GRAVITY_SIGNED_SOURCE_DENSITY_BOUNDARY_NOTE.md` — gravity_signed_source
  is an audit of source-density forms (rho_B, rho_s, rho_Q, rho_g) that
  consumes `rho = |psi|^2` from STAGGERED_FERMION_CARD upstream. It is
  not the upstream establishing the Born identification.

The 2026-05-27 repair narrows the binding claim to the bounded IF-chain above.
These dependency edges make the upstream authorities visible to the citation
graph and audit pipeline; they do not promote this row by themselves.
