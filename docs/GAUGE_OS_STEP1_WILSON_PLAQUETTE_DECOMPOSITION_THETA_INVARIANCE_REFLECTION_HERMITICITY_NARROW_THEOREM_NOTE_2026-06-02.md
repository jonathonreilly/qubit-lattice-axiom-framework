# Gauge OS Step 1 — Wilson Plaquette Decomposition and Symmetrized Reflection-Hermiticity in the Trivial-Holonomy `U_0=I` Sector (Narrow Theorem)

**Date:** 2026-06-02
**Post-audit source repair:** 2026-07-16
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:** [`scripts/frontier_gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_verifier.py`](../scripts/frontier_gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_verifier.py)
**Runner cache:** [`logs/runner-cache/frontier_gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_verifier.txt`](../logs/runner-cache/frontier_gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_verifier.txt)

## Honest scope

This note proves a finite-periodic, pure-gauge Wilson-action theorem only
on the following explicit sector:

```text
Λ = (Z/L_t) × (Z/L_s)^3,       L_t = 2n ≥ 4,       L_s ≥ 2,
G = SU(N_c),
P(x⃗) = ∏_(t=-n)^(n-1) U_0(t,x⃗) = I for every spatial site x⃗.
```

The last line is the **trivial temporal Polyakov-holonomy sector**.
Only in this sector does the lemma below construct a periodic gauge in
which every temporal link is the identity. The theorem itself is then
stated on configurations already satisfying `U_0=I`. Nontrivial
temporal holonomy and every residual-Polyakov-link formulation are
outside this packet.

On that restricted configuration space it proves:

1. the exact disjoint finite-periodic plaquette decomposition

   ```text
   S_W(U) = S_+(U) + S_+(ΘU) + S_mixed(U);
   ```

2. reality of the half-actions and
   `S_+(ΘU)=S_+(U)` on `Θ`-fixed configurations;
3. reflection-Hermiticity of the explicitly symmetrized class
   `F_f = f + conj(f∘Θ)`.

For one declared spatial plaquette `f`, the note also gives a worked
raw-link support check showing that this particular function depends
only on the declared positive-half spatial links. That witness is not
exported as positive-half admissibility of the observable used by any
downstream OS theorem. In particular, it does not establish membership
in a blocked or factorized algebra such as `A_+^(2)`.

If a downstream theorem independently proves that its chosen `f` is
admissible, the associated formal OS integrand is

```text
(Θf)(U) f(U) = conj(f(ΘU)) f(U),
```

not `conj(F_f(U))F_f(U)`. This packet does not prove non-negativity of
that Wilson-measure integral, an integrated reflection-positivity
inequality, a positive transfer operator, or the complete OS theorem.

### Machine-checked export contract

The primary runner parses this block exactly and fails if source prose
reintroduces the audited overreach.

<!-- gauge-os-step1-export-contract:start -->
```json
{
  "carrier": "finite periodic L_t=2n>=4 and L_s>=2",
  "group_and_action": "pure-gauge SU(N_c) Wilson plaquette action",
  "sector": "configurations already satisfying U_0=I; periodic construction from an unfixed configuration requires P(x)=I at every spatial site",
  "proved": [
    "P_+, P_-, and the two-boundary P_mixed form a disjoint exhaustive plaquette partition and S_W(U)=S_+(U)+S_+(Theta U)+S_mixed(U)",
    "the half-actions are real and S_+(Theta U)=S_+(U) on Theta-fixed configurations",
    "F_f=f+conj(f o Theta) is reflection-Hermitian for the explicitly symmetrized observable class"
  ],
  "worked_witness_only": "one declared spatial plaquette has raw link support contained in E_+",
  "open_downstream_bridge": "positive-half localization and admissibility of the actual observable consumed by any downstream OS argument"
}
```
<!-- gauge-os-step1-export-contract:end -->

---

## 1. Finite periodic carrier and Wilson conventions

Write the physical time representatives as

