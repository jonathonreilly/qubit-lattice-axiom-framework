# The Wilson--staggered Dobrushin certificate boundary does not identify a physical critical surface

**Date:** 2026-07-12  
**Type:** no_go  
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.  
**Primary runner:** [`scripts/wilson_staggered_dobrushin_certificate_boundary_critical_scaling_no_go_2026_07_12.py`](../scripts/wilson_staggered_dobrushin_certificate_boundary_critical_scaling_no_go_2026_07_12.py)  
**Cached output:** [`logs/runner-cache/wilson_staggered_dobrushin_certificate_boundary_critical_scaling_no_go_2026_07_12.txt`](../logs/runner-cache/wilson_staggered_dobrushin_certificate_boundary_critical_scaling_no_go_2026_07_12.txt)

## 0. Result

For the supplied massive Wilson--staggered model, write

```text
kappa(m)=14/(m^2+2),
alpha_F(m)=(3/2)kappa^2(2-kappa)/(1-kappa)^2.                         (0.1)
```

The preceding one-link theorem used the sufficient Dobrushin row
`alpha_old=18 beta+alpha_F`. The exact `SU(3)` trace range sharpens its Wilson
part without changing the action or Gibbs specification:

```text
alpha_sharp(beta,m)=(27/2)beta+alpha_F(m).                            (0.2)
```

Consequently `alpha_sharp<1` is itself a valid uniqueness, exponential
mixing, gauge--fermion full-sequence, and gauge-invariant OS-gap wedge. On the
old equality curve,

```text
alpha_old=1  implies  alpha_sharp=1-(9/2)beta.                        (0.3)
```

Every old-boundary point with `beta>0` is therefore strictly inside a valid
mixing region for the same model. At `m=8`, for example,
`beta=0.0447559919...` puts `alpha_old=1`, while
`alpha_sharp=0.7985980366...`. Thus equality in the old sufficient estimate
cannot identify a physical critical surface. At the shared endpoint
`beta=0`, equality still gives no converse and no criticality theorem.

There is also a quantitative necessary scaling condition inside the sharper
wedge. Let

```text
delta(a)=1-alpha_sharp(beta(a),m(a))>0.                               (0.4)
```

One may take `c=1/100` in the weighted comparison estimate. For covered local
gauge--fermion observable families,

```text
|omega_a(F_a G_a)-omega_a(F_a)omega_a(G_a)|
 <=C [L_F(a)L_G(a)/delta(a)]
      exp[-c delta(a) dist_latt(supp F_a,supp G_a)],                  (0.5)

Delta_OS(a)>=c delta(a)/a_tau.                                       (0.6)
```

Hence a gauge-invariant propagating family with a non-vacuum physical energy
bounded above along an isotropic `a_tau=a` trajectory must satisfy
`delta(a)=O(a)`, unless it leaves the sharper wedge. At fixed physical
separation `R`, a nonzero connected subsequential limit must evade

```text
c R delta(a)/a-log[C L_F(a)L_G(a)/delta(a)] -> +infinity.            (0.7)
```

These are **necessary certificate-escape/tuning conditions**, not a positive
continuum construction. Neither `alpha_old->1` nor `alpha_sharp->1` proves a
divergent actual correlation length, a closing actual spectral gap, a
singular free energy, phase coexistence, an RG fixed point, or a nontrivial
continuum limit. A worsening upper bound is not a lower bound on the physical
correlation length.

The result does not trigger an axiom-update stop. It improves and then locates
the limit of one proof method. Direct correlation-length or OS spectral-edge
control, block criteria, polymer methods, and constructive RG remain live.

## 1. Exact `SU(3)` Wilson oscillation

For `U in SU(3)`, diagonalize with eigenangles `theta_1,theta_2,theta_3` and
`theta_1+theta_2+theta_3=0 mod 2 pi`. Put
`s=(theta_1+theta_2)/2`, `d=(theta_1-theta_2)/2`. Then

```text
Re Tr U=2 cos(s)cos(d)+cos(2s).
```

Minimizing first over `d` and then over `x=|cos s| in [0,1]` gives

```text
min Re Tr U=min_(0<=x<=1) [2x^2-2x-1]=-3/2,
max Re Tr U=3.                                                        (1.1)
```

For fixed exterior product `A in SU(3)`, one plaquette contribution as a
function of the updated link can be written, up to orientation, as

```text
phi_A(u)=-(beta/3)Re Tr(uA).
```

Its oscillation is at most `(beta/3)(3-(-3/2))=3beta/2`. If changing another
link replaces `A` by `A'`, the change `h=phi_A-phi_A'` obeys

