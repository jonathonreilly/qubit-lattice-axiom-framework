---
title: Polynomial auxiliary-path resources for a conditional one-port controller
claim_id: polynomial_path_mediator_bounded_theorem_note_2026-10-15
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: two separately priced positive auxiliary-path families with polynomial sufficient resources at a supplied finite waveform interface
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: supplied computable waveform and background, prescribed controller input or quantified Gibbs marginal, paid precision and release; no native source or efficient general compiler
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
status: proposed_retained
upstream_dependencies: ["basis_state_waveform_clock_bounded_theorem_note_2026-10-15"]
runner: scripts/polynomial_path_mediator_2026_10_15.py
next_trace_action: execute reviewed source-integrity integration gates, then regular publication before independent retained audit
---

Claim type: bounded_theorem

A positive path Laplacian with a size-dependent mass supplies polynomial auxiliary responses for the existing one-port waveform controller. Two checked conditional families retain the fixed plant, the clock and every auxiliary/reference output. They change the physical auxiliary Hamiltonian and pay its shrinking unscaled gap. Their sufficient resource powers differ; neither supplies a native controller state, laboratory switching, a common coupling cap, or an efficient compiler for arbitrary target unitaries.

Primary-runner role: source integrity only. The 60-second primary checks exact bodies, recovery, parent bytes, historical fixture receipts and captured actual binding evidence. It runs no physics model, scientific fixture, numerical sweep or proof test. The historical source proposal remains unexecuted. This separately bound version requires the actual root publication review and selected PR 9619 base evidence; binding alone certifies no execution or publication. Historical root numerical scientific programs: one. New integration/source-primary science and historical replays: zero.

Root's qualified conditional source acceptance is the 2,910-byte decision `8f26be5fb28c966ea405bb97facb0a16f9abdbd75c110de23e96f875aa9a8df2`. The complete root derivation `45c211e6…`, protected independent derivation `0620431a…`, and exposed comparison `3cc7a9d3…` follow unchanged. Historical pending statements in those bodies are preserved. The current interpretation includes the explicit minimal-clock-size qualification below and attributes the new root-family majorants to the exposed comparison. Root separately accepted this publication interpretation at exact review d78856437e14673ea7c0a444c645527b2ca6a97fd4f99e81d9101b454cbff25f. This source assembly is not another independent mathematical assessment or a retained audit.

## 1. Supplied interface, actual geometry and complete target

The nonempty finite old plant occupies a nonnegative-coordinate lattice box with accessible corner `p=(0,0,0)`. Its unchanged supplied ordinary-NN two-qubit/onsite Hamiltonian is `H_P>=0`, with certified full norm at most `h`. All old plant factors, including memory and fillers, may have arbitrary inputs and arbitrary correlations with retained references. Whole positivity of `H_P` does not establish a positive local decomposition of each old block; a consumer requiring that stronger property must supply and price it separately.

Supply a finite waveform on `[0,tau]`, `tau>0`,

```
C(t)=a(t)I+b(t)X_p+c(t)Y_p,
sqrt(b(t)^2+c(t)^2)<=a(t)<=g,
C(0)=C(tau)=0,       ||C(t)-C(s)||<=L_C|t-s|.
```

Root assumes `C1` regularity, which is a sufficient subclass of this Lipschitz interface. Certified computable sample values and finite parameter bounds are additional effective-input requirements. A mathematically existing noncomputable waveform is not a coefficient-construction algorithm. `U_C` denotes the exact time-ordered propagator of `H_P+C(t)`; no commutation is assumed. The scalar lift in `a(t)` belongs to that target, including its phase. Coefficients use the fixed finite-Hamiltonian reference unit; `Delta` scales actual terms, not the time coordinate.

Choose integer `n>=1`, `r=n+1`, `m=n+4`. Clock sites are `c_j=(j,-1,-2)`, and auxiliary sites are

```
a=(-1,0,0), v_1=(-1,0,-1), v_2=(-1,-1,-1),
u_j=(j,-1,-1), 0<=j<=n,
auxiliary path a-v_1-v_2-u_0-...-u_n.
```

The declared edges are the clock path, auxiliary path, `c_j-u_j` and `p-a`. They add `2m-3=2n+5` sites and `3m-7=3n+5` geometric edges, with maximum new-site degree three. Within this inventory the only new-to-old NN adjacency is `p-a`, and all new-new NN pairs are declared. No original factor is moved, relabeled or assumed clean. Declared edge counts do not require every programmed coefficient to be nonzero: zero endpoints give zero endpoint source coefficients. Unknown outside couplings, fields and leakage faults require supplied isolation/compensation or full-space bounds over preparation, release and runtime.

The clock is the parent's explicitly adopted positive-edge clock. With `n_j=(I-Z_j)/2`, `S_j=(X_jX_(j+1)+Y_jY_(j+1))/2` and `Omega=pi/(2tau)`,

```
K_X=sum_(j=0)^(n-1) Omega[(n-j)n_j+(j+1)n_(j+1)
                         -sqrt((j+1)(n-j))S_j].
```

Each two-qubit block has spectrum `{0,0,Omega(n+1),Omega(n+1)}`. Its exact full-clock norm is `B_X=Omega n(n+1)`, scalar `B_X/2`. Starting at the one at `c_0` and zero elsewhere,

```
chi_n(t)=exp(-iOmega n t) sum_j sqrt(binomial(n,j))
              cos(Omega t)^(n-j)[i sin(Omega t)]^j |j>,
chi_n(tau)=|n>.
```

Store `C_j=C(s_j)` at `s_j=Omega^(-1)arcsin sqrt(j/n)`. The parent's finite binomial/chord estimate, including both deterministic endpoints, gives `E|s_J-t|^2<=tau^2/(2n)` for the free comparison vector. Thus the abstract `H_tar=H_P+K_X+sum_j n_j C_j` has complete isometry error at most `L_C tau t/sqrt(2n)` against `chi_n(t) tensor U_C(t)`. The actual interacting clock is not assumed to have the free distribution. Arbitrary many-body `C_j` are not directly realized by this two-qubit one-port interface.

## 2. Two physical auxiliary families and their inverse ledgers

For either family define

```
N_A=sum_(v in auxiliary path)n_v,
L(mu)=sum_(v,w in auxiliary path)[n_v+n_w-S_vw]+mu N_A,
T(mu)=(L_path+mu I)^(-1),
t_j=T_(a,u_j),       gamma_v=T_(v,v).
```

Each full pair edge has eigenvalues `0,0,2,2`; each onsite mass is positive. Therefore `L(mu)>=mu N_A`. Its unique kernel is the auxiliary vacuum. The uniform one-excitation vector has eigenvalue `mu`, so the exact complete nonvacuum inverse norm is `mu^-1`. On `k>=1` excitations the lower bound is `k mu`, including the two-excitation sector used by the corrector. This is an auxiliary-penalty certificate, not a spectral-gap claim for the whole coupled runtime generator.

The all-occupied auxiliary state attains every block's upper eigenvalue, proving

```
ell_A=||L(mu)||=2(m-1)+mu m,
s_A=m-1+mu m/2,
absolute collected Pauli coefficient sum=3(m-1)+mu m.
```

These are full-space quantities. Distinguish the complete inverse from individual response entries:

| Quantity | Root family R | Protected independent family I |
|---|---|---|
| Mass `mu` | `m^-3` | `m^-2` |
| Port parameter `q` | `1/m` | `sqrt(G)`, `G=max(1,g)` |
| Complete reduced inverse norm | `m^3` | `m^2` |
| Proven responses | every entry in `[7m^2/8,9m^2/8]` | endpoint-to-every-site in `[m/2,2m]` |
| Diagonal entries | `[m^2,9m^2/8]` | `[m,2m]` |
| Exact `ell_A` | `2(m-1)+m^-2` | `2(m-1)+m^-1` |
| Exact `s_A` | `m-1+1/(2m^2)` | `m-1+1/(2m)` |

The root proof uses `L_path>=(8/m^2)Q`: the edge coefficient in its finite Poincare sum is exactly `a(m-a)/2<=m^2/8`. The constant inverse mode contributes `m^2` to every entry, while the orthogonal remainder has norm at most `m^2/8` and nonnegative diagonal. The independent proof uses positive inverse row sums `m^2` and endpoint currents `u_k-u_(k+1)=mu sum_(j>k)u_j>0`; their sum keeps every endpoint response within a factor two of its mean `m`. A general-source current has magnitude at most one, yielding the diagonal upper bound, and Cauchy-Schwarz yields the lower bound.

The endpoint proof fits the actual endpoint port. It does not assert the root's all-pair interval for a different mass. Replacing one family's `mu`, inverse or `q` by the other's while retaining its coefficients would define an unchecked third generator.

## 3. Sources, both counterterms and physical positivity

For the chosen family use the actual inverse entries and coefficients

```
z_j=-(b_j+i c_j)/(2q t_j),
V=q(X_pX_a+Y_pY_a)+sum_j n_j[Re(z_j)X_(u_j)+Im(z_j)Y_(u_j)],
kappa=4q^2 gamma_a,       d_j=|z_j|^2 gamma_(u_j),
C_ct=kappa n_p+sum_j d_j n_j,
v=2q+sum_j|z_j|.
```

`v` is an actual coefficient sum and full-space norm allowance, not generally `||V||` exactly. Its loose upper bound cannot be substituted into an exact scalar ledger without paying the extra installed scalar. The separated allowances are

| Quantity | R | I |
|---|---|---|
| `abs(z_j)` | `<=4g/(7m)` | `<=sqrt(G)/m` |
| `v` | `<=2/m+4rg/(7m)<=2+g` | `<=3sqrt(G)` |
| Plant counterterm `kappa` | `[4,9/2]` | `[4mG,8mG]` |
| Clock counterterm `d_j` | `<=18g^2/49` | `<=2G/m` |
| Full counterterm allowance | `c_R=9/2+(18r/49)g^2` | `c_I=8mG+2G<=10mG` |

With `Y|0>=i|1>`, auxiliary creation from the port is `q(X_p+iY_p)`, whose adjoint product is `4q^2 n_p`. The port self-term is a genuine plant operator. The cross term through real `t_j` is `2q t_j[Re(z_j)X_p+Im(z_j)Y_p]n_j=-(b_jX_p+c_jY_p)n_j`; source self-terms are `d_j n_j`. Distinct source products vanish only on `N_X=1`. Thus, with `J_A` appending the auxiliary vacuum and `R` the full reduced inverse,

```
J_A* V R V J_A=C_ct-W,       W=sum_j n_j(b_jX_p+c_jY_p),
```

on the complete one-clock-head/old/reference domain. No assertion is made for arbitrary multihead input. No commutation with `H_P` is used.

Set `A=H_P+K_X+sum_j a_jn_j+C_ct` and install

```
K_Delta=Delta L(mu)+sqrt(Delta)V+A+R_pos I,
R_pos=sqrt(Delta)v,       Delta>0.
```

The source reserve is physically distributed: the port block receives `2q sqrt(Delta)I`, and source block `j` receives `sqrt(Delta)|z_j|I`. Their positive shifted pair-block norms are `4q sqrt(Delta)` and `2|z_j|sqrt(Delta)`. All auxiliary, clock, counterterm and scalar-sample blocks are separately positive. Positivity means semidefinite. Generic signed calibration errors can spoil zero eigenvalues; certify positive parametrizations or install and charge additional local identity reserves.

## 4. Bare-input corrector and complete same-time estimate

Use the chosen family's complete inverse, `x=v/mu`, `y=v^2/mu^2`, and

```
a_*=h+B_X+rg+c_family,       b_*=h+B_X+2rg,
D=a_*+b_*,
X=RVJ_A, Y=RVX, Z=J_A-e X+e^2Y, e=Delta^(-1/2).
```

`X` has one auxiliary excitation; `Y` has two after `R` removes the vacuum part. The literal residual is

```
(Delta L+sqrt(Delta)V+A)Z-ZH_tar
 =e(VY-AX+XH_tar)+e^2(AY-YH_tar).
```

All noncommuting products remain. The two bare-versus-corrected endpoint costs are both included. Uniformly through `tau`,

```
eta_A<=F_1/sqrt(Delta)+F_2/Delta,
F_1=2x+tau(Dx+v y),       F_2=2y+tau D y.
```

For prescribed `eta_med>0`, the sufficient recipe is `Delta>=max(1,(2F_1/eta_med)^2,2F_2/eta_med)`. An upper resource claim refers to choosing this maximum or another explicitly bounded sufficient choice, not every larger `Delta`.

The full isometry comparator at the same actual runtime `t` is

```
exp(-it R_pos)|vac_A> tensor chi_n(t) tensor U_C(t),
error <= L_C tau t/sqrt(2n)+F_1/sqrt(Delta)+F_2/Delta.
```

The ideal initial controller is bare vacuum on auxiliaries and the known clock endpoint bit string, initially product with arbitrary old/reference input. No dressed state is assumed supplied. Every output is retained. The unhalved full trace and corresponding isometry-channel diamond allowance is twice the isometry bound, capped at two for states. The clock endpoint phase is one; the installed reserve phase remains. The auxiliary scalar cancels on vacuum only together with its nonidentity terms, and is not removed from the physical generator.

## 5. Explicit sufficient polynomial recipes and mandatory clock ceiling

The root's displayed maximum has sufficient order `m^12/eta_med^2`. The following fully explicit majorant is **new in the exposed comparison**, not a verbatim formula or protected result from the root body:

```
V_R=2+g,       C_R=9/2+(18/49)g^2,
D_R0=2h+2Omega+3g+C_R,
A_R1=2V_R+tau D_R0 V_R+tau V_R^3,
A_R2=2V_R^2+tau D_R0 V_R^2,
M_R=1+4A_R1^2+2A_R2,
Delta_R=M_R m^12/eta_med^2,       0<eta_med<=1.
```

The comparison proves `F_1<=A_R1 m^6`, `F_2<=A_R2 m^8`. Retain the independent body's separate constants

```
D_I0=2h+2Omega+13G,
C_I1=6sqrt(G)+3tau D_I0 sqrt(G)+27tau G^(3/2),
C_I2=18G+9tau D_I0 G,
M_I=1+4C_I1^2+2C_I2,
Delta_I=M_I m^8/eta_med^2.
```

Here `F_1<=C_I1 m^4`, `F_2<=C_I2 m^6`. The different complete inverse costs propagate through the corrector; the improvement is not obtained by merely relabeling the root constants.

For either family a full interacting-generator norm allowance is

```
B_full=a_*+Delta ell_A+2sqrt(Delta)v.
```

It is an upper bound, not an exact interacting norm. Sufficient explicit upper bounds are