```text
t ∈ {-n, -n+1, ..., -1, 0, ..., n-1},        L_t = 2n.
```

Sites are `x=(t,x⃗)` with `x⃗∈(Z/L_s)^3`; all directions are periodic.
Directed links carry `U_μ(x)∈SU(N_c)`. Reverse traversal uses the
Hermitian conjugate. For `μ<ν`,

```text
U_(x;μν)
  = U_μ(x) U_ν(x+μ̂) U_μ(x+ν̂)^† U_ν(x)^†.                 (1)
```

The normalized plaquette and Wilson action are

```text
w_p(U) = (1/N_c) Re Tr U_p,
S_W(U) = -β Σ_(p∈P(Λ)) w_p(U),       β>0.                  (2)
```

This is the usual `βΣ_p(1-w_p)` Wilson action with the
configuration-independent constant `β|P(Λ)|` omitted.

Each unoriented plaquette is counted once, with `μ<ν`. Hence

```text
|P(Λ)| = 6 L_t L_s^3.
```

At each site, the three pairs `1≤i<j≤3` are spatial plaquette
orientations and the three pairs `(0,i)`, `i=1,2,3`, are temporal
plaquette orientations.

For the isotropic special case `L_t=L_s=L`, this is `6L^4`.
Orientation reversal sends `U_p` to a conjugate of `U_p^†`, so
`Re Tr U_p` and therefore `S_W` are real and orientation independent.

---

## 2. Periodic temporal gauge: exact holonomy criterion

### 2.1 Gauge convention

A periodic gauge transformation `g:Λ→SU(N_c)` acts by

```text
U_μ^g(x) = g(x) U_μ(x) g(x+μ̂)^†.                         (3)
```

At fixed `x⃗`, define the temporal Polyakov holonomy based at `t=-n`:

```text
P(x⃗)
 = U_0(-n,x⃗) U_0(-n+1,x⃗) ... U_0(n-1,x⃗).               (4)
```

Because `g` is periodic,

```text
P^g(x⃗) = g(-n,x⃗) P(x⃗) g(-n,x⃗)^†.                     (5)
```

Thus the conjugacy class of `P(x⃗)` is periodic-gauge invariant.

### 2.2 Complete-temporal-gauge lemma

**Lemma.** A periodic gauge transformation can set

```text
U_0^g(t,x⃗)=I for every t and x⃗                            (6)
```

if and only if

```text
P(x⃗)=I for every x⃗.                                      (7)
```

**Necessity.** If every transformed temporal link is `I`, their
ordered product is `I`. Equation (5) then gives
`g(-n,x⃗)P(x⃗)g(-n,x⃗)^†=I`, hence `P(x⃗)=I`.

**Sufficiency and construction.** Set `g(-n,x⃗)=I` and recurse:

```text
g(t+1,x⃗) = g(t,x⃗) U_0(t,x⃗).                            (8)
```

Equation (3) immediately gives `U_0^g(t,x⃗)=I`. After the last link,

```text
g(n,x⃗) = g(-n,x⃗) P(x⃗) = I,
```

so the recursion closes periodically exactly when (7) holds.
No residual Polyakov link is hidden in this construction. Once (6)
holds, the residual transformations that preserve it are
time-independent gauge transformations `g(t,x⃗)=h(x⃗)`.

### 2.3 Exact nontrivial-holonomy control

For `SU(3)`, take every temporal link to be `I` except the periodic
wrap link at one fixed spatial site, where

```text
H = diag(-1,-1,1) ∈ SU(3).                                (9)
```

Then `P(x⃗)=H`, with `Tr H=-1`, whereas `Tr I=3`. A periodic gauge
transformation can only replace `H` by a conjugate, preserving its
trace and eigenvalues. It therefore cannot set every temporal link to
`I`. The runner constructs this exact finite control and also verifies
the recursive gauge transformation on a nontrivial configuration with
`P(x⃗)=I` at every spatial site.

The rest of this theorem is explicitly restricted to configurations
satisfying (6). Equation (7) is only the criterion under which the
displayed periodic construction can reach that restricted space.

