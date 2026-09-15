---
claim_id: possibility_symmetric_sequential_formation_that_varies_has_order_dependent_record_statistics_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "On any finite nearest-neighbor window of Z^3 that contains a three-site path, sequential single-site formation that is order-blind has i.i.d. empty-neighbourhood laws on the two ends of that path, because those ends form with empty neighbourhoods in the ends-first order. For a possibility-symmetric one-neighbour Markov kernel K this is the identity K^2 = mu_0. On the two-point menu the residual is (pplus - pminus)^2; the only interior solutions are independent kernels. On the six-axis cubic orbit the residual is (a-b)^2 and the remaining Haar-square condition is (6c-1)^2/3=0, so only the uniform kernel. On S^2, covariant kernels are zonal; Haar-square kills every Legendre moment, so only Haar among densities, while atoms at ±p and the equator kernel fail Haar-square because K^2 stays atomic or has <t^2>=1/2 against Haar 1/3. If K_1 = mu_0, a star of m leaves in Z^3 forces every m-neighbour kernel to equal mu_0. Therefore a possibility-symmetric sequential rule that varies with nearest-neighbour conditions has order-dependent record statistics. The derivation uses the Qubit possibility-symmetry sentence and Admissibility's one covariant rule; it does not depend on soldering. No physical order, menu, or rule is selected; no axiom is added."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
runner: scripts/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.py
---

# Possibility-symmetric sequential formation that varies has order-dependent record statistics

**Date:** 2026-09-15
**Type:** bounded_theorem
**Scope:** sequential single-site formation products of a possibility-symmetric nearest-neighbor kernel on finite windows of `Z^3` that contain a three-site path; executed on the two-point menu, the six-axis cubic orbit, and zonal kernels on `S^2`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.py`](../scripts/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.py)
**Pinned cache:**
[`logs/runner-cache/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.txt`](../logs/runner-cache/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.txt)

## Result up front

Admissibility gives one nearest-neighbour rule, covariant under lattice
translations and proper cubic rotations, whose local law varies with the
neighbour conditions. Qubit says no possibility is privileged: possibilities
are distinguished by the one-site algebra `M_2(C)` alone, and a `Cl(3,0)`
presentation adds no further primitive structure. Record says records form.

Those sentences already decide a physical question that the rest of the
repository treats as a supplied process. On any three-site path in `Z^3`,
the two ends can form first. Each then sees an empty neighbourhood, so
each is drawn from the empty law `mu_0`, independently of the other. If
the sequential product is independent of formation order, that same
independent pair is the `(L,R)` marginal of every other order, including
the chain. The one-neighbour kernel `K` of the chain must therefore satisfy

```text
K^2 = mu_0.
```

The ends are independent. That identity is the whole mechanism.

It has no varying possibility-symmetric solution on the menus the axioms
actually supply.

- Two-point menu: `K^2(+|+) - K^2(+|-) = (pplus - pminus)^2`. Vanishes if
  and only if the kernel ignores the neighbour.
- Six-axis cubic orbit (the natural finite cubic menu): `K^2(same) -
  K^2(opp) = (a-b)^2`, and the remaining uniform-square condition is
  `(6c-1)^2/3 = 0`. Only the uniform kernel.
- Pure states `S^2`: covariance forces a zonal kernel. Haar-square kills
  every Legendre moment (`lambda_ell(K)^2 = 0`), so every density kernel
  is Haar; a covariant atom at the neighbour stays atomic under `K^2`;
  the equator kernel has two-step `<t^2> = 1/2` against Haar `1/3`.

Once `K_1 = mu_0`, a star of `m` leaves in `Z^3` (the origin and `m` of
its six neighbours) forces the same for every `m`-neighbour kernel: the
center-first order makes the leaves independent copies of `mu_0`, so the
leaves-first order can match only if `K_m = mu_0`.

Therefore variation forces order dependence. The derivation does not
depend on soldering: the six-axis menu is the cubic orbit of a Bloch
axis, and `S^2` is the Aut-orbit of a pure state. In both readings the
empty law is the unique invariant probability on that orbit, and `K^2 =
mu_0` has only that invariant kernel as a possibility-symmetric solution.

The physical formation order is not selected. The note selects neither
order and selects neither rule. Order-dependent statistics are registered
data under
[`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md).
The remaining covariant constructions that would make the order idle —
joint formation on a covariant set, or a covariant law on orders — are
owner decisions and are not adopted.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The ends-independence identity, the two-state and six-axis Haar-square classifications, and the zonal moment identities are proved exactly. No physical order, menu, or rule is selected; soldering is not adopted; joint formation and covariant order-laws are named and not adopted."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "whether a possibility-symmetric Admissibility rule can induce a unique sequential record law on Z^3"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "derive or witness a covariant joint-formation construction, or a covariant law on orders, without importing a Hamiltonian"
conditional_surface_status: "exact on three-site paths and on stars in Z^3; executed on the two-point menu, the six-axis orbit, and zonal S^2 kernels. No infinite-volume statement, no physical-law selection, no axiom edit."
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared mathematical objects

