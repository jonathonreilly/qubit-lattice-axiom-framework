# Fourth-Axiom Variational Dynamics — Scoping (does a ground-state dynamics select the generation moduli?)

**Date:** 2026-06-05
**Claim type:** meta
**Status:** **scoping only.** Owner-authorized exploration of what a candidate
**4th axiom** (a minimal variational / ground-state dynamics whose minimum
selects the generation Yukawa moduli) would have to be. **Sets no status,
adopts nothing, imports nothing into the axiom ledger.** It documents what
such an axiom would need to deliver and reports — with an explicit
computation — that the natural minimal functionals do **not** deliver it.
**Authority role:** scoping note. No theorem, no promotion, no admission. The
independent audit lane owns any classification; this note proposes none.
**Primary runner:** [`scripts/cl3_fourth_axiom_variational_dynamics_2026_06_05.py`](../scripts/cl3_fourth_axiom_variational_dynamics_2026_06_05.py)
**Cache:** [`logs/runner-cache/cl3_fourth_axiom_variational_dynamics_2026_06_05.txt`](../logs/runner-cache/cl3_fourth_axiom_variational_dynamics_2026_06_05.txt)

## Scoping disclaimer

This is a scoping exploration of a *candidate* axiom, not a proposal to adopt
one. It does not add A1/A2/A3 content, does not import a dynamics, and does not
set or predict any audit outcome. It is honest negative/partial scoping: it
runs the natural minimal functionals and reports where their minima land.

## Question

A1 (`Z^3` lattice) + A2 (qubit / `M_2(C)`) + A3 (Record) carry **no dynamics**.
On the retained `hw=1` `C_3`-equivariant circulant mass operator
`H = a I + b C + conj(b) C^2`, the generation masses are
`m_k = lambda_k^2`, `lambda_k = a (1 + sqrt(2r) cos(delta + 2 pi k / 3))`, and
the Koide ratio is the **exact** retained line

```
Q = (sum_k m_k) / (sum_k sqrt(m_k))^2 = 1/3 + (2/3) r,   r = |b|^2 / a^2.
```

Because the map `(a, |b|) -> r` is onto, `r` is a **free input** per sector
(retained chain-of-custody; the value reduces to the single Tier-A admitted
input `AC_φλ`). A **4th axiom supplying a dynamics** — an energy functional /
Hamiltonian `E(H)` on the A1/A2 lattice whose ground state / stationary point
fixes `H` — could in principle select `r`.

**Scoping question:** does a *minimal* (parameter-free or parameter-reducing)
variational dynamics select the **observed generic** moduli, or only the dial's
special points `r in {0, 1/2, 1}`?

## Two honesty bars (the falsifiers this note holds itself to)

1. **Generic-values bar.** The minimum must reproduce the **observed** moduli
   (LABELLED OBSERVATIONAL COMPARISON ONLY — never a fitting input):
   `r_lep ≈ 0.500`, `r_down ≈ 0.597`, `r_up ≈ 0.773`, `r_nu < 1/2`. A functional
   whose minimum is a **special point** is **falsified by the generic quark
   values**.
2. **Relocation bar.** If `E` has free couplings that just re-encode the moduli,
   the flavor input merely **relocates** from `r` to the couplings. A derivation
   needs **strictly fewer** free parameters than moduli it explains.

## What the observed moduli are (anchor-only)

Recovered from PDG `sqrt`-mass ratios via the **exact** circulant identity
`Var_k(sqrt m) / mean_k(sqrt m)^2 = 2 r` (proof in runner C0; `lambda_k` has
mean `a` and variance `2 a^2 r`):

| sector | `r_obs` | `Q = 1/3 + (2/3) r` | min distance to `{0, 1/2, 1}` |
|---|---|---|---|
| charged leptons (e, mu, tau) | **0.500** | 0.667 | 0.000 (**special**) |
| down quarks (d, s, b) | **0.597** | 0.731 | **0.097** (generic) |
| up quarks (u, c, t) | **0.773** | 0.849 | **0.227** (generic) |

The leptons sit *on* the special point `r = 1/2`; the quarks sit at **generic
interior** points, strictly between `1/2` and `1`. These values are never fed
into any minimization; they are the BAR-1 comparator only.

## The candidate functionals and where their minima land (computed)

All functionals act on the 1-parameter circulant family `H(r)` (`delta` is
`Q`-independent, set to 0; the overall scale is fixed per family by holding
`a = 1` or `Tr H^2` constant). The runner computes the minimizer in `r`.

