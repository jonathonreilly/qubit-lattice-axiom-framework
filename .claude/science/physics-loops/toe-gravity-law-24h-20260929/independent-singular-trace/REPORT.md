# Independent singular-trace branch analysis

Selected mathematical and procedural source: `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. Working mathematical bytes read match that revision; campaign HEAD may contain pack-only commits. This is a conditional mathematical route pass, not an audit, formal landing review, axiom decision or physical gravity claim.

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
reachability_to_target: prunes
conditional_surface_status: exact Dirac analysis of the supplied quadratic mode/stencil model
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**Result.** At `beta=-alpha/3`, the missing inverse is replaced by the primary trace-momentum constraint `tau=sum_j P_jj=0`. Its bracket with the scalar curvature constraint is `2K p²`, so at every nonzero mode these two constraints are **second-class**. Preservation fixes the lapse perturbation and trace-velocity multiplier; it does not generate the full momentum constraint. The original no-shift quadratic action has two TT oscillators, two free vector pairs and one free longitudinal scalar pair. Adding the three spatial momentum constraints as a separate supplied clause reduces the nonzero modes to two TT pairs, but the lapse is still fixed. The homogeneous sector is different and is treated below.

The nonzero constant trace/curvature bracket also gives a precise obstruction: regular higher-order corrections preserving the leading constraints cannot turn both into first-class constraints on a flat-vacuum branch. This excludes that specific singular all-lapse completion class. It does not exclude a theory with a fixed lapse, a modified scalar rule, additional variables, singular/rank-changing completions, or other kinetic branches.

## 1. Contract and premise boundary

Family tuple:

`(degenerate tracefree kinetic Legendre transform on six staggered strains; Dirac consistency and the trace/curvature Poisson pairing; nonlinear completion with either a determined lapse or a changed first-class constraint content)`.

The target of this pass is the exact linear constraint class at `alpha+3beta=0`, keeping block62/101's supplied R1 and R2, K>0, alpha>0, wbar>0, standard real canonical pairing and periodic boundaries. Nonzero Fourier symbols are arbitrary real p with p²>0; zero modes are not removed by an inverse. A real mode or its cosine/sine pair is understood; complex Fourier conjugacy does not change the class or rank.

The Hamiltonian analyzed is exactly the one obtained from the **quadratic** action

`L = alpha/w [tr(hdot²)-(tr hdot)²/3] + K w [u R1(h)+R2(h)]`,

where `w=wbar` is fixed and positive. The perturbation u has no time derivative. This supplies uniform `V2=-K R2`, and arbitrary site smearings of `C1=-K R1`. It does **not** supply a nonlinear local density for `N V2`, an arbitrary-lapse kinetic completion, or a nonlinear Hamiltonian constraint at zero momentum. Terms such as `u T2` and `u V2` would be beyond this action's order. Preserving that distinction is essential when discussing “all lapses.”

Current minimal axioms, primitive registry and all three primitive sources were read in the previous discrete pass at the same selected revision; their mathematical content is unchanged. None supplies this quadratic action, a nonlinear constraint algebra, a preferred lapse or a map identifying K=4alpha. The approved units, matter kinetic-form isotropy and pointwise-state premises are not counted as obstructions. No new premise is adopted.

## 2. Singular Legendre transform without division by alpha+3beta

Use independent coordinates

`h_A=(h_xx,h_yy,h_zz,h_xy,h_xz,h_yz)`

with `{h_A,P_B}=delta_AB`. Write the full symmetric matrix momentum as

`pi_jj=P_jj`, `pi_ij=P_ij/2` for i<j.

This gives `sum_A P_A dh_A = tr(pi dh)`. Differentiating the action gives

`P_jj = (2alpha/w)[hdot_jj-(tr hdot)/3]`,

`P_ij = (4alpha/w) hdot_ij` for i<j.

Therefore

`tau=tr pi=sum_j P_jj=0`.

The velocity Hessian has rank five, with trace direction `hdot=lambda I` as its one-dimensional kernel. The positive kinetic form on the traceless subspace has a well-defined Legendre dual. One smooth extension away from tau=0 is

`T_tf = [tr(pi²)-tau²/3]/(4alpha)`.

On tau=0 it is equivalently `sum_j P_jj²/(4alpha)+sum_(i<j)P_ij²/(8alpha)`. Terms proportional to tau in a different extension can be absorbed into its multiplier and do not alter the constraint surface.

The total Hamiltonian, treating u as a multiplier, is

`H_T = w[T_tf-K R2+u C1] + mu tau`,  `C1=-K R1`.

Its velocity is `hdot=w(pi-tau I/3)/(2alpha)+mu I`. In particular, on tau=0, the free trace velocity is `tr hdot=3mu` before consistency fixes it.

## 3. Exact general-p constraint algebra

Let `s=p²`,

`R1 = s tr h-p^T h p`,

`R2 = -s tr(h²)/4 + |hp|²/2 -(p^T h p)tr h/2 +s(tr h)²/4`.

A shift in the trace coordinate, `h -> h+lambda I`, gives the two identities

`delta R1=2s lambda`,

`d/dlambda R2(h+lambda I)|_(lambda=0)=R1/2`.

Using `{h_A,P_B}=delta_AB` consequently gives

`{tau,C1}=2K s`,

`taudot = {tau,H_T}=K w(2s u+R1/2)`,

`C1dot = {C1,H_T}=K w[p^T pi p-s tau/3]/(2alpha)-2K s mu`.

These are polynomial identities in arbitrary real p,h,P. No nonzero-mode axis assumption is needed to prove them.

For s>0 the multiplier variation imposes C1=0. The two preservation equations then fix

`u=0`,

`mu=w p^T pi p/(4alpha s)`

on tau=C1=0. Thus no secondary equation `p^T pi p=0` follows: the trace velocity multiplier absorbs that term. In particular, the full vector momentum constraint is not generated either.

The two-by-two constraint Poisson matrix is

`Delta = [[0,2Ks],[-2Ks,0]]`,

which has rank two. The pair is second-class, not a lapse gauge generator plus a separate conformal gauge generator.

If u is included as a canonical coordinate with conjugate pi_u, the primary constraints are tau and pi_u. Their secondary conditions can be written C1=0 and `chi=2s u+R1/2=0`. In the order `(tau,C1,pi_u,chi)`, the Poisson matrix has determinant

`16 K² s^4`.

It has rank four for s>0. Preservation fixes the remaining multipliers, with no tertiary physical constraint. Seven configuration variables (six strains plus u) minus four second-class constraints leave five configuration degrees of freedom, as in the multiplier treatment.

As a source cross-check only, add the specified external term `-e(t)u` to the action, with no strain-stress source. The scalar condition becomes `R1=e/(K w)`, while trace preservation gives

`u=-e/(4K w s)`.

The arbitrary source time dependence is absorbed by the trace/longitudinal evolution; there is no e-double-dot term in u. This exactly agrees with block101's already-landed substitution at beta=-alpha/3. This static coefficient is prior art, not a new result here. On a torus the source must have zero mean in this quadratic model. A coupled matter theory or stress response is not supplied by taking e as external data.

## 4. Exact real-space all-lapse statement

For the block62 staggering, put `D_j^+=T_j-1`, `D_j^-=1-T_j^-1`, `Delta_j=D_j^- D_j^+`, and `L=-sum_j Delta_j`. Let S insert a scalar into the three diagonal strain slots and zero into the three shear slots. Let R be the linear map `h -> R1(h)`, with

`R_diag,j = L+Delta_j`,

`R_face,ij = 2 D_i^- D_j^-`.

The symmetrized-gradient matrix A from bond shifts to strains is

`(A xi)_jj = 2 D_j^- xi_j`,

`(A xi)_ij = D_i^+ xi_j+D_j^+ xi_i`.

The exact finite-stencil identities are

`R S=2L`, `R A=0`.

For real smearing profiles f,N,

`{tau[f],C1[N]}=2K sum_x f_x (L N)_x`.

This formula tests **every** lapse profile, not only a uniform lapse or one Fourier representative. If Q is the real symmetric Hessian of the uniform quadratic R2, then

`S^T Q=R/2`, `Q A=0`.

The first trace-preservation equation becomes

`2L u + (R h)/2=0`.

In vacuum R h=0, so L u=0. On a connected periodic torus,

`u^T L u = sum_(x,j)(u_(x+e_j)-u_x)²`,

hence u is spatially constant. A freely chosen nonuniform lapse fails consistency. This is lapse fixing within the supplied quadratic model; it is not a derivation of a physical clock choice.

On a torus with V sites, rank(L)=V-1 and rank of the tau/C1 Poisson matrix is `2(V-1)`. The mean trace primary tau_0 is left first-class, while the zero scalar-curvature row is identically redundant. On the exact 3³ check the ranks are 26 and 52. A delta lapse at a site gives trace-preservation residual `12 K w` at that site; a uniform lapse gives zero residual.

No infinite-lattice boundary condition is implicit in this torus proof. At boundaries or on a different graph the kernel and multiplier conditions must be recomputed.

## 5. Dirac reduction and the actual propagating/free sectors

The second-class reduction can be written without choosing an axis. Let

`S=(1,1,1,0,0,0)^T`, `r_A=partial R1/partial h_A`.

Then `r S=2s`, and the reduced mixed bracket is

`{h_A,P_B}_D = delta_AB - S_A r_B/(2s)`.

The h-h and P-P reduced brackets vanish. The matrix is a projector, but is generally not an orthogonal projector in the six independent-coordinate Euclidean norm. Its denominator is the nonzero-mode inverse Laplacian. In real space the Dirac bracket is therefore generally nonlocal; no finite-range nonlinear reduction follows merely from writing it down.

For a transparent mode count, align the tensor-coordinate basis with p, so p=(0,0,k), k!=0. This is algebraic use of the supplied isotropic symbol forms, not a claim of continuous spatial-rotation symmetry of the cubic lattice. Write

`h=[[phi+a,b,cx],[b,phi-a,cy],[cx,cy,2ell]]`.

The canonical one-form defines

`Pphi=Pxx+Pyy`, `Pa=Pxx-Pyy`, `Pb=Pxy`, `Pcx=Pxz`, `Pcy=Pyz`, `Pell=2Pzz`.

C1=0 gives phi=0, and tau=0 gives `Pphi=-Pell/2`. The reduced canonical pairs are `(a,Pa),(b,Pb),(cx,Pcx),(cy,Pcy),(ell,Pell)`. Direct substitution gives

`H_red = w(Pa²+Pb²+Pcx²+Pcy²)/(8alpha) +3w Pell²/(32alpha) +K w k²(a²+b²)/2`.

There are exactly:

- two TT harmonic oscillators with `omega²=K w² p²/(4alpha)`;
- two free vector canonical pairs;
- one free longitudinal scalar canonical pair.

All these kinetic coefficients are positive for the stipulated alpha,w. “Free” means zero restoring frequency and possible secular linear-in-time strain, not an absent degree of freedom. The TT speed remains unfixed unless an additional relation among K,alpha,w is supplied.

## 6. Spatial momentum constraints are a separate clause

For any shift xi, define `G[xi]=sum_A P_A(A xi)_A`; in tensor symbols it is `tr(pi(p xi^T+xi p^T))`. In this quadratic model,

`{G[xi],G[eta]}=0`, `{G[xi],tau}=0`, `{G[xi],C1}=0`, `{G[xi],H_T}=0`.

These equations mean that the no-shift action has conserved spatial-relabelling charges. They do not set those charges to zero. Time-independent spatial transformations are symmetries; arbitrary time-dependent shifts of h alone are not automatically gauge symmetries of the kinetic action.

If one separately supplies shift multipliers and imposes the three independent G constraints at each nonzero mode, they are first-class relative to the second-class scalar pair and the Hamiltonian. In the aligned basis they set `Pcx=Pcy=Pell=0`, and quotienting their three gauge directions removes cx,cy,ell. Exactly two TT canonical pairs remain. A gradient-only shift constraint removes only the ell pair and leaves the two vector pairs. None of these shift constraints is forced by the trace consistency calculation.

The all-shift extension is a consistent **linear** constrained alternative, with fixed nonuniform lapse. It is not the all-lapse first-class structure of the nonsingular DeWitt target.

## 7. Zero modes and degeneracies

At p=0, both R1 and R2 vanish identically. The mean lapse perturbation decouples from this quadratic action. The primary tau_0 is first-class and generates an arbitrary time-dependent homogeneous trace shift. If u_0 is treated canonically, pi_(u0) is also first-class and decoupled. The remaining five homogeneous traceless canonical pairs have a free positive kinetic Hamiltonian. There is no preferred longitudinal direction at p=0, so calling these “two TT plus three longitudinal” would be inappropriate.

The spatial G constraints are identically zero at p=0 and cannot remove any of those five pairs. With all nonzero-mode G constraints added on a V-site connected torus, the total configuration count is therefore `2(V-1)+5`; without them it is `5V`.

The exact nonlinear uniform-lapse Hamiltonian constraint is not determined by this count. A term `u_0 T2` is cubic in the quadratic-action expansion but its variation would contribute a quadratic zero-mode constraint. That issue cannot be settled from the linearized u equation, and no arbitrary positive-mean compact source is supplied. The result concerns alpha>0,K>0,w>0; alpha=0, K=0 and a different rank of the velocity Hessian change the Dirac problem and are not excluded by this calculation.

## 8. What higher-order terms can and cannot repair

Let a proposed smooth completion on the **same** phase space have a persistent trace primary and lapse constraint with expansions

`tau_tilde=tau_1+O((h,P)²)`, `C_tilde=C1+O((h,P)²)`

near a flat vacuum h=P=0, with the leading linear parts just analyzed. For each nonzero mode, or smeared real-space profiles with `sum f L N !=0`,

`{tau_tilde[f],C_tilde[N]} = 2K sum f L N + O(h,P)`.

At the flat origin every constraint vanishes, whereas this bracket does not. A smooth finite-coefficient combination of constraints vanishes there. Thus these two constraints cannot both be first-class on that regular flat branch. Higher-order counterterms cannot cancel an order-zero bracket. An invertible regular recombination of the full constraint list preserves the nonzero rank of its Poisson matrix at the origin. A regular canonical change of variables preserves the same fact.

The scope is precise: the trace primary must persist, the scalar rule must keep its leading `-K R1`, the same canonical carrier and a regular flat vacuum must be retained, and structure functions must be nonsingular there. Adding extra canonical variables, changing the leading scalar rule, using a noncanonical symplectic structure, allowing a singular field redefinition, or having a rank-changing kinetic Hessian away from flat changes the problem. Such alternatives are untested, not refuted. Adding an h-only linear term to the trace primary cannot cancel the bracket with the h-only C1, but changing its momentum direction would change the stipulated null direction.

A determined-lapse nonlinear theory is a different live target. Its exact remaining lemma is to construct nonlinear kinetic/potential terms and spatial constraints whose complete Dirac algorithm closes with the trace/scalar sector remaining second-class, whose lapse equation has a controlled kernel and solutions, and whose physical sector has the claimed stability and degrees of freedom. That lemma is **target-equivalent** for this altered nonlinear target; the quadratic result supplies its tangent structure but not its completion. For the original regular all-lapse first-class target with persistent trace primary, this branch is excluded under the just-stated premises, so no terminal lemma is hidden behind an unavailable inverse.

## 9. Source and novelty disposition

Complete core source reads at the selected revision: block62, block101 and block112, including their hypotheses and exceptions. Block101 explicitly states that its e-double-dot coefficient vanishes at beta=-alpha/3; the source response above is a check of that prior result. Block62 excludes alpha+beta=0 in its mode determinant discussion, whereas the present branch has alpha+beta=2alpha/3 and is distinct from that DeWitt degeneracy. Block112 explicitly excludes alpha+3beta=0 from its inverse-Hessian T1 and leaves additional canonical constraints unanalyzed. No application of its nonsingular ratio theorem to this singular branch is used.

The selected-main search used the statement patterns `(alpha+3beta | α+3β | beta=-alpha/3 | trace ... primary/second-class | singular trace | kinetic conformal)` with flexible spacing in the relevant admissibility, gravity and constraint notes. Matches were block101's elimination, block112's explicit exclusion, block124's trace kinetic coefficient and homogeneous-sector sign discussions. Those matches are scope/prior-art evidence, not independent derivations of the present constraint classification. No matching singular-trace Dirac classification was found in this bounded search; an exhaustive literature or repository novelty claim is not made.

Relevant open work was refreshed with `gh pr list --state open --limit 100 --json number,title,headRefOid`. PR9363 remained at `fd51a1f4c7f38c124d6f0f7dde396198eadf8b36`. Its matching viability-map/finite-slot sources and gravity-wall exercise were searched for this singular condition; no matching singular-trace branch construction was found. A quantum-link source matched broader trace vocabulary but uses a finite-spin assignment and is not the singular Legendre problem; it supplies no premise here. The earlier discrete pass records the actual inspected A1 proposal and its scope. Unrelated open proposals were not read in full.

Read-only remote-main check again returned `d84eacf1cb9388f424f7037b5bbdf18f9be8fca7`. The intervening paths were previously checked: this pass's mathematical and selected physics-loop sources did not change. Source/procedure SHA remains `7146fe17...`; no refs, primary sources or audit state were mutated.

## 10. Checks and negative-claim discipline

`check.py` independently differentiates the six-coordinate kinetic form and Hamiltonian with SymPy. Its general-p identities, extended four-constraint determinant, explicit canonical reduction and Dirac projector are exact. Its independent real-space 3³ construction uses rational matrices for the actual site/bond/face staggering, verifies the rank-52 scalar Poisson matrix, rank-78 symmetrized gradient, `R S=2L`, `R A=0`, `S^T Q=R/2`, `Q A=0` and the tracefree kinetic kernel. It imports no primary science runner.

Actual command:

`python3 -u .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-singular-trace/check.py`

Actual final result: exit 0, `TOTAL: PASS=7 FAIL=0`, seven named check groups. The first run was interrupted during SymPy's generic integer matrix-rank reduction, which caused unnecessary integer growth. Replacing that mechanical rank calculation with exact rational DomainMatrix rank completed the same checks in about five seconds. The interrupted run is not counted as a scientific failure or a passed check. `results.txt` is the full final output.

No formal no-go packet PASS is claimed. This is a scoped route return; the five-distinct-defeated-family packet minimum of the selected no-go skill has not been established. Its exact second-class obstruction is not broadened into a no-go on fixed-lattice gravity.

- **N1:** Direct consistency, Dirac reduction, multiplier extension, canonical/recombination invariance and analytic order counting are actual calculations for this one singular family, not five independent gravity routes. Fixed-lapse completion, extra variables and rank-changing completions remain live changed-premise alternatives.
- **N2:** Nonzero trace/curvature bracket, lapse fixing and the regular-completion obstruction are consequences of one algebraic fact, not independent walls. No inflated count is used.
- **N3:** K,alpha,w signs, real pairing, periodic domain, fixed R1/R2, persistence of the trace primary and regular flat branch are explicit supplied hypotheses.
- **N4:** Block112's nonsingular necessity theorem is not used as a witness against this branch. Block101's source formula is only an exact matching cross-check. No other family is cited as a negative proof.
- **N5:** General-p symbolic proof and real-space periodic argument establish the stated scope; zero modes are separately treated. Runner resolution lines disclose the finite checks.
- **N6:** Approved primitives are not walls. No axiom amendment is inferred from the result; choosing a different constrained dynamics is an open physical construction question.
- **N7:** Strongest alternative: keep the second-class trace/scalar pair and construct a consistent spatially gauged nonlinear theory with a determined lapse. The given quadratic Hamiltonian already shows that two TT pairs can coexist with such a second-class sector when shifts are separately imposed. The nonlinear Dirac algorithm, lapse solvability and physical identification remain unproved.
- **N8:** Prior sources deliberately preserve the singular edge. This pass analyzes it rather than extending the nonsingular inverse beyond its domain. The constructive fixed-lapse alternative prevents a blanket no-go conclusion.
