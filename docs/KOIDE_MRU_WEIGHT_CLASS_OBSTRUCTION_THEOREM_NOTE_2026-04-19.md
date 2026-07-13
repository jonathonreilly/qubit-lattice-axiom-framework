# Koide MRU Weight-Class and Quotient-Forcing Obstruction Theorem

**Date:** 2026-04-19 (first-principles quotient-forcing repair 2026-07-12)
**Lane:** Charged-lepton Koide / MRU
**Type:** no_go
**Claim type:** no_go
**Claim scope:** exact negative boundary for two proposed forcing steps on the
supplied `d=3` cyclic carrier: the unreduced determinant has weights `(1,2)`,
and the supplied cyclic carrier does not force the real doublet to factor
through one radius. The obstruction survives even after granting the proposed
coefficient-space `C_3` action, algebraic conjugation invariance,
spectrum-scalar grammar, and a common Record-content-to-carrier encoding. The
result does not forbid a future physical law that independently removes the
cubic phase channel.
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote an audit outcome.
**Primary runner:**
[`scripts/frontier_koide_mru_weight_class_obstruction_theorem.py`](../scripts/frontier_koide_mru_weight_class_obstruction_theorem.py)
**Runner cache:**
[`logs/runner-cache/frontier_koide_mru_weight_class_obstruction_theorem.txt`](../logs/runner-cache/frontier_koide_mru_weight_class_obstruction_theorem.txt)

## Question

The old positive route replaced the real doublet coordinates `(r_1,r_2)` by
one radius and then applied an equal-weight two-slot determinant. The auditor's
load-bearing objection was precise:

> The scalar lane quotients the internal SO(2) frame of the real doublet and
> therefore retains only the doublet radius, giving the two-slot carrier
> `(rho_+,rho_perp)`.

Does that quotient follow from the current framework and cyclic-carrier
structure, or is it an additional physical readout law?

## Inputs

Only two source authorities are load-bearing:

| Authority | Consumed content |
|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Record content is one admissible local `M_2(C)` possibility, and scalar readout is finitely additive over disjoint record collections. The memo supplies no map from that content to the cyclic `3 x 3` carrier, readout-context selection, weighting, log-determinant law, or arbitrary physical-observable identification. |
| [`KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md`](KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md) | exact compression to `H=aI+bC+bbar C^2` and the real cyclic coordinates `(r_0,r_1,r_2)`. |

No observed mass, fitted selector, literature value, new axiom, unapproved
primitive, or target value is used.

## 1. Cyclic carrier and block powers

Let `C` be the real `3 x 3` cyclic shift, `C^3=I`, and

```text
H = a I + b C + bbar C^2,             a in R, b=x+iy in C.
```

With

```text
B_0 = I,
B_1 = C+C^2,
B_2 = i(C-C^2),
H = (r_0/3)B_0 + (r_1/6)B_1 + (r_2/6)B_2,
```

the real Frobenius norms are `(3,6,6)`, so

```text
E_+    = r_0^2/3                 = 3a^2,
E_perp = (r_1^2+r_2^2)/6        = 6|b|^2.
```

Write

```text
u = |b|^2 = x^2+y^2.
```

The proposed radius quotient keeps `(a,u)` and erases the angle of `b`.

## 2. Exact positive boundary: quadratic scalars are radial

Grant the proposed coefficient-space action in which the cyclic generator acts
on the doublet plane by
`b -> omega b`, where `omega^3=1`, `omega != 1`. A homogeneous real quadratic
scalar on `R a direct-sum R^2_(x,y)` has a singlet term, singlet-doublet cross
terms, and a symmetric quadratic form on the doublet.

The cross terms vanish under `C_3`, because the doublet has no fixed real
covector. If `G` is the symmetric doublet matrix, invariance gives

```text
R(2pi/3)^T G R(2pi/3) = G,
```

whose symmetric solutions are exactly `G=lambda I_2`. Therefore every
`C_3`-invariant homogeneous quadratic scalar has the form

```text
q(a,b) = A a^2 + B |b|^2.
```

Including lower degrees adds only a constant and a term linear in `a`.
Consequently every cyclic scalar polynomial of total degree at most two
factors through `(a,u)`. This is the strongest radialization theorem under the
granted coefficient-space action.

It does not prove the physical quotient. The framework does not say that the
charged-lepton scalar readout stops at quadratic order.

## 3. Exact invariant-ring obstruction at degree three

Define the cubic real invariants

```text
v = Re(b^3) = x^3-3xy^2,
w = Im(b^3) = 3x^2y-y^3.
```

They obey

```text
v^2+w^2 = u^3.
```

The exact real polynomial invariant ring of the cyclic doublet is