The scientific dependencies are the current four-axiom authority
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
and the registered realized-state primitive
[`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md).
The axiom sentences used, verbatim:

- Qubit: "The full one-site possibility domain has algebraic presentation
  `M_2(C)`." — "A `Cl(3,0)`-compatible real-algebra presentation may be
  used equivalently and adds no further primitive structure." — "No
  possibility is privileged. Possibilities are distinguished by the
  supplied algebraic structure alone."
- Admissibility: "There is one fixed nearest-neighbor admissibility rule,
  covariant under lattice translations and proper cubic rotations." and
  "For each site, the probability distribution over the possibilities is
  determined by, and varies with, the nearest-neighbor conditions."
- Record: "Records form." — "Only records are readable."
- Lattice: sites are the points of `Z^3` with nearest-neighbor adjacency
  and proper cubic rotations about each site.

Admissibility supplies no record-production process, order, clock, or
rate. The realized-state primitive supplies no average over alternative
orders.

Declared mathematical scaffolding, not fitted physics:

- sequential single-site formation products, with the records-only
  reading of partial neighbourhoods;
- the two-point menu `{0,1}` with a general one-neighbour kernel
  `(pplus, pminus)`;
- the six axis points `{±e_x, ±e_y, ±e_z}` with a cubic-covariant kernel
  of orbit weights `(a, b, c)` on same, opposite, and orthogonal pairs,
  `a + b + 4c = 1`;
- zonal Markov kernels on `S^2`, written as densities `g(p·q)` with
  respect to Haar `dt/2` on `[-1,1]`, plus the covariant atomic family
  supported at `{p, -p}` and the equator kernel.

No Hamiltonian, action, carrier, Born weight, Gauss kernel, or readout
instrument is imported. No soldering intertwiner is supplied.

## Exact target and objects

**Target.** Derive that a possibility-symmetric sequential rule whose
one-neighbour kernel varies cannot have an order-independent formation
law on any window of `Z^3` that contains a three-site path, and that
matching on stars then forbids variation at every neighbour cardinality.

Let `mu_0` be the empty-neighbourhood law. Let `K` be the one-neighbour
kernel. A formation order `σ` on a finite window has law the product of
the rule along recorded-neighbour sets. The rule is possibility-symmetric
when `K` intertwines the action of the possibility symmetry group of the
menu (inner automorphisms of `M_2(C)` on `S^2`; the proper cubic group
on the six-axis orbit). It varies when `K` is not equal to `mu_0`.

## Prior art and what is new

The Q8 pair and the six-neighbour affine-channel note already separate
soldering from independent internal naturality for occupancy-to-Bloch
response maps. They do not treat sequential formation products or the
`(L,R)` marginal of a three-site path.

The 2026-09-06/07 formation-versus-static and monotone-order notes work
inside a declared six-projector product family and compare formation to
the static law, or monotone orders to one another. They do not prove
`K^2 = mu_0`, and they do not classify Haar-square kernels.

The 2026-09-13 formation-order covariance note (open pull request #8096,
not a premise) classified interior isotropic binary order-blind kernels
as independent by a path3 matching residual. The present argument is the
mechanism of that residual: ends-first independence, not a binary
specialization, and it is executed on the six-axis cubic orbit and on
`S^2` as well. This note does not depend on that pull request.

Born-form notes in the repository assume a supplied menu and an
additivity or homogeneity clause. Nothing here is a Born derivation.

## Proof-obligation graph

| obligation | exact disposition |
|---|---|
| ends-first makes the two ends i.i.d. `mu_0` | neither end sees the other; each sees the empty neighbourhood |
| order-blindness copies that marginal to the chain | the joint is one law |
| chain `(L,R)` is `mu_0(dL) K^2(dR\|L)` | Markov product |
| therefore `K^2 = mu_0` | identity of kernels `mu_0`-almost everywhere |
| two-state Haar-square | residual `(pplus - pminus)^2` |
| six-axis Haar-square | residual `(a-b)^2`, then `(6c-1)^2/3 = 0` |
| `S^2` densities | zonal; `lambda_ell(K)^2 = 0` so `lambda_ell(K) = 0`; Legendre uniqueness |
| `S^2` atoms and equator | `K^2` atomic, or `<t^2> = 1/2 ≠ 1/3` |
| unique invariant empty law on each orbit | transitivity of Aut on `S^2`; cubic transitivity on six axes, orbit average of a point mass is `1/6` |
| star promotion | center-first leaves are i.i.d. `mu_0` once `K_1 = mu_0` |
| identify a physical order or rule | open and not claimed |

Every leaf needed for the stated finite target is discharged. The last
row is a downstream physics question.

## Theorem 1 — ends-first independence is `K^2 = mu_0`

Let `L—M—R` be any three-site nearest-neighbour path in `Z^3` (three
collinear sites, or an L). In the ends-first order `(L, R, M)`, both `L`
and `R` form with empty neighbourhoods, so

```text
(L, R) ~ mu_0 ⊗ mu_0.
```

The middle kernel never enters this marginal. In the chain order
`(L, M, R)`,

```text
L ~ mu_0,    M ~ K(· | L),    R ~ K(· | M),
```

hence `(L, R) ~ mu_0(dL) K^2(dR | L)`. If the sequential product is
independent of order, these two laws of `(L, R)` agree, so `K^2(· | x) =
mu_0` for `mu_0`-almost every `x`.

The runner executes the identity on the two-point menu: ends-first with
`mu_0` fair is `1/4` on every `(L,R)` pair; the Ising chain with
`(pplus, pminus) = (4/5, 1/5)` has `K^2(+|+) = 17/25` and
`P(L=R=+) = 17/50`. The independent kernel matches ends-first exactly.

## Theorem 2 — two-state Haar-square is independence

Write `pplus = K(+ | +)` and `pminus = K(+ | -)`. Then

```text
K^2(+ | +) = pplus^2 + (1 - pplus) pminus,
K^2(+ | -) = pminus pplus + (1 - pminus) pminus,
```

and their difference is `(pplus - pminus)^2`, checked on six kernels
including the deterministic copy and flip. `K^2` is independent of the
starting point if and only if `pplus = pminus`. Stationarity then forces
that common value to equal `mu_0(+)`, so `K` is the independent kernel.

In particular the identity does not use a swap symmetry of the two
labels. It applies to `{+I, -I}`, which the algebra distinguishes, as
well as to an isotropic pair.

## Theorem 3 — six-axis Haar-square is uniformity

The proper cubic group has 24 elements and is transitive on the six axis
points; the orbit average of any axis point mass is uniform `1/6`. A
cubic-covariant kernel on that orbit has three weights `(a, b, c)` with
`a + b + 4c = 1`. The squared kernel's same-orbit and opposite-orbit
entries differ by `(a-b)^2`. Haar-square therefore forces `a = b`, hence
`a + 2c = 1/2`. Substituting into the remaining same-orbit identity
`2a^2 + 4c^2 = 1/6` yields

```text
(6c-1)^2 / 3 = 0,
```

so `c = 1/6` and `a = b = 1/6`. The runner checks the closed forms
against the explicit six-by-six product, checks the quadratic identity
at five values of `c`, and scans every cubic kernel with denominator at
most 8: the only Haar-square solution is the uniform kernel.

## Theorem 4 — zonal kernels on `S^2`

Inner automorphisms of `M_2(C)` act as `SO(3)` on the pure-state sphere.
The unique invariant probability is Haar. A covariant Markov kernel is
zonal about the neighbour: a density `g(p·q)` with respect to Haar, plus
possible covariant atoms at `{p, -p}`, plus possible mass on latitudes,
of which the equator is the distinguished continuous orbit.

Haar on the zonal coordinate `t = p·q` is `dt/2` on `[-1,1]`. For a
density `g`, Funk–Hecke (the Legendre convolution of zonal kernels)
diagonalizes `K` on degree `ell` with multipliers `lambda_ell(K)`. Haar
is the projection onto degree `0`, so `K^2` Haar means `lambda_ell(K)^2
= 0` for every `ell >= 1`, hence `lambda_ell(K) = 0`. The Legendre
expansion of `g` then has only the constant term, so `K` is Haar.

The runner executes the first two moments on the normalized family `g(t)
= 1 + beta t + gamma P_2(t)`: the dipole is `beta/3` and the quadrupole
is `gamma/5`. Both vanish if and only if `beta = gamma = 0`.

A covariant atom at the neighbour of mass `a > 0` produces an atom of
mass at least `a^2` in `K^2`. Haar has no atoms. The covariant equator
kernel (uniform on `{q : q·p = 0}`) has vanishing dipole, but two steps
draw `w` on a random great circle through `p`, which is the arcsine law
on `t = w·p` with `<t^2> = 1/2` against Haar `<t^2> = 1/3`.

## Theorem 5 — stars kill delayed variation

Suppose `K_1 = mu_0`. Take the origin and `m` of its six neighbours, `1
<= m <= 6`. In the center-first order the center is `mu_0` and each leaf
sees only the center, hence is `mu_0` independent of the center and of
the other leaves. The joint is `mu_0^{m+1}`. In the leaves-first order
the leaves are i.i.d. `mu_0` and the center is drawn from the
`m`-neighbour kernel `K_m`. Matching forces `K_m = mu_0`.

Thus a possibility-symmetric sequential rule cannot postpone variation
to two or more recorded neighbours without breaking order-blindness on a
star that `Z^3` actually contains.

## Theorem 6 — variation forces order dependence

On each of the three menus, the only possibility-symmetric solution of
`K^2 = mu_0` is `K = mu_0`. Combined with Theorem 5, every
neighbour-cardinality kernel equals `mu_0`. That rule does not vary with
nearest-neighbour conditions.

Therefore, on every finite window of `Z^3` that contains a three-site
path, a possibility-symmetric sequential rule that varies has at least
two formation orders whose record laws differ. The difference is already
visible in a two-site marginal of a three-site path. The formation order
is not a record; the realized-state primitive then classifies every
order-dependent statistic as registered data.

This does not depend on soldering. The six-axis calculation is the cubic
reading; the `S^2` calculation is the Aut reading. Both fail in the same
place: `K^2 = mu_0`.

## Boundary and falsifiers

The result is falsified if any of the following finite statements fails:

- ends-first on a three-site path gives a joint in which the two ends are
  not independent copies of `mu_0`;
- the two-state residual is not `(pplus - pminus)^2`;
- the six-axis residual is not `(a-b)^2`, or `(6c-1)^2/3` has a root in
  `[0, 1/4]` other than `c = 1/6`;
- a zonal density with `beta ≠ 0` or `gamma ≠ 0` has vanishing dipole and
  quadrupole;
- the equator two-step second moment equals `1/3`.

The theorem does not treat deterministic 0/1 kernels as a surviving
interior class: copy and flip are included in the two-state residual and
fail it. It does not classify kernels that take the formation order as
an extra argument (Admissibility's rule is one fixed nearest-neighbour
rule). It does not derive a joint-formation construction or a covariant
law on orders. It is not a Born derivation and not an axiom edit.

## Separating clauses, not adopted

The sequential product of a varying possibility-symmetric rule is not a
derivation of a unique record law. The constructions that would make the
order idle, recorded as owner decisions and not adopted, are:

1. records on a covariant set form jointly, not along a total order;
2. the formation order is drawn from a covariant law on orders;
3. the rule is not possibility-symmetric (a privileged possibility
   frame that is not lattice-covariant).

Clause 3 conflicts with the Qubit sentence as written. Clauses 1 and 2
are process constructions Admissibility does not supply. None is adopted
here.

## Honest-auditor read

The load-bearing step is Theorem 1. Everything after it is a
classification of `K^2 = mu_0` under a symmetry. The classification is
complete for two-state kernels, for cubic kernels on the six-axis orbit,
and for zonal densities plus the two covariant singular kernels named
above. It is not a scan of every measure on `M_2(C)`. Mixed states with
a free radial empty law are not a separate escape: an Aut-invariant
empty law is a mixture of shells, and on each shell Theorem 4 applies to
the directional kernel. A purely radial one-neighbour kernel still has
to satisfy radial Haar-square for `mu_0`-almost every radius, which
again forces it not to depend on the neighbour.

What the block settles is that "apply one possibility-symmetric
Admissibility rule along some sequential order and read the finished
window" does not produce a unique record law once the rule varies. That
is a derivation from the axiom symmetry sentences, not a supplied
Hamiltonian.

## Verification

```bash
python3 scripts/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.py
```
