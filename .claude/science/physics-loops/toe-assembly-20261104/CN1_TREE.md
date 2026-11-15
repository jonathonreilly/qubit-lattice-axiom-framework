**Proof tree, sketched (owner 2026-11-08: "do more physics on astra max for sketching the proof trees").** Written by Codex gpt-6-astra at max effort, read-only, on the laptop; finished 2026-11-08T21:07:18Z. Template `~/toe-lap/tmpl/treeCN1.txt`. A sketch: no node below is proved by this file, and nobody has checked it. Statuses quote the frozen parts.

**W3 — Common light cone. Proof tree.**

> “species that interact through a common gauge field have speed differences that flow to zero.” — [TOE_ASSEMBLY.md:751](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:751)

> “specified mathematical flows, not a derived framework dynamics” — [CN1.md:5](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:5)

`PROVED` below means the stated frozen result, with its hypotheses. Those results are inputs. `REFUTED` applies to the specified shortcut. `OPEN` identifies a proposed theorem or an unsupplied hypothesis. No proposed reading is adopted.

```text
W3  Common-cone theorem                                      OPEN
│
├── R1  Two massless Dirac species and one U(1) field         OPEN
│   ├── RG      Exact scale integration with summable errors OPEN
│   ├── LIMIT   Full speed spread and regulator removal      OPEN
│   ├── OBS     Running coefficients → invariant thresholds  OPEN
│   └── P1–P4   Frozen flow and free-threshold inputs         PROVED
│
├── R2  Realization on the framework gauge layer              OPEN
│   ├── PHI     Photon phase and a usable vacuum             OPEN
│   ├── MAP     Compatible invariant-algebra zoom            OPEN
│   ├── TICK    Tick coefficients and lattice remainders     OPEN
│   ├── CH      Charged-sector dictionary                    OPEN
│   ├── TRANS   Class-(a) comparison → spectral comparison   OPEN
│   └── P5–P6   Frozen comparison and implementation inputs  PROVED
│
├── R3  Extension to every light species                     OPEN
│   ├── NA      Gauge factors, breaking and mass thresholds  OPEN
│   └── NEUTRAL Neutral sectors and the graviton             OPEN
│
├── RATE  Additional power-rate obligation for LZ1            OPEN
│
└── N1–N9  Frozen obstructions to specified shortcuts         REFUTED
```

**W3. Root statement — OPEN**

> “CN1-T, proposed and open.” — [CN1.md:31](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:31)

> “Referee repair CN1-T′ (proposed, not adopted).” — [CN1.md:39](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:39)

The root is the repaired CN1 target. Its scope is a common gauge-connected light sector. R3 must establish its applicability to every light species.

Fix the following data and hypotheses.

- **H-LAW.** At each scale \(k\), fix a quasi-local algebra \(\mathfrak A_k\), its local gauge action, an admissible tick \(\alpha_k\), and the cell-group action. Use a named live law. On five-mode sites, use \(F_x=\Lambda\mathbb C^5\). Use the chosen finite link registers. The tick has a fixed finite NN-a decomposition. Its complete automorphism preserves the local gauge generators and cell covariance.
- **H-VAC.** Fix normalized positive states \(\omega_k\). They are gauge invariant, cell invariant and tick stationary. The fine state is the specified VC1 vacuum. A different stationary witness does not satisfy this hypothesis merely by being stationary.
- **H-ZOOM.** Fix an integer \(L\ge2\). At every step, require a unital injective, cell-covariant, exponentially local map
  \[
  \Phi_k:\mathfrak A_{k+1}^{G}\longrightarrow\mathfrak A_k^{G}.
  \]
  Coarse sites satisfy R-form. One coarse tick represents \(L\) fine ticks. Exponential-locality constants may depend on the input support radius. No charged-field map is assumed.