```text
R[x,y]^(C3) = R[u,v,w] / (v^2+w^2-u^3).                 (1)
```

To prove (1), work over the complex variables `(b,bbar)`. A monomial
`b^p bbar^q` is `C_3` invariant exactly when

```text
p-q = 0 mod 3.
```

If `p>=q`, it equals `u^q (b^3)^((p-q)/3)`; if `q>=p`, use `bbar^3`
instead. Thus `u,b^3,bbar^3` generate, with the single relation
`b^3 bbar^3=u^3`. For completeness, reduce any polynomial modulo
`z zbar-u^3` to the unique shape

```text
f_0(u) + sum_(k>=1) f_k(u) z^k + sum_(k>=1) g_k(u) zbar^k.
```

Under `z -> b^3`, the displayed monomials have pairwise-distinct exponent
pairs in `C[b,bbar]`, so their images are linearly independent. The kernel is
therefore exactly the stated principal relation. Taking real and imaginary
parts gives (1).

If algebraic conjugation invariance is also granted, it sends `b -> bbar`, so
it fixes `(u,v)` and reverses `w`. The invariant ring after adjoining this
reflection, equivalently for the dihedral action generated by the cyclic
rotation and reflection, is therefore

```text
R[x,y]^(D3) = R[u,v].                                    (2)
```

Indeed reflection swaps `z=b^3` and `zbar`; its fixed polynomials are generated
by `z+zbar=2v` and `z zbar=u^3`, together with `u`. Thus no additional
reflection-even generator is omitted from (2).

Full `SO(2)` invariance is strictly stronger:

```text
R[x,y]^(SO(2)) = R[u].                                   (3)
```

Equations (1)-(3) isolate the missing step. Cyclic symmetry permits both
cubic phase channels. Conjugation removes the orientation-odd channel `w`,
but it leaves

```text
v = |b|^3 cos(3 arg b).
```

Only full circle invariance, or a separately derived rule eliminating every
nonzero angular harmonic, gives the one-radius quotient.

## 4. Spectrum-native scalars retain the cubic channel

Even granting the proposed spectrum-scalar grammar, the matrix multiplication
already present on the cyclic carrier makes `v` coordinate-free. Direct
evaluation gives

```text
tr(H)   = 3a,
tr(H^2) = 3a^2+6u,
det(H)  = a^3-3au+2v,
tr(H^3) = 3a^3+18au+6v.                                 (4)
```

Hence `(a,u,v)` can be reconstructed from ordinary symmetric spectral
invariants. Spectrum-nativity does not erase `v`; it exposes it.

A positive-definite same-radius witness makes the failure decisive. Set
`a=3`, and compare

```text
b_1 = 1,
b_2 = exp(i pi/6).
```

Both have `u=1`. Their spectra are

```text
spec(H_1) = {5,2,2},
spec(H_2) = {3+sqrt(3),3,3-sqrt(3)},
```

so both matrices are positive definite. But

```text
det(H_1)=20,       tr(H_1^3)=141,
det(H_2)=18,       tr(H_2^3)=135.
```

The two points have the same proposed quotient coordinates `(a,u)` and are in
different `D_3` orbits, yet even the positive-cone scalar `log det(H)`
distinguishes them. The radius is therefore not a sufficient statistic for
generic spectrum-native scalar content.

## 5. Record additivity does not select the quotient

Record says that record content is one admissible local `M_2(C)` possibility
and that the finite scalar readout over pairwise-disjoint records is additive.
Neither load-bearing authority maps that local content to the cyclic `3 x 3`
carrier. Therefore Record alone cannot constrain a function of `H`; the
physical source/readout bridge is already absent before additivity is used.

The stronger conditional test also fails constructively. Grant a
Record-content domain with two distinct labels and choose one common encoding
`eta` into the cyclic Hermitian carrier whose image contains the two witness
matrices of Section 4; write `H_R=eta(content(R))`. This is a hypothetical
bridge held fixed in both models, not a claimed physical construction. Then
both laws

```text
I_rad(S) = sum_(R in S) tr(H_R^2),
I_ang(S) = sum_(R in S) det(H_R)
```

obey

```text
I(empty)=0,
I(S disjoint-union T)=I(S)+I(T).
```

Both are determined by record content through the same fixed `eta` and use the
same law for every record.
The first depends only on `(a,u)`; the second also depends on `v`. The witness
in Section 4 makes the two laws disagree on equal-radius content.

Thus the actual packet stops before any Record-to-carrier identification; even
after granting a common identification, Record additivity is compatible with
a radial scalar law and with a phase-sensitive scalar law. It cannot select
one of them. This conditional two-model witness is the first-principles
non-entailment step that the old runner was missing.

## 6. Unreduced weight-class obstruction