```
B_R<=[h+Omega+g+C_R+2M_R+2V_R sqrt(M_R)] m^13/eta_med^2,
B_I<=[h+Omega+11G+2M_I+6sqrt(M_I G)] m^9/eta_med^2.
```

**Mandatory size qualification:** to infer polynomial powers in a target accuracy, choose

```
n=max(1,ceil[L_C^2 tau^4/(2eta_X^2)]),
```

or impose an explicit matching upper bound on `n`. The lower condition `n>=...` by itself guarantees the clock error but does not imply `m=O(eta_X^-2)`. For example an exponentially oversized `n` satisfies that lower condition while making the positive clock norm superpolynomial. The immutable root sentence is interpreted with this explicit sufficient choice.

At fixed supplied `h,g,tau,L_C`, for ideal input and exact installation choose `eta_X=eta_med=epsilon/4`, `0<epsilon<=1`, and the displayed minimal ceiling, equivalently `n=max(1,ceil(8L_C^2tau^4/epsilon^2))`. Then the full trace error is at most `epsilon`, with these sufficient orders:

| Quantity | R | I |
|---|---|---|
| `Delta` | `O(m^12/eta_med^2)`, `O(epsilon^-26)` | `O(m^8/eta_med^2)`, `O(epsilon^-18)` |
| Full norm / scalar allowance | `O(m^13/eta_med^2)`, `O(epsilon^-28)` | `O(m^9/eta_med^2)`, `O(epsilon^-20)` |
| Reserve | `O(m^6/eta_med)` | `O(m^4/eta_med)` |
| Largest new local block norm | `O(m^12/eta_med^2)` | `O(m^8/eta_med^2)` |
| Physical port coefficient | `O(m^5/eta_med)` | `O(m^4/eta_med)` |
| Physical source coefficient | `O(m^5/eta_med)` | `O(m^3/eta_med)` |
| Auxiliary mass coefficient / penalty gap `Delta mu` | `O(m^9/eta_med^2)` | `O(m^6/eta_med^2)` |

These are large sufficient bounds, not optimal exponents, complexity lower bounds or practical efficiency. If source, release, timing or calibration consumes part of the budget, reserve those portions first. If `h,g,tau,L_C` themselves grow, retain their displayed dependence. The theorem does not bound a general compiler's recurrence search, waveform length, pulse count, duration, phase-lift cost, plant-dimension dependence or real-sample oracle complexity.

## 6. Exact scalar, action and prepared-input moments

The normalized full-space scalar is exactly

```
s_full=s_(H_P)+B_X/2+(sum_j a_j)/2+Delta[m-1+mu m/2]
       +kappa/2+(sum_j d_j)/2+sqrt(Delta)v.
```

The actual `v` is used once. All diagonal loads, auxiliary edges/masses, clock scalar and positive reserves remain. Runtime action has allowance `tau B_full`. Scalar coefficients, full norm, positive-block prices, collected Pauli budgets and state-dependent mean energy are distinct quantities; none is automatically microscopic actuator work or a detector identification.

At `C(0)=0`, let `D_P=H_P+kappa n_p`. Applying the actual static generator to the ideal bare input gives orthogonal original-controller, clock-one and auxiliary-at-a components. For arbitrary plant/reference input with plant marginal `rho_P`,

```
mean=Tr(rho_P D_P)+Omega n+R_pos,
variance=Var_(rho_P)(D_P)+Omega^2 n
                           +4Delta q^2 Tr(rho_P n_p).
```

The covariance of `H_P` and `n_p` inside `Var(D_P)` remains. R has sufficient mean `O(m^6/eta_med)` and variance `O(m^10/eta_med^2)`; I has `O(m^4/eta_med)` and `O(m^8/eta_med^2)`. At the minimal common accuracy recipe these become R `O(epsilon^-13)` / `O(epsilon^-22)` and I `O(epsilon^-9)` / `O(epsilon^-18)`. The root port counterterm stays bounded; the independent one grows. Input-dependent vanishing terms can improve a particular case.

For nonzero initial sample, restore the diagonal `a_0+d_0` and additional variance `Delta|z_0|^2`; the displayed theorem specializes to zero endpoints. These exact formulas do not hold unchanged for an imperfect thermal/correlated controller. For complete input replacement error `e`, safe mean, second-moment and variance discrepancies are `B_full e`, `B_full^2 e`, `3B_full^2 e`. Small state error does not alone control a growing high-energy tail. The leakage allowance `Delta ell_A eta_A^2` need not vanish. Static total moments are conserved under the actual generator, not automatically under its approximate product comparator or individual subsystems. No rare-reference-conditioned moment or reuse conclusion follows.

## 7. Effective coefficients, physical calibration and positivity faults

For R, `m^3 T^-1` is integer tridiagonal; for I, `m^2 T^-1` is. Hadamard determinant/cofactor bounds give `O(m log m)` bit lengths, and positive definiteness prevents zero pivots. Exact rational elimination has polynomial arithmetic bit cost for these particular matrices. This establishes the auxiliary coefficient construction conditional on computable waveform samples; it does not establish their evaluation complexity or an efficient arbitrary-unitary compiler.

For real symmetric weighted-path/mass perturbations `B'=B+delta B`, with `d=||delta B||<=mu/2`,

| Family | Inverse change bound | Additional response condition |
|---|---|---|
| R | `norm(B'^-1-B^-1)<=2m^6 d` | `d<=7/(32m^4)` leaves `t'_j>=7m^2/16` |
| I | `norm(B'^-1-B^-1)<=2m^4 d` | `d<=1/(8m^3)` leaves endpoint `t'_j>=m/4` |

Both conditions in a row apply. Ordered positive entries require this real weighted-path context. Arbitrary complex edge-phase faults instead require a full-generator estimate or a separately supplied complex calibration contract. Recomputing a favorable effective response does not erase physical generator error against the fixed prescribed target.

For positive actual `Delta'`, a safe complete-space bound is

```
||K'-K|| <= |Delta'-Delta|ell_A+Delta'||L'-L||
 +|sqrt(Delta')-sqrt(Delta)|v+sqrt(Delta')||V'-V||
 +||A'-A||+|R_pos'-R_pos|.
```

Use `||V'-V||<=2|q'-q|+sum_j|z'_j-z_j|` and `||L'-L||<=2sum_edges|delta w|+sum_sites|delta mu|`. Actual counterterm and scalar changes remain in `A'` and `R_pos'`. Positive edge weights and positive masses retain the full bound `(min mass)N_A`; arbitrary signed faults do not inherit it.

The unchanged layout has at most `7r+3m<=10m` new collected physical Pauli coefficient slots, including the identity and allowing zero coefficients. Per-slot absolute physical error `delta` gives `||delta K||<=10m delta` when the old generator is exact; `delta<=epsilon_cal/(20tau m)` suffices for full trace budget `epsilon_cal`. Relative precision on coefficients of order `Delta` is correspondingly much stricter. A coordinate-error norm bound alone is not a positive-block certificate. Add actual fault-norm identity margins where required, including their scalar, phase, moment and work costs.

Integrated full generator error costs `integral||delta K(t)||dt` in isometry norm and twice that in complete trace norm. A fixed-target timing fault costs `B_actual|delta t|` in isometry norm. Leakage that changes clock number forbids sector-only fault norms. A pure scalar defect is invisible to an ordinary channel but remains in a phase-sensitive isometry contract.

## 8. Supplied controller marginal, actual release and complete chronology

The static runtime is autonomous after initialization; its initial state is not thereby native. There are `k=2m-3` new bits. A supplied preparation Hamiltonian

```
G_prep=nu_p[(I-n_(c_0))+sum_(other new bits v)n_v], nu_p>0,
```

has the desired bit string as unique ground state, gap `nu_p`, norm `k nu_p`, scalar `k nu_p/2`. If its Gibbs marginal is supplied at `beta>0`, its bad population is `delta_G=1-(1+exp(-beta nu_p))^-k<=k exp(-beta nu_p)`. Its controller marginal trace distance to the pure target is exactly `2delta_G`, irrespective of outside correlations. Using `2delta_G` as the full joint replacement cost additionally requires product independence.

For arbitrary complete old/reference extension `sigma_CY`, the checked pure-factor lemma uses the **exact unconditional** `omega_Y=Tr_C sigma`:

```
||sigma_CY-P_C tensor omega_Y||_1
 <= g(delta)=delta+sqrt(delta(4-3delta)),
delta=1-Tr[(P_C tensor I)sigma].
```

The parent supplies its finite proof and coherent Gibbs-purification witness. A delivered marginal at half-trace distance at most `d` from the Gibbs law has `delta<=delta_bar=min(1,k exp(-beta nu_p)+d)`. Charge `g(delta_bar)` first. With exact delivery, `beta nu_p>=log(9k/epsilon_prep^2)` suffices for complete joint allowance `epsilon_prep`. There is no normalized-success marginal or restored nominal old input. Fixed coldness cannot keep a growing whole controller arbitrarily pure.

The preparation gap `nu_p`, runtime mass `mu` and scaled penalty gap `Delta mu` are separate. Runtime terms need not preserve the preparation Gibbs law. Those interactions must actually be absent, isolated or compensated while the source premise is asserted. No equilibration-time, refrigerator, purity-supplier or microscopic energy mechanism is supplied.

For an optional supplied finite smooth monotone release, write `K_Delta=H_P+F`, `F>=0`, and use

```
H_rel(r)=H_P+(1-u(r))G_prep+u(r)F,
0<=u<=1, u(0)=0, u(s)=1.
```

On the ideal controller `G_prep` vanishes. Its comparison to that fixed controller and old state aged under literal `H_P` costs at most `||F|| integral_0^s u(r)dr` in isometry norm. The runtime old target is therefore `U_C(t)exp(-isH_P)` on the actual delivered old/reference marginal. Every actual source wait must also retain its stipulated old evolution. Starting from an unaged earlier old state would change the target.

Use `B_F=B_X+rg+c_family+Delta ell_A+2sqrt(Delta)v>=||F||` and choose `s=eta_rel/B_F` for a sufficient release allowance. A supplied ramp with `max|u'|<=c_u/s` has full slew at most `c_u(B_F+k nu_p)B_F/eta_rel`. The preparation norm stays in this price. The actual interpolated scalar and all finite durations remain. For ideal closed monotone release, `|W_rel|<=||F-G_prep||<=B_F+k nu_p`; faulty paths need their endpoint/variation allowance. Static runtime has no explicit drive-work term, but installation, cooling, release and reset are not free. These are finite-Hamiltonian budgets, not laboratory actuator or energy identification.

The complete state budget adds `g(delta_bar)`, twice the release/clock/mediator isometry allowances, and actual full-space calibration/timing/isolation prices, capped at two. A finite supplied idle waveform window preserves its declared old-aging comparison while the clock continues to move. It does not permanently halt, return a fresh controller, isolate the endpoint or recycle consumed resources.

## 9. Parent, scope and retained failure routes

The sole direct mathematical parent is the [basis-state waveform-clock note](BASIS_STATE_WAVEFORM_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-15.md), 110,611 bytes, SHA256 `0c3f1b569d41b75fa1c23e815e55f8481af640a9b292469e056541f698702ed1`. Its actual regular, attached, open PR 9619 has head `aa4beefe822ee4564adaa48fd7ef5e3a5c033bf9`. The inherited root proof occupies bytes `[23221,46477)`, protected independent proof `[46638,75811)`, and exposed comparison `[75964,110611)`, with unchanged hashes `0fc2b704…`, `84f03ca0…` and `8c3ba783…`. Its positive-edge clock, finite sampling bound, fixed exterior geometry, general corrector and exact-marginal lemma are used within their stated domains. The initial parent/publication nulls remain preserved in `INITIAL_BINDING.json`; the later observed canonical, parent-review and publication pins are separate in `PARENT_BINDING.json`. The source draft's own null fields remain historical. Actual root publication-wrapper review d78856437e14673ea7c0a444c645527b2ca6a97fd4f99e81d9101b454cbff25f and selected PR 9619 base are now bound separately; actual execution and publication outcomes require their own records. Git ancestry does not import compiler, memory-bank, Gibbs-controller or other milestone mathematics. Historical source pins inside the unchanged bodies remain provenance and do not create extra current theorem edges.

Zero mass leaves an extra one-excitation zero mode and invalidates this reduced inverse. Fixed positive mass has opposite-end response `sinh(theta)/(mu_0 sinh(m theta))`, with `cosh(theta)=1+mu_0/2`; under this contraction a fixed far-source target cannot keep both `q` and `z` polynomial in that fixed-mass family. This is a scoped route failure, not a universal no-go for NN simulators. The new families change the physical mass and pay its gap cost.

Other witnesses remain explicit: a merely positive response without a lower bound is not a resource certificate; a one-head inverse is insufficient for the two-excitation corrector; multiple heads leave cross-source products and clock vacuum does not launch; one XX axis lacks the supplied complex X/Y control; dropping the nonscalar plant counterterm changes the target; a dressed-input argument omits the bare endpoint costs; linear position-to-time samples implement the wrong waveform; omitted clock/reserve phases change the coherent target; oversized `n` or `Delta` invalidates upper bounds tied to the sufficient recipe. A product Gibbs controller marginal need not be independent of old records. Small trace error without norm factors does not control energy moments. None of these is expanded into a broad impossibility claim.

Native preparation/cooling, physical interactions and isolation, calibration and release hardware, controller basis/initial coherence supply, efficient total compilation, common resource caps, physical energy and detector identification, permanent stopping, final isolation, restoration and reuse remain open. The independent family has the smaller sufficient full-norm exponent, while the root family has a bounded plant counterterm; no universal superiority or optimality is asserted.

## 10. Actual evidence, exposure and publication boundary

The protected independent proof was frozen before access to the root polynomial candidate. Root's complete pre-comparison read was recorded at `20:01:16 UTC`; the exposed comparison read the root candidate at `20:01:44 UTC`. Earlier campaign mass-regularized resolvent work, shared controller machinery, and the same model/effort were already known. Independence is relative to the current unseen candidate text, not all prior ideas or an independent-model replication. The later comparison and its explicit root-family majorants are source exposed. This assembler read all three complete bodies, the relevant complete parent comparison, root acceptance, exposures and fixture records; that adds no new independence claim.