```text
osc_u h<=osc phi_A+osc phi_A'<=3beta.                                (1.2)
```

The half-`L1` likelihood-ratio lemma used in the direct dependency therefore
gives

```text
c_(e,f)^W<=tanh(3beta/4)<=3beta/4                                   (1.3)
```

for each plaquette incidence. One link has six plaquettes, each containing
three other links. Summing the 18 incidences proves

```text
alpha_W^sharp<=18(3beta/4)=27beta/2.                                 (1.4)
```

The rooted-loop fermion row is unchanged. Adding (1.4) to the established
`alpha_F` proves (0.2). This is a theorem about a sharper sufficient row, not
an assertion that the new bound is optimal or saturated.

## 2. The old equality curve remains inside the sharper wedge

Subtracting the two valid row majorants gives

```text
alpha_old-alpha_sharp=(9/2)beta.                                    (2.1)
```

Equation (0.3) follows immediately. More strongly, every old equality point
with `beta>0` has an open parameter neighborhood on which
`alpha_sharp<1`. The uniqueness, mixing, and OS conclusions therefore persist
through that old proof boundary.

This does not prove that no physical phase boundary can ever intersect the
old curve. It proves that equality of the old majorant neither forces nor
identifies such a boundary. The underlying Gibbs specification is unchanged
while valid proof envelopes have different equality curves.

The same logic applies at `alpha_sharp=1`: the Dobrushin theorem is one-way.
It proves consequences below one and makes no assertion at or above one. A
further improved one-link estimate, a block criterion, or a different norm
could enlarge the controlled region again.

## 3. A universal margin-dependent weighted estimate

Let

```text
S(q)=sum_(n>=2)nq^n=q^2(2-q)/(1-q)^2.
```

Inside `alpha_sharp<1`, necessarily `beta<2/27` and
`kappa<kappa_0=0.3916615362...`, where `(3/2)S(kappa_0)=1`. With exponential
link-distance weight `lambda`, the same incidence proof gives the weighted
row majorant

```text
A(lambda)=(27/2)beta exp(2lambda)
          +(3/2)S(kappa exp(2lambda)).                               (3.1)
```

For `0<=lambda<=1/100`, one has
`kappa exp(2lambda)<0.4`. Since

```text
S'(q)=(4q-3q^2+q^3)/(1-q)^3,
A'(lambda)=27beta exp(2lambda)+3qS'(q),
q=kappa exp(2lambda),                                                (3.2)
```

the endpoint bounds `beta<2/27`, `q<0.4` give `A'(lambda)<9`. Set
`lambda=delta/100`. The mean-value theorem then yields

```text
A(delta/100)<A(0)+9delta/100
            =1-0.91delta<1-delta/2.                                 (3.3)
```

Weighted Dobrushin comparison consequently gives (0.5), with the displayed
`1/delta` covering the resolvent norm and with `L_F,L_G` bounding aggregate
coefficient, local-variation, degree, and support-multiplicity factors. The
cross-Wick argument from the direct dependency extends the estimate from
gauge functions to its fixed-degree local gauge--fermion class.

For a centered local OS vector, a two-step time translation moves the support
by two lattice units. Positivity of the spectral measure and the common decay
rate imply

```text
spec(T_2|Omega^perp) subset [0,exp(-2delta/100)].                     (3.4)
```

Thus (0.6) follows from
`Delta_OS=-(2a_tau)^(-1)log T_2`. The statement concerns the supplied
gauge-invariant OS reconstruction. It does not identify charged sectors or
compare operators across otherwise uncontrolled continuum Hilbert spaces.

## 4. Necessary scaling, not sufficient criticality

Suppose an isotropic trajectory remains in the sharper wedge and has a
covered non-vacuum gauge-invariant excitation with physical energy at most
`M` for all sufficiently small `a`. Equation (0.6) gives

```text
delta(a)<=100 M a.                                                    (4.1)
```

Therefore `delta=O(a)` is necessary for that bounded-energy propagation.
Equivalently, a trajectory with `delta/a->infinity` pushes every covered
non-vacuum gauge-invariant OS excitation above every fixed physical energy.

For supports separated by `R>0` in physical units,
`dist_latt>=R/a-O(1)`. Equation (0.5) proves vanishing whenever the left side
of (0.7) diverges. In particular, for polynomial observable complexity and
normalization, `delta/a >> log(1/a)` is sufficient for vanishing. A nonzero
subsequential limit must violate this sufficient vanishing condition.