For completeness, the original determinant obstruction remains exact. Let
`P_+` and `P_perp` be the rank-one and rank-two real-isotype projectors. On the
unreduced isotypic-scalar carrier,

```text
D = alpha P_+ + beta P_perp,
det(D)=alpha beta^2.
```

For

```text
S_(mu,nu)=mu log(E_+)+nu log(E_perp)
```

at fixed `E_++E_perp=E_tot`, the unique interior stationary point satisfies

```text
E_+/E_perp = mu/nu,
kappa := a^2/|b|^2 = 2mu/nu.
```

The unreduced determinant weights `(mu,nu)=(1,2)` and therefore lands at
`kappa=1`, not the MRU leaf `kappa=2`.

## 7. Exact factorization criterion and live positive route

For any scalar function `f(a,b)`, the following are equivalent:

1. `f(a,b)=F(a,|b|^2)` for some `F`;
2. `f` is constant on every circle of fixed `b` radius;
3. `f` is invariant under the full action `b -> exp(i theta)b`.

For a polynomial cyclic scalar, this says exactly that its normal form lies
in `R[a,u]`; all `v` and `w` dependence must vanish.

This gives three honest ways a future positive theorem could close the
physical route without changing the algebra above:

- derive full `SO(2)` invariance of the charged-lepton readout;
- derive naturality under the full orthogonal automorphism group of the real
  `C_3` module (whose doublet centralizer contains `SO(2)`), so the readout
  factors through the orbit map; merely saying that multiplication is
  forgotten does not eliminate the cubic invariants;
- derive an exact quadratic/Frobenius scalar grammar together with decoupling
  of every cubic and higher invariant.

The quadratic theorem in Section 2 proves the algebra needed by the third
route after that physical grammar is supplied. None of these physical
selection statements is contained in the current two-source packet.

## 8. Conditional reduced-carrier corollary

If a future theorem supplies any equivalent factorization criterion from
Section 7, define

```text
rho_+^2    = E_+,
rho_perp^2 = E_perp.
```

Then the supplied two-slot carrier has

```text
det diag(rho_+,rho_perp)=rho_+ rho_perp.
```

At fixed `rho_+^2+rho_perp^2=E_tot`, its unique positive log-volume maximum is

```text
rho_+^2=rho_perp^2=E_tot/2,
```

equivalently `E_+=E_perp`, `a^2=2|b|^2`, and `kappa=2`. This corollary is
exact after the quotient is supplied. It is not used to prove the no-go.

## 9. No-Go Discipline gate

The negative claim is deliberately narrow: the two supplied authorities do
not force the quotient, and the obstruction persists under the explicitly
granted strengthenings above. It does not say the physical quotient is false
or that no future dynamics/readout theorem can derive it.

### N1 — alternative routes

| Route | Retained authority consumed | Result | Honesty marker |
|---|---|---|---|
| granted cyclic scalarity | [cyclic compression](KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md) supplies `H`; the coefficient action is granted locally | the exact ring (1) retains `(u,v,w)` | ATTEMPTED |
| granted algebraic conjugation | [cyclic compression](KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md) plus the stated reflection | the exact ring (2) still retains `v` | ATTEMPTED |
| granted spectrum-scalar grammar | [cyclic compression](KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md) supplies matrix multiplication | (4) reconstructs `v`; positive same-radius matrices have different determinants | ATTEMPTED |
| Record finite additivity | [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md); no carrier map is supplied | absent a bridge Record is irrelevant; after constructing one common `eta` containing the witness pair, `I_rad` and `I_ang` are compatible additive laws | ATTEMPTED |
| unreduced determinant forcing | [cyclic compression](KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md) supplies the rank-one/rank-two carrier | determinant multiplicities give `(1,2)` and `kappa=1` | ATTEMPTED; EXACT OBSTRUCTION |
| real Schur / quadratic uniqueness | [cyclic compression](KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md) plus the granted coefficient action | succeeds only through degree two; the first surviving phase scalar is cubic | ATTEMPTED; PARTIAL POSITIVE |

The first five routes fail as forcing arguments on the supplied or explicitly
granted structures. The sixth identifies the smallest live positive
subtheorem instead of being counted as another wall.

### N2 — wall independence

The collapsed wall set contains one item: a physical law must eliminate `v`
(and, without conjugation, `w`) from the scalar readout. Full `SO(2)`
invariance, full orthogonal-module naturality, and exact higher-order
decoupling are alternative ways to close that same wall, not three independent
walls.

### N3 — hidden-wall scan

The cyclic carrier and Record clauses are not silently linked: the current
packet contains no map from local `M_2(C)` Record content to `H`. The stronger
two-model test explicitly constructs one common `eta` whose image contains the
witness pair. The
positive-definite domain is checked explicitly, not assumed. The conditional
reduced carrier is labelled non-load-bearing. No standard-physics convention,
observed value, target match, registered primitive, or background selector is
hidden in the proof.