---

## 3. Reflection through `t=-1/2`

The site reflection is

```text
r(t,x⃗)=(-1-t,x⃗)                                          (10)
```

with time understood modulo `L_t`. Its action on directed links is

```text
(ΘU)_i(t,x⃗) = U_i(-1-t,x⃗),                    i=1,2,3,
(ΘU)_0(t,x⃗) = U_0(-2-t,x⃗)^†.                           (11)
```

The dagger and shifted base point in the temporal rule are required:
the reflected temporal edge has reversed orientation. Direct
substitution gives `Θ²U=U`. In the complete-temporal-gauge sector,
`(ΘU)_0=I`, so the sector is stable under `Θ`.

Within the `U_0=I` sector, reflection bijects plaquettes and may reverse
their orientation. Because `Re Tr U_p = Re Tr U_p^†`,

```text
S_W(ΘU)=S_W(U).                                            (12)
```

The primary runner verifies the sector identity on generic spatial links
with `U_0=I`. A separate hostile definition check uses nonidentity
temporal links only to ensure that omitting the dagger in (11) is
detectable; that control is not an exported theorem beyond the declared
sector.

---

## 4. Exact finite-periodic plaquette partition

Let `P_sp(t)` be the spatial plaquettes in time slice `t`, and let
`P_0i(t)` be the temporal plaquettes based at `t`, spanning
`t→t+1`.

Define:

```text
P_+
 = {spatial p at t=0,...,n-1}
   ∪ {temporal p based at t=0,...,n-2};

P_-
 = {spatial p at t=-n,...,-1}
   ∪ {temporal p based at t=-n,...,-2};

P_mixed
 = {temporal p based at t=-1}       [reflection-plane family]
   ∪ {temporal p based at t=n-1}.   [periodic-wrap family]   (13)
```

These sets are disjoint and exhaustive. The wrap family is part of
`P_mixed`; discarding it would make the finite-periodic partition
false. Reflection maps `P_+` bijectively to `P_-` and preserves each
mixed boundary family setwise while reversing the temporal orientation.

The exact counts are

```text
|P_+| = |P_-| = 3nL_s^3 + 3(n-1)L_s^3
                  = 3(2n-1)L_s^3,
|P_mixed| = 6L_s^3,                                      (14)
```

whose sum is `6L_tL_s^3`.

Define

```text
S_+(U)     = -β Σ_(p∈P_+)     w_p(U),
S_-(U)     = -β Σ_(p∈P_-)     w_p(U),
S_mixed(U) = -β Σ_(p∈P_mixed) w_p(U).                    (15)
```

Disjointness and exhaustivity give

```text
S_W(U)=S_+(U)+S_-(U)+S_mixed(U).                          (16)
```

The reflection bijection and orientation-independent real trace give

```text
S_-(U)=S_+(ΘU),                                           (17)
```

and therefore

```text
S_W(U)=S_+(U)+S_+(ΘU)+S_mixed(U).                         (18)
```

Each term in (15) is real. On a `Θ`-fixed configuration, (17) reduces
to `S_+(ΘU)=S_+(U)`. This fixed-configuration consistency statement is
not a proof of the integrated reflection-positivity inequality.

In complete temporal gauge, a temporal plaquette reduces to

```text
U_(t,x⃗;0i)=U_i(t+1,x⃗)U_i(t,x⃗)^†.                      (19)
```

The load-bearing reduction (19), including its mixed-kernel use, is
also supplied by
[`GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md`](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md).
This note uses that authority only for the reduced temporal-gauge
mixed-plaquette surface; it does not import a full positivity theorem.

---

## 5. Worked raw-link support witness and the open admissibility bridge

### 5.1 Raw-link support witness in this sector

After complete temporal gauge, the temporal links are fixed constants.
The dynamical positive-half link set is

```text
E_+ = {(t,x⃗,i): t∈{0,...,n-1}, i∈{1,2,3}}.              (20)
```