Root separately ran one bounded floating-point scientific fixture at `20:03:09.827816–20:03:10.280094 UTC`, exit zero. Its source is 5,571 bytes `ade7e28f58c4029eb4505cc29f1a951e7ee135db895928385aaf8699294c3d71`, results 8,166 bytes `311d09793428b5a5ba64be3577a611d42b4671c60d1651718c8ab23e650e5a8f`, and final fixture freeze `eb5027b361fd91e2dfc944f39d86a448dbfc1d30994fc1a3e2a54e561f35eb32`. It checked 14 full auxiliary spectra (`m=2..8`, both masses), 14 finite inverse examples (selected sizes through 64), and four noncommuting complex-source corrector/moment cases (`n=2,m=6`, two `Delta` values per mass). Complete auxiliary sectors were retained; the contractions used the admitted one-clock-head sector. The reported residuals are below `5e-14`, moment residuals below `1.2e-13`, at the script's floating-point tolerances.

This is one exposed numerical sanity program, not 32 independent checks, a universal proof, long-time simulation, device test or native supplier test. Its selected Delta values check identities, not the uniform runtime error or resource exponent. The comparison checker received a notification of that run but never inspected or relied on its source/results/freeze/receipts. This assembler has now read them for accurate packaging; no rerun occurs. The actual `N/run.py` receipt records source-at-launch and streams; no separate historical `LAUNCH.json` is invented. Exact source, receipt, result and root interpretation bytes are recoverable by hash.

Root accepted both qualified source families through the metadata-only acceptance run at `20:17:47.959933–20:17:48.020149 UTC`; its directory label is not substituted for its actual time. The acceptance verified source identities and recorded root's analytical reading; execution did not prove the theorem. The present drafting metadata and proposed primary likewise certify only source integrity. Historical scientific count is one, new drafting science count zero, historical replay count zero. Root publication-wrapper review and the actual PR 9619 base are now separately bound. Actual primary/cache/mutation/graph execution, regular publication and independent retained audit remain separate actual records. Historical source-proposal pending fields remain null. The selected base branch physics-loop/toe-basis-state-clock-20261015 does not add mathematics beyond the separately pinned sole basis-clock parent. No editable prompt file, axiom or platform instruction is changed.


---

## Immutable source body: root_mass_m3

Historical source retained exactly; current status and interpretation are given above.

# A positive auxiliary path with polynomial one-port controller prices

Status: root analytic candidate, not yet independently checked or accepted. This is a conditional replacement of the auxiliary Hamiltonian in the basis-start single-port controller. It supplies neither a Gibbs state nor laboratory controls. All generator coefficients are expressed in a fixed reference unit; that convention does not identify the microscopic energy or a physical actuator.

The earlier basis-clock comparison supplies the declared NN geometry, complete-input clock theorem and general corrector identity. This note rederives every changed spectral, response, coefficient and resource estimate. The protected follow-on worker received the polynomial-resource target before this candidate was written, and has not received candidate access. Shared prior machinery and model family limit the eventual independence claim. No numerical, symbolic or Lean science program has run here. No novelty claim is made for path Laplacians or their resolvents.

## 1. Contract and exact geometry

Let a nonempty finite plant P occupy a nonnegative lattice box, with accessible corner p=(0,0,0), supplied positive generator H_P of norm at most h. All original plant factors may be arbitrary and entangled with an arbitrary retained reference. An admitted C1 single-port waveform on [0,tau], tau>0, is

    C(t)=a(t)I+b(t)X_p+c(t)Y_p,
    sqrt(b(t)^2+c(t)^2)<=a(t)<=g,
    C(0)=C(tau)=0,    ||C(t)-C(s)||<=L_C |t-s|.

Its target is the exact time-ordered U_C generated by H_P+C(t). H_P need not commute with any sample. Whole positivity of H_P is distinct from a separately positive decomposition of its old local terms; the latter remains a separate premise when required by a consumer. Effective coefficient construction needs computable sample values and certified bounds, not just the mathematical existence of a Lipschitz function.

Choose n>=1, r=n+1 clock sites c_j=(j,-1,-2), and m=n+4 auxiliary sites on the path

    a=(-1,0,0), v1=(-1,0,-1), v2=(-1,-1,-1),
    u_j=(j,-1,-1), j=0,...,n,
    a-v1-v2-u0-...-un.

The new edges are the n clock edges, m-1 auxiliary edges, r source edges c_j-u_j, and the port edge p-a. They are NN, have maximum new degree three, and add 2n+5 sites and 3n+5 declared geometric edges. These counts do not assert that every source coefficient is nonzero. Isolation of every unlisted interaction over the full lifetime is supplied or charged as a full-space error.

Use the checked positive-edge clock, with Omega=pi/(2tau), number operators n_j=(I-Z_j)/2 and S_j=(X_j X_(j+1)+Y_j Y_(j+1))/2:

    K_X=sum_j Omega[(n-j)n_j+(j+1)n_(j+1)
                          -sqrt((j+1)(n-j))S_j].       (1)

Each full pair block has eigenvalues 0,0,Omega(n+1),Omega(n+1). Its exact full-clock norm and scalar are B_X=Omega n(n+1), s_X=B_X/2. The one-head vector starting at |0> is

    chi(t)=exp(-i Omega n t) sum_j sqrt(binomial(n,j))
             cos(Omega t)^(n-j) [i sin(Omega t)]^j |j>,
    chi(tau)=|n>.

Take t_j=Omega^-1 arcsin sqrt(j/n) and C_j=C(t_j). The earlier uniform estimate, including the p=0,1 endpoints, is

    E|t_J-t|^2 <= tau^2/(2n), J~Bin(n,sin^2(Omega t)).

For H_tar=H_P+K_X+sum_j n_j C_j, the complete isometry residual therefore integrates to

    ||exp(-itH_tar)J_0-chi(t) tensor U_C(t)||
       <= L_C tau t/sqrt(2n), 0<=t<=tau.              (2)

This is an operator estimate on all plant inputs and retained references. It uses the free binomial vector as a comparator, not as an assumption about the interacting clock's distribution. Clock and reference outputs remain included. The present change is entirely in the mediator realizing the n_j C_j terms.

## 2. Full-space positive auxiliary generator

On the same m-site auxiliary path, let N_A=sum_v n_v and set

    mu=m^-3,
    L_A=sum_{(v,w) in path}(n_v+n_w-S_vw)+mu N_A.    (3)

Each edge has eigenvalues 0,0,2,2, and each onsite mu n_v is positive. Thus L_A>=mu N_A. Vacuum is its unique zero vector, and the inverse on the entire nonvacuum space satisfies

    R=(L_A restricted to vacuum-perp)^-1,
    ||R||<=mu^-1=m^3.                              (4)

The uniform one-head vector has edge energy zero and onsite energy mu, so the full vacuum gap is exactly mu and ||R||=m^3. The lower bound applies to every excitation sector, including the two-excitation sector needed below; no one-particle gap is substituted for a full-space gap.

Every full edge block attains its norm on |11>, and every onsite block on |1>. Hence the all-occupied auxiliary vector attains the sum of block norms:

    ell_A=||L_A||=2(m-1)+mu m,
    s_A=(m-1)+mu m/2.                             (5)

The exact collected absolute Pauli coefficient sum is 3(m-1)+mu m. Identity and Z coefficients all have the same respective signs across overlapping blocks; distinct XX/YY edge strings do not cancel. These are full-space quantities, despite the vacuum input used in the theorem.

## 3. Uniform response by an elementary Poincare bound

On one excitation, B=mu I+L_path, with the ordinary unweighted path Laplacian L_path. For any complex vector x and its mean xbar,

    sum_i |x_i-xbar|^2 = (1/m)sum_{i<j}|x_i-x_j|^2
      <=(1/m)sum_{i<j}(j-i)sum_{e=i}^{j-1}|x_e-x_(e+1)|^2.

For edge e separating a=e+1 vertices from m-a vertices, its coefficient on the last line is

    (1/m)sum_{i<a<=j}(j-i)=a(m-a)/2<=m^2/8.

Thus L_path>=8m^-2 Q, where Q is orthogonal to the uniform unit vector u=m^-1/2(1,...,1). The only zero vector of L_path is constant, since its energy is the sum of adjacent squared differences. Decompose the inverse exactly:

    B^-1=mu^-1 |u><u|+Q(mu I+L_path)^-1 Q.

The second term has operator norm at most m^2/8. Every one of its matrix entries has magnitude at most that norm. Its diagonal is nonnegative. Since 1/(mu m)=m^2, for every pair of auxiliary sites v,w,

    7m^2/8 <= (B^-1)_(v,w) <= 9m^2/8,
    m^2 <= gamma_v=(B^-1)_(v,v) <= 9m^2/8.          (6)

In particular every port-to-source entry t_j=(B^-1)_(a,u_j) is strictly positive with a polynomial lower bound. There is no cancellation assumption about an alternating spectral sum: the uniform mode dominates a bounded remainder. The shrinking gap mu and the corresponding full reduced-inverse cost m^3 have been paid explicitly.

The old lower certificate 12^(-distance) belonged to a different fixed-mass path. It is not imported here or declared false. Equation(3) changes the actual physical auxiliary generator. This construction does not establish polynomial prices for an arbitrary supplied auxiliary Hamiltonian or a common positive lower gap.

## 4. Polynomial coefficient and counterterm bounds

Choose q=1/m and define actual source coefficients

    z_j=-(b_j+i c_j)/(2q t_j),
    V=q(X_p X_a+Y_p Y_a)
           +sum_j n_j[Re(z_j)X_(u_j)+Im(z_j)Y_(u_j)]. (7)

All blocks use the same previously declared NN edges. Because sqrt(b_j^2+c_j^2)<=g, equation(6) gives

    |z_j|<=4g/(7m),
    v=2q+sum_j|z_j|<=2/m+4rg/(7m)<=2+g.           (8)

Here v bounds ||V|| on the complete space, not just one clock head. Put

    C_ct=4q^2 gamma_a n_p+sum_j |z_j|^2 gamma_(u_j)n_j.

Every counterterm is positive onsite, including the nonscalar port term. A valid complete-space norm bound is

    c_ct<=c_m=9/2+(18r/49)g^2.                    (9)

The first term uses 4m^-2 gamma_a<=9/2. Each source square is at most (16g^2/(49m^2))(9m^2/8)=18g^2/49. There is no trace over the old port and no replacement of n_p by the identity.

Let J_A append auxiliary vacuum, restricted only in its clock input to N_X=1. With Y|0>=i|1>, creation from auxiliary vacuum is q(X_p+iY_p) at a and z_j n_j at u_j. The port square is 4q^2 n_p. The mixed contribution through t_j is

    2q t_j[Re(z_j)X_p+Im(z_j)Y_p]n_j
       =-(b_j X_p+c_j Y_p)n_j.

The source self-squares give the stated onsite counterterms. For j!=k, source cross terms contain n_j n_k and vanish on the one-head sector. Therefore the exact restricted identity is

    J_A^* V R V J_A=C_ct-W,
    W=sum_j n_j(b_j X_p+c_j Y_p).                (10)

It is not asserted on multihead inputs. The full R in(4) is still required in the higher-order calculation. No sign of the Y term or physical source coefficient is dropped.

## 5. Explicit finite bare-input error

Set

    A=H_P+K_X+sum_j a_j n_j+C_ct,
    K_Delta=Delta L_A+sqrt(Delta)V+A+R_pos I,
    R_pos=sqrt(Delta)v,
    a_*=h+B_X+rg+c_m,     b_*=h+B_X+2rg,
    x=v m^3,             y=v^2 m^6.

All are written in the fixed reference units. Delta is a positive scaling parameter, not an unpriced change of the time coordinate. The global source reserve can be decomposed physically: add 2q sqrt(Delta)I to the port block and sqrt(Delta)|z_j|I to source block j. Their sum is exactly R_pos. The resulting NN blocks are positive on their complete pair spaces. The other new blocks already have positive decompositions.

For epsilon=Delta^-1/2 define X=RVJ_A, Y=RVX, Z=J_A-epsilon X+epsilon^2Y. On the one-clock-head domain, X contains one auxiliary excitation and Y contains two, after R removes the vacuum part. Since L_A commutes with excitation number and is invertible on every nonvacuum sector, these are genuine bounded maps. The cancellation(10) yields the exact residual

    (Delta L_A+sqrt(Delta)V+A)Z-ZH_tar
       =epsilon(VY-AX+XH_tar)+epsilon^2(AY-YH_tar). (11)

In particular the order-one vacuum contribution is AJ_A-J_A(C_ct-W)=J_A H_tar. This calculation does not commute H_P with n_p or any clock operator with n_j. It uses ||X||<=x, ||Y||<=y, ||A||<=a_* and ||H_tar||<=b_*. The two corrected-versus-bare endpoint differences cost 2(epsilon x+epsilon^2 y). Integrating the residual gives, uniformly through tau,

    eta_A<=F1/sqrt(Delta)+F2/Delta,
    F1=2x+tau[(a_*+b_*)x+v y],
    F2=2y+tau(a_*+b_*)y.                         (12)

For any admitted eta_med>0, choose

    Delta>=max(1,(2F1/eta_med)^2,2F2/eta_med).    (13)

Then eta_A<=eta_med. This is a bare-vacuum input bound; no dressed state is assumed supplied. It is not a global effective-Hamiltonian identity or an approximate equality on arbitrary auxiliary/multihead inputs.

Combining(2) with(12), for all plant/reference inputs and retaining all physical outputs,

    ||exp(-itK_Delta)J_bare
       -exp(-itR_pos)|vac_A> tensor chi(t) tensor U_C(t)||
       <=L_C tau t/sqrt(2n)+F1/sqrt(Delta)+F2/Delta. (14)

At t=tau the clock factor is exactly |n>, including its phase. The actual reserve phase exp(-itR_pos) remains. The unhalved complete trace-distance allowance is twice the right side, by expansion of the two isometry channels; tensoring any reference does not increase the operator bound. No output is postselected or discarded.

## 6. Full resources and what 'polynomial' means

A full-space generator norm allowance, normalized scalar and action allowance are

    B_full=a_*+Delta ell_A+sqrt(Delta)v+R_pos,
    s_full=s_(H_P)+B_X/2+(sum_j a_j)/2+Delta s_A
                  +2q^2 gamma_a+(sum_j |z_j|^2 gamma_j)/2+R_pos,
    action<=tau B_full.                            (15)

V is traceless. The diagonal counterterms, the new auxiliary scalar, and all source reserves are paid separately. Delta ell_A is a full-sector penalty price; replacing it by a one-excitation estimate is invalid.

Equations(5),(8),(9),(12),(13),(15) are explicit polynomial/rational bounds in m,h,g,tau,1/tau and eta_med^-1. For fixed finite h,g,tau, with eta_med<=1 and m>=5, they imply

    v=O(1), c_m=O(m), a_*+b_*=O(m^2),
    x=O(m^3), y=O(m^6), F1=O(m^6), F2=O(m^8),
    Delta=O(m^12 eta_med^-2),
    R_pos=O(m^6 eta_med^-1),
    B_full and |s_full|=O(m^13 eta_med^-2).          (16)