- **H-a2.** For every support radius \(R\), compare all local invariant \(A,B\) with norms at most one. Write \(F^T_{0,k}\) for their fine truncated correlation through \(\Phi_k\). Write \(F^T_{1,k}\) for their coarse truncated correlation. Require
  \[
  |F^T_{0,k}(\beta,t)-F^T_{1,k}(\beta,t)|
  \le C_{k,R}\bigl(r^{-2}+tr^{-3}\bigr)M_k(r,t),
  \quad r=|\beta|_\infty\ge1,\quad t\in\mathbb N_0,
  \]
  \[
  M_k(r,t)=
  \sup_{|\beta'|_\infty\ge r}
  \max_{i=0,1}|F^T_{i,k}(\beta',t)|.
  \]
  Zero envelope means zero correlations on both sides.
- **H-PHOTON.** At every scale there is a physical photon band with node \(K=0\) and positive speed \(c_k\). For the literal CN1-T′ formulation, its node is Clifford in the source’s sense. The physical conical-spectrum alternative is candidate C-PH below.
- **H-CHARGED.** Supply the charged-sector dictionary. Its species carry nonzero charges under the common gauge field. The vertices coupling them to that field are nonzero. For the first rung, these are two massless Dirac species with \(q_1=q_2=1\).
- **H-T2.** Every other light band or continuum belongs to the supplied charged-sector dictionary, including its invariant pair channels. No additional light neutral bound species is included in this conditional target. The R-CS\(^{\rm str}\) prescription and its parity label remain explicitly named inputs. Their existence and physical identification are obligations of CH.

The owner imports have the following scope.

| Import | Exact source anchor |
|---|---|
| PS-5 | “five fermion modes” — [TOE_ASSEMBLY.md:205](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:205) |
| Live law choice | “keep both live” — [TOE_ASSEMBLY.md:214](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:214) |
| NN-a | “required of the complete update only” — [TOE_ASSEMBLY.md:235](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:235) |
| ZM1-INV | “Impose no map on charged fields or Gauss generators.” — [TOE_ASSEMBLY.md:252](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:252) |
| Class (a) | “No separate one-point matching is imposed.” — [TOE_ASSEMBLY.md:243](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:243) |
| Charged reading | “a named working candidate for lanes. It is not adopted.” — [TOE_ASSEMBLY.md:225](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:225) |
| Static subtraction | “Tick-fixed weight is recorded as a separate static class” — [TOE_ASSEMBLY.md:229](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:229) |

Let \((\pi_k,\mathcal H_k,\Omega_k)\) be the GNS representation. Let \(\widetilde U_k,T_k\) implement the commuting tick and translations. Set
\[
\mathcal H_{\mathrm{phys},k}
=\overline{\pi_k(\mathfrak A_k^G)\Omega_k},
\qquad
\xi^s_{A,k}
=P_{\ker(\widetilde U_k-1)^\perp}
\bigl(\pi_k(A)\Omega_k-\omega_k(A)\Omega_k\bigr).
\]
Let \(\mu^s_{A,k}\) be its joint spectral measure. Use quasienergy \(\lambda\in(-\pi,\pi]\). For \(0<\kappa\le1\), define
\[
W_\kappa=\{(\lambda,K):|\lambda|\le\kappa,\ 0<|K|\le\kappa\},
\]
\[
S_k(\kappa)=
\bigcup_{A\ \mathrm{local,\ invariant}}
\overline{
\left\{
\frac{|\lambda|}{|K|}:
(\lambda,K)\in
\operatorname{sing\,supp}\mu^s_{A,k}\cap W_\kappa
\right\}}.
\]
Singular support means the complement of the largest open set with a smooth Lebesgue density.

**Target conclusion**
\[
\boxed{
\forall\varepsilon>0\ \exists\kappa_0>0\ \exists k_0\
\forall k\ge k_0\ \forall\,0<\kappa\le\kappa_0\
\exists s>0:
\quad
\varnothing\ne S_k(\kappa)\subset[s,(1+\varepsilon)s].
}
\]

This states relative cone agreement. A common positive limiting speed in fixed units additionally needs the bounds and convergence delivered by LIMIT.

**Children:** R1, R2. Applicability extension: R3. Stronger consumer requirement: RATE.  
**Imports:** H-LAW, H-VAC, H-ZOOM, H-a2, H-PHOTON, H-CHARGED, H-T2.

**Preferred route.** Construct the exact running theory. Prove \(D_k\to0\), where
\[
D_k=\max\{c_k,v_{1,k},\ldots,v_{n,k}\}
-\min\{c_k,v_{1,k},\ldots,v_{n,k}\}.
\]
Then prove an invariant spectral comparison with error
\[
\eta_k(\kappa)\le C G_k+\omega(\kappa),
\qquad
G_k\to0,\quad \omega(\kappa)\to0,
\]
uniformly in the consumed scales and momenta. If every spectral speed lies within \(\eta_k\) of the running-speed set, and every running speed is at least \(v_*>0\), then
\[
\frac{\sup S_k-\inf S_k}{\inf S_k}
\le
\frac{D_k+2\eta_k}{v_*-\eta_k}.
\]
This gives the target with the required quantifier order.

**First hard step:** RG, followed by OBS. Gauge-fixed coefficients do not yet supply the spectral comparison.

**Second route.** Renormalize invariant current and flux correlators directly. Treat relative metric deformations as insertions. Prove contraction of those insertions in the source-dependent RG. This could avoid identifying a charged pole.

**First hard step:** obtain a uniform contraction estimate for the relative metric insertions without assuming Lorentz covariance.

**Programmes:** L1–L4 below.  
**Smallest rung:** two Dirac species and one Gaussian U(1) field, with invariant current sources.

---

**R1. Two species and one U(1) field — OPEN**

> “persistence of massless interacting modes and counterterm selection are assumptions to be proved.” — [CN1MOD.md:25](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1MOD.md:25)

**Statement.** Construct the massless infinite-volume invariant theory of the supplied M″ model. Prove common-cone convergence for its two Dirac species and photon.

Use the Wilson action specified at [CN1MOD.md:19](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1MOD.md:19), whose field content is quoted as “four-component Grassmann species”. Its coefficients are
\[
w_{a0}=1,\qquad w_{aj}=v_a>0,\qquad
U_{a\mu}(x)=e^{ieq_aA_\mu(x)}.
\]
Use periodic photons and spatially periodic fermions. Fermions are antiperiodic in Euclidean time. Take two unit charges. Use photon covariance
\[
\widehat C_{\mu\nu,m}(p)=
\frac{\delta_{\mu\nu}}{\widehat p^{\,2}+m^2},
\qquad
\widehat p^{\,2}=\sum_\mu4\sin^2(p_\mu/2).
\]
Choose critical fermion counterterms by proof. Fix a compact positive set of bare speeds. Require small positive \(G_0=e^2\). Constants must be uniform in volume and in
\[
N=\lfloor\log_L(1/m)\rfloor.
\]

**Children:** RG, LIMIT, OBS; P1–P4.  
**Imports:** the explicit M″ action; critical counterterms; physical invariant reconstruction. None is a framework identification.

**Preferred route.** Retain photon and fermion fields throughout a constructive block RG. Separate relevant, marginal and irrelevant coordinates. Prove a real invariant domain and summable velocity errors.

**First hard step:** a single exact blocking step with bounds that can be iterated uniformly in \(N\).

**Second route.** Begin with continuous-time spatial lattice QED. Establish the invariant correlation theorem there. Then prove a quantitative comparison with M″.

**First hard step:** compare the two regularizations through current and flux correlators, including the counterterms.

**Programmes:** L1, L2, L3, L4.  
**Smallest rung:** one blocking step for two Wilson species, with a massive photon.

---

**RG. Exact integration with summable velocity errors — OPEN**

> “B1 (open)” and “B2 (open)” — [CN1MOD.md:163](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1MOD.md:163)

> “C1 (open)” — [CN1MOD.md:165](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1MOD.md:165)

**Statement.** Derive an exact RG recursion for M″. Establish a sufficient convergence estimate without requiring the sharp pair exponent.

Let \(x_k=(v_{1,k},v_{2,k},c_k)\). A useful candidate estimate is
\[
x_{k+1}=x_k+hG_k\mathcal F(x_k)+r_{k,N},
\qquad h=\log L,
\]
where \(\mathcal F\) is the positive star vector field in P1, and
\[
b_-\le G_{k+1}^{-1}-G_k^{-1}\le b_+,
\]
\[
\|r_{k,N}\|_\infty
\le C\left(
G_k^2+G_ke^{-\beta k}+G_ke^{-\beta(N-k)}
\right).
\tag{W}
\]
All constants are independent of \(N\) and volume. The action norm must control every other marginal coordinate that can feed the velocity equations.

Estimate (W) is a proposed sufficient gate. It does not replace UB″.

**Children:** none.  
**Imports:** M″; P1–P3; the complete marginal-coordinate census; counterterm normalization.

**Preferred route.** Port background-field block averaging. First prove uniform inverses for the rescaled blocked Wilson operator,
\[
D_v(A)+aQ_A^*Q_A,
\]
for \(v\) in a positive compact set. Seek exponential decay in the block metric. Control gauge changes between adjacent blocks. Then establish determinant decoupling across large-field regions.

The weaker target is deliberate. \(O(G_k^2)\) absolute forcing is summable when \(G_k\asymp k^{-1}\). W3 convergence need not first establish a remainder proportional to \(G_k^2(v_1-v_2)\).

**First hard step:** B1 with complex backgrounds on compatible local gauges, or a real-domain substitute strong enough for exact integration.

**Second route.** Use a finite-range covariance decomposition. Keep the complete induced bosonic interaction in a polymer norm. Extract local kinetic terms after exact integration.

**First hard step:** C1. Bound the actual bosonic interaction and large fields. The continuum quartic cancellation does not identify the lattice quartic.

**Programmes:** L3 and L4 for the first route; L2 and L4 for the second.  
**Smallest rung:** one four-dimensional block with two species, unequal speeds, and a photon mass below the block cutoff.

---

**LIMIT. Full spread, positive speed and regulator removal — OPEN**

> “U2–U4 alone do not give it, so U5 remains an independent UB″ condition.” — [CN1MOD.md:102](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1MOD.md:102)

> “all speeds converge to one limit; no rate is claimed.” — [CN1.md:135](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:135)

**Statement.** For the exact model, prove
\[
0<v_*\le v_{a,k},c_k\le v^*<\infty,
\qquad
D_k\longrightarrow0.
\]
Construct the massless, infinite-volume invariant correlations. Preserve the estimates in that limit. Prove convergence of the common speed in the fixed spatial and temporal units.

Pair agreement \(v_1-v_2\to0\) is insufficient. The photon must join the pair.

**Children:** none.  
**Imports:** RG; P1–P3; critical mass selection; positivity or another justified invariant reconstruction.

**Preferred route.** Prove discrete consensus directly. The leading update is a stochastic averaging step on a star. Over intervals with fixed accumulated gauge time,
\[
\tau=\sum_k hG_k,
\]
every species communicates through the photon. Uniform positivity gives a diameter contraction. Estimate (W) gives uniformly vanishing forcing tails:
\[
\lim_{K\to\infty}\sup_{N\ge K}
\sum_{k=K}^{N}\|r_{k,N}\|=0.
\]
A small total displacement keeps the speeds positive. Compactness then supplies regulator limits.

**First hard step:** prove compactness and uniform tail bounds for the actual correlations, not just their local coefficients.

**Second route.** Interpolate the exact discrete flow. Prove that the interpolation satisfies P2’s hypotheses. Apply the frozen integrable-forcing conclusion.

**First hard step:** control the interpolation error and the photon-mass endpoint uniformly. A formal replacement \(k\mapsto\ell\) is insufficient.

**Programmes:** L1 and L4.  
**Smallest rung:** one fermion speed and one photon speed. This detects the gap left by pair-only contraction.

---

**OBS. Invariant thresholds from running coefficients — OPEN**

> “Interactions may broaden, remove, shift or create singularities” — [CN1.md:48](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:48)

**Statement.** Identify the invariant spectral speed set with the running kinetic speeds at sufficient precision for W3.

Prove nonemptiness. Prove an upper bound on every relevant singular-support speed. Prove visibility of each species whose speed is being claimed. Establish a positive denominator. The comparison must be uniform for every sufficiently small \(\kappa\).

A sufficient form is
\[
\sup_{s\in S_k(\kappa)}
\operatorname{dist}(s,\{c_k,v_{1,k},\ldots,v_{n,k}\})
\le CG_k+\omega(\kappa),
\]
with \(\omega(\kappa)\to0\) uniformly in \(k\). Species visibility is a separate reverse comparison.

**Children:** none.  
**Imports:** R1’s limiting theory; P4; invariant current and flux sources; local spectral access.

**Preferred route.** Carry conserved-current sources through the exact RG. Prove boundary-value estimates for the retarded current matrix. Separate threshold location from threshold amplitude. Use positivity to retain a nonzero spectral channel.

**First hard step:** show that the faster species remains identifiable after coupling to the slower species and photon.

**Second route.** Construct dressed charged sectors. Identify their energy-momentum boundaries. Relate suitable neutral products to invariant pair spectra.

**First hard step:** control dressing limits and soft-photon continua without assuming an isolated charged pole.

**Programmes:** L2 for source-dependent RG; L1 and L5 for metric coefficients and their observable identification.  
**Smallest rung:** the free two-species current matrix, followed by one exact interaction step. Test all relevant bilinears, not one preferred density.

---

**R2. Framework gauge-layer realization — OPEN**

> “M″ is a proposed supplied model for rung 1, not a realization of a live law.” — [CN1MOD.md:171](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1MOD.md:171)

**Statement.** Supply R1’s physical hypotheses on one specified live law, one VC1 vacuum and one compatible ZM1-INV trajectory. Match actual matter representations, charges, node multiplicities and photon observables.

**Children:** PHI, MAP, TICK, CH, TRANS.  
**Imports:** PS-5, PS-6r, NN-a, ZM1-INV, VC1, R-CS\(^{\rm str}\), a specified plaquette update, Y2-W.

**Preferred route.** Work directly with the unitary tick. Derive its Gaussian comparison, vertices and invariant source RG. Control cell-scale terms through TICK and TRANS.

**First hard step:** PHI. A propagating invariant channel must become an identified photon in the actual vacuum.

**Second route.** Construct a reflection-positive Euclidean representation. Match its invariant correlations to the tick. Port the constructive gauge programme through that comparison.

**First hard step:** prove the transfer identification for the same unitary update.

> “no reading is adopted, and all four stay live” — [TOE_ASSEMBLY.md:269](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:269)

R-SUM and R-IA remain possible comparison branches. Their generator cannot silently replace the tick’s dynamics.

**Programmes:** L1–L3, L6–L8.  
**Smallest rung:** a fixed-register U(1) subsector with matter and a magnetic layer coupling adjacent cubes.

---

**PHI. Photon phase and vacuum — OPEN**

> “a magnetic quadratic form, not the full electric-plus-magnetic energy.” — [GA1_5.md:140](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GA1_5.md:140)

> “It has neither a Clifford cone nor a pair of photon polarizations.” — [GA15PHI.md:125](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GA15PHI.md:125)

**Statement.** Construct a non-character VC1 phase with nonzero transverse flux correlations. Prove two physical photon polarizations and
\[
|\lambda(K)|=c|K|+o(|K|),\qquad c>0.
\]
Prove compatibility with the chosen matter sector. Address the literal Clifford-band requirement separately through C-PH.

**Children:** none.  
**Imports:** GA1-P-5; NN-a; PS-6r; VC1; the selected generator branch if used; P6; N5–N6.

**Preferred route.** Port the Coulomb-phase programme for finite-spin U(1) systems. Use an explicit layer coupling cubes. Derive positive electric and magnetic stiffnesses. Control fluctuations and monopole effects in the chosen invariant state.

**First hard step:** obtain a uniform long-distance stiffness and transverse spectral estimate from finite-register operators.

**Second route.** Use a growing-register family as a comparison problem. Prove the harmonic photon limit with explicit register errors. Then prove that a fixed finite member retains the phase.

**First hard step:** estimates uniform in wavelength and register size. Taking the register limit first does not prove the fixed-register statement.

**Programmes:** L8, with L3 for a possible constructive control step.  
**Smallest rung:** two coupled cubes, followed by arbitrary-size periodic boxes. A finite-box oscillator calculation is the first check, not the phase theorem.

---

**MAP. Compatible invariant-algebra zoom — OPEN**

> “some even \(m_1\in\{2,4,6,8\}\)” — [KINV.md:41](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:41)

> “Compatibility across local supports and defect sectors remains to be constructed” — [ZM1INV.md:126](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:126)

**Statement.** Construct a faithful, unital, cell-covariant, exponentially local invariant-algebra embedding. Make the embeddings composable. Prove class-(a) comparison in the non-character photon vacuum.

The U branch with even fine register should first use an even coarse register. The O branch needs its own construction.

**Children:** none.  
**Imports:** R-form; ZM1-INV; class (a), \(p=2\); the actual vacuum; N3–N4.

**Preferred route.** Work with finite-region invariant algebras decomposed over boundary representation sectors. Construct compatible multiplicity embeddings on every sector. Keep defect sectors. Pass to the quasi-local limit.

**First hard step:** a globally unital extension that stays faithful on defect sectors and intertwines the specified rotations.

**Second route.** Seek equivariant maps of the ordered dimension data of the invariant inductive systems. Lift them to local algebra maps by controlled approximate intertwining.

**First hard step:** obtain spatial locality and exact covariance from that algebraic construction. Abstract embeddability would not suffice.

**Programmes:** L6 and L7. Their carriers differ from the framework’s finite quantum links.  
**Smallest rung:** \(m=m_1=2\), \(L=2\), on two overlapping coarse cells. Test the common boundary before attempting a full tower.

---

**TICK. Tick coefficients and decaying lattice errors — OPEN**

> “a source at every scale needs its own bound.” — [CN1.md:56](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:56)

**Statement.** Derive the velocity beta function from the actual ordered tick. Identify the continuum coefficients. Bound every additional marginal term. Prove summable forcing or the stronger consensus-vanishing remainder.

**Children:** none.  
**Imports:** the explicit gate order; free node projectors; PHI’s Gaussian comparison; CH’s matter census; exact gauge identities; N2.

**Preferred route.** Expand the ordered tick with a Gaussian photon. Derive both linear and quadratic gauge vertices. Prove the discrete Ward identity. Split each loop integral into node neighborhoods and their complement. Extract logarithms analytically. Bound the complement and lattice corrections.

**First hard step:** establish the vertex identity with all contact terms and Floquet branches included. Then show that omitted marginal coordinates cannot generate persistent \(O(G)\) relative forcing.

**Second route.** Derive a Euclidean effective action for the tick. Use a complete local operator classification. Match its logarithms to the continuum action through analytic remainder estimates.

**First hard step:** justify the Euclidean action and its continuation for the chosen tick. The summed gate generator is not automatically its conserved energy.

**Programmes:** L1 and L5; L2 for separating lattice corrections from continuum terms.  
**Smallest rung:** two free cube-tick species coupled to a supplied Gaussian U(1) field. The first deliverable is an analytic one-loop theorem.

---

**CH. Charged-sector dictionary — OPEN**

> “they need a separate bridge.” — [TOE_ASSEMBLY.md:255](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:255)

> “If no such sequence exists the construction supplies no sector.” — [RCS1.md:95](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/RCS1.md:95)

**Statement.** Construct the charged sectors used in H-CHARGED. Identify their charges, multiplicities and massless dynamics. Connect them to invariant observables across the zoom.

For the straight-string candidate, the states are
\[
\omega_r^{(x)}(A)=
\frac{\sum_b\omega(B_{r,b}^*AB_{r,b})}
{\sum_b\omega(B_{r,b}^*B_{r,b})}.
\]
Their denominators must remain positive along an unbounded sequence. The weak-* limits and their translated representations must supply the claimed sector.

**Children:** none.  
**Imports:** R-CS\(^{\rm str}\); relative parity \(\chi_{\rm tot}\); VC1; the actual gauge representation; N7.

**Preferred route.** Construct invariant current and pair channels first. Prove their charge labels through the Gauss action on endpoints. Establish their relation to the supplied string-sector limits.

**First hard step:** show that the same species appears in both constructions with nonzero spectral weight.

**Second route.** Investigate cone-supported dressings as candidate C-DRESS. Seek translation-covariant charged representations without a sharp transverse ray label.

**First hard step:** prove existence and covariance of the dressing limits. Dropping a sharp label does not construct a moving sector.

**Programmes:** L2’s observable RG and L6’s gauge-covariant operator-algebra organization. The dressing construction is an additional port obligation.  
**Smallest rung:** one charged species and its conjugate over a fluctuating U(1) vacuum.

---

**TRANS. Class-(a) comparison to spectral comparison — OPEN**

> “class (a) ‘does not by itself prove speed transfer’.” — [LZ1I.md:224](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LZ1I.md:224)

**Statement.** Prove the spectral-transfer estimate used by W3 from the actual invariant comparison. Cover continua, not just isolated branches. Control quasienergy aliases.

**Children:** none.  
**Imports:** H-a2; MAP; spectral regularity and weight bounds derived from the model; P5.

**Preferred route.** Derive long-distance asymptotics for invariant pair correlations. Recover threshold surfaces from their phases and singular powers. Compare those asymptotics using the relative envelope.

**First hard step:** prove that the leading asymptotics identify every relevant threshold. Spatial separation alone does not impose momentum support.

**Second route.** Obtain stronger source-dependent estimates directly from the RG. Prove convergence of smeared spectral measures with enough boundary regularity to control singular-support edges.

**First hard step:** uniform boundary-value control. Weak convergence of measures alone permits singularities to disappear.

**Programmes:** L2 and L7.  
**Smallest rung:** a free cube-tick pair continuum under \(L=2\) blocking. Include all folded pair branches. The single-particle alias check does not settle pair aliases.

---

**R3. Every light species — OPEN**

> “T2 is a restriction, not a proof of neutral-sector behavior.” — [CN1.md:48](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:48)

**Statement.** Prove the actual light-sector census. Extend common-cone agreement to each sector in that census. Include neutral composites and tensor modes. Do not remove them by definition.

**Children:** NA, NEUTRAL.  
**Imports:** R2; GA2; BK1; CH1; the actual mass and confinement scales; the gravity sector if present.

**Preferred route.** Derive the interaction graph and its scale-dependent positive contraction operator. Match through every change of effective field content.

**First hard step:** show that every surviving relative-speed mode receives sufficient accumulated contraction.

**Second route.** Derive a shared stress-tensor or soft-spin-2 identity for the full interacting sector. Use it to relate dispersion surfaces.

**First hard step:** construct the identity from the lattice dynamics without assuming the common metric it would imply.

**Programmes:** L1, L9 and L10.  
**Smallest rung:** add one neutral scalar with a specified Yukawa coupling to the completed U(1) rung.

---

**NA. Gauge factors, breaking and mass thresholds — OPEN**

> “H-NA asks for nonabelian drag and its termination at breaking or confinement.” — [CN1.md:60](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:60)

> “T0 is pure gauge.” — [TOE_ASSEMBLY.md:637](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:637)

**Statement.** Derive contraction for the actual gauge and matter content. Prove finite matching at mass, breaking and confinement thresholds. Identify which relative-speed modes continue to contract afterwards.

For a reversible positive interaction graph, a useful sufficient condition is a contraction coefficient \(\lambda_{\rm rel}(k)\) satisfying
\[
\sum_k\lambda_{\rm rel}(k)=\infty.
\]
The graph’s mere connectivity is insufficient. For nonreversible flows, prove a corresponding contraction of the evolution products.

**Children:** none.  
**Imports:** R2; P1; N8; group representations and couplings; GA2’s Y1–Y5 bridges; actual threshold matching.

**Preferred route.** Extend the star calculation to all gauge factors and charged multiplets. Track the relative kinetic tensors. Match gauge-invariant operators through each threshold.

**First hard step:** determine the surviving contraction after a species decouples or a factor confines. A finite interval of weak-coupling attraction leaves a residual difference.

**Second route.** Construct a common interacting critical theory for the combined sector. Prove that every relative metric perturbation is irrelevant, with uniform remainder control.

**First hard step:** establish the critical theory and its stability in the physical dimension. A one-loop expansion does not supply that theorem.

**Programmes:** L1, L5 and L9.  
**Smallest rung:** two fermion representations under one SU(2) factor, first above a specified mass threshold. Keep the finite matching error explicit.

---

**NEUTRAL. Neutral species and the graviton — OPEN**

> “Neutral sectors and gravitons need separate bridges.” — [CN1.md:58](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:58)

**Statement.** Tie each additional light neutral mode to the charged-sector cone. Tie both tensor polarizations to that cone. Establish the required physical identifications.

**Children:** none.  
**Imports:** the actual neutral census; actual interaction vertices; R2; GR’s tensor-sector construction; N1 and N8.

**Preferred route.** Derive neutral-to-charged speed exchange from an actual marginal interaction. A Yukawa-coupled scalar is the first model. Prove divergent accumulated drag where it occurs.

**First hard step:** distinguish a marginal coupling from an irrelevant polarizability or gravitational coupling. An interaction that becomes too weak can leave finite total drag.

**Second route.** Port the soft-spin-2 argument. Derive a closed Ward identity, external soft-pole factorization and a sufficiently rich connected scattering family. Include hard gravitons in the family. Then derive the common dispersion coefficient.

**First hard step:** obtain the closed Ward identity from the framework. Extra transforming background sources can invalidate that closure.

**Programmes:** L9 for the scalar route; L10 for the tensor route.  
**Smallest rung:** one neutral scalar coupled to the charged pair; separately, one tensor mode coupled to two unequal-speed test species.

---

**RATE. Additional LZ1 power rate — OPEN**

> “a power of \(k\), not \(O(L^{-\beta k})\)” — [CN1.md:105](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:105)

> “\(p\ge2\)” — [TOE_ASSEMBLY.md:387](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:387)

**Statement.** Derive the stronger physical-momentum suppression required by LZ1. Common-cone convergence alone does not establish it.

**Children:** none.  
**Imports:** W3; the full irrelevant-operator spectrum; tensor anisotropy control; N9.

**Preferred route.** Reach an interacting fixed point with a strictly positive scaling exponent for every relative metric perturbation. To obtain the stated LZ1 rate, establish an exponent at least two for the relevant correction, or a symmetry that removes slower terms.

**First hard step:** prove the fixed point and its exponents in the required model and dimension.

**Second route.** Derive an exact symmetry of the reconstructed theory that removes relative dimension-four kinetic terms. Then bound the leading symmetry-allowed irrelevant terms.

**First hard step:** derive the common spacetime action on every sector. Equal spatial and temporal graining does not provide it.

**Programmes:** L9; L5 and L7 for operator and reconstruction control.  
**Smallest rung:** one charged fermion and one scalar at a controlled critical point. A small-\(\epsilon\) calculation is a diagnostic rung.

---

**P1. Positive star-flow consensus — PROVED**

> “All speeds remain in \(B\); \(m\) increases and \(M\) decreases.” — [CN1.md:80](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:80)

**Source:** CN1, Theorems 1–2.

For finite \(n\), \(n_a>0\), \(q_a\ne0\), positive initial speeds and coupling, and positive locally Lipschitz \(P,R,S\),
\[
v_a'=Gq_a^2P(v_a,c)(c-v_a),\qquad
c'=G\sum_b n_bq_b^2R(v_b,c)(v_b-c),
\]
\[
G'=-G^2\sum_b n_bq_b^2S(v_b).
\]
The speeds converge to a common positive limit.

The displayed QED coefficients are
\[
P=\frac{4v^2+3vc+c^2}{6\pi^2c(v+c)^2},
\quad
R=\frac{v+c}{12\pi^2cv},
\quad
S=\frac1{6\pi^2v}.
\]
For an equal-charge pair, the stated smoothness hypotheses give
\[
|v_1-v_2|\sim C(1+\ell)^{-2q^2/W},
\qquad W=\sum_an_aq_a^2.
\]

**Children:** none.  
**Imports:** the stated ODE hypotheses. The identification of this ODE with a quantum model is not imported.

---

**P2. Robust star-flow consensus — PROVED**

> “every speed converges to the same positive limit.” — [CN1.md:125](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:125)

**Source:** CN1, Theorem 3, with its integrable-forcing amendment at line 135.

Assume
\[
|\rho_a|,|\rho_0|\le KG^2D+f,\qquad
|\rho_G|\le KG^3,
\]
the source’s regularity conditions, and its smallness condition
\[
KG_0\le S'/2,\qquad
\frac a2e^a(D(0)+2F)+F\le m(0)/2,
\]
where \(a=4KG_0/S'\) and \(F=\int_0^\infty f\).

Integrable \(f\) gives convergence. Exponential forcing gives the stated power in RG time. The sharp pair exponent requires the additional exchange-remainder hypothesis.

**Children:** none.  
**Imports:** P1; \(\mathcal R\); Sm; the amendment’s integrability and regularity conditions.

---

**P3. UB″ implies discrete pair contraction — PROVED**

> “The theorem proves only UB″ ⇒ R1″-MOD[d].” — [CN1MOD.md:110](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1MOD.md:110)

**Source:** CN1MOD, Theorem 3.

Under U0–U5 and the theorem’s smallness inequalities,
\[
|v_{1,k}-v_{2,k}|
\le C(1+G_0k)^{-\gamma}|v_{1,0}-v_{2,0}|,
\]
uniformly in the mass cutoff.

U0 controls other exchange-odd data initially. U1 is exchange covariance. U2 is the uniform holomorphic remainder bound. U3 contracts the other odd coordinates. U4 controls the running coupling. U5 supplies the positive speed box.

**Children:** none.  
**Imports:** U0–U5; CN1MOD’s coordinate norm and exchange involution; its explicit smallness conditions. UB″ itself remains RG’s stronger alternative target.

---

**P4. Free invariant current threshold — PROVED**

> “Its singular-support speed set in \(W(\kappa)\) is \(\{v\}\).” — [CN1.md:151](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:151)

**Source:** CN1, Proposition 5, with its positivity amendment.

For the free massless Dirac current in the positive-energy vacuum,
\[
\rho^{00}(\lambda,K)=C_v|K|^2\mathbf1_{\lambda\ge v|K|},
\qquad C_v>0.
\]

**Children:** none.  
**Imports:** free continuum Dirac theory; the nonzero pair matrix element; the unsmeared distributional current. Smearing needs a separate nonvanishing condition.

---

**P5. Conditional isolated-band speed transfer — PROVED**

> “only ‘along every ray of’ a closed cone \(\Gamma\)” — [CN1.md:52](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:52)

**Source:** LZ1I, Theorem 10′.

Under RC-Z’s summability, Fourier representation, band-limited error, finite-branch and nonzero isolated-weight hypotheses, the speed transfers as
\[
v\longmapsto \frac{M}{L'}v.
\]
For equal spatial and temporal scaling, the split is preserved.

**Children:** none.  
**Imports:** RC-Z0–Z4. This does not import H-a2 as a substitute for those hypotheses.

---

**P6. Finite implementation of the proposed gauge-layer class — PROVED**

> “Every member of GA1-P-5, on either law” — [GA1_5.md:264](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GA1_5.md:264)

**Source:** GA1_5, Proposition C.

The stated members admit the finite edge-layer implementation. This supplies the implementation input once a member is specified.

**Children:** none.  
**Imports:** GA1-P-5’s definitions and compilation hypotheses; NN-a. It supplies no vacuum or photon identification.

---

**N1. Symmetry or admissibility forces equal speeds — REFUTED**

> “two exactly decoupled neutral bands with unequal speeds.” — [CN1.md:52](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:52)

**Source:** LZ1I, Theorems 7–9.

**Exact blocking hypothesis:** the allowed update class contains the constructed decoupled neutral sectors.

**Surviving variant:** common-cone attraction for a specified interacting sector with derived accumulated drag.

**Weakest escape:** prove that the actual law and vacuum do not realize the decoupled witness. No axiom change is needed for that distinction. A law asserting that every sector already has divergent drag would insert W3’s mechanism.

**Children:** NA, NEUTRAL.  
**Imports:** the witness’s update, state and band hypotheses.

---

**N2. An unrestricted \(O(G)\) source preserves consensus — REFUTED**

> “Then \(\Delta\to\sigma/(q^2P_\infty)\).” — [CN1.md:137](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:137)

**Source:** CN1, Proposition 4.

**Exact blocking hypothesis:** persistent signed forcing \(\sigma G\), with \(\sigma\ne0\).

**Surviving variant:** summable absolute forcing, or the stronger consensus-vanishing remainder.

**Weakest escape:** prove an \(O(G^2)\) absolute bound or a decaying lattice factor. A finite initial offset needs no escape; it is initial data.

**Children:** RG, TICK.  
**Imports:** divergent gauge time and positive limiting drag.

---

**N3. Odd coarse register under the specified rotations — REFUTED**

> “no unital \(*\)-homomorphism” — [KINV.md:37](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:37)

**Source:** KINV, Theorem 2 and Corollary 2.1.

**Exact blocking hypotheses:** even fine U register or O; odd coarse U register; unitality; the specified end-exchanging rotation covariance. Injectivity and locality are not needed.

**Surviving variant:** an even coarse register. Odd fine U registers are outside this theorem’s stated scope.

**Weakest escape:** test an already allowed even \(m_1\). Changing the rotation lift is a larger candidate reading change.

**Children:** MAP.  
**Imports:** the locked fine character and integer coarse end-number spectrum.

---

**N4. Repair a good-sector map with a character filler — REFUTED**

> “no character \(\chi\) satisfies \(\Phi(a)E=\chi(a)E\)” — [KINV.md:63](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:63)

**Source:** KINV, Theorem 5, R-NGF and Corollary 5.1.

**Exact blocking hypotheses:** injectivity, uniform exponential locality and a nonzero defect projection on which the image acts as a character.

**Surviving variant:** a faithful extension with nontrivial action on defect sectors.

**Weakest escape:** change the construction on the defect sectors. Dropping unitality does not evade R-NGF.

> “Neither result excludes invariant-only maps without a full-algebra charge-equivariant extension.” — [KINV.md:91](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:91)

KINV Theorem 6 also blocks the specified full-algebra charge-equivariant decimation. The owner’s invariant-only map leaves that extension unrequired.

**Children:** MAP.  
**Imports:** uniform locality; the specified projection or class-J extension.

---

**N5. Single-tiling cube gates propagate a photon in empty matter — REFUTED**

> “every physical band of an empty-matter D1 state is \(V=1\)” — [GA1_5.md:160](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GA1_5.md:160)

**Source:** GA1_5, Theorem 6.2.

**Exact blocking hypotheses:** empty-matter D1 state and every added link gate supported within one tiling cube.

**Surviving variant:** a specified update coupling cubes, or a different vacuum where the reduction does not apply.

**Weakest escape:** remove one of those two restrictions. A cube-coupling layer must still satisfy NN-a and complete-update covariance.

**Children:** PHI.  
**Imports:** the empty-matter reduction and cube-support condition.

---

**N6. R-Φ membership identifies the photon — REFUTED**

> “R-Φ is not invariant under these admissible conjugations.” — [GA15PHI.md:121](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GA15PHI.md:121)

**Source:** GA15PHI, Theorem 7 and Corollary 7.1.

**Exact blocking hypothesis:** identify a photon solely by orthogonality to the chosen neutral algebra.

**Surviving variant:** a physical flux-correlation criterion with transverse polarizations and spectral weight.

**Weakest escape:** change the identification criterion. No gate modification is required to expose the distinction.

> “In a character state \(H_{\rm phys}=\mathbb C\Omega\).” — [ZM1INV.md:52](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:52)

ZM1INV Theorem 2.2 also prevents a zero-correlation character benchmark from supplying a nontrivial photon sector.

**Children:** PHI, OBS.  
**Imports:** admissible conjugation; the character-state hypothesis for the second obstruction.

---

**N7. A sharp transverse straight-string label permits a Clifford node — REFUTED**

> “no update gives a Clifford node on spinor-class straight-string sectors whose transverse position is observable” — [RCS1.md:14](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/RCS1.md:14)

**Source:** the frozen RCSPC Theorem 1 imported by RCS1 Amendment 3.

**Exact blocking hypothesis:** observable conserved transverse position of the straight-string sector.

**Surviving variant:** a charged construction without that sharp transverse label, subject to the remaining sector and covariance requirements.

**Weakest escape:** change the dressing or background so the separating label is absent. This is a candidate representation change, not evidence for a moving charged mode.

**Children:** CH.  
**Imports:** the amended theorem’s sector class and transverse-label condition.

---

**N8. Nonzero interactions or finite drag force exact agreement — REFUTED**

> “exactly when it starts at zero or the integral diverges.” — [LZ1I.md:184](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LZ1I.md:184)

**Source:** LZ1I, Theorem 11.

For
\[
\Delta'=-(a+b)\Delta,\qquad a,b\ge0,
\]
\[
\Delta(\ell)=\Delta(0)e^{-\int_0^\ell(a+b)\,ds}.
\]

**Exact blocking hypothesis:** nonzero initial difference and finite integrated drag.

**Surviving variant:** derive divergent drag, or derive an independent exact relation between dispersion coefficients.

**Weakest escape:** keep the relevant interaction active sufficiently far into the infrared. Assuming that outcome as a law would fail the target and downstream tests.

**Children:** NA, NEUTRAL.  
**Imports:** the two-sector drag equations.

---

**N9. Fixed bare-coupling analyticity or logarithmic attraction supplies the stronger target — REFUTED**

> “uniformly bounded holomorphic observable or coordinate on a fixed disc” — [CN1MOD.md:130](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1MOD.md:130)

**Source:** CN1MOD, Corollary 4″.

**Exact blocking hypotheses:** a fixed bare-coupling disc, uniform bounds, and the stated normalization at zero coupling.

**Surviving variant:** real-axis estimates, suitable scale-dependent domains, or a justified tangent-domain construction.

**Weakest escape:** relax the fixed-disc proof requirement. No physical law change is needed.

> “not \(O((a_{\rm lat}|k|)^p)\) for any \(p>0\)” — [LZ1I.md:188](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LZ1I.md:188)

**Source:** LZ1I, Theorem 12.

**Exact blocking hypotheses:** nonzero initial difference and marginal drag proportional to \((1+W\kappa_0\ell)^{-1}\).

**Surviving variant:** logarithmic common-cone convergence. A physical-momentum power needs an additional mechanism.

**Children:** RG, RATE.  
**Imports:** the stated analytic normalization or marginal-flow law.

---

**Candidate specifications attached to the tree**

> “It states or fixes something that a part lists as its target.” — [TOE_ASSEMBLY.md:173](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:173)

> “It settles a downstream physics question by premise.” — [TOE_ASSEMBLY.md:175](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:175)

The four columns test target insertion, open-endedness, downstream insertion and unnecessary structure. `C` means the stated qualification must be resolved. None is adopted.

| Candidate | 1 | 2 | 3 | 4 | Disposition |
|---|---:|---:|---:|---:|---|
| **C-OBS:** use the explicitly defined static-subtracted singular-support set | P | P | P | C | A measurement convention. Its coverage and stability remain OBS and TRANS. |
| **C-PH:** replace the literal photon Clifford-node input by nonzero transverse conical spectral weight | P | P | P | P | Acceptable as a conditional CN1 hypothesis. It becomes F on tests 1 and 3 if adopted as an axiom guaranteeing GA1’s photon. |
| **C-T2:** exclude all extra neutral light species | F | P | F | P | Reject as a law or an all-species reading. Keep only as the explicit scope of a conditional theorem. |
| **C-W:** demand summable RG errors as a physical law | F | P | F | P | Reject. Estimate (W) is a proof obligation. |
| **C-DRAG:** require divergent integrated drag for every species | F | P | F | P | Reject. NA and NEUTRAL must derive it where applicable. |
| **C-EVEN:** first test an allowed even coarse register | P | P | P | P | A test-case selection inside R-form. It proves no map. |
| **C-DRESS:** use a fully quantified family of cone-supported dressing limits | P | C | C | C | Specify the family, normalization, covariance and parity meaning before use. Prove its relation to physical species. |
| **C-MAG:** add a particular finite cube-coupling gate list | P | C | P | C | Four-test the actual list. “Add whatever produces a photon” fails tests 1 and 2. |
| **C-REG:** use a photon mass solely as a removable proof regulator | P | P | P | P | Its removal and Ward correction are LIMIT and RG obligations. |
| **C-GEN:** identify the summed gate generator with tick energy | P | P | C | C | Needs a dynamical identification. The existing SMG1 convention does not provide one for CN1. |

> “Scope: SMG1’s rungs only, not every TOE gap.” — [TOE_ASSEMBLY.md:261](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:261)

> “CN1-OBS needs only \(|\lambda|=c|K|+o(|K|)\)” — [CN1.md:195](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1.md:195)

C-PH addresses a real representation issue. A positive-frequency photon branch need not be \(C^1\) at its conical vertex. That issue should be specified before attempting a Clifford-band construction.

---

**Literature imports and ports**

The entries are programmes to extend. Their hypotheses must be checked on the proposed rung. They are not framework theorems.

`FROM MEMORY` flags citations not checked against the supplied corpus at the stated equation or theorem. For those entries, the primary online text was checked for the locator.

| ID | Programme and locator | Port and limit |
|---|---|---|
| **L1** | Isobe–Nagaosa, 2012, [arXiv:1205.2427](https://arxiv.org/abs/1205.2427), Eqs. (9)–(11). Anber–Donoghue, 2011, [arXiv:1102.0789](https://arxiv.org/html/1102.0789), Eqs. (54), (57). | Coupled velocity flow and logarithmic attraction. The corpus records “Eqs. (9)-(11) are the one-loop flows” and “The differences normally vanish only logarithmically.” — [CN1_OUTLINE.md:51](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1_OUTLINE.md:51), [CN1_OUTLINE.md:52](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1_OUTLINE.md:52). |
| **L2** | Giuliani–Mastropietro–Porta, 2012, [arXiv:1107.4741](https://arxiv.org/html/1107.4741), Eqs. (4.32), (5.12). **FROM MEMORY** for these locators. | Lattice source RG, Ward identities and velocity flow. The factorial coefficient bound does not establish summability. Its planar fermions also differ from M″’s bulk fermions. |
| **L3** | Dimock, 2017 preprint, revised 2020, [arXiv:1712.10029](https://arxiv.org/pdf/1712.10029), Lemmas 5–6, Eqs. (94)–(95), Theorem 1. **FROM MEMORY.** | Background-field propagators, local inverses and gauge regularity. Port from three Euclidean dimensions to four. Recheck the marginal estimates. |
| **L4** | Bauerschmidt–Brydges–Slade, 2015, [arXiv:1211.2477](https://arxiv.org/html/1211.2477), Theorem 1.4 and Corollary 1.8. **FROM MEMORY.** | Stability of a nonhyperbolic RG flow under quantified perturbations. Its triangular structure and derivative bounds must be re-established for the velocity system. |
| **L5** | Kostelecký–Lane–Pickering, 2002, [arXiv:hep-th/0111123](https://arxiv.org/abs/hep-th/0111123), beta display following Eq. (27), solution Eq. (34). | Tensor-valued relative kinetic deformations. The corpus identifies “the running solution Eq. (34)”. — [CN1_OUTLINE.md:50](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CN1_OUTLINE.md:50). |
| **L6** | Brothier–Stottmeister, 2019, [arXiv:1901.04940](https://arxiv.org/pdf/1901.04940), Eq. (2.1), Lemma 2.1, Proposition 2.9. **FROM MEMORY.** | Gauge-covariant algebra refinement. The construction uses a different carrier and dimension. It supplies a design pattern for MAP. |
| **L7** | Morinelli–Morsella–Stottmeister–Tanimoto, 2021, [arXiv:2010.11121](https://arxiv.org/pdf/2010.11121), Theorem 4.7, Proposition 4.8, Corollary 4.9. **FROM MEMORY.** | Coherent scaling maps and convergence of free dynamics. Neither finite-link gauge refinement nor class-(a) threshold transfer follows directly. |
| **L8** | Hermele–Fisher–Balents, 2004, [arXiv:cond-mat/0305401](https://arxiv.org/pdf/cond-mat/0305401), Eqs. (42), (44), (48). **FROM MEMORY** for these locators. | Finite-spin Coulomb-phase and Maxwell effective-action programme. The RK-point quadratic dispersion must be distinguished from a linear photon phase. Numerical phase evidence is not used as proof here. |
| **L9** | Roy–Juričić–Herbut, 2016, [arXiv:1510.07650](https://arxiv.org/html/1510.07650), action Eq. (2), velocity analysis §§3–4. **FROM MEMORY** for the locator. | Gauge–Yukawa velocity attraction and critical-point alternatives. The calculation is a one-loop \(\epsilon\)-expansion. |
| **L10** | Hertzberg–Sandora, 2017, [arXiv:1704.05071](https://arxiv.org/html/1704.05071), Eqs. (23)–(28). **FROM MEMORY** for these locators. | Soft-spin-2 dispersion universality. A framework port must derive the closed Ward identity, scattering assumptions and hard-graviton participation. |

---

**Ranking of open leaves**

The ranking weighs wall movement against the chance of a useful analytic result. “Likelihood” refers to the smallest stated rung. It does not predict completion of the full leaf.

| Rank | Leaf | Movement on success | Likelihood at the first rung |
|---:|---|---|---|
| **1** | **RG** | Replaces conditional flow dynamics by exact model estimates. The weaker summable-error gate could remove unnecessary sharp-rate obligations. | Moderate for a block-operator lemma. Low for full uniform iteration. |
| **2** | **TRANS** | Establishes the observable meaning of the owner’s zoom, or finds a concrete failure of the proposed spectral inference. | High for a decisive free pair-continuum result. |
| **3** | **TICK** | Connects the established continuum mechanism to the actual discrete-time vertices. | Moderately high for an analytic Gaussian one-loop theorem. |
| 4 | LIMIT | Upgrades pair contraction to photon-inclusive consensus and a massless theory. | High for the abstract discrete comparison. Low for regulator removal. |
| 5 | OBS | Converts running parameters into physical cone claims. | Moderate for the first interacting current calculation. Low for all-observable control. |
| 6 | MAP | Supplies a prerequisite of every framework zoom branch. | Moderate for a local compatibility obstruction or construction. Low for the full tower. |
| 7 | PHI | Supplies the missing physical carrier of the mechanism. | Moderate for a finite-block stiffness lemma. Low for the infinite-volume phase. |
| 8 | CH | Makes the charged species and their observable dictionary concrete. | Low to moderate for a specified fluctuating U(1) background. |
| 9 | NA | Extends the mechanism across gauge factors and thresholds. | Moderate for a perturbative interval. Low for confinement matching. |
| 10 | NEUTRAL | Determines whether the result reaches the graviton and all remaining species. | Moderate for a Yukawa toy. Low for the native spin-2 identity. |
| 11 | RATE | Addresses LZ1’s stronger suppression requirement. | Moderate for a controlled critical-point diagnostic. Low for the framework’s \(p\ge2\) theorem. |

---

**Lane brief 1 — RG: exact errors sufficient for convergence**

Take M″ with two unit-charge Wilson species and unequal positive speeds. Keep the photon. Target one exact blocking step and a real invariant domain supporting estimate (W). Begin with a uniform inverse and decay bound for \(D_v(A)+aQ_A^*Q_A\). Include compatible gauge transitions. Track every marginal coordinate that can source speed differences.

Port L3’s local inverse construction and L4’s perturbation control. Keep UB″ open as the stronger alternative.

Stop with a proof or a counterexample. Otherwise stop at the precise block-operator or stability lemma after three named attacks fail: **local axial-gauge resolvent expansion**, **covariant random-walk expansion**, and **finite-range polymer localization**. Record the failure of each attack analytically. Do not replace uniform estimates by finite-volume numerics.

---

**Lane brief 2 — TRANS: the free cube-tick pair continuum**

Fix the free cube tick, its stationary sea, \(L=2\), and explicit local invariant bilinears. Derive the pair spectral measures analytically. Include every folded quasienergy branch. Determine which singular surfaces survive the observable form factors.

Then test whether the actual class-(a) bound forces the intended threshold comparison. Keep the isolated-band theorem as an input.

Stop with a transfer proof or an explicit counterexample. Otherwise stop at the threshold-recovery lemma after three named attacks fail: **stationary-phase recovery**, **positive-measure Fourier localization**, and **direct folded-branch decomposition**. The deliverable must identify the missing regularity or visibility hypothesis. Any proposed strengthening of the observable reading receives the four tests.

---

**Lane brief 3 — TICK: derive the gauge logarithm from the ordered update**

Fix two cube-tick fermion species and a supplied Gaussian U(1) photon. Derive the exact linear and quadratic gauge vertices. Prove the tick Ward identity. Compute the logarithmic self-energy and polarization terms by analytic integration. Keep node multiplicities and Floquet aliases explicit.

Compare the result with P1’s coefficients. Separate initial matching offsets from forcing repeated at every scale.

Stop with a coefficient-and-remainder theorem or an analytic mismatch. Otherwise stop at the vertex or remainder lemma after three named attacks fail: **direct ordered-gate expansion**, **discrete Ward-identity reduction**, and **Euclidean small-step comparison**. A one-loop result advances TICK. It does not establish RG, PHI or OBS.