Let `A_+^link` be the raw link-function algebra whose value depends only
on link variables indexed by `E_+`. Equivalently, `f∈A_+^link` when any
two `U_0=I` configurations that agree on `E_+` give the same value of
`f`.

The worked witness is the normalized complex spatial plaquette trace at
a declared plaquette `p_+` in slice `t=0`:

```text
f(U) = (1/N_c) Tr U_(p_+),       p_+=(t=0,x⃗;1,2).         (21)
```

Its four link keys are

```text
(0,x⃗,1), (0,x⃗+1̂,2), (0,x⃗+2̂,1), (0,x⃗,2),             (22)
```

with the last two traversed in reverse. Every key in (22) lies in
`E_+`; hence `supp(f)⊂E_+` and `f∈A_+^link`. This is an exact
structural support proof for this one function, not a prose inference
from the location of the loop.

The same argument applies to any explicitly enumerated Wilson loop
whose nonconstant link support is a subset of `E_+`. It does not show
admissibility in the observable algebra actually consumed by a
downstream OS theorem. In particular, membership in a separate blocked
or factorized algebra such as `A_+^(2)` remains an open downstream
bridge.

### 5.2 Reflected conjugate and the OS-form product

For a function independently admitted by a downstream construction,
define the antilinear reflected observable

```text
(Θf)(U) := conj(f(ΘU)).                                    (23)
```

Its support is the reflected negative-half link set `r(supp(f))`.
The formal OS product associated with `f` is

```text
(Θf)(U) f(U) = conj(f(ΘU)) f(U).                           (24)
```

Equation (24) is only a formal identity here. This packet does not
admit a downstream observable or prove the measure/kernel hypotheses
needed for non-negativity after integration.

### 5.3 The two-half symmetrization

Define

```text
F(U) = f(U) + conj(f(ΘU)) = f(U)+(Θf)(U).                  (25)
```

Using `Θ²=id`,

```text
F(ΘU)
 = f(ΘU)+conj(f(U))
 = conj(F(U)).                                             (26)
```

Thus this explicitly symmetrized `F` is reflection-Hermitian. No such
identity is asserted for an arbitrary unsymmetrized Wilson loop. But

```text
supp(F)=supp(f) ∪ r(supp(f)),                              (27)
```

so a nonconstant `F` depends on both halves. In particular,
`supp(F)⊄E_+`; this construction does not place `F` in `A_+^link` or
in any downstream positive-half test algebra. Reflection-Hermiticity
does not imply plus-locality.

The runner verifies all of these statements structurally and includes
three observable-class hostile controls:

- a deliberately leaky `f_bad` whose support contains a negative-half
  variable is rejected by the `supp(f)⊂E_+` test;
- `F` itself is rejected as plus-local and changes when an appropriate
  negative-half link is changed while the genuine `f` does not;
- the unsymmetrized `f` fails the reflection-Hermiticity identity on a
  deterministic generic-sector configuration, while the explicitly
  symmetrized `F` satisfies it.

---

## 6. What is and is not proved

### Proved on the declared finite carrier and sector

- A periodic complete temporal gauge exists exactly for
  `P(x⃗)=I` at every spatial site.
- The recursive periodic gauge transformation (8) constructs it.
- A finite exact `SU(3)` nontrivial-holonomy control prevents complete
  `U_0=I` gauge under periodic transformations.
- The two-boundary-family partition (13) is disjoint and exhaustive.
- The normalized Wilson action obeys (18), with correct reflection
  orientation, boundary assignment, and reality.
- The declared spatial plaquette witness (21) has raw link support
  contained in `E_+`.
- The explicitly symmetrized `F` in (25) is reflection-Hermitian, while
  an unsymmetrized loop is not thereby reflection-Hermitian.

### Not proved

- any residual-Polyakov-link action or measure treatment;
- positive-half localization or admissibility of the actual observable
  consumed by a downstream OS theorem;
- membership of the worked witness in a downstream
  factorized/blocked observable algebra;