The Delta upper statement means choose the explicit maximum in(13), not that every larger Delta has that bound. Choose n>=max(1,ceil[L_C^2 tau^4/(2eta_X^2)]), for which the clock error is at most eta_X. If the fixed inputs include finite L_C and the error split eta_X,eta_med is proportional to eta, then m=O(eta^-2), and the deliberately loose full norm bound is O(eta^-28). It is polynomial and very large. No optimal exponent, practical efficiency, constant gap, bounded coupling cap or favorable universal timescale is asserted.

The statement is conditional on an explicitly supplied waveform and its norm/time/regularity bounds. It supplies no polynomial bound for the one-port compiler's recurrence search, compiled duration, number of pulses, plant dimension dependence or waveform oracle cost. A compiled endpoint can compose at its own actual-time window with its own phase/error; it does not imply a prescribed intermediate trajectory. It would be an overclaim to infer a polynomial general unitary-synthesis algorithm from(16).

At fixed coefficient input precision, B has rational entries with denominators m^3. Multiplying B by m^3 gives an integer tridiagonal matrix of entries O(m^3), with positive determinant. Cofactor/determinant formulas and Hadamard bounds give O(m log m) bits for its integer determinants and minors, hence polynomial-size exact rational inverse entries. Straight rational elimination has polynomial arithmetic bit cost for this particular matrix. This establishes a constructive inverse, not computability of unspecified real samples b_j,c_j or their evaluation complexity.

## 7. Initial moments, calibration and preparation

For the ideal bare clock0/auxiliary-vacuum input and C(0)=0, let D_P=H_P+4q^2 gamma_a n_p. Applying the actual K_Delta produces mutually orthogonal vacuum/clock0, vacuum/clock1 and one-auxiliary-at-a components. Consequently

    mean=Omega n+Tr(rho_P D_P)+R_pos,
    variance=Var_rho(D_P)+Omega^2 n
                          +4Delta q^2 Tr(rho_P n_p).   (17)

The H_P/n_p covariance remains. At the explicit choices above, the mean is O(m^6/eta_med) and variance is O(m^10/eta_med^2) for fixed inputs. These are upper bounds; the actual input can eliminate some terms. Variance is not simply the clock's binomial variance, and the reserve has not disappeared from the mean. With a nonzero starting sample the extra diagonal/source terms must be restored; that is outside the displayed zero-endpoint specialization.

A physical calibration promise must apply to the entire installed K, including scalar/reserve errors. A sufficient comparison remains

    ||K'-K||<=|Delta'-Delta|ell_A+Delta'||L_A'-L_A||
       +|sqrt(Delta')-sqrt(Delta)|v+sqrt(Delta')||V'-V||
       +||A'-A||+|R_pos'-R_pos|.                       (18)