### N4 — residual matching

No prior no-go is used as a load-bearing witness. Earlier demotion,
real-structure, and reduced-carrier notes are context for why this question was
asked; the present invariant-ring proof uses the retained carrier, while the
Record result first identifies the absent bridge and then tests a common
hypothetical encoding. Their narrower route failures are not presented as a
global proof.

### N5 — rhetoric audit

The polynomial and spectral statements are per supplied cyclic matrix. Record
supplies no bridge to that matrix. The conditional countermodel is per finite
disjoint record collection after constructing one common encoding containing
the witness pair. No lattice-wide
dynamics, record-formation process, physical species identification, or
all-observable theorem is claimed. The result is exactly non-forcing by the
listed and granted premises, not universal physical impossibility.

### N6 — partial-closure paths

Section 7 preserves three closure paths. A separately retained readout theorem
could supply the quotient without a new axiom. A degree-two physical grammar
would immediately consume the positive theorem of Section 2. The relevant
existing surfaces are:

| Existing path | Current ledger status | What it closes / what remains |
|---|---|---|
| `docs/CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md` | `audited_clean`, `retained` | proves phase erasure by `Q` for a supplied positive mass triple; explicitly does not select the physical registered-mass functional or source carrier |
| `docs/KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md` | `unaudited`, `bounded_theorem` | supplies degree-two algebra only; the physical measure/readout remains open |
| `docs/KOIDE_Q_REDUCED_CARRIER_PHYSICAL_IDENTIFICATION_OBSTRUCTION_NOTE_2026-06-12.md` | `unaudited`, `open_gate` | names the physical bridge but does not construct it |
| `docs/KOIDE_CONVENTION_INVARIANT_SCALAR_SELECTOR_DOUBLET_CONSTANCY_NARROW_THEOREM_NOTE_2026-07-12.md` | `unaudited`, `bounded_theorem` | controls fixed-label doublet selectors and gives an unordered-PVM counterexample; it does not derive the carrier/readout |

Thus no retained item in this focused inventory supplies the missing physical
grammar. What would close the wall is still explicit: a retained theorem
deriving full orbit invariance, or a retained exact second-order readout
grammar with higher harmonics excluded.

### N7 — steelman

The strongest counterargument is that the physical charged-lepton observable
may be first-live and exactly second order, so real Schur theory would make it
radial even though the full cyclic algebra has cubic invariants. That would
break a broader all-possible-futures no-go. It does not break this theorem:
the current minimal axiom memo explicitly leaves readout-context and arbitrary
physical-observable identification outside its content, and the retained
cyclic-compression theorem supplies three channels without selecting a
second-order grammar. The steelman is therefore the next positive bridge, not
an unspoken premise already present here.

### N8 — cross-cycle echo

Prior nearby walls were checked individually:

| Prior surface | Retired? | Mechanism and applicability here |
|---|---|---|
| `docs/KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md` | no; `unaudited`, `positive_theorem` | narrowed the earlier MRU presentation; it did not derive the quotient |
| `docs/KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md` | no; `unaudited`, `no_go` | real/CPT block counting leaves the scalar-lane quotient open |
| `docs/KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md` and `docs/KOIDE_A1_PROBE_Q_READOUT_FUNCTIONAL_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe16.md` | no; `unaudited`, `bounded_theorem` | supply only conditional `Z_2` and functional-pivot mechanisms, neither a retained quotient theorem |
| `docs/BAE_U1B_CANONICAL_PHASE_NOTE_2026-05-17.md` | no; `unaudited`, `bounded_theorem` | tests a different phase-selection lane and supplies no retained charged-lepton quotient theorem |
| `docs/CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md` | partially; retained | retires only `Q` phase dependence for a supplied mass triple, not source-domain or physical-carrier selection |

The present mechanism is applicable because the exact invariant ring and
conditional two-model test evaluate the same missing factorization step. It
does not relabel any prior open wall as retired, and future
readout-factorization work remains open.

**No-Go Discipline result:** PASS for the narrow current-premise non-forcing
claim.

## 10. Reproduction and interpretation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_koide_mru_weight_class_obstruction_theorem.py
```

The runner checks the retained dependency classes, invariant rings, the
degree-two boundary, the exact spectral formulas, the positive same-radius
witness, the conditional Record-additivity countermodel, the unreduced `(1,2)`
determinant, and the conditional reduced corollary.

The claim-state movement is exact but negative: the physical quotient cannot
be obtained from the restricted packet by renaming a radius as the scalar
lane. A positive derivation must supply an actual law that removes the cubic
phase invariant.