- positivity of the integrated product (24);
- full Wilson reflection positivity, a positive transfer matrix, the
  coupled fermion-gauge theorem, continuum OS reconstruction, or a
  parent-row status change.

The recently landed Wilson transfer/reflection blocks may be used by
downstream work only for their own proved scopes. They are not a
substitute for the link-support test in §5.

---

## 7. Validation and hostile controls

The primary runner uses the exact carrier

```text
L_t=4,   L_s=2,   SU(3),
```

with `32` sites and `192` plaquettes. Unlike `L_t=2`, this carrier has
nonempty same-half temporal plaquette families. It checks:

- `|P_+|=72`, `|P_-|=72`, `|P_mixed|=48`;
- `24` reflection-plane and `24` periodic-wrap mixed plaquettes;
- disjointness, exhaustivity, the `Θ` plaquette bijection, (16), (17),
  and (18);
- `Θ²=id` and `S_W(ΘU)=S_W(U)` within the `U_0=I` sector;
- the exact temporal-holonomy criterion, constructive trivial-holonomy
  gauge transformation, Polyakov-holonomy conjugacy, and Wilson-action
  gauge invariance;
- the `H=diag(-1,-1,1)` nontrivial-holonomy obstruction;
- exact raw-link support inclusion for the worked `f`, negative-half
  mutation independence, the formal product (24), and
  reflection-Hermiticity of the explicitly symmetrized `F`;
- independent agreement of (24) with the reflected negative plaquette,
  and rejection of the incorrect `conj(F)F` substitution;
- structural rejection of a negative-half leak, rejection of `F` as
  plus-local, and a hostile unsymmetrized-loop reflection-Hermiticity
  failure;
- failure of an omitted-wrap partition;
- failure of a reflection rule with the wrong temporal orientation;
- exact parsing of the export contract and sharded-ledger discovery of
  direct-consumer non-inheritance firewalls, without reading or pinning
  audit outcomes.

Run:

```bash
python3 scripts/frontier_gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_reflection_hermiticity_narrow_verifier.py
```

The registered cache is refreshed from this live runner. Audit status
remains solely an independent-audit decision.

---

## 8. Direct-consumer boundary

Downstream consumers may cite this note for:

- the trivial-holonomy complete-temporal-gauge lemma;
- the exact finite-periodic Wilson plaquette split;
- the worked raw-link support fact `supp(f)⊂E_+` for the exact declared
  plaquette;
- reflection-Hermiticity of the explicitly symmetrized class and its
  distinction from positive-half locality.

They may not cite it as admitting the actual observable used by a
downstream OS argument, as proving that arbitrary Wilson loops belong
to a separate `A_+^(2)` surface, or as proving positivity of a Gram
matrix. Those remain additional hypotheses or theorems of the consuming
packet.

---

## 9. Explicit construction inputs

| Input | Role | Boundary |
|---|---|---|
| Finite periodic `SU(N_c)` link carrier and gauge law (3) | explicit construction surface | no continuum claim |
| Normalized Wilson action (2) | explicit action definition | pure gauge only |
| Trivial temporal Polyakov holonomy (7) | explicit sector hypothesis | not derived; no general-orbit claim |
| Reflection rule (11) | explicit finite-lattice convention | temporal dagger retained |
| Mixed temporal-gauge reduction (19) | load-bearing reduced plaquette identity | cited retained mixed-kernel note; no full RP import |

No fitted values, empirical targets, new axioms, or new framework
primitives are introduced.

---

## Dependencies

- [`GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md`](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md)
  — load-bearing only for the complete-temporal-gauge reduction of a
  temporal plaquette to adjacent spatial links.

Context only, not upstream premises:

- `REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`
- `RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`
- `RP_TWO_STEP_TRANSFER_MATRIX_GRASSMANN_BEREZIN_BRIDGE_NARROW_NOTE_2026-06-02.md`
- `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`

This source repair does not edit any audit ledger, queue, verdict, or
durable audit status.
