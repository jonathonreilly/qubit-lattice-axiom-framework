# Infinite Redundancy And Quasilocal Record Sectors

**Date:** 2026-07-14

**Type:** meta / exact thermodynamic-sector formation probe

**Authority:** none. This is a conditional exact construction and bounded
no-go stress test. It is not an axiom proposal, canonical-law selection,
primitive, retained theorem, interpretation choice, boundary selection, or
audit verdict. It changes no live foundation, registry, policy, review, or
audit surface.

## Question

Finite redundant witnesses remain coherently reversible. Does the infinite-
volume limit do something genuinely stronger—make the relative phase
unobservable to every local physical operation, turn record values into
nonreconnecting sectors, and thereby derive record permanence or actuality?

The mathematical setting is the quasilocal algebra of an infinite qubit
lattice: finite-site matrix algebras followed by norm closure. This is the
standard operator-algebraic carrier for infinite quantum spin systems; see
Naaijkens' lecture notes for the construction and sector language
([arXiv:1311.2717](https://arxiv.org/abs/1311.2717)). The finite proof below is
self-contained and does not assume a measurement interpretation.

## Result Up Front

Infinite redundancy can genuinely retire the hidden relative phase from the
quasilocal predictive state.

For `N` qubits, compare

```text
|GHZ_theta> = (|0^N> + exp(i theta)|1^N>)/sqrt(2)
```

with the incoherent mixture

```text
rho_mix = (|0^N><0^N| + |1^N><1^N|)/2.
```

Every operator supported on fewer than all `N` sites has exactly the same
expectation in the cat and the mixture. The cross term contains an untouched
factor `<0|I|1>=0`. Only a full-support operator such as `X^(tensor N)` can
recover the phase. In the infinite chain/lattice, every quasilocal observable
is a norm limit of finite-support observables, so all phases define the same
quasilocal state: the half-half mixture of the two branch functionals.

The two branches themselves remain locally distinct. One onsite `Z` has
expectation `+1` in the all-zero branch and `-1` in the all-one branch. No
finite-support operation converts one infinite branch to the other, because
infinitely many untouched sites retain the old value. Thus infinite redundant
records give an exact operational phase quotient and superselection-like
nonreconnection under quasilocal operations.

This is stronger than decoherence in a finite environment. It can make
record-only future sufficiency and permanence theorems **conditional on** an
infinite tail sector and the quasilocal operation algebra.

It does not actualize one branch. The quasilocal restriction of the cat is the
mixture, not either extremal record state. Mixtures with weights `1/2` and
`2/3` share the same two sector supports and the same nonreconnection theorem
but predict different local record frequencies. Sector separation supplies
neither the central weight nor one realized member.

It also does not explain finite-time formation. A finite-range law starting
from a finite seed reaches only a finite causal ball at every finite step. Its
redundancy can be extremely large but remains globally reversible in principle
by an operation covering the full finite record. A literally infinite tail
must be boundary/asymptotic content, an infinite-time limit, or a theorem about
the representation selected by the actual history.

The constitutional consequence is therefore reductive, not additive:

- permanence and loss of hidden phase may be theorems of an exact law plus its
  infinite sector and allowed operations;
- infinite redundancy does not force a reader or two-witness sentence into
  Record; and
- the exact law still must supply or derive event occurrence, the sector
  weights/deterministic successor, and one actual record history.

## Exact Local-Indistinguishability Proof

Let `A_S` act only on a proper subset `S` of the `N` sites. Then

```text
<0^N| A_S tensor I_(S^c) |1^N>
  = <0_S|A_S|1_S> product_(j in S^c) <0|I|1>
  = 0.
```

The conjugate cross term also vanishes. Hence

```text
<GHZ_theta|A_S|GHZ_theta>
 = 1/2 <0^N|A_S|0^N> + 1/2 <1^N|A_S|1^N>
 = Tr(rho_mix A_S)
```

for every `theta` and every proper support.

The companion exhausts every Pauli string through six sites and verifies that
all strings containing at least one identity have equal expectations. The
full-support string `X tensor ... tensor X` instead has expectation `cos(theta)`
in the cat and zero in the mixture.

Let `A` be a quasilocal observable on the infinite lattice and `A_n` a norm-
convergent finite-support sequence. The cat-phase restrictions agree on every
`A_n`; continuity of states gives agreement on `A`. This is the precise phase
retirement. It is not a claim that a normal infinite GHZ vector exists in one
chosen branch representation.

## Branch Separation And Permanence Scope

Write `omega_0` and `omega_1` for the infinite product states with every site
in `0` and `1`. They are separated by one local record read:

```text
omega_0(Z_x)=+1,
omega_1(Z_x)=-1.
```

A unitary supported in a finite set `S` can change only sites in `S`. At every
site outside `S`, the two product states still have opposite content. No such
unitary maps the whole all-zero branch to the all-one branch.

This is the relevant permanence statement:

> Inside the quasilocal operation domain, an infinitely redundant record
> value cannot be revoked by any finite physical operation.

It is not absolute permanence under arbitrary nonquasilocal automorphisms. A
global bit flip maps the two product states, and a full-support phase operator
can distinguish finite cats. The allowed operation algebra is load-bearing.

## Actuality And Weight Remain Separate

The state

```text
omega_p = p omega_0 + (1-p) omega_1
```

is a valid quasilocal state for every `0<=p<=1`. Every member has the same two
permanent branch sectors. Yet

```text
omega_p(Z_x)=2p-1,
```

so `p=1/2` and `p=2/3` are operationally distinct. Sector structure does not
select a weight.

Nor does `omega_p` name an actual member. The realized-state reference can
evaluate a supplied actual branch; it does not derive whether that branch is
`omega_0` or `omega_1`, or why an ensemble has weight `p`.

A deterministic infinite history can close actuality by selecting one
extremal sector. A sampled law can close it by supplying a sample. A global
boundary condition can close it by admitting one branch. These remain live
law/boundary routes; infinite redundancy alone closes none of them.

## Finite-Time And Capacity Boundary

With nearest-neighbor finite propagation on `Z^3`, a seed at the origin can
influence after `t` discrete layers only the Manhattan ball

```text
|B_t|=(4t^3+6t^2+8t+3)/3.
```

This is finite for every finite `t`. Therefore no finite-time event can create
a literally infinite redundant tail from a finite seed. For the finite ball,
an operation supported on all of `B_t` can in principle recover a phase or
reverse a finite copy circuit, subject to the exact law's operation set.

The infinite-sector theorem can still arise in three honest ways:

1. the initial/boundary state already selects an infinite representation;
2. permanence is an asymptotic `t -> infinity` statement; or
3. the exact law admits only quasilocal operations and the actual history
   defines a tail sector whose inverse is outside that operation domain.

Each route is scientifically meaningful. None makes an infinite tail a free
consequence of two witnesses or one clock tick.

## TOE-Lane Classification

| lane | conditional closure | remaining content |
|---|---|---|
| `STATE` | all finite-support future protocols forget GHZ phase in the infinite tail | sector weights and actual extremal member |
| `RECORD` | infinite redundant value is stable against every finite-support operation | derivation of infinite sector and exact allowed-operation scope |
| `ACTUALITY` | no closure from the mixture | deterministic/sample/boundary selector |
| `STATISTICS` | local expectations follow after `p` is supplied | why `p`, prepared-state link, and trial corpus |
| `CLOCK` | causal growth gives layer order | no metric rate; infinite tail takes infinite layers from finite seed |
| `CAPACITY` | infinite lattice can hold the tail | blank tail/boundary and permanent storage cost |
| quantum interference | phase is unavailable to quasilocal observables in the limit | finite cats remain globally coherent; interaction/context law still needed |

No lane result adds a universal axiom sentence. It specifies what the eventual
exact law and boundary theorem could derive.

## No-Go Discipline Gate

The licensed negative is narrow:

> On the displayed infinite product-sector construction, quasilocal phase
> retirement and branch nonreconnection do not select mixture weights or one
> actual branch, and a finite seed cannot create the infinite tail in finite
> nearest-neighbor time.

It is not a no-go against infinite-volume collapse, topological
superselection, deterministic sectors, objective stochastic laws, or an exact
boundary-conditioned history.

### N1 — Alternative-route enumeration

Tested routes are finite GHZ redundancy, infinite product sectors,
finite-support/quasilocal observables, full-support phase recovery, local
branch separation, finite-support branch conversion, central mixtures,
deterministic extremal histories, and nearest-neighbor causal growth. Live
routes include non-product topological sectors, algebraic scattering sectors,
tail algebras generated dynamically, collapse laws, and two-boundary global
solutions.

### N2 — Wall-independence audit

Phase retirement, branch distinguishability, branch nonreconnection, mixture
weight, actual member, finite-time reach, and operation scope are separated by
the explicit controls. They are not counted as seven axiom needs; an exact law
and boundary theorem may derive several together.

### N3 — Hidden-wall scan

`Infinite`, `quasilocal`, `record`, `phase`, `sector`, `permanent`, `actual`,
`weight`, `finite time`, and `boundary` are all load-bearing. The product-state
fixture, equal-amplitude cat, operation algebra, and seed are exposed rather
than treated as foundation content.

### N4 — Exact residual matching

The proper-support Pauli census witnesses local phase retirement only. Onsite
`Z` witnesses branch distinction only. Finite bit flips witness failure to
convert infinite branches only. The `p=1/2` versus `2/3` pair witnesses weight
freedom only. The Manhattan ball witnesses finite reach only.

### N5 — Resolution and rhetoric audit

The proof is exact for finite cats and their quasilocal limiting functionals.
It does not construct a normal cat vector in one infinite product
representation, classify all infinite sectors, or prove absolute permanence.
“Superselection-like” is used unless a representation theorem is explicitly
stated.

### N6 — Partial-closure paths

The phase quotient and finite-operation permanence are genuine closures. A
final law can use them to prove record-only future sufficiency and remove a
separate permanence clause from its dynamics. A deterministic extremal sector
can also remove separate sampling. The remaining work is to derive the sector,
operation algebra, boundary, and frequency corpus from one exact law.

### N7 — Strongest surviving steelman

The strongest route is an infinite-volume algebraic law whose low-record tail
selects a disjoint representation, whose quasilocal dynamics carries one
record value into a stable central sector, and whose extremal decomposition is
unique with Born weights fixed by a preparation theorem. If one actual
extremal component is selected by the same boundary/history law, permanence,
state sufficiency, actuality, and statistics could close jointly. The finite
controls here do not refute that construction.

### N8 — Cross-cycle echo

Finite two-witness probes showed reversible coherence; the infinite limit
explains exactly how that conclusion can change when the allowed inverse needs
unbounded support. The infinite export QCA likewise made no-return conditional
on a blank tail and operation domain. This probe strengthens that positive
route while preserving its boundary and the independent actuality/weight
residual.

## Bottom Line

Infinite redundancy can make a fact permanent in a stronger bare-metal sense:
the inverse would require an operation with unbounded support, outside the
quasilocal physical algebra. It can also erase the hidden GHZ phase from every
finite future record protocol.

It still does not make one fact happen. The infinite cat restricts to a
mixture, and the mixture neither chooses its weight nor names one member. From
a finite seed the infinite certificate is also never finished at finite time.

So this route can derive permanence and predictive-state sufficiency inside a
completed exact law. It does not supply a formation trigger, probability law,
actuality, or a new Record sentence.

## Verification

Run:

```bash
python3 scripts/infinite_redundancy_quasilocal_record_sector_probe_2026_07_14.py
```

The runner exhausts finite Pauli controls and checks the exact branch, weight,
reach, and documentation boundaries. It does not prove a general infinite-
volume superselection theorem or select a law.