No converse follows. If `delta=a`, (0.6) merely leaves an order-one lower
bound; if `delta=o(a)`, the lower bound becomes uninformative. Neither case
constructs an excitation. Likewise a majorant approaching one can coexist
with identically zero true influences: a product specification has actual
Dobrushin row zero but may be reported under any looser row majorant
`1-delta(a)`. Saturation of a certificate is additional mathematics, not a
consequence of its definition.

A positive interacting continuum theorem would still need an actual line of
constant physics, nonzero tight renormalized Schwinger functions, an actual
correlation-length or spectral-edge scaling law, compatible OS transfer
limits, and multiscale control. Those objects are not supplied by (0.2)--(0.7).

## 5. Relation to the conventional Wilson scaling direction

The sharper wedge still obeys

```text
beta<2/27,
m>5.8090575... .                                                      (5.1)
```

It therefore does not reach the conventional weak-bare-coupling and
light-lattice-mass direction `beta=6/g_0^2->infinity`, `m_lat->0` for the
supplied `SU(3)` Wilson normalization. This disjointness is not a no-go for
that route; it says the one-link heavy-mass certificate cannot control it.

The repo's free same-object staggered theorem is a tuned free exemplar with
`m_lat=a m_phys`, but it is not a coupled gauge continuum theorem. Existing
Wilson small-`a`, QCD running, interacting-Lorentz, Standard Model, and GR
notes do not provide the missing coupled constructive-RG trajectory and are
not dependencies of this result.

## 6. Runner contract

Run:

```bash
python3 scripts/wilson_staggered_dobrushin_certificate_boundary_critical_scaling_no_go_2026_07_12.py
```

The runner checks the exact trace-range minimization, the `27beta/2` Wilson
row, old-versus-sharp equality examples, the universal weighted derivative
bound, the three `delta=a^p` certificate regimes, disjoint standard-scaling
parameters, a non-saturation countermodel, and the source/N1--N8 contract.
The Dobrushin comparison and OS spectral arguments remain analytic machinery.

## 7. No-Go Discipline N1--N8

The no-go is only against identifying a sufficient certificate equality with
physical criticality. It does not declare the continuum program closed.

### N1 — alternative-route enumeration

| Route | Status | Test and result | Why it remains live outside the claim |
|---|---|---|---|
| Sharpen the one-link Wilson oscillation | `ATTEMPTED` | Equations (1.1)--(1.4) move the equality curve and retain mixing across the old one. | Still sharper estimates may exist. |
| Measure the actual correlation length | `ATTEMPTED` | No lower bound follows from either row majorant. | A direct observable estimate could establish critical scaling. |
| Measure the actual OS spectral edge | `ATTEMPTED` | Equation (3.4) is an upper spectral-radius certificate, not a saturation result. | Direct transfer-spectrum control could prove gap closure. |
| Dobrushin--Shlosman or block criteria | `ATTEMPTED` | One-link equality says nothing about optimized block influences. | Blocks can enlarge the uniqueness region. |
| Polymer or cluster control | `ATTEMPTED` | The present absolute row norm is not a polymer convergence norm. | Running polymer activities can cross this boundary. |
| Constructive multiscale RG | `ATTEMPTED` | No coupled gauge--staggered RG map is used here. | A controlled RG trajectory could produce nontrivial scaling. |
| Weak-bare-coupling/light-mass Wilson route | `ATTEMPTED` | Equation (5.1) is disjoint from that parameter direction. | Disjointness leaves, rather than closes, the conventional route. |
| Alternative action or microscopic carrier | `ATTEMPTED` | This computation is specific to the supplied Wilson--staggered action. | Another derived admissible dynamics can have another critical surface. |

### N2 — wall-independence audit

| Left condition | Right condition | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| certificate equality | actual correlation-length or spectral scaling | No | No | Yes |
| certificate equality | controlled observable normalization | No | No | Yes |
| certificate equality | line of constant physics and action trajectory | No | No | Yes |
| actual correlation-length or spectral scaling | controlled observable normalization | No | No | Yes |
| actual correlation-length or spectral scaling | line of constant physics and action trajectory | No | No | Yes |
| controlled observable normalization | line of constant physics and action trajectory | No | No | Yes |

No condition is double-counted. Physical criticality requires actual
observable or spectral behavior; certificate equality is neither one of
those facts nor a consequence of them.

### N3 — hidden-condition phrase scan