| candidate "4th-axiom" energy `E` | free params | minimizer in `r` | bar verdict |
|---|---|---|---|
| single-trace quadratic Casimir `Tr H^2` (fixed `a`) | 0 | boundary `r = 0` (`[1,1,1]` democratic) | **WRONG-VALUES** |
| single-trace shape invariants `Tr H^n` (`n=3..6`, fixed `Tr H^2`) | 0 | special: `argmin -> 0`, `argmax -> 1` | **WRONG-VALUES** |
| 2-isotype-sector power entropy | 0 | `r = 1/2` (max) | special point (lepton-only) |
| 3-eigenvalue spectral power entropy | 0 | `r = 0` (max) | **WRONG-VALUES** |
| 2-coupling single-trace mix `c3 Tr H^3 + c4 Tr H^4` | 2 | clusters at `{0, 1, 3}` — **does not reach generic** `r` | **WRONG-VALUES** (special-locked) |
| quadratic target potential `(Tr H^2 - tau)^2` | 1 | `r* = (tau - 3)/6` — **any** `r` by choosing `tau` | **RELOCATES** (1 in / 1 out) |
| nearest-neighbour qubit ring (hopping `J`, on-site `h`) | 2 | ground state gives `r = J^2 / h^2` | **RELOCATES** (ratio = modulus) |

**Two structural facts the computation establishes:**

- **Minimal => special.** Every **parameter-free** functional extremizes at a
  special point `r in {0, 1/2, 1}`. The generic quark moduli `r_up ≈ 0.77`,
  `r_down ≈ 0.60` are **never** an untuned minimum. Even the 2-coupling
  *single-trace* mix is special-locked (its minima cluster at `{0, 1, 3}`),
  because single-trace invariants of a circulant are extremized by the
  collapsed/aligned spectrum, not by a generic interior split.
- **Generic-capable => relocation.** The functionals that *can* reach a generic
  `r` (the quadratic target potential, the qubit-ring ground state) do so only
  through a free coupling whose value **is** the modulus: the minimizer is a
  smooth, invertible function of the coupling (`r* = (tau-3)/6`;
  `r = J^2/h^2`). One coupling buys exactly one modulus — never fewer.

## Verdict

**PARTIAL, leaning WRONG-VALUES / RELOCATES.**

- For the **charged-lepton lane only**, the parameter-free 2-sector balance /
  entropy functional has a genuine stationary point at `r = 1/2` — a real
  *partial* success that **matches the existing retained `r = 1/2` stationary-
  point result** ([FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md](FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md),
  [FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md)).
  But `r = 1/2` is a **special** point, so this functional cannot explain the
  quarks, and even for leptons it is not by itself a derivation: *which* extremum
  is selected (`2`-sector entropy `-> 1/2` vs dimension/Plancherel `-> 1` vs
  spectral entropy `-> 0`) is the unresolved `det_C`-vs-`det_R` measure choice
  carried by the chain-of-custody note
  ([CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)).
- For the **generic sectors (quarks, neutrinos)**, **no minimal dynamics tested
  derives `r`.** Minimal functionals give special points (**falsified by the
  generic quark values**, BAR-1); functionals flexible enough to reach the
  generic moduli carry `>= 1` free coupling per modulus and merely **relocate**
  the flavor input from `r` to the couplings (BAR-2).

This is exactly the **expected** and important finding: the candidate 4th axiom,
in its natural minimal forms, **does not select the generic moduli**. It
reproduces — now from the *variational / ground-state* side — the
assumptions-audit conclusion that the framework's canonical content reaches
**special points / fixed-point endpoints** but **never the continuous generic
modulus** ([FLAVOR_R_HALF_ASSUMPTIONS_AUDIT_NOTE_2026-05-30.md](FLAVOR_R_HALF_ASSUMPTIONS_AUDIT_NOTE_2026-05-30.md)), and it
echoes the spectral-action probe, whose `Tr f(D/Lambda)` minima land at
`|b|/a ≈ 1` (`r ≈ 1`), not at the lepton value
([KOIDE_A1_PROBE_SPECTRAL_ACTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe4.md](KOIDE_A1_PROBE_SPECTRAL_ACTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe4.md)).

## Parameter ledger (BAR-2 count)