Here Delta'>0 and the square-root difference equals |Delta'-Delta|/(sqrt(Delta')+sqrt(Delta)). Integrate(18) over actual time for the isometry error; double for the full trace allowance. Positive auxiliary edge weights and positive onsite masses preserve a priced full-sector lower bound. Independent coefficient errors give, for example, ||L_A'-L_A||<=2sum_edges|delta w_e|+sum_sites|delta mu_v|. Thus inverse-polynomial absolute precision suffices at the polynomial resource choices, but fixed arbitrary errors do not.

For source design based on a perturbed one-head B', if ||B'-B||<=d<=mu/2 then the resolvent identity gives ||B'^-1-B^-1||<=2m^6 d. Taking d<=7/(32m^4) as well ensures t_j' stays at least 7m^2/16. Both inequalities must hold; they are explicit polynomial tolerances. This does not erase coherent generator errors after recomputing a favorable response: those still require(18), actual counterterm errors and actual positive margins. Unknown clock-number leakage prevents sector-only fault estimates.

The same onsite preparation Hamiltonian penalizing every wrong bit of the complete one-at-clock0/all-other-zero string has k=2n+5 bits, gap nu_p, norm k nu_p and scalar k nu_p/2. If its Gibbs marginal is supplied at beta>0, its bad population is delta_G=1-(1+exp(-beta nu_p))^-k<=k exp(-beta nu_p). The controller marginal distance is exactly 2delta_G regardless of external correlations. For an arbitrary complete old/reference extension and actual bad population delta, the retained-output replacement allowance is instead

    g(delta)=delta+sqrt(delta(4-3delta)),               (19)

with the exact unconditioned old marginal. A half-trace delivery error d adds at most d to the bad-event budget. Combining(19) with(14), actual release, calibration and timing prices gives a complete state estimate. It is not a native cooling theorem. The preparation interactions must be isolated or actually compensated, and release to runtime must be supplied. The positive interpolation H_P+(1-u)G_prep+u(K_Delta-H_P) has comparator error <=||K_Delta-H_P|| integral u; its duration ages the old state under H_P, and its work/scalar costs remain. A finite fast release requires the corresponding finite slew contract.

For imperfect input with complete replacement error e, the ideal moments(17) have actual mean error at most B_full e, second-moment error at most B_full^2 e, and variance error at most 3B_full^2 e. The auxiliary leakage penalty allowance Delta ell_A eta_A^2 need not tend to zero. Static total moments are conserved under the actual static generator, not automatically under a comparison product. Final isolation, permanent stopping, restoration/reuse, detector behavior and physical energy identification remain separate.

## 8. Scope checks and open obligations

The improvement changes the auxiliary spectrum and pays its shrinking gap. It neither alters the lattice/geometry nor adds an axiom. Full positivity, full-sector inversion, all-source X/Y signs, nonscalar port square, positive physical reserves, bare-input corrector, complete target and actual scalar ledger are retained.

The inherited vacuum/multihead, omitted-counterterm, lost-clock-phase and wrong-linear-sampling witnesses retain their narrow scopes. The old fixed-mass exponential response allowance is not a lower bound on every possible architecture. Conversely a lower eigenvalue without the checked matrix-element estimate would not by itself certify useful port/source response. Neglecting the gap cost or using the new one-head response as a full-sector inverse would invalidate the error bound.

This root candidate awaits the independent follow-on proof, full source-exposed comparison and qualified root acceptance. No executable PASS line proves the mathematics. A publication wrapper must keep the fixed-input and explicit-parameter meanings of polynomial distinct, preserve the old immutable sources, and identify every actual imported body and conditional supplier. Native realization, cooling time, efficient general compilation, common hardware caps, exact energy/detector correspondence and controller reuse remain open.


---

## Immutable source body: independent_mass_m2

Historical source retained exactly; current status and interpretation are given above.

# Polynomial one-port path mediation with a bare-input, complete-output bound

## 1. Status, source boundary, and precise claim

This is a pre-exposure analytical construction for the current polynomial-path question. The current root polynomial-mediator candidate and other workers' current work have not been opened, listed, hashed, searched, or used. The allowed science sources are my frozen basis-clock comparison, SHA256 `8c3ba783afdfa526e9da08df73760d8b6f0477c2598002b4c71fc042e480a2c2`, and the earlier autonomous source/review `0e91f9369e387608f8fb3720c290e67f6aa98b10f13428866334c8507b9e989d` / `52eb2e2dcd9fc56a7be490e193b57754bd85bfad5d585244d4a9fce947b4465d`. Their unchanged complete readings are reused. The new path Green-function bounds and all changed resource constants are proved below. No scientific program or numerical fixture is used.

The campaign previously included mass-regularized Laplacian/resolvent work that I saw and reviewed. Thus this is independence from the current unseen candidate, not first discovery of mass regularization, independence from all prior ideas, or an independent-model replication. The same model and effort are retained. This packet is not an audit or a root acceptance.

The answer is positive under a finite supplied-Hamiltonian contract: use a path Laplacian with mass `mu = 1/m^2`, where m is the number of auxiliary qubits. Its unique vacuum and complete reduced inverse have explicit bounds, while every endpoint-to-source one-excitation response is of order m. With the positive blocks written below, the bare-input isometry error is at most `eta` for a penalty `Delta = D_Delta m^8 / eta^2`, with an explicit finite D_Delta. The full generator norm is at most `C_B m^9 / eta^2`. These are sufficient, deliberately conservative bounds, not optimal exponents or an assertion about every smaller Delta.

The precise target is the entire old plant and reference, the actual retained clock, and the auxiliary vacuum, at the same physical runtime t. Only the initial controller state is restricted: one known clock excitation and auxiliary vacuum, initially product with the arbitrary old plant/reference. An approximate correlated preparation is a separate, explicitly priced extension in Section 10. We do not claim the contraction on arbitrary clock sectors, a gap for the entire coupled Hamiltonian, native initialization, an efficient compiler for arbitrary unitaries, or controller reuse.

All matrices act on finite-dimensional Hilbert spaces. The unit and energy scales are the supplied finite-Hamiltonian convention, not a microscopic laboratory work identification. Every specified waveform value and coefficient must be computable to the requested certified accuracy. Merely postulating an arbitrary real-valued function does not provide an evaluation procedure.

## 2. Geometry and the allowed one-port samples

Let the nonempty old plant occupy a finite subset of a nonnegative coordinate box, with port p = (0,0,0). Its complete supplied background is H_P, with `H_P >= 0` and `||H_P|| <= h`. To claim positive local blocks for the whole apparatus, the old plant must already come with its positive nearest-neighbor/onsite block decomposition and any needed reserves. Whole positivity of H_P alone is not a local decomposition theorem. The new blocks below are explicitly positive and local.

Choose n >= 1, r = n+1, and m = n+4. Use clock sites

    c_j = (j,-1,-2),  j = 0,...,n,

and auxiliary sites

    a = (-1,0,0), v_1 = (-1,0,-1), v_2 = (-1,-1,-1),
    u_j = (j,-1,-1), j = 0,...,n.

The auxiliary path is `a-v_1-v_2-u_0-...-u_n`. Its port is its endpoint a. The source edges are c_j-u_j; the plant edge is p-a; the clock has its usual path edges c_j-c_(j+1). There are exactly `2n+5 = 2m-3` new sites and `3n+5 = 3m-7` declared geometric edges. The maximum new-site degree is three. The only new-to-old nearest-neighbor adjacency is p-a. The listed paths and sources exhaust the nearest-neighbor pairs among these new coordinates. These counts inherit the fully checked geometry in the frozen comparison; no coordinate or geometric edge has changed here.

Declared geometric edges can have zero programmed interaction coefficients. In particular zero waveform endpoints imply zero source coefficients at c_0 and c_n. No universal connectedness of the nonzero interaction graph is asserted. Unknown exterior sites or couplings still require an actual isolation/error contract.

Write `n_v = (I-Z_v)/2` and `S_uv = (X_u X_v + Y_u Y_v)/2`. The permitted samples at the one old port are

    C_j = a_j I + b_j X_p + c_j Y_p,
    sqrt(b_j^2+c_j^2) <= a_j <= g,

with real coefficients and `g >= 0`. Thus C_j is positive and `||C_j|| <= 2g`. Define `G = max(1,g)` and choose the port parameter `q = sqrt(G)`. This particular choice is a sufficient balanced scale; optimizing q is unnecessary.

The physical construction below implements this one-port X/Y interface, not an arbitrary many-body matrix coupled directly to each clock qubit. Scalar lifts needed to put a signed drive into this positive form belong to its prescribed waveform and phase. They are not silently removed from the target.

## 3. A complete positive auxiliary penalty

Index the auxiliary path by k = 0,...,m-1, with a at k=0. Set

    mu = 1/m^2,
    L_A = sum_(k=0)^(m-2) [n_k+n_(k+1)-S_(k,k+1)]
          + mu sum_(k=0)^(m-1) n_k.                    (1)

Each edge block has the two-qubit eigenvalues `0,0,2,2`. Indeed its one-excitation block is `[[1,-1],[-1,1]]`, its vacuum value is zero, and its |11> value is two. Every onsite mass is positive. Consequently

    L_A >= mu N_A,
    ker L_A = span{|vac_A>},
    ||R_A|| = 1/mu = m^2,                             (2)

where R_A is zero on the vacuum and the inverse of L_A on its entire orthogonal complement. The equality in (2) follows because the uniform one-excitation vector has eigenvalue mu. On every sector with k >= 1 auxiliary excitations, the lower bound is k mu; in particular the two-excitation sector required by the corrector is included. This is not merely a one-excitation gap assertion.

The triangle upper bound from the positive blocks is attained by the all-occupied auxiliary state. Therefore the exact full-space norm and normalized scalar coefficient are

    ell_A = ||L_A|| = 2(m-1)+1/m,
    s_A = (m-1)+1/(2m) = ell_A/2.                    (3)

The absolute Pauli-coefficient sum is `3(m-1)+1/m`: the scalar and total Z-coefficient magnitudes each equal s_A, and the XX/YY magnitudes sum to m-1. An auxiliary site has incident positive-block norm sum at most `4+mu`. Multiplication by Delta multiplies these prices by Delta. The physical penalty gap is Delta/m^2; no statement here gives this as a spectral gap of the entire coupled runtime Hamiltonian.

## 4. Endpoint Green entries without an exponentially small path bound

In the one-excitation sector, (1) is the m-by-m matrix

    B = L_path + mu I,    T = B^(-1).

The inverse is entrywise strictly positive. One direct proof is

    B = (2+mu) I - M,
    M = Adj_path + diag(2-degree),

where M is nonnegative and has row sum two. The convergent Neumann series for B^-1 has nonnegative terms, and a path term is strictly positive between every pair. Moreover `B 1 = mu 1`, so every row and column of T sums to `1/mu = m^2`.

For endpoint forcing put `u_k = T_(k,0)`. Summing `Bu=e_0` over a prefix gives

    u_k-u_(k+1) = mu sum_(j=k+1)^(m-1) u_j > 0,
                    k = 0,...,m-2.                  (4)

Thus the response decreases along the path. Summing (4), and bounding each u_j by u_0, yields

    u_0-u_(m-1)
      <= mu [m(m-1)/2] u_0
       = [(m-1)/(2m)] u_0 < u_0/2.

The average of the u_k is m. Therefore `u_0 >= m`, and `m^2 = sum u_k >= m u_0/2`. In particular, for every auxiliary source site,

    m/2 <= T_(0,k) <= 2m.                            (5)

The weak endpoint constants in (5) suffice; the slightly stronger lower bound obtainable from (4) is not needed. This is an elementary conserved-current argument, not an inference from a finite positive response or a numerical sample.

For an arbitrary source index k, put u = T e_k. Across any path edge,

    u_j-u_(j+1) = 1_(k<=j) - mu sum_(i=0)^j u_i.

The right side lies between -1 and 1 because all u_i are positive and their total is 1/mu. Thus the maximum and minimum entries differ by at most m-1. Their average is again m, giving `T_(k,k) <= 2m-1 <= 2m`. The matching lower estimate follows from Cauchy-Schwarz in the B inner product:

    1 = (e_k^T 1)^2
      <= (e_k^T B^(-1)e_k)(1^T B 1)
       = T_(k,k) mu m.

Hence, writing gamma_k = T_(k,k),

    m <= gamma_k <= 2m.                              (6)

Equations (2), (5), and (6) are compatible: the full inverse norm is m^2, individual response entries are of order m, and the port counterterm will really grow with m for the chosen constant q. No one of these quantities is substituted for another.

These statements also cover the elementary m=1 limit, where T=[1] and the path has no edge. The actual geometric construction uses m>=5. No exact fixture is needed because the prefix identities prove the asserted inequalities for every finite m.

## 5. Polynomial source coefficients and the exact contraction

Let `t_j = T_(a,u_j)`, and define

    z_j = -(b_j+i c_j)/(2 q t_j),
    V = q(X_p X_a+Y_p Y_a)
        + sum_j n_(c_j)[Re(z_j) X_(u_j)+Im(z_j) Y_(u_j)],
    C_ct = kappa n_p + sum_j d_j n_(c_j),
    kappa = 4 q^2 gamma_a,   d_j = |z_j|^2 gamma_(u_j).

These d_j are counterterm coefficients, not the onsite terms of the earlier alternative clock. Bounds (5)-(6) give

    |z_j| <= sqrt(G)/m,
    4mG <= kappa <= 8mG,
    0 <= d_j <= 2G/m,
    v := 2q+sum_j|z_j| <= 3 sqrt(G),
    c_ct := kappa+sum_j d_j <= 8mG+2G <= 10mG.         (7)

All bounds are valid on the full Hilbert space as norm allowances, even though the desired contraction will use N_X=1. In particular `||V|| <= v` and `||C_ct|| <= c_ct`. There is no exponentially small denominator in the programmed sources.

Let J insert the auxiliary vacuum, leaving all clock, plant, and reference factors untouched. The auxiliary-creation amplitude on the port is `q(X_p+iY_p)`, whose squared operator is `4q^2 n_p`, not a scalar. A source creation amplitude is z_j n_(c_j). The port/source contraction through T has cross contribution

    2 q t_j n_(c_j)[Re(z_j)X_p+Im(z_j)Y_p]
      = -n_(c_j)(b_j X_p+c_j Y_p).

The source self-contraction is d_j n_(c_j). Source-source cross contractions for j!=k contain `n_(c_j)n_(c_k)` and vanish exactly on the sector `N_X=sum_j n_(c_j)=1`. It follows that on that entire sector,

    Sigma := J^* V R_A V J = C_ct-W,
    W = sum_j n_(c_j)(b_j X_p+c_j Y_p).              (8)

This retains all mixed inverse entries and the complex-source Y sign. The old plant can be arbitrarily correlated and its Hamiltonian need not commute with n_p, W, or C_ct. Formula (8) is not asserted for zero or multiple clock heads.

## 6. Positive runtime blocks, clocks, and physical scalar

The mediator construction works for any supplied clock Hamiltonian K_X preserving N_X, with a certified full-space norm B_X. To make the polynomial and endpoint constants concrete, use the simpler positive-edge basis clock from the frozen comparison. With `Omega=pi/(2 tau)`, tau>0, set

    K_X = sum_(j=0)^(n-1) Omega[
              (n-j)n_(c_j)+(j+1)n_(c_(j+1))
              -sqrt((j+1)(n-j)) S_(c_j,c_(j+1))].    (9)

Each edge block has eigenvalues `0,0,Omega(n+1),Omega(n+1)`. Consequently

    K_X = Omega n N_X - sum_j w_j S_(c_j,c_(j+1)),
    w_j=Omega sqrt((j+1)(n-j)),
    B_X=||K_X||=Omega n(n+1) <= Omega m^2,
    s_X=B_X/2.

The initial state is the computational-basis product state with its only clock excitation at c_0. Its free vector is

    chi_n(t)=exp(-i Omega n t) sum_(j=0)^n sqrt(binomial(n,j))
               cos(Omega t)^(n-j) [i sin(Omega t)]^j |j>.

In particular `chi_n(tau)=|n>` exactly, including phase. This differs from the root's other positive clock phase; it is the explicitly rederived substitution in the allowed comparison, not a silent change to that historical source.

Define

    A = H_P+K_X+sum_j a_j n_(c_j)+C_ct,
    H_tar = H_P+K_X+sum_j n_(c_j) C_j,
    R_pos = sqrt(Delta) v,
    K_Delta = Delta L_A+sqrt(Delta)V+A+R_pos I.       (10)

Every new runtime term admits a positive local decomposition. Use the auxiliary blocks (1), clock blocks (9), positive onsite a_j and counterterm fields, and the shifted source blocks

    sqrt(Delta)[q(XX+YY)_(p,a)+2q I],
    sqrt(Delta)[n_(c_j)(Re z_j X_(u_j)+Im z_j Y_(u_j))
                          +|z_j| I].

Their norms are `4q sqrt(Delta)` and `2|z_j| sqrt(Delta)` respectively. Their identity coefficients add once to R_pos. No global positivity argument is being substituted for the displayed block decomposition. Positive here means positive semidefinite; additional strict positive margins, if requested or needed for faults, must be installed and paid.

The normalized scalar of (10), with s_P the actual scalar coefficient of H_P, is exactly

    s_full = s_P+B_X/2+(sum_j a_j)/2
             +Delta[(m-1)+1/(2m)]
             +kappa/2+(sum_j d_j)/2+R_pos.           (11)

V is traceless. The mass and Laplacian scalar in (11) is real physical bookkeeping although L_A annihilates the ideal vacuum; it is canceled there by the other Pauli components, not by dropping a scalar from the generator. The reserve phase exp(-i R_pos t) remains explicitly in the isometry comparator. Channels are insensitive to a total global phase, while a specified coherent isometry or controlled use need not be.

## 7. Complete bare-input corrector and an explicit sufficient penalty

The full auxiliary inverse (2), not just its one-excitation restriction, is used here. All operators preserve N_X=1. Let

    x=v m^2,       y=v^2 m^4,
    X=R_A V J,    Y=R_A V X,
    Z=J-epsilon X+epsilon^2 Y,  epsilon=Delta^(-1/2).

X creates one auxiliary excitation. After R_A removes the vacuum part, Y has two. Thus `||X||<=x`, `||Y||<=y`, and the following exact residual identity holds on the N_X=1 input sector, before the scalar R_pos is added:

    (Delta L_A+sqrt(Delta)V+A)Z-Z H_tar
       = epsilon(VY-AX+XH_tar)
          +epsilon^2(AY-YH_tar).                    (12)

For completeness, `L_A X=VJ`, `L_A Y=(I-JJ^*)VX`, `JJ^*VX=J Sigma`, and `JJ^*VY=0` by auxiliary parity. Substituting these into the left side cancels its epsilon^-1 terms and its order-one part is `AJ-J Sigma=J H_tar` by (8). This proves (12) without discarding any noncommuting background term.

Use the full-space bounds

    a_* = h+B_X+r g+c_ct,
    b_* = h+B_X+2r g,
    D = a_*+b_* <= 2h+2B_X+13mG.

The corrected residual costs at most `epsilon[v y+D x]+epsilon^2 D y`. Each of the two bare/corrected endpoint changes costs at most `epsilon x+epsilon^2 y`. Duhamel integration therefore gives, uniformly for `0<=t<=tau`,

    ||exp(-itK_Delta)J
       -exp(-itR_pos)J exp(-itH_tar)||
      <= F_1/sqrt(Delta)+F_2/Delta,

    F_1=2x+tau[D x+v y],
    F_2=2y+tau D y.                                 (13)

This is an operator norm bound on the entire allowed plant/clock input sector and remains valid after tensoring an arbitrary reference. It starts from the bare supplied auxiliary vacuum, not a physically prepared dressed state. It keeps the actual auxiliary output and clock output. For density operators, including mixed and arbitrarily reference-entangled inputs, the complete output trace-norm and associated isometry-channel diamond error are at most twice the right side. No trace over an unwanted subsystem is required to make the assertion true.

A sufficient general recipe is

    Delta >= max(1, (2F_1/eta)^2, 2F_2/eta).          (14)

Here eta is the desired isometry error of the mediator, not a full trace-error budget. To make the polynomial constants entirely explicit for clock (9), put

    D_0 = 2h+2Omega+13G,
    C_1 = 6sqrt(G)+3tau D_0 sqrt(G)+27tau G^(3/2),
    C_2 = 18G+9tau D_0 G,
    D_Delta = 1+4C_1^2+2C_2.

Since m>=1, (7) gives `x<=3m^2 sqrt(G)`, `y<=9m^4G`, and `D<=D_0 m^2`. Thus

    F_1 <= C_1 m^4,   F_2 <= C_2 m^6.

For `0<eta<=1`, the explicit choice

    Delta = D_Delta m^8/eta^2                        (15)

satisfies (14). In particular the F_2 term is covered because `m^8/eta^2 >= m^6/eta`. No asymptotic threshold or unspecified sufficiently large constant is hidden in (15).

## 8. Polynomial physical prices, moments, and waveform composition

A valid full-space norm allowance, including every auxiliary and clock sector, is

    B_full = a_*+Delta ell_A+2sqrt(Delta)v
       <= h+Omega m^2+11mG
          +2D_Delta m^9/eta^2
          +6sqrt(D_Delta G)m^4/eta
       <= C_B m^9/eta^2,

    C_B = h+Omega+11G+2D_Delta+6sqrt(D_Delta G).        (16)

It is an upper bound on the interacting generator norm, not an exact equality. Its corresponding action allowance on the runtime horizon is tau B_full. The principal local quantities are as follows; all constants are specified above.

| Quantity | Explicit value or sufficient upper bound |
|---|---|
| Unscaled auxiliary gap / complete inverse norm | `m^-2` / `m^2` |
| Endpoint-to-every-source response | `[m/2,2m]` |
| Auxiliary diagonal Green entries | `[m,2m]` |
| Physical auxiliary penalty gap | `Delta/m^2` (not a total-Hamiltonian gap) |
| Auxiliary edge block norm | `2Delta` |
| Auxiliary onsite mass coefficient | `Delta/m^2` |
| Clock edge block norm | `Omega(n+1)` |
| Physical port XX and YY coefficient | `sqrt(Delta G)` each |
| Physical source complex coefficient | at most `sqrt(Delta G)/m` |
| Port counterterm coefficient | between `4mG` and `8mG` |
| Each clock counterterm coefficient | at most `2G/m` |
| Sum of counterterm coefficients | at most `10mG` |
| Paid scalar reserve R_pos | at most `3sqrt(Delta G)` |
| Exact auxiliary full norm / scalar | `Delta[2(m-1)+1/m]` / half that |
| New geometric sites / edges | `2m-3` / `3m-7` |

The largest new local block norm is at most a polynomial dominated by Delta at fixed h,g,tau. The collected identity coefficient can be larger by a factor of m; it is already included in (11) and (16). The physical onsite Z coefficients from the auxiliary edges are of order Delta even though the extra mass itself is Delta/m^2. Neither is omitted by calling the transport a Laplacian.

For the ideal input `|clock_0,vac_A>` and C_0=0, let

    D_P=H_P+kappa n_p.

Applying the actual K_Delta once produces three mutually orthogonal controller components: the original controller with plant operator `D_P+Omega n+R_pos`, clock_1 with amplitude `-Omega sqrt(n)`, and one auxiliary excitation at a with plant operator `sqrt(Delta)q(X_p+iY_p)`. Therefore, for any old plant/reference state with plant marginal rho_P,

    mean(K_Delta) = Tr(rho_P D_P)+Omega n+R_pos,
    Var(K_Delta) = Var_(rho_P)(D_P)+Omega^2 n
                     +4Delta G Tr(rho_P n_p).        (17)

The covariance of H_P and n_p in Var(D_P) is retained. If C_0 is nonzero, the diagonal operator adds `a_0+d_0` and the variance adds `Delta |z_0|^2`; the port and source creation sites are distinct. Formula (17) is for the ideal bare input, not an exact moment statement for an imperfect thermal/correlated source.

For C_0=0, sufficient positive mean and variance allowances are

    mean <= h+8mG+Omega m+3sqrt(D_Delta G)m^4/eta,
    Var <= (h+8mG)^2+Omega^2 m
                         +4D_Delta G m^8/eta^2.     (18)

Thus prepared-input mean is O(m^4/eta) and variance O(m^8/eta^2) at fixed supplied h,g,tau. The actual static total moments are conserved during the runtime. Small output state error alone does not imply small returned subsystem energy: for example the auxiliary penalty expectation has only the allowance `Delta ell_A eta^2` from a leakage estimate eta, which need not tend to zero.

For a concrete waveform application, let the positive one-port matrix waveform C(t) on [0,tau] have the coefficient form of Section 2, zero endpoints, and supplied operator Lipschitz constant L_C. Use

    t_j = (1/Omega) arcsin sqrt(j/n),  C_j=C(t_j).

For the free clock (9), j is binomial with parameter `sin^2(Omega t)`. The allowed comparison proves

    E |t_j-t|^2 <= tau^2/(2n),

by the square-root embedding `(sqrt(1-p),sqrt(p))`, the chord-angle estimate with constant pi^2/8, and the binomial variance. Inserting `chi_n(t) tensor U_C(t)` into the literal Schrödinger residual gives full-isometry error at most `L_C tau t/sqrt(2n)` for the abstract H_tar. Here U_C solves the old-plant evolution with H_P+C(t); H_P and C(t) need not commute. The binomial law is used only for the comparison vector, not assumed for the actual interacting clock.

Combining this checked clock bound with (13), the complete same-time target is

    exp(-i R_pos t)|vac_A> tensor chi_n(t) tensor U_C(t),

with error at most

    L_C tau^2/sqrt(2n) + eta                         (19)

uniformly up to tau. At tau its clock factor is exactly |n>, with no missing endpoint clock phase. Every old output and arbitrary reference is retained. Scalar phases within H_P and C(t) remain in U_C.

For ideal preparation and exact installed parameters, a sufficient full-output trace budget `0<epsilon<=1` is

    n = max(1, ceil(8 L_C^2 tau^4/epsilon^2)),
    eta=epsilon/4,

so (19) is at most epsilon/2 and the full trace error is at most epsilon. At fixed h,g,tau,L_C, this explicit recipe gives

    m=O(epsilon^-2),
    Delta=O(epsilon^-18),
    B_full and the collected scalar allowance=O(epsilon^-20),
    largest new local block norm=O(epsilon^-18),
    prepared mean=O(epsilon^-9), prepared variance=O(epsilon^-18).

These powers are sufficient recipes, not lower bounds or optimality claims. If preparation, release, calibration, or timing also consume the final error budget, reserve those portions first and apply the same formulas to the smaller remaining budget. A common coefficient cap independent of epsilon is not obtained.

## 9. Computability, calibration, timing, and positivity margins

The entries of B are rational for integer m, and B is a positive tridiagonal matrix with no zero pivot. Exact rational elimination gives T with finite bit lengths polynomial in m log m: after multiplying B by m^2, determinant and cofactor integer sizes have O(m log m) bit bounds from the row norms. This is coefficient bookkeeping, not an assertion that the original waveform or an arbitrary target-unitary compiler is efficient. Their evaluation/certification costs remain supplied.

There is no hidden exponential sensitivity in the local inverse-entry certificate. For real symmetric path-parameter perturbations with `||delta B|| <= 1/(2m^2)`, the resolvent identity gives

    ||(B+delta B)^(-1)-B^(-1)|| <= 2m^4 ||delta B||.

In particular `||delta B|| <= 1/(8m^3)` keeps every endpoint response within m/4 of its nominal value, so the positive lower bound m/4 remains. On that domain the reciprocal response changes by at most `8|delta t_j|/m^2`. These are mathematical coefficient-stability bounds. For physical dynamics against one fixed prescribed target, the actual installed generator error must still be charged; recomputing a convenient effective waveform does not remove it.

For positive actual Delta', a safe full-space operator comparison is

    ||K_actual-K_Delta||
      <= |Delta'-Delta| ell_A + Delta'||L_A'-L_A||
         +|sqrt(Delta')-sqrt(Delta)| v
         +sqrt(Delta')||V'-V||
         +||A'-A||+|R_pos'-R_pos|.                  (20)

For source changes alone, `||V'-V|| <= 2|q'-q|+sum_j|z_j'-z_j|`. Physical counterterm and scalar errors stay in A' and R_pos'. For auxiliary edge-weight error at most sigma_e and mass error at most sigma_mu,

    ||L_A'-L_A|| <= 2(m-1)sigma_e+m sigma_mu.

Thus, for example, choosing both errors no larger than `epsilon_cal/(12 tau Delta m)` assigns at most epsilon_cal/2 of full trace error to that contribution when Delta is fixed. Impose the additional `sigma_mu <= mu/2` if preserving a positive mass by this parametrization. All these required absolute or relative precisions are inverse polynomial in the displayed parameters; none is a size-independent tolerance assertion.

Equivalently, the new collected Pauli operator has at most `7r+3m <= 10m` nonzero-coordinate slots, counting the identity and allowing zero coefficients. This count includes clock and auxiliary Z fields, their XX/YY hoppings, source X/Y and ZX/ZY coefficients, the port XX/YY, and its Z counterterm. If each of these *physical, already scaled* coefficients has absolute error at most delta and the old plant is exact, then `||delta K|| <= 10m delta`. Taking `delta <= epsilon_cal/(20 tau m)` suffices for full trace error epsilon_cal. Relative accuracy for a coefficient of size Delta is consequently of order epsilon_cal/(tau m Delta), not a free constant.

Semidefinite blocks can lose positivity under unrestricted signed calibration faults. One must either realize certified positive block parametrizations or add an actual identity reserve at least equal to each block's fault-norm allowance. Such reserves have real scalar, phase, moment, and work prices. There are at most 6m new blocks in the explicit uncollected decomposition, before old-plant blocks; their additional scalar sum must be included in the actual target or error budget. A favorable recombination of faulty Pauli coefficients is not a positivity certificate.

An integrated full-generator error costs at most `integral ||delta K(t)||dt` in the isometry estimate and twice that in complete trace norm. A fixed-endpoint timing defect delta_t costs at most `B_actual |delta_t|` in isometry norm, using a certified actual full-space norm; the doubled bound is sufficient for full trace norm. A global scalar defect is harmless for an ordinary channel but matters for the specified phase-sensitive isometry. Sector-restricted error estimates cannot replace (20) when physical faults can create extra clock heads or auxiliary excitations.

## 10. Supplied preparation, actual release chronology, and work

The runtime theorem is autonomous after initialization: (10) is static. That does not make its pure initial clock and auxiliary vacuum native. There are k=2m-3 new bits. For nu>0, a supplied positive product preparation Hamiltonian

    G_prep = nu[(I-n_(c_0))+sum_(other new bits v) n_v]

has the required bit state as its unique ground state, norm k nu, scalar k nu/2, and gap nu. For its exact product Gibbs marginal at inverse temperature beta>0, the probability delta_G outside that bit state obeys

    delta_G=1-(1+exp(-beta nu))^-k <= k exp(-beta nu).

The controller marginal trace distance to the pure bit projector is exactly 2delta_G, even if that marginal is part of an arbitrarily correlated old/reference state. For replacing the *entire joint input* while retaining the exact unconditional old/reference marginal, the general pure-factor lemma reused from the allowed comparison gives

    g(delta)=delta+sqrt(delta(4-3delta)).

If the delivered controller marginal is at half trace distance at most d from the prescribed Gibbs marginal, use `delta_bar=min(1,k exp(-beta nu)+d)` and add g(delta_bar) to the complete output trace budget by channel contraction. Only an actually independent product source permits the smaller joint replacement price 2delta. No conditioning on a successful/rare reference event and no restoration of a nominal earlier old marginal is justified.

For d=0, `g(delta)<=3sqrt(delta)` gives the sufficient choice `beta nu >= log(9k/epsilon_prep^2)` for a joint preparation budget epsilon_prep. This is an equilibrium/source contract; the runtime Hamiltonian does not in general preserve that preparation Gibbs law, cool the bits, or deliver the marginal. Couplings must actually be absent, isolated, or compensated while the preparation source operates.

A supplied finite release can be priced explicitly, without assuming it is native. Write `K_Delta=H_P+F`; the new block sum F is positive. For a supplied smooth monotone u from zero to one on a duration s, use

    H_rel(t)=H_P+(1-u(t))G_prep+u(t)F.

On the ideal bit state G_prep vanishes. Relative to that fixed controller and the actual H_P-aged old input, the release isometry error is at most `||F|| integral_0^s u(t)dt <= ||F||s`. The correlated source replacement g(delta_bar) is charged first. Runtime then starts from the old state aged by this real duration s. Starting its U_C on the pre-release old state would discard actual evolution. The complete source, release, runtime, and reference chronology is retained.

Let `B_F=B_X+r g+c_ct+Delta ell_A+2sqrt(Delta)v`, a computable bound on ||F||. For a chosen release isometry allowance eta_rel, take `s=eta_rel/B_F`. If the fixed ramp shape has `max|u'|<=c_u/s`, its full-generator slew is at most `c_u(B_F+k nu)B_F/eta_rel`. This retains the preparation Hamiltonian's norm, which need not be smaller than B_F. It is a polynomial *allowance* in the displayed runtime parameters, k nu and eta_rel^-1, not an actuator implementation. The ramp's actual scalar is included. For the ideal closed evolution under this monotone interpolation,

    |W_rel| <= integral ||dot H_rel||dt <= ||F-G_prep||.

Endpoint defects or an imperfect path require their actual endpoint-or-variation work allowance. Static runtime itself has no explicit time-dependent work term and conserves its total energy distribution; installation, cooling, release, and resetting are not thereby free. At an ideal instantaneous release with C_0=0, the finite-Hamiltonian expectation jump is `Omega n+kappa Tr(rho_P n_p)+R_pos`, but an actual finite ramp and an imperfect correlated source require the preceding full dynamics and norm prices.

With preparation joint error e_prep, moment differences from the ideal bare formulas can be bounded by `B_full e_prep` for the mean, `B_full^2 e_prep` for the second moment, and `3B_full^2 e_prep` for the variance. These growing factors must be paid if moment accuracy, not only state accuracy, is requested. The exact marginal and small trace error do not imply accurate high-energy tails automatically.

The clock continues to evolve after the endpoint and can return. A supplied final idle waveform interval can give a finite observation window under its stated certificate; it does not create a permanent halt, a reset, an autonomous refrigerator, or a reusable fresh memory bank.

## 11. Failure routes and the boundary of the polynomial conclusion

1. **Zero mass is not an acceptable shortcut.** With mu=0, the uniform one-excitation vector is another zero-energy vector of the positive Laplacian blocks. The auxiliary vacuum is not the unique kernel and the required reduced inverse does not exist. The shrinking positive mass in (1) and its complete inverse price are essential to this proof.

2. **A fixed positive mass can give an exponential source price.** For fixed mu_0>0, put `cosh(theta)=1+mu_0/2`. Solving the tridiagonal recurrence for endpoint forcing gives the opposite-end response

       [(L_path+mu_0 I)^(-1)]_(0,m-1)
             = sinh(theta)/[mu_0 sinh(m theta)].     (21)

   To verify it directly, the decreasing solution is proportional to `cosh((m-j-1/2)theta)`; the right endpoint equation uses `cosh(3theta/2)/cosh(theta/2)=mu_0+1`, and summing the components fixes their total to 1/mu_0. For fixed mu_0 this response is exponentially small in m. A fixed nonzero far-source target with the exact contraction requires `2q|z|t=|b+ic|`; q and z cannot both stay polynomial in m along that fixed-mass family. This is a failure of that parameter family and contraction, not a universal impossibility claim for other local simulators. Our mu=m^-2 avoids it while paying the shrinking unscaled gap.

3. **The one-head and one-port hypotheses matter.** Multiple clock occupations leave cross terms n_j n_k in (8); a clock vacuum does not run the waveform. A single XX coupling lacks the independent complex X/Y source needed here. Arbitrary many-body C_j cannot be attached directly by these two-qubit source edges. The physical one-port compiler, if used, must separately supply the required finite waveform and its complete background/phase certificate.

4. **Counterterms and scalar phases are actual terms.** Omitting kappa n_p leaves a nontrivial plant defect, not an ignorable scalar. Omitting the positive source reserves changes positivity and the coherent target phase. Using a one-excitation inverse to bound Y without (2), or preparing Z rather than proving the two bare endpoint costs in (13), would change the theorem.

5. **Polynomial in this interface is not polynomial in arbitrary computation.** The constants depend explicitly on h, g, tau, and waveform regularity; the approximation order n depends on L_C tau^2 and the error budget. An external finite controllability compiler may have enormous length, horizon, coefficient sizes, phase lifts, or computational effort as functions of the original plant size and target unitary. This theorem does not bound those quantities, derive the old plant, or supply its native states and controls. The new polynomial transport prices do not erase those limits.

6. **State accuracy is not a common-cap or work theorem.** Delta, physical penalties, global scalar, preparation and release prices grow. Full output trace error requires norm factors before it controls energy moments. Neither the equilibrium Gibbs certificate nor a positive static controller supplies a laboratory cooling, calibration, pulse, isolation, or switching mechanism.

## 12. Verification, scope, and disposition

The load-bearing new argument is the path prefix-current bound (4)-(6), followed by the literal full-sector corrector identity (12) and explicit inequalities leading to (15)-(16). The geometry, one-port contraction pattern, complete-output Duhamel method, and basis-clock concentration are explicitly reused at their frozen identities; their changed constants, scalar, and moments are spelled out here. The smaller Green-entry estimates are not used as a replacement for the full-sector inverse norm.

No scientific code, sweep, numerical example, or prior science replay was needed. Metadata programs only check identities, local recovery copies, syntax, source-freeze members, and actual receipt integrity. They are not evidence that the mathematical statements are true. Any failures are recorded as actual operations rather than converted into scientific outcomes. No current root candidate or other worker's current polynomial-path work was accessed before this derivation was sealed.

The justified disposition is a positive conditional construction at the specified finite interface. It supplies an explicit polynomial resource recipe for this NN auxiliary path, preserves the unique penalty vacuum and all-sector inverse, and approximates the same-time bare-input complete-output target with the stated error. It leaves native preparation, calibration and release hardware, total compiler complexity, a uniform physical resource cap, indefinite holding, and controller recycling open.


---

## Immutable source body: source_exposed_comparison

Historical source retained exactly; current status and interpretation are given above.

# Exposed comparison of two polynomial auxiliary-path mediator constructions

## 1. Disposition and exact exposure boundary

The inspected constructions are analytically supported as two different conditional finite-Hamiltonian families. No blocking algebraic defect was found in the root's Poincare bound, full-sector gap, coefficients, bare-input corrector, phase, or moment calculation. The root accuracy-power statement requires one explicit interpretation: choose the displayed minimal clock-size ceiling, or give a matching upper bound on the chosen size. Its lower condition `n >= threshold` alone does not imply `m=O(eta^-2)`. Root agreed to preserve the source and state this qualification in the current interpretation. Both source proofs remain unchanged.

The protected independent derivation is `polynomial_path_mediator_independent/DERIVATION.md`, 35057 bytes, SHA256 `0620431acdfc9b0c9e36f4ec1364cf2eaff8891ba2697aeadee37501b1e493a7`, frozen by `2a3310794f09b61c77122ca3e627544a3a677c61578712aafa891c13be8badd9`. Root's complete pre-comparison read record is `polynomial_path_mediator_precomparison_root_review/READ_REVIEW.json`, 3149 bytes, SHA256 `8f29f1e4e660dad0aeb38aefa61883e4a96f6bd95fa3fff115b41893f57485a6`, recording 20:01:16 UTC. It is a read/metadata record, not final acceptance or an invented executable launch receipt.

After that record and explicit authorization, I read the complete root candidate, `polynomial_path_mediator_root_candidate/DERIVATION.md`, 18554 bytes, SHA256 `45c211e6c44bb694cf01ac11e15ede8a85442b95baa125dd0b01519a031ee893`, and its complete 695-byte proposal freeze `60389ac284bab6672606985a55b6ab9ea5d532ac1fcb24aa83c02cf6f411ff04`; that read returned at 20:01:44 UTC. The complete source pins `78ecb13acae41c653c96f3c5b2943f69aa4969022a7061f03318189b27cd88e2` were then read at 20:04:10 UTC. The earlier protected proof was not revised in light of these exposures.

This comparison is source-exposed and uses the same model family and reasoning effort. Earlier campaign mass-regularized Laplacian work was already known and is disclosed in the independent freeze. The protected result is independent of this root candidate's text, not of all prior mathematics or all shared machinery. Reading an already favorable root pre-comparison assessment does not establish this report's correctness. No new agent, model override, current other-worker source, W/Git/PR/audit/lock/checkpoint/axiom/prompt mutation, or scientific rerun was used.

The previously complete readings reused at unchanged identities are the basis-clock comparison `8c3ba783afdfa526e9da08df73760d8b6f0477c2598002b4c71fc042e480a2c2` and the autonomous source/review `0e91f9369e387608f8fb3720c290e67f6aa98b10f13428866334c8507b9e989d` / `52eb2e2dcd9fc56a7be490e193b57754bd85bfad5d585244d4a9fce947b4465d`. Their geometry, clock concentration, and complete-output contracts are reused only within their checked domains. The changed auxiliary and resource arguments are reconstructed here.

## 2. Shared interface, different physical generators

Both constructions use n>=1, r=n+1 clock sites, m=n+4 auxiliary sites, and the same declared exterior path and source geometry. The old plant is nonempty with an accessible boundary port, complete supplied positive H_P of norm at most h, and arbitrary old/reference correlations. Its positive local block decomposition is a separate requirement if a consumer requires every old block to be positive. No whole-to-local positivity implication is assumed.

The admitted one-port waveform is `C(t)=a(t)I+b(t)X_p+c(t)Y_p`, with `sqrt(b^2+c^2)<=a<=g`, known finite Lipschitz bound L_C, zero endpoints, and computable sample certificates. Root further assumes C1 regularity; the inherited Lipschitz argument is valid on that smaller class. General many-body matrix controls are not directly realized by these two-qubit source edges. Scalar lifts and a compiler's target phase must be part of the supplied interface.

The shared positive-edge clock has `Omega=pi/(2tau)`, full norm `B_X=Omega n(n+1)`, scalar B_X/2, and free vector

    chi(t)=exp(-i Omega n t) sum_j sqrt(binomial(n,j))
              cos(Omega t)^(n-j)[i sin(Omega t)]^j |j>.

Thus chi(tau)=|n> exactly, including phase. The sample times are `Omega^-1 arcsin sqrt(j/n)`. Its complete isometry error against H_P+C(t) is at most `L_C tau t/sqrt(2n)`. The free binomial distribution belongs to this comparison vector, not to an asserted distribution of the actual interacting clock. No factor of sqrt(2), reference, or clock output changes in this comparison.

The auxiliary path starts at a, connects through v1,v2 to u0,...,un, and has exactly m-1 path edges. Every source c_j-u_j and the old port edge p-a is NN. The unchanged layout adds 2m-3 sites and 3m-7 declared geometric edges, with maximum new degree three and no other new-to-old adjacency in the stated nonnegative old box. Zero programmed source coefficients are allowed, including both endpoint sources. Declared connectivity does not imply nonzero interaction on every declared edge. Unknown outside couplings remain supplied isolation or a priced full-space error.

For either family let

    E_vw=n_v+n_w-(X_vX_w+Y_vY_w)/2,
    L(mu)=sum_path E_vw+mu N_A,
    T(mu)=(L_path+mu I)^(-1),
    t_j=T_(a,u_j), gamma_v=T_(v,v),
    z_j=-(b_j+i c_j)/(2q t_j).

The choices are different physical operators:

| Quantity | Root family R | Protected independent family I |
|---|---|---|
| Mass mu | `m^-3` | `m^-2` |
| Port q | `1/m` | `sqrt(G)`, `G=max(1,g)` |
| Complete reduced inverse norm | `m^3` | `m^2` |
| Proven entry lower bound | every entry `>=7m^2/8` | every endpoint-to-site entry `>=m/2` |
| Proven diagonal interval | `[m^2,9m^2/8]` | `[m,2m]` |
| Exact auxiliary norm | `2(m-1)+m^-2` | `2(m-1)+m^-1` |
| Exact auxiliary scalar | `m-1+1/(2m^2)` | `m-1+1/(2m)` |

These changes are not a scalar shift or a clock gauge transformation. A choice of family requires its own inverse entries, q, z, counterterms, physical reserve, corrector constants, and Delta. There is no license to take one family's gap and the other's coefficients without rederiving the resulting Hamiltonian.

## 3. Full-sector positivity and the two inverse arguments

For either positive mu, E_vw has pair eigenvalues 0,0,2,2, and `L(mu)>=mu N_A`. Its auxiliary vacuum is the unique kernel. The uniform one-excitation vector has eigenvalue mu, so the exact nonvacuum gap is mu and the complete reduced inverse has norm mu^-1. On k excitations the lower bound is k mu. This explicitly covers the two-excitation space needed by the second corrector. It is not a statement about the spectral gap of the entire coupled controller Hamiltonian.

The all-occupied auxiliary state simultaneously attains every positive edge norm and every onsite mass. Hence

    ||L(mu)||=2(m-1)+mu m,
    scalar(L(mu))=m-1+mu m/2,
    absolute Pauli sum=3(m-1)+mu m.

Both sources use these full-space quantities correctly. Replacing them by a one-head norm would lose real full-sector resource prices.

For root's all-entry estimate, the finite complex-vector identity is

    sum_i|x_i-xbar|^2=(1/m)sum_(i<j)|x_i-x_j|^2.

Cauchy-Schwarz along the interval from i to j gives the weighted edge sum. If an edge has a vertices to its left and m-a to its right, its coefficient is

    (1/m)sum_(i<a<=j)(j-i)=a(m-a)/2 <= m^2/8.

The equality follows by summing j over the right interval and i over the left; their mean separation is m/2. Therefore `L_path >= (8/m^2)Q`, with Q orthogonal to the constant vector. There is no missing factor of two: the path Laplacian quadratic form is exactly the sum of adjacent squared differences. The same Cauchy-Schwarz proof works for complex x.

On Q, `(mu I+L_path)^(-1)` has norm at most m^2/8. At root's mu=m^-3 the constant-mode contribution to every matrix entry is `1/(mu m)=m^2`. The residual is real symmetric, has every entry in [-m^2/8,m^2/8], and has nonnegative diagonal. Thus root's all-entry interval `[7m^2/8,9m^2/8]` and diagonal interval `[m^2,9m^2/8]` follow. A positive eigenvalue alone would not prove this; the explicit entry estimate does.

The independent proof uses a different argument at the larger mass m^-2. The strictly positive resolvent has row/column sums m^2. For endpoint forcing u=T e_a, the prefix current is

    u_k-u_(k+1)=mu sum_(j>k)u_j>0.

Summing over k yields `u_0-u_(m-1) <= [(m-1)/(2m)]u_0 < u_0/2`. Its mean entry is m, so every endpoint response lies in [m/2,2m]. For forcing at any site, each edge current has magnitude at most one, so the largest and smallest entries differ by at most m-1. Their mean is m, implying diagonal entries at most 2m. Cauchy-Schwarz in the B inner product gives the lower diagonal bound `gamma>=1/(mu m)=m`.

The independent endpoint argument fits this geometry because the old port is the auxiliary path endpoint. It does not claim root's stronger all-pair interval at the different mass. Conversely, directly substituting mu=m^-2 into root's uniform-mode-versus-remainder proof would give a remainder bound of order m^2 against a mean entry m; that estimate alone would not prove the needed positive lower bound for large m. The two proofs must be kept distinct.

No numerical example is required for either argument: the displayed finite identities prove their stated domains. The root's elementary Poincare constant is exact at the two-vertex path and remains a valid lower spectral bound at all larger sizes; this analytic endpoint observation is not a new computation.

## 4. Source coefficients, contraction, and positive local blocks

Let `kappa=4q^2 gamma_a`, `d_j=|z_j|^2 gamma_(u_j)`, and `C_ct=kappa n_p+sum_j d_j n_j`. Retaining the actual v, not just its loose upper bound,

    V=q(XX+YY)_(p,a)+sum_j n_j[Re(z_j)X_(u_j)+Im(z_j)Y_(u_j)],
    v=2q+sum_j|z_j|.

The correctly separated bounds are

| Quantity | Root R | Independent I |
|---|---|---|
| Each `|z_j|` | `<=4g/(7m)` | `<=sqrt(G)/m` |
| Full `||V||` allowance v | `<=2/m+4rg/(7m)<=2+g` | `<=3sqrt(G)` |
| Port counterterm kappa | `[4,9/2]` | `[4mG,8mG]` |
| Each source counterterm d_j | `<=18g^2/49` | `<=2G/m` |
| Complete counterterm allowance | `c_m=9/2+(18r/49)g^2` | `c_ct<=8mG+2G<=10mG` |

For root, the source estimate uses `2q t >= 7m/4`; its square times gamma gives `(16g^2/(49m^2))(9m^2/8)=18g^2/49`. Root's bounded port counterterm is a real benefit of its q choice. Independent's port counterterm grows with m and remains in its mean, scalar, covariance, and full norm. Neither family is being presented as uniformly better in every physical quantity.

The contraction can be checked before any effective-Hamiltonian interpretation. Appending auxiliary vacuum, the port creation amplitude is q(X_p+iY_p), whose square is `4q^2 n_p`. A source creation amplitude is z_j n_j. Since t_j is real,

    q t_j[(X_p-iY_p)z_j+(X_p+iY_p)conj(z_j)] n_j
       =2q t_j[Re(z_j)X_p+Im(z_j)Y_p]n_j
       =-(b_jX_p+c_jY_p)n_j.

For distinct sources the contraction contains n_j n_k, which vanishes only on N_X=1. Source self-squares give d_j n_j. Therefore, on that full clock sector and arbitrary plant/reference inputs,

    J_A^* V R V J_A = C_ct-W,
    W=sum_j n_j(b_jX_p+c_jY_p).

Both signs, the nonscalar port term, and all source-source terms are accounted for. No commutation with H_P is needed. The identity is not extended to arbitrary multihead input.

For either family the actual physical reserve is `R_pos=sqrt(Delta)v`. Add `2q sqrt(Delta)I` to the port block and `sqrt(Delta)|z_j|I` to source block j. The resulting full pair blocks are positive, of norms `4q sqrt(Delta)` and `2|z_j|sqrt(Delta)`. Their identity coefficients sum exactly to R_pos. Every auxiliary edge/mass, clock edge, and counterterm/sample onsite field is already positive. Using a loose upper bound for v as an installed reserve instead would add a further scalar; that scalar must be included, not substituted silently into the exact ledger.

The word positive means positive semidefinite in these constructions. Arbitrary signed coefficient faults can spoil zero eigenvalues; an actual positive parametrization or priced extra block margins are required. No missing physical local-reserve assumption is repaired merely by whole-generator positivity.

## 5. Full noncommuting corrector, bare endpoints, and phase

Set

    A=H_P+K_X+sum_j a_j n_j+C_ct,
    H_tar=H_P+K_X+sum_j n_j C_j,
    K_Delta=Delta L_A+sqrt(Delta)V+A+R_pos I.

Let J=J_A, epsilon=Delta^-1/2, `X=RVJ`, `Y=RVX`, and `Z=J-epsilon X+epsilon^2Y`. R is the inverse on the entire nonvacuum space. Since V changes auxiliary excitation parity, X has one excitation and Y has two after R removes the vacuum part. In particular `P VY=0`, with P the auxiliary vacuum projector. The exact identities are

    L_A X=VJ,
    L_A Y=(I-P)VX,
    P VX=J(C_ct-W).

Expanding all powers of epsilon now gives

    (Delta L_A+sqrt(Delta)V+A)Z-ZH_tar
       =epsilon(VY-AX+XH_tar)+epsilon^2(AY-YH_tar).   (C1)

The order epsilon^-1 terms cancel, and the order-one vacuum part is `AJ-J(C_ct-W)=JH_tar`. Terms AX-XH_tar and AY-YH_tar have not been deleted or replaced by commutators assumed small. This is why arbitrary noncommuting H_P, n_p, clock propagation, and sampled controls are allowed.

Writing `a_*=h+B_X+rg+counterterm_bound`, `b_*=h+B_X+2rg`, `D=a_*+b_*`, and `x=v/mu`, `y=v^2/mu^2`, the residual norm is at most `epsilon[v y+D x]+epsilon^2 D y`. The two bare-to-corrected endpoint changes each cost `epsilon x+epsilon^2 y`. Consequently, uniformly through tau,

    eta_A <= F_1/sqrt(Delta)+F_2/Delta,
    F_1=2x+tau(Dx+v y),
    F_2=2y+tau D y.                                 (C2)

This is an operator estimate on the entire allowed N_X=1 input sector, with arbitrary retained references. It does not require a supplied dressed state. Tensoring any reference preserves the operator bound, and expanding two isometry channels gives the unhalved complete trace/diamond allowance twice (C2). Neither auxiliary nor clock output is discarded.

Combining with the shared clock residual, the actual complete same-time comparator is

    exp(-iR_pos t)|vac_A> tensor chi(t) tensor U_C(t),

with error at most `L_C tau t/sqrt(2n)+eta_A`. At t=tau the clock has endpoint phase one, but the actual reserve phase remains. The large scalar from Delta L_A annihilates the vacuum only together with its Z/hopping terms; it is not a deleted global energy term. Old H_P and waveform scalars remain in U_C. Channel insensitivity to a global phase does not justify dropping it from this prescribed coherent isometry.

## 6. Separate sufficient resource recipes and the clock-size qualification

Both sources' general sufficient choice is

    Delta >= max(1,(2F_1/eta_med)^2,2F_2/eta_med).

An upper resource claim refers to a chosen sufficient recipe, not every arbitrary larger Delta. Root already states this correctly for Delta. At fixed h,g,tau, its x,y,F bounds are `O(m^3), O(m^6), O(m^6), O(m^8)` respectively. Independent's are `O(m^2), O(m^4), O(m^4), O(m^6)`.

For an explicit check of root's asymptotic constants, without changing its source, define

    V_R=2+g,
    C_R=9/2+(18/49)g^2,
    D_R0=2h+2Omega+3g+C_R,
    A_R1=2V_R+tau D_R0 V_R+tau V_R^3,
    A_R2=2V_R^2+tau D_R0 V_R^2,
    M_R=1+4A_R1^2+2A_R2.

Because r<=m and m>=1, `D<=D_R0 m^2`, `F_1<=A_R1 m^6`, and `F_2<=A_R2 m^8`. Hence the new, explicitly labeled comparison majorant

    Delta_R=M_R m^12/eta_med^2,  0<eta_med<=1,        (C3)

is sufficient. It is a convenient explicit polynomial upper recipe for the same root family, not an attributed verbatim formula or a replacement of its original maximum. The original maximum is no larger than a constant of this order. This derivation verifies rather than assumes root's polynomial claim.

For the independent family retain its own printed constants

    D_I0=2h+2Omega+13G,
    C_I1=6sqrt(G)+3tau D_I0 sqrt(G)+27tau G^(3/2),
    C_I2=18G+9tau D_I0 G,
    M_I=1+4C_I1^2+2C_I2,
    Delta_I=M_I m^8/eta_med^2.                       (C4)

They cover `F_1<=C_I1 m^4`, `F_2<=C_I2 m^6`. The fourth-power difference in the sufficient penalty comes from the different full inverse cost and its corrector propagation; one cannot obtain it by merely relabeling root's F values.

For root, `a_*<=h+Omega m^2+(g+C_R)m` and ell_A<=2m. A full norm allowance is therefore

    B_R <= [h+Omega+g+C_R+2M_R+2V_R sqrt(M_R)]
                                      m^13/eta_med^2.

Independent retains

    B_I <= [h+Omega+11G+2M_I+6sqrt(M_I G)]
                                      m^9/eta_med^2.

These are full interacting-generator upper bounds, not equalities. The scalar, action, and all-sector costs remain as in Section 7 below.

The required root wording qualification is precise. Its clock lower bound

    n >= max(1,ceil[L_C^2 tau^4/(2eta_X^2)])

guarantees the stated clock error. To conclude `m=O(eta^-2)` when eta_X and eta_med are fixed positive fractions of eta, choose n equal to that displayed right side, or explicitly bound n above by a constant multiple of it. Taking, for example, n larger than exp(1/eta) satisfies the lower condition and makes even `B_X=Omega n(n+1)` superpolynomial in eta^-1. Since the clock is a positive summand of the positive-block runtime Hamiltonian, its exact norm also gives a lower bound on the full runtime norm; this is not only looseness of an upper estimate. The existence of a polynomial choice is unaffected.

For matched full trace budget epsilon and fixed waveform/background parameters, one possible common convention is `eta_X=eta_med=epsilon/4` and the minimal ceiling for n. Then m=O(epsilon^-2), and the distinct sufficient orders are

| Quantity | Root R | Independent I |
|---|---|---|
| Penalty Delta | `O(m^12/eta_med^2)` / `O(epsilon^-26)` | `O(m^8/eta_med^2)` / `O(epsilon^-18)` |
| Full norm and collected scalar allowance | `O(m^13/eta_med^2)` / `O(epsilon^-28)` | `O(m^9/eta_med^2)` / `O(epsilon^-20)` |
| Reserve allowance | `O(m^6/eta_med)` | `O(m^4/eta_med)` |
| Largest new local block norm | `O(m^12/eta_med^2)` | `O(m^8/eta_med^2)` |
| Physical port coupling | `O(m^5/eta_med)` | `O(m^4/eta_med)` |
| Physical source coefficient | `O(m^5/eta_med)` | `O(m^3/eta_med)` |
| Physical auxiliary mass / penalty gap | `O(m^9/eta_med^2)` | `O(m^6/eta_med^2)` |

These are conservative sufficient recipes at fixed supplied h,g,tau,L_C. Their explicit constants show dependence on h,g,tau and tau^-1; those inputs cannot be hidden when they themselves grow. No optimality, lower complexity bound, common cap, or practical efficiency claim is justified.

## 7. Exact scalar, moments, and coefficient construction

For either family the full normalized scalar is exactly

    s_full=s_P+B_X/2+(sum_j a_j)/2
            +Delta[m-1+mu m/2]
            +kappa/2+(sum_j d_j)/2+sqrt(Delta)v.      (C5)

Thus the root auxiliary contribution is `Delta[m-1+1/(2m^2)]` and the independent contribution `Delta[m-1+1/(2m)]`. Their port terms are respectively `2gamma_a/m^2` and `2G gamma_a`. Every source reserve uses the actual v. This exact scalar ledger is distinct from the large bound on its magnitude and from the prepared state's mean energy. The runtime action-norm allowance is tau B_full for the chosen family; it is not a microscopic mechanical-work identification.

Let `D_P=H_P+kappa n_p`. Since C_0=0, applying the actual Hamiltonian to the bare controller produces mutually orthogonal original, clock_1, and auxiliary-at-a components. Their operators/amplitudes are `D_P+Omega n+R_pos`, `-Omega sqrt(n)`, and `sqrt(Delta)q(X_p+iY_p)`. Consequently

    mean=Tr(rho_P D_P)+Omega n+R_pos,
    Var=Var_(rho_P)(D_P)+Omega^2 n
                               +4Delta q^2 Tr(rho_P n_p).    (C6)

This holds for arbitrary old/reference input with the stated plant marginal. It retains H_P/n_p covariance. For root, kappa<=9/2 and q^2=m^-2, so its printed sufficient mean `O(m^6/eta_med)` and variance `O(m^10/eta_med^2)` follow. For independent, kappa<=8mG and q^2=G, giving its mean `O(m^4/eta_med)` and variance `O(m^8/eta_med^2)`. At the minimal common clock size these become root `O(epsilon^-13)` / `O(epsilon^-22)` and independent `O(epsilon^-9)` / `O(epsilon^-18)`. Input-dependent vanishing terms can improve particular cases; these are uniform upper allowances.

For a nonzero starting sample, the initial diagonal adds a_0+d_0 and the variance adds Delta|z_0|^2 because the port and source creation sites are distinct. Root deliberately specializes to zero endpoints. The exact formulas are not carried unchanged to a finite-temperature or correlated imperfect controller input.

For an imperfect complete input with replacement error e, safe mean, second-moment, and variance errors are B_full e, B_full^2 e, and 3B_full^2 e. A leakage norm eta_A by itself bounds auxiliary penalty expectation by Delta ell_A eta_A^2, which need not vanish. Positive total-energy conservation can give additional bounds, but it does not imply a returned zero-energy auxiliary, clock restoration, or reuse. Static total moments are conserved under the actual generator; comparison-product moments are not automatically equal.

The rational inverse construction is also sound. Multiplying root's B by m^3, or independent's by m^2, yields an integer tridiagonal matrix with polynomial-size entries. Hadamard bounds place determinants and cofactors in O(m log m) bits; positive definiteness prevents zero pivots. Standard reduced rational elimination therefore has polynomial arithmetic bit cost for this supplied matrix. This does not compute unspecified real waveform samples or make a general one-port compiler efficient.

## 8. Physical calibration, source delivery, release, and actual time

Both exact families require calibration of the written full physical generator, not only a favorable effective contraction. For positive Delta',

    ||K'-K|| <= |Delta'-Delta|ell_A+Delta'||L_A'-L_A||
        +|sqrt(Delta')-sqrt(Delta)|v
        +sqrt(Delta')||V'-V||+||A'-A||+|R_pos'-R_pos|. (C7)

The source bound is `||V'-V||<=2|q'-q|+sum_j|z_j'-z_j|`. Counterterm and scalar errors remain in A' and R_pos'. For positive weighted path blocks and positive masses, the entire auxiliary space still has lower bound `(min mass)N_A`; `||L_A'-L_A||<=2sum_edges|delta w|+sum_sites|delta mu|`. Actual positivity must be certified, not inferred from small generic signed errors.

Root's resolvent bound follows from `||B^-1||=m^3` and, when d<=mu/2, `||B'^-1||<=2m^3`:

    ||B'^-1-B^-1||<=2m^6 d.

With also `d<=7/(32m^4)`, the entry change is at most 7m^2/16, leaving every t'_j at least 7m^2/16. This literal ordered-positive-entry statement is for real weighted-path/mass perturbations of the supplied design. Arbitrary complex edge-phase errors do not define an ordered real t'_j; they must be treated as full generator faults or given a separately explicit complex-source calibration contract. The root paragraph's positive-weight premise supplies the needed real path context.

Independent's corresponding estimates are `||B'^-1-B^-1||<=2m^4 d` for d<=1/(2m^2), and d<=1/(8m^3) leaves endpoint entries at least m/4. The precision powers cannot be transferred between families. Both sets are inverse polynomial, and neither grants fixed arbitrary coefficient tolerances as m grows.

The full physical Pauli layout is unchanged: at most `7r+3m<=10m` new coefficient slots including the collected identity. A per-slot absolute physical error delta therefore gives `||delta K||<=10m delta`, so `delta<=epsilon_cal/(20tau m)` is one sufficient full trace budget if the old generator is exact. Relative precision for coefficients as large as Delta is much stricter. This coordinate error allowance does not itself ensure block positivity: certify positive parametrizations or install additional reserves at least equal to each local fault norm, with their scalar/phase/work included.

Integrated full generator error gives isometry error `integral||delta K||dt`, doubled for complete trace norm. A fixed-endpoint timing error gives at most `B_actual|delta t|` in isometry norm. Clock-number leakage faults prohibit replacing these bounds by estimates only on the prepared clock sector. A pure global scalar defect is channel-invisible but remains relevant to a prescribed coherent isometry; the full-norm bound is a safe conservative way to charge it.

The same preparation bit string has k=2m-3 bits in both families. With nu_p>0 the supplied onsite preparation Hamiltonian has gap nu_p, norm k nu_p, scalar k nu_p/2, and bad Gibbs population

    delta_G=1-(1+exp(-beta nu_p))^-k <= k exp(-beta nu_p).

The controller marginal distance is exactly 2delta_G for that marginal regardless of outside correlations. For arbitrary complete old/reference extensions, replacing the entire joint input while keeping its exact unconditional old/reference marginal costs

    g(delta)=delta+sqrt(delta(4-3delta)).              (C8)

A half-trace marginal delivery error d increases the bad-event budget by at most d. Only an actually independent product source permits the smaller 2delta as a joint replacement bound. Neither conditioning on a good event nor restoring a nominal pre-delivery old state is allowed. This clause reuses the checked general pure-factor lemma; it is not an independent derivation of a native thermal supplier.

The preparation gap nu_p is separate from the runtime auxiliary mass mu and from Delta mu. Runtime interactions need not preserve the preparation Gibbs state. Isolation/compensation during preparation and an actual release are supplied or charged. Write `F=K_Delta-H_P>=0` and use the optional supplied positive interpolation

    H_rel(t)=H_P+(1-u(t))G_prep+u(t)F.

On the ideal bit state G_prep vanishes. Comparing to the fixed bit string and the H_P-aged old state gives release error `||F|| integral u`. This includes every release scalar in that error; no phase was removed for free. The runtime then starts from the old state aged by the actual release duration s, not the pre-release state.

A concrete extension of the inherited release ledger is to choose a computable B_F>=||F|| and `s=eta_rel/B_F`. If the supplied monotone ramp shape has `max|u'|<=c_u/s`, its full slew is at most `c_u(B_F+k nu_p)B_F/eta_rel`. The preparation norm must be kept, even if nu_p is large. For ideal closed evolution the absolute work is bounded by `||F-G_prep||<=B_F+k nu_p`; endpoint defects or a varying faulty path require their actual endpoint-or-variation allowance. This ledger applies separately with each family's F. It is not laboratory switching hardware, cooling time, or a native energy source.

For a correlated input, charge (C8) first, then the release, clock, mediator, calibration and timing budgets by channel contraction/triangle bounds at their actual elapsed durations. The exact retained marginal and growing norm factors for moments remain. Optional finite idle intervals do not supply permanent stopping, final isolation, reset, a fresh bank, or indefinite recycling.

## 9. Retained failure routes and scientific obligations

The following are narrow witnesses or missing-contract warnings, not universal no-go claims.

- Zero auxiliary mass leaves the constant one-excitation vector in the kernel along with the vacuum, so the full reduced inverse required here is undefined.
- At a fixed positive mass mu_0, the path's opposite-end response is `sinh(theta)/(mu_0 sinh(m theta))`, with `cosh(theta)=1+mu_0/2`. It is exponentially small in m; a fixed nonzero far-source target cannot have both q and z polynomial under this exact contraction. Changing the mass and paying its gap cost avoids this particular failure. The older fixed-mass bound is not a theorem about all NN simulators.
- A finite positive matrix entry without a quantitative lower bound is insufficient for a polynomial source claim. Likewise a useful one-excitation response does not give a full-sector inverse bound.
- Multiple heads leave source-source n_j n_k terms; vacuum clock input does not execute the waveform. Omitting kappa n_p leaves a plant operator defect. A single XX source lacks this contraction's independently adjustable X/Y response. A dressed-state theorem does not automatically establish the bare input without both endpoint terms.
- Wrong linear position-to-time sampling and discarded clock/reserve phases retain their earlier counterexamples. The inverse-sine samples and the explicit positive-edge clock phase are required here.
- Choosing an arbitrarily oversized n, or an arbitrarily oversized Delta, invalidates resource upper claims tied to a specific sufficient recipe. Only n's sufficient-choice wording needs the current root qualification; its Delta qualification is already explicit.
- Fixed thermal purity or small state error does not establish accurate energy moments against a growing norm. The exact full retained marginal, source delivery, and actual release aging cannot be replaced by an independent nominal state or an unaged input.
- Polynomial prices in the supplied waveform parameters do not bound the external compiler's recurrence search, length, pulse count, duration, phase-lift complexity, or dependence on general plant/target descriptions. Old local-block reserves and complete computable background remain premises. Neither family supplies native controller initialization, cooling, field calibration, release hardware, common physical caps, detector identification, or reuse.

The two valid conditional resource families should therefore be presented as separately priced choices. Independent's smaller sufficient full-norm power is not a proof of optimality, and root's bounded port counterterm should not be erased when comparing their ledgers.

## 10. Coverage, actual evidence, and final limits

All eight root sections were read completely: interface/geometry/clock; complete auxiliary positivity; Poincare and inverse-entry bounds; source coefficients and contraction; full bare corrector; sufficient resources and computational representation; moments/calibration/source/release; and scope. The complete protected proof was read at its frozen identity before this task and its changed parameter dependence is checked explicitly above. No original proof was edited.

The root pre-comparison read record and source pins are provenance, not scientific certification. Metadata capture/verification checks exact sources, recovery, frozen members, receipt integrity and syntax only. Source hashing does not verify inequalities or establish absence of all exposure. This author's comparison has no scientific program execution or numerical rerun.

Root separately announced one finite floating-point fixture after the analytic checks had identified the clock-size qualification. That notification's reported favorable outcome is disclosed exposure. This checker did not open the fixture source, results, freeze, or execution records, did not rerun it, and does not use its announced outcome as verification evidence. There is no claim that the broader root campaign ran no science. General correctness here rests on the finite analytic arguments, not fixture case counts.

The justified disposition is conditional source support for both frozen families, with the explicit minimal-clock-size interpretation of the root accuracy powers. Root acceptance, publication, native realization, and retained audit status are outside this report. No editable prompt file changed.