| Mandated phrase | Classification |
|---|---|
| `we assume` | No load-bearing hit. |
| `by construction` | No proof-substitute hit. |
| `as is standard` | No hit. |
| `the framework provides` | No hit. |
| `bridge context` | No hit. |
| `background` | No hidden condition. |
| `naturally` | No hit. |
| `obviously` | No hit. |
| `standard QFT` | No hit. |
| `registered` | No premise-granting hit. |
| `canonical` | No unqualified use. |

### N4 — citation/residual matching

| Witness | Witness residual | Present residual | Match? | Disposition |
|---|---|---|---:|---|
| [Massive Wilson--staggered Dobrushin wedge](MASSIVE_WILSON_STAGGERED_DOBRUSHIN_SPATIAL_UNIQUENESS_WEDGE_BOUNDED_THEOREM_NOTE_2026-07-12.md) | A sufficient one-link row and its mixing/OS consequences | Sharpen its Wilson row and quantify the surviving consequences | Yes | Sole direct dependency. |
| Compact-interior continuum boundary (context only) | Uniform interior margins imply separated-point ultralocality | Margin-dependent rate near a certificate boundary | Partial | No transitive claim import. |
| Free same-object staggered continuum theorem | Tuned free relativistic scalar spectral/covariance limit | Coupled interacting critical trajectory | No | Context/counterexample to blanket lattice no-go only. |
| Wilson small-`a` matching note | Coefficient matching inside a supplied Wilson action | Continuum existence and scale setting | No | Context only; no dependency. |

After residual matching, only the massive Dobrushin theorem is a direct
dependency. The new `SU(3)` oscillation and margin scaling are proved here.

### N5 — rhetoric and resolution audit

| Resolution | Tested? | Permitted conclusion |
|---|---:|---|
| One `SU(3)` plaquette | Yes | Exact oscillation range. |
| One-link influence row | Yes | Sharper sufficient Dobrushin wedge. |
| Infinite-volume gauge and covered gauge--fermion state | Yes | Dependency machinery applies inside the sharper wedge. |
| Old equality curve with `beta>0` | Yes | It lies strictly inside the sharper wedge. |
| Shared `beta=0` endpoint | Yes | Equality gives no conclusion. |
| New equality curve | Partly | It is a proof boundary; no physical identification. |
| Actual phase diagram or all block scales | No | No claim that a physical critical surface never intersects either curve. |
| Continuum QFT/SM/GR limit | No | No existence or impossibility claim. |

The deliberately narrow phrase is “does not identify a physical critical
surface,” not “cannot contain any physical critical point.”

### N6 — partial-closure and primitive scan

The improvement is ordinary model mathematics: exact `SU(3)` oscillation plus
the existing likelihood-ratio and comparison lemmas. It neither changes an
axiom nor introduces a new primitive. The live closure path is likewise a
derived-theorem path: construct an actual correlation-length/spectral-edge
estimate or a controlled multiscale RG trajectory. A naming convention or
meta-ratification cannot turn a sufficient upper bound into a saturated
physical observable.

The approved Lattice, Qubit, Admissibility, Record, scale-reference,
kinetic-isotropy, and realized-state premises are not enlarged here. No
contradiction with them is proved, and no axiom-update stop is triggered.

### N7 — hostile steelman

A hostile reviewer should object that a true physical critical surface could
still intersect the old curve, the sharper curve, or their shared endpoint;
improving one upper bound cannot rule out such a coincidence. Correct. This
claim does not exclude an intersection. It excludes only the inference from
certificate equality to physical criticality and proves that the old equality
curve is especially non-identifying because most of it remains in a rigorously
mixing region. Direct correlation, spectrum, susceptibility, or RG evidence
could still establish criticality at a point by independent means.

### N8 — cross-cycle echo

| Prior surface | Similar wall | Lesson here |
|---|---|---|
| Compact-interior Dobrushin continuum boundary | Uniform certificate control excluded covered propagation | Approaching a proof boundary is necessary only relative to that certificate, not sufficient. |
| Beta-six cluster/KP work | Loss of one convergence criterion left multiscale control open | A failed norm is not a phase transition. |
| Free staggered continuum | Actual pole tuning and covariance convergence supplied positive scaling data | A continuum claim needs observable convergence, not only parameter-boundary tuning. |
| Lorentz naturalness obstruction | A supplied-parameter comparator did not become a general impossibility theorem | Proof residuals must not be widened beyond the tested family. |

No similar prior wall was retired by a mere relabeling. Improvements came from
new exact bounds or new controlled constructions, which are precisely the live
routes retained here.

**No-Go Discipline status: PASS.** All eight checks are answered; eight
distinct routes were tested; the claim is narrowed to certificate-boundary
non-identification; no continuum route or axiom family is declared closed.