| functional | free params | moduli reached | reduction? |
|---|---|---|---|
| single-trace `Tr H^n` (untuned) | 0 | special only | n/a (WRONG-VALUES) |
| 2-coupling single-trace mix | 2 | special only | n/a (WRONG-VALUES) |
| quadratic target `(Tr H^2 - tau)^2` | 1 | any `r` (per sector) | **no** (1 in / 1 out) |
| Landau-Ginzburg `alpha(Tr H^2)^2 + beta Tr H^4 + gamma Tr H^2` | 3 | any `r` (per sector) | **no** |
| nearest-neighbour qubit ring (`J, h`) | 2 | `r = J^2/h^2` | **no** (ratio = modulus) |
| 2-sector / spectral entropy | 0 | `r in {0, 1/2}` | n/a (WRONG-VALUES) |

Moduli to explain (4 sectors): **4**. No tested functional reproduces the
generic values with **strictly fewer** free parameters than moduli explained.
Parameter-free functionals are special-point-locked; generic-reaching ones carry
`>= 1` coupling per modulus.

## What would have to be true for a real derivation (scoping target)

A genuine 4th-axiom dynamics would have to:
1. produce an **interior** minimum (not a special point) — already non-trivial,
   since single-trace invariants are special-locked; and
2. land that minimum at the **observed generic** `r` in **`>= 2` sectors at once
   with strictly fewer free parameters than sectors** (otherwise it relocates).

Both fail for the natural minimal functionals here. The one genuinely untested
object flagged by the assumptions audit — a **native (framework-derived) matter
`beta`-function** with an attractive fixed point at a generic `r` — is **not**
constructed here (it requires the bridge-gap action) and is **not** foreclosed
by this note. This scoping result narrows where a positive route must live:
**not** in single-trace energetics, **not** in static sector/spectral entropy,
and **not** in any 1-coupling target potential — all of which either give special
points or relocate. The next path this opens is the native-RG fixed-point
structure in `r` (a flow, not a static functional minimum), which is the only
candidate that could in principle hit a generic interior value without one
coupling per modulus.

## Honest caveats

- **Normalization choice.** Any energy needs a scale; each family fixes it
  (`a = 1` or `Tr H^2` const). The minimizer *location* in `r` is reported under
  the stated normalization; a different normalization rescales `E` but the
  special-point structure of the parameter-free functionals is robust (verified
  across `Tr H^n`, `n=1..6`, and both normalizations).
- **`delta`-independence.** `Q` (hence `r`) is independent of `delta = arg b`;
  `delta` is a separate modulus (the `2/9` open gate) not addressed here.
- **Not a no-go.** This is scoping, not a no-go theorem. It rules out the
  *natural minimal* functionals as derivations of the generic moduli; it does
  not claim the search space is exhausted. The native-`beta`-function route
  remains open.

## Provenance (verified 2026-06-05)

- Exact backbone `Var/mean^2 = 2r`, `Q = 1/3 + (2/3)r`, observed-moduli recovery
  (`r_lep = 0.500`, `r_down = 0.597`, `r_up = 0.773`), and the minimizer of every
  candidate functional: verified directly (runner **10/10 PASS**).
- Consistent with, and reached independently from, the retained `r = 1/2`
  stationary-point line, the assumptions audit's "discrete/endpoint-reaching,
  not continuous-modulus" finding, and the spectral-action probe.
- Adopts nothing; imports nothing; sets no status. Does not load-bear on any
  retained row.

## Cross-references

- Retained exact line + chain of custody: [CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
- `r = 1/2` stationary-point reframe: [FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md](FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md)
- `r = 1/2` stability under the thermalizing arrow: [FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md)
- Assumptions audit (discrete-reaching, not continuous modulus; native-`beta` route flagged): [FLAVOR_R_HALF_ASSUMPTIONS_AUDIT_NOTE_2026-05-30.md](FLAVOR_R_HALF_ASSUMPTIONS_AUDIT_NOTE_2026-05-30.md)
- Spectral-action probe (`Tr f(D/Lambda)` minimum at `r ≈ 1`, not at the lepton value): [KOIDE_A1_PROBE_SPECTRAL_ACTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe4.md](KOIDE_A1_PROBE_SPECTRAL_ACTION_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe4.md)
- Circulant character backbone: [KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md](KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md)
- Generation axiom boundary (`H = aI + bC + b̄C^2`, 3 dof): [GENERATION_AXIOM_BOUNDARY_NOTE.md](GENERATION_AXIOM_BOUNDARY_NOTE.md)

## Validation

```bash
python3 scripts/cl3_fourth_axiom_variational_dynamics_2026_06_05.py
```

Expected: 10/10 PASS — backbone identity, observed-moduli recovery, the
minimizer of each candidate functional, the special-point structure of the
parameter-free family, and the relocation structure of the coupling-bearing
family, ending in the PARTIAL (WRONG-VALUES / RELOCATES) verdict.
