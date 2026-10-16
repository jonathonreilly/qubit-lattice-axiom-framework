# Conditional scalar reconstruction from identified observation channels

The result is a local inverse formula, a deterministic error bound, and explicit
families illustrating which action and boundary data remain free. It supplies
no empirical action selection, absolute scalar normalization, initial state, or
new observation. The intended consumer is the campaign's common-action test
across independently calibrated environments, followed by a coupled response
calculation with the action held fixed.

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "focus on deriving the remaining assumptions rather than supplying them"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: "Local inverse and error bounds under the explicitly stated metric, action and measurement hypotheses."
hypothetical_axiom_status: "Candidate action class and example material action are premises; neither is promoted to an axiom."
admitted_observation_status: "No new empirical data admitted; examples and perturbations are synthetic mathematical controls."
claim_type_reason: "The conclusions have explicit local-domain, channel-identification and input-envelope hypotheses."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Derive coupled material, metric and scalar response at fixed action parameters and identify a realizable forcing/readout."
```

## Exact claim and obligations

**Target.** Within the action and chart below, compatible ideal clock, radial
timing and circular-motion functions determine the relative scalar profile by
the displayed integral; its pullback to a common observation label obeys the
displayed joint-input bound and weighted radar-bin lower bound.

| Obligation | Disposition and dependency |
|---|---|
| Metric field equations and angular-minus-time transport | Derived below from the stated action; an imported physical class |
| Local vacuum action reconstruction | Derived below, conditional on nonzero transport and scalar slope |
| Relative-profile integration | Proved algebraically from transport |
| Physical identification of clocks, timing, orbits and radius | Ideal relations derived below; identification with actual records remains open |
| Shared-label pullback | Proved from the relative profile and the chain rule |
| Joint-input error bound | Proved by log bounds and rational-function derivative envelopes |
| Radar-bin lower bound | Proved by weighted Cauchy–Schwarz, including the equality case |
| Common-action agreement | Conditional consistency on actual overlapping field ranges; overlap itself remains open |
| Sourced, regular-center and spherical-domain examples | Exact constructions below, with additional explicit premises |
| Action, state, scale and environment selection from observations | Open; none of the preceding lemmas is equivalent to this target |

The strongest missing physical lemma is an independently calibrated map from
actual environmental forcing and readout to a response that distinguishes the
remaining action and normalization parameters with all couplings held fixed.
Even that lemma would leave initial-state/history and broader action-class
selection questions. This is support for that problem, not a reduction claiming
that its remaining step is easier than the original target.

## Imported premises and provenance

| Input | Role | Provenance | Open bridge |
|---|---|---|---|
| Local single-scalar, universal metric coupling, two-derivative action | Candidate physical class | Explicit choice below; standard scalar-tensor reconstruction class | Derive or discriminate the class observationally |
| Static spherical metric, vacuum or stated dust region | Domain restriction | Chosen mathematical problem | Actual environment, exterior and time dependence |
| Physical areal radius, clock comparison, radial timing and circular motion | Measurement identification | Ideal geodesic/clock calculation below | Instrument/source/medium calibration and aligned records |
| Positive input envelopes and derivative-error certificates | Deterministic mathematical hypotheses | Supplied for the theorem, analytic only in synthetic controls | Obtain valid certificates from measurements |
| Dust action, state and round-sphere continuation in examples | Candidate material/domain premises | Chosen explicitly here | Matter realization, preparation and global evidence |
| Differential geometry, integrating factors, mean-value bounds and Cauchy–Schwarz | Mathematical tools | Used with derivations below | No new physical premise attributed to these tools |
| Normalizations, scales and potential coefficients | Free parameters | Reconstructed or stipulated, never fitted here | Independent determination |

Single-metric inverse reconstruction is prior art: Bronnikov, Badalov and
Ibadov, [arXiv:2212.04544v1](https://arxiv.org/abs/2212.04544v1), section 2,
equations (12)–(14). This note derives its own conventions and emphasizes
observation inputs, error propagation and cross-environment compatibility. No
novelty claim is made for reconstructing an action from one prescribed metric.

## Field equations and local inverse

Use signature −+++ and natural units in the field equations. Let

\[
 S=\int\!\sqrt{-g}\,[FR/2-Z(F)(\partial F)^2/2-V(F)]\,d^4x+S_m[g,\psi],
 \qquad Z(F)=\omega(F)/F.
\]

Here the curvature scalar is denoted \(\mathcal R\) below to distinguish it
from a clock ratio. Variation gives

\[
 FG_{\mu\nu}=T_{\mu\nu}+Z\partial_\mu F\partial_\nu F
 -\tfrac12Z(\partial F)^2g_{\mu\nu}-Vg_{\mu\nu}
 +\nabla_\mu\nabla_\nu F-g_{\mu\nu}\Box F,
\]
\[
 \mathcal R/2+Z\Box F+Z_F(\partial F)^2/2-V_F=0.
\]

On a connected vacuum annulus, take \(r>0\), smooth positive \(N,B,F\),
\(ds^2=-N^2dt^2+dr^2/B+r^2d\Omega^2\), and \(\ell=\log N\).
Use \(G_t,G_r,G_a\) for the diagonal mixed Einstein components:

\[
 G_t=(B-1)/r^2+B'/r,\quad G_r=(B-1)/r^2+2B\ell'/r,
\]
\[
 G_a=B(\ell''+\ell'^2+\ell'/r)+\tfrac12B'(\ell'+1/r).
\]

The mixed scalar Hessian entries are
\((B\ell'F',BF''+B'F'/2,BF'/r,BF'/r)\). Their sum is
\(\Box F=BF''+(B'/2+B\ell'+2B/r)F'\).
Angular minus temporal field equations therefore give

\[
 F a=dF',\qquad a=G_a-G_t,\quad d=B(1/r-\ell').
\]

On a chart with \(d\ne0\) and \(u=a/d\ne0\), set

\[
 x'=u,\quad F=Ce^x,\quad
 H=G_r-G_t-B(u'+u^2)-(B'/2-B\ell')u,
\]
\[
 W=-G_t-H/2-B(u'+u^2)-(B'/2+2B/r)u.
\]

The radial-minus-temporal and temporal equations yield
\(\omega(F(r))=H/(Bu^2)\) and \(V(F(r))/F(r)=W\).
Nonzero \(u\) makes \(F\) locally invertible, so these are local action
functions. Substitution satisfies all metric equations. Their divergence,
with conserved matter, gives \(F'\) times the scalar equation; it vanishes
on this chart. The runner also substitutes into the scalar equation directly.
Positive \(2\omega+3\) is only the Einstein-frame kinetic-sign condition;
it does not establish nonlinear stability or an acceptable exterior.

For environments with actual overlapping field values, define
\(\gamma_i(x)=(\omega_i(x),W_i(x))\). A common action requires
\(\gamma_1(x)=\gamma_2(x+\delta)\), where
\(\delta=\log(C_1/C_2)\). There is no independent vertical rescaling of
\(W=V/F\). Separate metric profiles do not themselves fix this registration.

A concrete local construction uses \(N=1,B=b\),
\(c=(1-b)/b\), \(F=Cr^c\),
\(\omega=(1-c)/c\), and
\(V=-bc(c+1)C^{2/c}F^{1-2/c}/2\).
For \(1<r<2\), the choices \((b,C)=(1/2,1)\) and \((1/3,4)\)
give field ranges \((1,2)\) and \((4,16)\), respectively. A smooth
step \(\chi(F)\) equal to zero for \(F\le2\) and one for \(F\ge4\)
joins their restrictions through
\(\omega=-\chi/2\), \(V=-(1-\chi)/(2F)-4\chi\), with
\(2\omega+3\ge2\). This is a local common-action existence witness on
disjoint intervals, not a global solution or a symmetry changing \(C\)
inside an already fixed action.

## From ideal channels to relative field

Put \(y=1/r-\ell'\), with nonzero fixed sign. Algebraically,

\[
 u=-y'/y-2/r-\ell'-B'/(2B)+1/(Byr^2).
\]

Integration gives
\[
 \log(F/F_0)=-\log|y/y_0|-2\log(r/r_0)-\log(N/N_0)
 -\tfrac12\log(B/B_0)+\int_{r_0}^r\frac{dt}{B(t)y(t)t^2}.
\]

For identical static clocks, let \(R=N/N_0\) be the ratio of received
frequency at \(r_0\) to emitted frequency at \(r\). Let
\(\rho=c\tau_{\rm roundtrip}/2\), referenced to the clock at \(r_0\),
and \(S=d\rho/dr\). The radial null equation gives
\(S=1/(R\sqrt B)\). A circular timelike geodesic has angular rate
\(\Omega_0\) per reference proper time, satisfying
\(\Omega_0^2/c^2=RR'/r\). Thus
\(v^2=r^2\Omega_0^2/(c^2R^2)=r\ell'\), with \(0\le v^2<1\).
Orbit stability is an additional question. Clock and orbit data must satisfy
\(\log(R/R_0)=\int v^2dr/r\); constructing one from the other does not
constitute an independent test.

These substitutions give

\[
 \frac F{F_0}=\frac S{S_0}\frac{r_0}{r}
 \frac{1-v_0^2}{1-v^2}
 \exp\!\int_{r_0}^r\frac{R^2S^2}{t(1-v^2)}\,dt.
\]

The clock assumption matters: for an ideal static coherent turnaround with
ratio \(k_t\), the uplink frequency scales as \(1/R\), and the downlink
scales as \(R\); the returned-to-emitted carrier ratio is \(k_t\).
It is not an independent remote-clock ratio. Actual moving coherent links can
still measure timing and dynamics; the static cancellation proves nothing
about their full information content. The metrics \(N=r^p,B=r^{-2p}\),
reference \(r_0=1\), \(0<p<1\), have \(S=1\) while their clocks and
circular rates vary. This is a kinematic illustration only, with no assertion
of a shared healthy scalar action for that family.

No identification \(G_{\rm measured}=1/F\) has been made.

## Shared-label functional and certified input error

Let the aligned observation label be \(z\), with
\(q=dr/dz>0\), \(P=d\rho/dz>0\), and
\(D=R^2-r^2\Omega_0^2/c^2>0\). Then

\[
 L:=\log(F/F_0)=E(z)-E(z_0)+\int_{z_0}^zJ\,dz,\quad
 E=\log P-\log q-\log r-\log D+2\log R,
\]
\[
 J=\frac{R^4P^2}{qrD}.
\]

This follows from \(S=P/q\), \(1-v^2=D/R^2\) and \(dr=qdz\).
Under a common relabeling with strictly positive derivative \(h=dz/d\tilde z\),
\(P,q\) multiply by \(h\); \(E\) is unchanged and \(J\) multiplies
by \(h\). Independent relabeling or uncertain record alignment is not covered.

Consider two candidate input tuples on the same label interval. Both obey
common positive lower envelopes \(r_*,R_*,q_*,P_*,D_*\), upper envelopes
\(r^*,R^*,|\Omega_0|\le O^*,P^*\), and uniform difference bounds
\(e_r,e_R,e_O,e_q,e_P\). Set

\[
 e_D=2R^*e_R+2r^*(O^*)^2e_r/c^2+2(r^*)^2O^*e_O/c^2,
\]
\[
 K_R=\frac{4(R^*)^3(P^*)^2}{q_*r_*D_*},\quad
 K_P=\frac{2(R^*)^4P^*}{q_*r_*D_*},\quad
 K_q=\frac{(R^*)^4(P^*)^2}{q_*^2r_*D_*},
\]
\[
 K_r=\frac{(R^*)^4(P^*)^2}{q_*r_*^2D_*},\qquad
 K_D=\frac{(R^*)^4(P^*)^2}{q_*r_*D_*^2}.
\]

Then
\[
 |\Delta L|\le\frac{2e_P}{P_*}+\frac{2e_q}{q_*}+\frac{2e_r}{r_*}
 +\frac{2e_D}{D_*}+\frac{4e_R}{R_*}
 +|z-z_0|(K_Re_R+K_Pe_P+K_qe_q+K_re_r+K_De_D).
\]

To prove it, telescope \(R^2-r^2\Omega_0^2/c^2\) and use
\(|a^2-b^2|\le2\max(|a|,|b|)|a-b|\), obtaining \(e_D\).
Apply \(|\log a-\log b|\le|a-b|/\min(a,b)\) at both endpoints.
For the integral, regard \(J(R,P,q,r,D)\) as a rational function on the
positive enclosing rectangle. Its five partial derivatives are bounded by the
displayed \(K\)'s. Telescope along coordinate directions, then integrate.
The rectangle argument does not require these intervening tuples to solve the
field equations. In particular, the same clock variable contributes both
directly and through \(D\); dropping either contribution is unjustified.

This is a deterministic bound, with no independence assumption or statistical
coverage. Differentiation error, radius calibration and alignment certificates
are required inputs, not quantities inferred from smoothness alone. The
functional bound also applies to off-shell tuples; only compatible identified
channels inherit the physical scalar interpretation.

## Information retained by finite radar bins

For known positive \(w=R^2/[r(1-v^2)]\), define on each bin
\(I=\int wS^2dr\), \(\Delta\rho=\int Sdr\), \(H=\int dr/w\).
Cauchy–Schwarz applied to \(\sqrt w S\) and \(1/\sqrt w\) gives

\[
 I\ge(\Delta\rho)^2/H,
 \qquad S=\Delta\rho/(Hw)\quad\hbox{at equality}.
\]

Summing gives a lower bound across bins. Splitting a bin into \((x,h)\)
and \((y,k)\) increases the bound by
\((kx-hy)^2/[hk(h+k)]\). With certified uncertain positive increments
and upper \(H\) bounds, a valid bound is
\(\sum_i\max(0,\Delta\rho_i^-)^2/H_i^+\).
The endpoint factors \(S/S_0\) and \((1-v_0^2)/(1-v^2)\) remain in
the full relative-field formula.

For \(R=1,\Omega_0=0\), \(w=1/r\), this is
\(I\ge2(\Delta\rho)^2/(b^2-a^2)\), with equality \(S\propto r\).
A separate existence witness describes finite sampling: choose a positive
smooth baseline \(S_0\), equal to one near endpoints, of area \(b-a-A\),
and add \((A/\epsilon)\psi((r-r_c)/\epsilon)\) inside one unsampled bin.
Here \(\psi\ge0\) is smooth, normalized and supported strictly inside
\((-1/2,1/2)\). All bin increments and endpoint slopes stay fixed, while
\(I\ge w_{\min}A^2\int\psi^2/\epsilon\). These are smooth positive
observation functions; no claim is made that every such function comes from
a common healthy action. This explicit family does not quantify over all
measurement systems or all possible added physical constraints.

## Known sources, regular centers and a distinct global-domain premise

For a known conserved static stress \(T^\mu{}_{\nu}=\operatorname{diag}
(-\rho,p_r,p_t,p_t)\), angular minus temporal equations give
\(Fa=(\rho+p_t)+dF'\). Thus, for \(M=\exp\int a/d\,dr\),

\[
 F=M\left[F_0-\int\frac{\rho+p_t}{dM}\,dr\right].
\]

The remaining equations reconstruct
\[
 K:=ZBF'^2=F(G_r-G_t)-(\rho+p_r)-BF''-(B'/2-B\ell')F',
\]
\[
 V=-FG_t-\rho-K/2-BF''-(B'/2+2B/r)F'.
\]
Stress conservation requires
\(p_r'=-(\rho+p_r)\ell'+2(p_t-p_r)/r\). A prescribed conserved
tensor by itself does not derive a material action or state.

An explicit material construction uses the chosen irrotational-dust action
\(S_m=-\frac12\int\sqrt{-g}\lambda[(\partial T)^2+1]\,d^4x\).
Variation before imposing the constraint yields
\((\partial T)^2=-1\), \(\nabla_\mu(\lambda\nabla^\mu T)=0\), and
on shell \(T_{\mu\nu}=\lambda\partial_\mu T\partial_\nu T\).
Choose \(T=t,\lambda=\rho_0>0,N=1,B=1-kr^2\), \(k>0\), on
\(0\le r<R_b\), \(kR_b^2<1\). For
\(\rho_0R_b^2/2<C<\rho_0/(2k)\), put

\[
 F_C=\frac{C-\rho_0r^2/2}{1-kr^2},\qquad
 Z(F)=\frac{3k}{\rho_0-2kF},\qquad
 V_C(F)=\frac{\rho_0}{2}+\frac{3(\rho_0-2kF)^2}{2(\rho_0-2kC)}.
\]

Let \(A=2kC-\rho_0<0\). Then \(F'=Ar/B^2\),
\(\Box F=3A/B^2\), \(Z(F_C)=-3kB/A>0\),
\(2FZ+3=3\rho_0/(\rho_0-2kF)>0\). Substituting these expressions,
\(G_t=-3k,G_r=G_a=-k\), in every metric and scalar equation makes
each residual zero. The fields are smooth in Cartesian coordinates at the
center, where \(F'=0\) but \(F''=A\). The dust equations hold as well.
This constructs different potential coefficients and central fields at the
same regular metric, dust density and kinetic function. Static clocks, radial
timing and stationary zero-speed geodesics coincide. It does not assert the
existence of nonzero circular motion, an exterior match or stability.

For a separately stipulated round-sphere continuation, set
\(r=\sin(\sqrt k\,\chi)/\sqrt k\), \(0\le\chi\le\pi/\sqrt k\).
The equator \(B=0\) is a regular turning point of areal radius, not a lapse
horizon. The undivided angular-time equation is
\(2kF-\rho_0=\sqrt k\cot(\sqrt k\chi)F_\chi\).
Its solution on each hemisphere is
\(F=\rho_0/(2k)+A_\chi\sec^2(\sqrt k\chi)\).
Finiteness through the equator fixes \(A_\chi=0\) on both sides. Direct
field equations for this separate constant branch require
\(F_0=\rho_0/(2k)\), \(V(F_0)=\rho_0/2\), \(V_F(F_0)=3k\).
Finite \(Z(F_0)\) and higher potential derivatives remain free, subject to
the chosen kinetic-sign condition. Substituting this endpoint into the
singular nonconstant-family action is invalid. The global geometry is an
additional hypothetical premise, not an observation or a derived history.

Once one action is selected, \(\rho_0,k,C\) appearing in its coefficients
are fixed parameters. Perturbing material density must not retune those
coefficients. The identities \(V_C'(C)=-6k\) and
\(V_C''(C)/Z(C)=4k\) are useful checks but neither is a coupled-system
mass or a demonstrated observational discriminator. In particular,
\(\Box F(0)=3A\) is nonzero. A response calculation must include metric,
scalar and matter perturbations together.

## Domain, dimensional and empirical limits

The inverse divides by \(d\) and \(u\); points where either vanishes need
separate equations. The integrated relative formula only divides by \(y\);
its physical interpretation still inherits a valid action solution. The
shared-label bound requires strictly positive margins and degrades near
\(D=0\), \(q=0\) or \(P=0\). Centers and the equator are treated only
in the explicit constructions, without applying singular annular formulas.
Zero angular speed is a stationary control, not a measured orbit population.

In natural units, \(r,T\) have length dimension; \(F,C,k\) have mass
dimension two; \(\rho_0,V,\lambda\) dimension four; \(Z\) dimension
minus two. The ratio \(F/F_0\), \(\omega\), and \(v^2\) are
dimensionless. In the observation formulas, \(c\) restores length/time.

No parameters are calibrated or fitted, no independent empirical test is
reported, and no new raw observation is opened. Mathematical perturbation
tuples, exact metrics and material examples are exposed development controls.
The campaign's previously seen external data remain development material;
unopened data require a frozen prediction/readout protocol before use.

## Verification and review record

Primary runner: [scalar_observation_inverse.py](../scripts/scalar_observation_inverse.py).

It imports the
[pure math helper](../scripts/scalar_observation_inverse_math.py). It checks
general symbolic pullbacks, exact backgrounds, the material and scalar
equations, endpoint/domain controls, deterministic bounds and bin examples.
Besides importing the helper implementation, its explicit file-byte reads of
this note and the helper supply integrity hashes. Its problem inputs are the
declared synthetic symbols and constants. Its canonical receipt
is `outputs/scalar_observation_inverse.json`, and its canonical execution
envelope is `logs/runner-cache/scalar_observation_inverse.txt`. These are
author evidence, never audit verdicts.

This integration replaces no landed science. Earlier derivations and focused
checks are preserved on the separate checkpoint branch
`codex/observations-backward-derivation-20261015`, through commit
`74f9132b33a259a01a950f5928f154c71519cbf3`, in its campaign pack. They used
reduced-action, Cartesian-curvature and completed-square routes. Earlier
attempts, including the terminated symbolic expansion and corrected bump
support, remain historical provenance; the present proof and primary runner
do not require those archived programs or their outputs. Final source-bound
integration evidence is carried with this milestone in
`.claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_integration/`.
Mutation and integration records accompany the self-contained canonical result.

Outstanding at landing, as hard landing conditions: the single shared combined
pipeline, strict lint and changed-evidence pass on the integrated tree; verify
the intended citation node and imported-helper closure there; regenerate the
citation manifest on that tree; and obtain the normal independent review/audit
disposition. No helper-registry policy edit is needed because the primary
runner directly imports its load-bearing helper. This note proposes only
conditional support and carries no audit-ratified authority.
