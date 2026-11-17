## Repo search

Author: **OpenAI Codex; assigned gpt-6-astra / max**. The runtime model
identifier is not independently exposed to this session. Research row 1077,
not an audit; no scientific status or Yang–Mills mass gap claimed.

The target-specific prior file is absent at checkout
`01755194be302f294887aea3c29e45bac32da547`. The lead's November 8 digest
searched main and PRs 10114, 10133, 10134 and 10141 for thirteen earlier
UV/RG targets. It does not report a proof of this face-gap target. Its
nearest soft-route hits were checked at PR 10114 commit
`f76f6c649cff7dffbab664d8976e680e8f287fe9`. In the table, `S/` means
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`:

| Source checked | Closeness |
|---|---|
| Main `research/ym4d/library/out-mu.md:8–32,69–82,180–190` | Regular-window minimizers and axial representatives on Balaban's constrained domains. No flat-plane Gibbs limit or face-gap stability statement. |
| Main `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145` | A noncompact Dirichlet Maxwell covariance comparison, for a different measure. |
| `S/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` | A positive one-step plaquette witness. It supplies neither decay nor a face-gap stability theorem. |
| `S/BOTTOM_SECOND_CURVATURE_ASTRA.md:353–364` | “Face lifts” are momentum-chart covers, a different object. |
| Rows 1053, 1061, 1062 | Direct prior work: the free longitudinal-box reduction, product anchor, and residual-symmetry twist bound. Reused below, not claimed as new. |
| Rows 1070, 1072, 1074 | Direct prior work: the unpinned scope of the posted mixing theorem, the face-path question, and corrected strength comparisons. |

The main sources and rules were read at `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`.
No competing owner was found under the face-gap labels in
`library/open-registry.md`, `open-core.md`, or `l17c.md`. The parked
FACE-TW problem concerns charged annulus decay; this row concerns the
gauge-invariant gap and stops at the requested port obstruction. This is
a bounded prior search, not a claim of exhaustive absence.

# The flat longitudinal face as a two-dimensional system

Source checkout: `01755194be302f294887aea3c29e45bac32da547`.
PROVED below means a written hand argument, sometimes conditional on a
named published input. It does not mean independently checked or retained.
No Lean formalization has been run.

## Plan and checkpoint

1. Check repository prior work, ownership, operating rules, and the required
   local results; locate the published sources through their indexes.
2. State the face measure, gauge reduction, residual symmetry, and reflection
   positivity, distinguishing the already proved reduction from new details.
3. Test the first applicable step of OpenAI's pinned-cell/bracket proof against
   the transverse on-site potential; write the exact surviving or failing step.
4. Determine what the anchor proves about small positive transverse coupling,
   keeping every uniformity and missing stability hypothesis explicit.
5. State the first open face-path assertion and its actual implications for
   the four-dimensional target; run the requested mathematical controls.
6. Check the written arguments, citations, and scope; end with one RESULT line.

Current checkpoint: steps 1–6 complete. The surviving port is (5)–(8).
Independent-sheet (3.6) and the conditional-ferromagnet conversion fail
by (9) and (12). A positive size-uniform neighbourhood remains OPEN.
No further attack is launched after the requested stopping condition.
The two Sussman–Alpoge source downloads are in the newly created scratch
directory `/tmp/sa-gap-face-2d-astra.8I9J4p`; OpenAI's single PDF download
is in `/tmp/sa-gap-face-2d-openai.sw1Var`. No paper is committed.
The requested mathematical steps use no computation as proof.

## Step 1 result: premises and the precise distinction to test

**PROVED in prior work, reused:** row 1053 §§6.1–6.3 gives FACE-LIM,
ANCH and RIG. Rows 1061 §§1–2 and 1062 steps 2–3 check them. Their
corrections matter: free longitudinal boundaries; residual gauge-invariant
observables remain invariant; arbitrary compact groups need different
constants; FACE-MW needs integer inner radius at least one. Neither
FACE-MW nor charged decay gives a singlet gap.

**ARGUED, supplied published input:** OpenAI's *Sharp mass bounds for the
two-dimensional O(4) model*, pin `4eaee87548250b2682affda7d05d947c05554bae`.
The local copy is `/tmp/sa-gap-face-2d-openai.sw1Var/paper.pdf`.
Its Theorem 3.1 concerns unpinned free subgraphs and sufficiently large
unpinned tori, Lipschitz observables, and weakened ferromagnetic bonds.
Row 1070 §1 already rejects attributing arbitrary-boundary all-observable
mixing to that theorem. This row will not reintroduce that attribution.

**ARGUED, supplied published input:** Jürg Fröhlich, Barry Simon and Thomas
Spencer's infrared-bound theorem. Row 1074 §2's hand bound gives its
sufficient three-dimensional O(4) ordering threshold below 2. Thus its
corrected CA-FAIL applies throughout the requested window, but only to
the specified full-link strong-mixing claim. No slab obstruction to the
present face statement is inferred.

The outline search first used `sa-index/README.md`, neighbouring rows
`chunk-01.md:62–73`, and `obligations.md:18–29`. The cited source
`YM4_sketch_500.tex:588–599` explicitly separates polynomial decay from a
spectral gap. Searches for principal-chiral, face-model and mass-gap terms
in the 4.12–4.19 account index found no face supplier. Its scalar/operator
gaps are different objects. Credit **Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text**, for this source distinction;
credit **Tadeusz Balaban** for the ultraviolet construction behind the
account. No Balaban UV estimate is being used as an infrared gap theorem.
Pinned primary copies: [outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex)
and [complete account I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex).

The transverse-lattice/chiral-model picture is credited to **Peter Orland**,
with the preceding work of Erik and Herman Verlinde and Irina Aref'eva
identified by rows 1061–1062. His Hamiltonian analysis is not substituted
for the finite Euclidean measure identity proved in row 1053.

## Step 2 result: the precise face and its positive transfer operator

### 2.1 Reduction, including the transverse torus — PROVED

Let $K=SU(2)$, $V_T=(\mathbb Z/T\mathbb Z)^2$, and let $E_T$ contain
the positively oriented transverse edges. Let $P_T$ contain one positively
oriented elementary square per site. We use $T\geq3$, so every square has
four distinct edges; $|E_T|=2T^2$ and $|P_T|=T^2$. This specifies a
cofinal family of transverse sizes. No assertion about collapsed $T=1,2$
cellulations is implicit. Put $\tau(q)=\tfrac12\operatorname{tr}q$.
For a finite longitudinal rectangle $D$, the spin at $u$ is
$\Phi(u)=(\Phi_e(u))_{e\in E_T}\in K^{E_T}$. Define

```math
W_T(\Phi)=\sum_{p\in P_T}\tau(\Phi_{e_1}\Phi_{e_2}
                                \Phi_{e_3}^{-1}\Phi_{e_4}^{-1}),
\qquad V_T^{\rm onsite}(\Phi)=-\lambda W_T(\Phi),
```

where $\lambda=\beta_T$. With normalized product Haar reference measure,
the face density is proportional to

```math
\exp\!\left\{\beta\sum_{\langle u,v\rangle\subset D}
       \sum_{e\in E_T}\tau(\Phi_e(v)\Phi_e(u)^{-1})
       +\lambda\sum_{u\in D}W_T(\Phi(u))\right\}.                 \tag{1}
```

Here $\beta=\beta_M$. Boundary-crossing longitudinal bonds are included
when boundary spins are prescribed. This is a two-dimensional spin system
with a nonconstant on-site potential, not a single O(4) magnet.

The residual gauge group is

```math
G_T=K^{V_T},\qquad
(g\Phi)_e(u)=g_{s(e)}\Phi_e(u)g_{t(e)}^{-1},\quad g\text{ independent of }u.
                                                                    \tag{2}
```

Its action kernel on all configurations is the common diagonal centre
$\{\pm1\}$. Indeed, setting one edge variable to 1 forces equality of
its endpoint transformations. Connectivity forces a common transformation;
varying that edge forces it to commute with every quaternion. We can use
the nonfaithful group $G_T$ without quotienting. This identifies the residual
gauge group, not every additional discrete symmetry of (1).

**Proof and prior credit.** Apply row 1053's checked FACE-LIM proof separately
to each longitudinal rectangle at a transverse vertex. Its comb forest
uses no transverse edge. Therefore transverse periodicity changes none of
the Haar changes of variables or the independent longitudinal plaquette
coordinates. The latter have normalized densities proportional to
$e^{\beta_L\tau(h)}$ and converge to $\delta_1$. The remaining density is
bounded, positive and continuous on the finite compact space, so its
normalized integral converges too. Each mixed plaquette becomes the bond
term in (1), and each transverse square gives $W_T$. This is the same
proof as FACE-LIM, with its previously unused transverse boundary condition
removed. It adds no estimate uniform in $\beta_L$.

A gauge transformation preserves longitudinal links equal to 1 exactly
when it is constant on each connected longitudinal plane. This proves (2).
At each fixed $u$, the plaquette product transforms by conjugation at its
base vertex, so $W_T$ is invariant under $G_T$. Original gauge-invariant
observables restrict to $G_T$-invariant functions. On $\mathbb Z^2$, flat
longitudinal transport is path independent because elementary squares
generate the relations between finite lattice paths. Transport from one
base point therefore gives the same representative on every finite path.
The infinite-plane face can be constructed by local limits of (1).

The order just justified is finite $D$, then $\beta_L\to\infty$, then a
longitudinal local limit. It does not interchange these limits. A periodic
*longitudinal* Wilson lattice keeps commuting flat holonomies. Periodic
spin approximants of (1) select trivial longitudinal holonomy; they are not
silently identified with the full periodic Wilson face limit.

At $\lambda=0$, ANCH gives independent O(4) sheets, one per transverse
edge. Their symmetry contains $\prod_e(K_L\times K_R)$, up to its central
kernel. At positive $\lambda$ the plaquette potential preserves (2) but
not those independent sheet rotations. The counterexample in step 3
shows that loss explicitly.

### 2.2 Longitudinal reflection positivity — PROVED

Write each quaternion as its unit vector $s\in\mathbb R^4$. A bond
crossing a longitudinal link-reflection plane has kernel

```math
e^{\beta s\cdot s'}=
\sum_{n\geq0}\frac{\beta^n}{n!}
                \langle s^{\otimes n},(s')^{\otimes n}\rangle .     \tag{3}
```

For $\beta\geq0$ each summand is a positive kernel, and the series is
uniformly absolutely convergent on the spheres. Products over transverse
edges remain positive kernels. All on-site weights and all bonds on one
side are a positive factor times its reflected copy. Integrating the
positive-kernel expansion proves $\mathbb E[(\Theta F)F]\geq0$.
For a site reflection, condition on the seam spins: the two remaining
halves give a squared modulus, integrated against a positive seam weight.
The same proofs apply on even longitudinal spin tori and pass to matching
local limits. This is OpenAI's §3.12.2 argument with the positive on-site
factor retained. It requires no product symmetry of the sheets.

More concretely, make one longitudinal spatial direction a circle of
length $L$. One time slice has variables $Q\in K^{L|E_T|}$. Let
$A_\lambda(Q)$ be its longitudinal-spatial bond action plus
$\lambda\sum_{r,p}\tau(\Phi_p(r))$. Its transfer kernel is

```math
K_\lambda(Q,Q')=e^{A_\lambda(Q)/2}
 e^{\beta\sum_{r,e}\tau(\Phi'_e(r)\Phi_e(r)^{-1})}
 e^{A_\lambda(Q')/2}.                                             \tag{4}
```

Equation (3) proves operator positivity. The kernel is continuous and
strictly positive on a compact space. Hence it is compact, has a simple
positive largest eigenvalue, and its normalized leading eigenfunction is
strictly positive. For completeness, maximizing its Rayleigh quotient
allows replacing an eigenfunction by its absolute value; strict kernel
positivity makes equality possible only for a constant phase, excluding
two orthogonal leading eigenfunctions. The operator commutes with (2),
so this leading eigenfunction is $G_T$-invariant. The physical singlet
transfer space is the invariant subspace. A full-space spectral bound
implies its singlet bound; the converse is not asserted.

## Step 3 result: a Ward port survives; the direct mixing port fails

Source: [OpenAI's pinned paper](https://raw.githubusercontent.com/openai/math/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf),
§3.1, pp. 13–14, equations (3.4)–(3.8), and §3.11, pp. 29–32.
The formulas on pp. 13 and 31 were checked against rendered PDF pages,
not inferred from damaged text extraction. The generated text locators
are `paper.txt:718–773` and `1860–1880` in the scratch directory.

### 3.1 The first geometry-dependent step — PROVED port

Fix one transverse vertex $x$. For each of its four incident edges, put
$q_j(u)=\Phi_j(u)$ if the edge leaves $x$, and
$q_j(u)=\Phi_j(u)^{-1}$ if it enters $x$. All four then transform as
$q_j(u)\mapsto g(u)q_j(u)$ under a transformation at $x$. Inverting an
incoming edge keeps its mixed-bond scalar product and Haar measure.
For a longitudinal bond $b=(u,v)$, write

```math
t_{jb}+s_{jb}=q_j(v)q_j(u)^{-1},\qquad s_{jb}\in\operatorname{Im}\mathbb H.
```

Use imaginary unit generators $a^2=-1$, so $e^{ta}=\cos t+a\sin t$.
This angle is half the angle parameter in row 1053's RIG convention.
Let $w_{jb}$ be the bond weights with $|w_{jb}|\leq\beta$, with half
allocation for tangent boundary bonds as in OpenAI. All other parts of the action are left in
the probability law. In particular the plaquette potential is retained.
Set $\mathcal A=-\mathcal S$ for the complete action exponent in (1).

Under $q_j(u)\mapsto e^{ta f_u}q_j(u)$, the on-site potential is
unchanged for every $t$, separately at every longitudinal site. Direct
quaternion multiplication therefore gives exactly

```math
D_f\mathcal A=\sum_{j,b}w_{jb}(s_{jb}\cdot a)(f_v-f_u),\qquad
D_f^2\mathcal A=\sum_{j,b}w_{jb}t_{jb}(f_v-f_u)^2.                  \tag{5}
```

This is OpenAI (3.6) summed over four sheets, under the *actual interacting
face law*.
For an arbitrary imaginary profile $\eta$, differentiating
$e^{t\eta_v}(t_{jb}+s_{jb})e^{-t\eta_u}$ gives

```math
D_\eta s_{jb}=t_{jb}(\eta_v-\eta_u)
                       +(\eta_v+\eta_u)\times s_{jb}.             \tag{6}
```

The cross product is the first explicitly noncommutative term in the
source calculation, (3.7). It survives without change. No general
curvature theorem has been invoked; this is the quaternion identity.
There is no corresponding cross-product term for an abelian group.

Define $J(F)=\sum_{j,b}w_{jb}s_{jb}\cdot F_b$. For $\eta$ zero on the
pinned boundary, the simultaneous changes of the four incident variables
preserve product Haar measure and the pins. Integrating
$D_\eta(He^{-\mathcal A})$ gives
$\mathbb E D_\eta H=\mathbb E[H J(d\eta)]$, and putting $H=1$
gives $\mathbb E J(d\eta)=0$. Apply this to $H=J(F)$ and use (6):

```math
\operatorname{Cov}(J(d\eta),J(F))
 =\mathbb E\sum_{j,b}w_{jb}t_{jb}(d\eta)_b\cdot F_b
  +\mathbb E J\bigl(F_b\times(\eta_v+\eta_u)\bigr).              \tag{7}
```

This proves the compact-profile Ward identity, OpenAI (3.8), on the
face. The sum of endpoint profiles, and hence the factor two for a slowly
varying profile, remains. Finite-dimensional smooth integration proves
the identity; there is no limiting or numerical proof step.

For a cell of side $S$ and a real constant $3\times2$ matrix $F$, define
the stiffness exactly as in (3.4), with $|F|$ the Frobenius norm:

```math
H_x(F,F)=S^{-2}\mathbb E\sum_{j,b}w_{jb}t_{jb}|F_{\mu(b)}|^2
                                      -\operatorname{Var}(S^{-1}J(F)).
```

Dropping its nonnegative variance gives

```math
H_x(F,F)\leq 4\beta\,|F|^2.                                     \tag{8}
```

Indeed each incident sheet contributes at most $\beta S^2$ per
longitudinal direction before division by $S^2$. Thus (8) is uniform in
$T$, $\lambda$, and the boundary pins. This also ports the initial upper
bound (3.5); it is not a positive gap. Equations (5)–(8) are the requested
proved port of one step. The subsequent stiffness iteration has not been
ported, and neither FACE-TW nor FACE-CH is asserted here.

### 3.2 Independent sheet rotations fail first at (3.6) — PROVED

The same equations are false if each sheet retains its independent
$K_L\times K_R$ action. Choose one transverse edge $e$ and start with
all links equal to 1. Rotate only this sheet, at each $u$, to
$\Phi_e(u)=e^{ta f_u}$. Exactly two transverse plaquettes contain $e$.
Both have trace scalar $\cos(tf_u)$, irrespective of orientation.
Consequently the on-site part of $\mathcal A$ changes by

```math
2\lambda\sum_u(1-\cos(tf_u)),\qquad
\left.\frac{d^2}{dt^2}\right|_{t=0}\mathcal A
 =\beta\sum_{\langle u,v\rangle}(f_v-f_u)^2
                       +2\lambda\sum_u f_u^2.                    \tag{9}
```

The last term is absent in OpenAI (3.6), p. 13. It is nonzero for every
$\lambda>0$ and every nonzero profile, including profiles vanishing on
the pinned boundary. For a constant profile on a periodic longitudinal
box, the gradient term is zero while this term is positive. Thus the
literal independent-sheet port fails at that equation, before any claimed
bracket gain. This is not a counterexample to the face gap.

Restricting to $G_T$ repairs (5), but loses precisely the invariant
coordinates. For any transverse plaquette, $f(\Phi)=\tau(\Phi_p)$ is
nonconstant and invariant under all local transverse gauge rotations.
All their infinitesimal derivatives of $f$, and all iterated brackets
of those derivatives, vanish. Its variance is strictly positive under any
finite positive-density face law: $f$ takes distinct values on two open
sets of positive Haar measure. Hence an inequality of the form

```math
\operatorname{Var}_\mu f\leq C\sum_a\mathbb E_\mu|D_a f|^2        \tag{10}
```

with only these gauge-orbit directions is false for every finite $C$.
This proves a precise limitation of the surviving bracket algebra.
It does not rule out an argument using additional directions or the
dynamics of invariant variables.

### 3.3 The all-observable conversion fails too — PROVED

The first line of OpenAI's §3.11.3 after the a priori law, p. 31, is
the exact claim **“the two circle sectors are independent XY models”**
conditional on the amplitudes. Their displayed couplings then involve
only the longitudinal nearest-neighbour edges. In the face law a factor
$e^{\lambda\tau(\Phi_p)}$ remains at every longitudinal site. It is a
four-link interaction and couples those conditional variables. For example,
when the four quaternions lie in one circle it is
$e^{\lambda\cos(\theta_1+\theta_2-\theta_3-\theta_4)}$.
The claimed conditional pair-XY law is therefore not the face law.

There is an exact sign obstruction to importing the following FKG step,
not just an extra factor whose sign is unknown. Take $T\geq4$ and two
opposite edges $e,f$ of one transverse square, at one longitudinal site.
Write every quaternion coordinate as a magnitude times a sign; conditioned
on the magnitudes, Haar gives independent fair signs. These are the same
coordinate signs obtained by applying the paper's two-circle and then
two-sign decompositions. Fix all signs except the real-coordinate signs
$\sigma,\sigma'$ of $e,f$. Since the plaquette is multilinear in its
four quaternion variables, its dependence on them is

```math
\log w(\sigma,\sigma')=c_0+h\sigma+h'\sigma'
                                      +\lambda c\sigma\sigma'.  \tag{11}
```

No other transverse plaquette contains both opposite edges. All other
plaquettes, and all mixed bonds with the other longitudinal sites fixed,
contribute only to $c_0,h,h'$. Set the two remaining edges of the square
to $1,-1$. At real-coordinate magnitude one for $e,f$, the coefficient
is $c=-1$. Quaternion inversion leaves the real coordinate unchanged, so
this sign is independent of the chosen square orientation. Continuity
makes $c<0$ on an open set with all coordinate magnitudes positive, near
these choices. That set has positive measure; this is not a null-pin
argument at a coordinate pole.

The log lattice condition on this two-sign slice requires
$w(+,+)w(-,-)\geq w(+,-)w(-,+)$. Instead (11) gives

```math
\frac{w(+,+)w(-,-)}{w(+,-)w(-,+)}=e^{4\lambda c}<1
\quad(\lambda>0).                                                \tag{12}
```

Thus the conditional sign system lacks the FKG lattice condition used
in §3.11.1–3.11.3. Conditionalising a putative ferromagnetic Ising law
cannot produce this negative pair coefficient. This fails for arbitrarily
small positive $\lambda$; its magnitude becomes small but its sign does
not change. It turns row 1053's §6.5 warning about sign clusters into an
explicit counterexample for this conditional port. It proves neither
failure of every correlation inequality nor failure of exponential decay.

The requested port/failure stopping condition is met. The
remaining steps record the small-coupling inference and the controls;
they do not launch another stiffness or FACE-TW attack.

## Step 4 result: what small-coupling perturbation actually proves

### 4.1 Anchor and finite-cylinder comparison — PROVED given OpenAI

Take $\beta\in[23/10,13/5]$. In the notation of Theorem 3.1, fix its
absolute constants $C,c>0$ once and put

```math
\Xi(\beta)=\exp\!\left\{\pi\beta+
              C\sqrt{(1+\beta)\log(2+\beta)}\right\},\qquad
a(\beta)=c/\Xi(\beta)>0.
```

The transfer gap means $-\log(\kappa_1/\kappa_0)$, with eigenvalues
ordered with multiplicity, on the full or explicitly specified singlet
space. The value is $+\infty$ if $\kappa_1=0$. For
longitudinal spatial circles $L\geq L_0(\beta)=\lceil C\Xi(\beta)\rceil$,
the single-sheet transfer gap is at least $a(\beta)$.

Here is the implication from the posted theorem, keeping the finite-size
quantifier. Fix $L$ and send the other torus side to infinity. Strict
positivity of the finite-slice transfer kernel selects its leading state.
Theorem 3.1's estimate survives this limit. For a centered Lipschitz
function $F$ of the complete finite spatial slice, its time correlation
is bounded by a polynomial in time times $e^{-a n}$. Its positive
spectral measure therefore has no support above $e^{-a}$ for the
normalized transfer operator: any mass on $[r,1)$ with $r>e^{-a}$
would give a lower bound proportional to $r^n$. Such slice functions
times the strictly positive leading eigenfunction are dense in the slice
Hilbert space. The whole orthogonal complement of the leading vector
therefore has spectrum at most $e^{-a}$. This is the spectral step of
OpenAI §3.12.2, applied with fixed $L$ before taking the time limit.

At the anchor, (4) is a tensor product of $2T^2$ single-sheet transfer
operators. A normalized product eigenvalue outside the vacuum contains
at least one nonvacuum sheet eigenvalue. Its modulus is at most
$e^{-a}$. Thus the full gap, and hence the singlet gap, is at least
$a(\beta)$, uniformly in $T$ and these $L$. No multiplication by the
number of sheets is lost. On the compact window one can use
$a_*=c/\Xi(13/5)>0$ and a common $L_0$.

For positive $\lambda$, put
$V(Q)=\sum_{r,p}\tau(\Phi_p(r))$ and $N=LT^2$. Then $|V|\leq N$,
and the *exact* transfer relation is

```math
K_\lambda=M_\lambda K_0M_\lambda,\qquad
M_\lambda=e^{\lambda V/2}.                                       \tag{13}
```

For each eigenvalue $\kappa_j$ in decreasing order, positivity and the
min–max principle give

```math
e^{-\lambda N}\kappa_j(K_0)\leq\kappa_j(K_\lambda)
                       \leq e^{\lambda N}\kappa_j(K_0).           \tag{14}
```

To verify rather than assume the comparison, the nonzero spectra of
$M K_0M$ and $K_0^{1/2}M^2K_0^{1/2}$ coincide. The latter operator
lies between $e^{-\lambda N}K_0$ and $e^{\lambda N}K_0$ in quadratic
forms. Apply min–max. The argument also holds on the invariant subspace,
since $M$ is invariant. Dividing the $j=1$ upper bound by the $j=0$
lower bound proves, for either full or singlet transfer gap,

```math
m_{L,T}(\beta,\lambda)\geq a(\beta)-2\lambda LT^2.
\quad
0\leq\lambda\leq\frac{a(\beta)}{4LT^2}
\ \Longrightarrow\ m_{L,T}(\beta,\lambda)\geq\frac{a(\beta)}2.    \tag{15}
```

These are written operator inequalities, not numerical eigenvalue tests.
They give a concrete interval at each finite spatial cylinder. Their
common interval over unbounded $L,T$ is exactly $\{0\}$.

### 4.2 Decision on the purported uniform neighbourhood

**OPEN:** a positive $T$-uniform interval for the actual face law.
**FAILS as a justification:** ordinary bounded-operator perturbation of
the posted gap, using the norm of the full perturbation. Equation (15)
does not give such an interval. Failure of this sufficient bound is not
a proof that the face gap closes. In particular no positive number
$\varepsilon$ in $\beta_T\Xi(\beta)^2\leq\varepsilon$ is supplied
by the posted theorem or by (15).

A spectral gap alone cannot justify an unrestricted local-perturbation
stability theorem. Here is a hand-checkable counterexample to that abstract
inference, not to O(4). On a cycle of $N\geq3$ Ising variables, take the
diagonal Hamiltonian

```math
H_0(s)=\tfrac12\#\{i:s_i\ne s_{i+1}\}+\mathbf1_{s_1=-1},\qquad
H_\lambda(s)=H_0(s)-\lambda\sum_i\mathbf1_{s_i=-1}.               \tag{16}
```

At zero coupling the unique ground configuration is all plus. Every
other configuration has energy at least 1, and all minus has energy 1.
Thus the gap is exactly 1 for every $N$. At $\lambda=1/N$, all plus
and all minus both have energy zero. A mixed configuration has at least
two walls and at most $N-1$ minus spins, so its energy is at least
$1-(N-1)/N=1/N>0$. Each perturbing term has norm $\lambda$, yet
the vacuum gap closes at couplings tending to zero. The single pin in
(16) breaks translation invariance; it is deliberately not claimed to
satisfy OpenAI's unpinned homogeneous hypotheses. It proves why the
abstract gap argument needs additional stability assumptions, not that
those stronger O(4) hypotheses cannot yield stability.

The stronger published datum is unpinned Lipschitz covariance decay,
uniform under weakening *pair* couplings. A transverse plaquette insertion
leaves that class, as (9) and (12) show. A positive uniform interval would
need a local perturbation theorem whose hypotheses are proved from this
datum, or a new estimate for the perturbed law. Arbitrary pinned mixing
and a convergent connected expansion cannot be inserted as consequences
of Theorem 3.1. Rows 1066–1070 already leave the corresponding seed open.
Accordingly the interval established here uniformly in size is the anchor
$\lambda=0$, conditional on the posted theorem. The existence and size
of a positive interval remain undecided; no negative claim about that
interval is proved.

## Step 5 result: the open face statement, its strength, and controls

### 5.1 Quantifiers and strength — OPEN target; PROVED implication

Fix a translation-invariant, reflection-positive state obtained as a local
limit of the periodic spin measures (1); where there is more than one
such limit, include every such state in the quantifier. The local form
of **(FACE-SG-T)** attacked here is: for every
$\beta\in[23/10,13/5]$, there is $m_\beta>0$, uniform in
$T\geq3$ and $0\leq\lambda\leq\beta$, such that for all fixed local
$G_T$-invariant Lipschitz $F,H$,

```math
|\operatorname{Cov}_{\mu_{\beta,\lambda,T}}
       (F,\tau_{ne_0}H)|\leq C_{F,H,\beta}e^{-m_\beta n}.         \tag{17}
```

The prefactor is independent of $T,\lambda$, the selected state and
translations, for a fixed support shape and fixed observable norms.
For transverse limits use supports embedded without wrapping once $T$
is sufficiently large. This includes invariant functions supported on
more than one longitudinal time slice, with their fixed time thickness
absorbed into the prefactor.

The first open statement is already (17) on some interval
$[0,\varepsilon_\beta]$ with $\varepsilon_\beta>0$. If that were supplied,
the remaining open face assertion would be a common positive rate on
$[\varepsilon_\beta,\beta]$. No proof here bounds how far such an interval
extends. A uniform finite-cylinder singlet gap for (4), for all sufficiently
large $L$ and all $T$, is a sufficient stronger input for (17), by positive
spectral measures and local limits. To keep the prefactor uniform, the
insertion kernel for a bounded observable in a time slab of thickness $r$
is bounded pointwise in absolute value by $\|F\|_\infty K^r$.
After normalizing $K$, its operator norm is at most $\|F\|_\infty$:
apply the positive kernel to the absolute values of the two test vectors
and then the contraction bound. Subtracting the vacuum contribution
and applying the spectral bound between the two slabs gives a constant
at most $4\|F\|_\infty\|H\|_\infty e^{m(r_F+r_H)}$, independent
of $L,T$. This also covers nonslice local observables. We have not
identified the finite-cylinder hypothesis with (17) in both directions.

**What a size-uniform face estimate gives.** Suppose (17) holds. Take a
subsequence $T_j\to\infty$ along which the face laws converge locally.
Such subsequences exist by compactness of the countable product of compact
spin spaces and a diagonal selection of finite marginals. At fixed $n$,
the expectations of $F$, $H$, and their product converge, so (17) passes
with exactly the same rate and prefactor. Thus the limiting face state
on $\mathbb Z^2\times\mathbb Z^2$ has longitudinal exponential
clustering on that invariant algebra. Reflection positivity from step 2
and density of local Lipschitz functions then give the corresponding
positive spectral exclusion in its longitudinal transfer sector, by the
same positive-measure argument used in step 4.

This is a forward implication with matching local limits and observable
identifications. An infinite-volume gap does not, by the argument just
given, imply uniform gaps on finite transverse cylinders. No converse has
been supplied. This keeps row 1074 §8's correction to BR-7.

The face estimate still gives no bound at finite $\beta_L$, no comparison
to the isotropic point, and no cutoff-uniform physical gap. It also does
not, by merely exchanging directions, give transverse clustering: the
face is anisotropic. A separate descent bound with matched states and
observables is needed for BR-2's second leg. Nor does a local singlet
estimate alone control every finite-torus electric-flux sector, the
partition-function seed (W), or its continuum carry. No equivalence,
strict weakness, or strict strength between (17) and the full isotropic
target is proved here. The supplied existence/UV account does not remove
these obligations: CA-I 2706–2712 explicitly excludes a mass-gap claim.

### 5.2 Compact U(1) — PROVED control given Fröhlich–Spencer

At the anchor this is a product of XY sheets. The relevant control is
already in row 1062, J1, L114: it applies to a *singlet*, not just to a
charged spin. If $g(n)=\mathbb E e^{i(\theta(0)-\theta(ne_0))}$ is one
sheet's two-point function and $P(u)$ is the oriented sum of four
independent sheet angles around one transverse plaquette, then

```math
\mathbb E\cos P(u)=0,\qquad
\operatorname{Cov}(\cos P(0),\cos P(ne_0))=\tfrac12 g(n)^4.        \tag{18}
```

The identity follows by expanding the two cosines. The equal-charge term
vanishes under an independent sheet rotation; the opposite-charge term
factorizes into four copies of $g$. Fröhlich and Spencer's low-temperature
XY theorem supplies a power-law lower bound, so (18) excludes a positive
exponential rate for this gauge-invariant observable at sufficiently large
stiffness. This cited theorem is not rebuilt here; see OpenAI's introduction
and reference [18], *Communications in Mathematical Physics* 81 (1981),
527–602. No theorem-level threshold in the specific window is asserted.

Reflection positivity and the group-blind gradient bound survive this
test, as they should. The three-component bracket term does not. Any
extension purporting to prove (17) for every compact group from those
group-blind ingredients would contradict (18).

### 5.3 Frozen Q_8 and 2T — PROVED frozen-limit control

These groups have no nonzero infinitesimal rotation fields. Thus the
Ward/bracket port does not apply. There is also a direct invariant
frozen-limit test. At $\lambda=0$, take the symmetric anchor and send
$\beta_M\to\infty$ at finite longitudinal volume first. Each sheet
becomes a constant $h_e$, independently uniform in the finite group.
This follows since a bond has its unique maximum when its endpoint
group elements agree; all nonconstant configurations have strictly lower
weight on the finite connected graph. Then take longitudinal local limits.

The plaquette product $h_p$ is uniform in the group and constant in $u$.
The centre-even invariant $f(u)=\tau(h_p)^2$ therefore has covariance
$\operatorname{Var}(\tau(h_p)^2)$ at every longitudinal separation.
For $Q_8=\{\pm1,\pm i,\pm j,\pm k\}$, its squared real part is 1
on two elements and 0 on six. Hence this variance is
$1/4-(1/4)^2=3/16$. For

```math
2T=Q_8\ \cup\ \{(\pm1\pm i\pm j\pm k)/2\},
```

the sixteen added elements have squared real part $1/4$. Its first
and second moments are $1/4$ and $1/8$, so the variance is $1/16$.
These are displayed finite counts, not machine enumeration. Both
symmetric frozen faces fail singlet clustering even in a centre-even
observable. No transition coupling, no finite-temperature window
statement, and no statement about a selected pure ordered state follows
from this frozen-mixture calculation.

### 5.4 Pin(2) — exact algebra; GUIDE phase test

For $\operatorname{Pin}(2)=U(1)\cup jU(1)$, the identity-component Lie
algebra is one-dimensional and abelian. Its infinitesimal bracket gain
vanishes, although the group is noncommutative. Row 1053's Lemma EVEN
adds the relevant invariant-sector restriction: conjugation by $j$
inverts every circle variable, so invariant functions restricted to that
component are even. The cosine plaquette in (18) obeys that restriction.
Restricting every sheet to the identity component gives the XY control;
that restriction is a different model, not a proof for the full Pin(2)
measure with fluctuating components. A massless phase of the latter is
used only as a GUIDE-grade test. No claimed theorem for it enters this row.

### 5.5 Five-dimensional face — PROVED scope; isotropic test remains GUIDE

For the $2+3$ split, replace the transverse torus by
$(\mathbb Z/T\mathbb Z)^3$. Then there are $3T^3$ edges, $3T^3$
plaquettes, and six edges incident to a vertex. The reduction and
reflection-positivity proofs are unchanged. The anchor remains a product
of two-dimensional O(4) sheets. The proved Ward upper bound becomes
$H_x\leq6\beta I$, and (15) becomes
$m_{L,T}\geq a(\beta)-6\lambda LT^3$. The four-link conditional sign
counterexample also embeds in a transverse square.

Thus the pieces proved here do not distinguish four from five dimensions,
and none claims an isotropic gap in either. A hypothetical uniform
five-dimensional *face* gap would still need a descent theorem to give
an isotropic gap. The expected weak-coupling five-dimensional behaviour
therefore tests that combined claim; it does not by itself refute a face
gap or force dimensional selectivity to occur at this step.

## Step 6 result: verification and disposition

The self-check recomputed the quaternion derivative and its sign, the
incoming-edge inversion, the two adjacent-plaquette contribution in (9),
the conditional FKG ratio, the transfer min–max comparison, and the
finite-group counts by hand. The source first-failure locations are
OpenAI (3.6), p. 13, for independent sheet rotations, and §3.11.3's
conditional-XY statement, p. 31, for the all-observable conversion.
The original §3.11.1 sign argument is on pp. 29–30. Equations (3.67)
and §3.12.1, p. 32, retain their unpinned scope.

The public search confirmed OpenAI's primary source and located Orland's
anisotropic principal-chiral-model work; no new stability theorem was
imported from that search. Both Sussman–Alpoge files were fetched once at
`31a47c543775`. The full account was searched through its index and read
only at CA-I 2697–2713; the outline's source read was 588–599. Neither
whole source was read. No Balaban paper was downloaded or copied.

`pdftotext` was unavailable; PyMuPDF supplied text and page images instead.
This was source extraction, not a mathematical calculation. No numerical
experiment, computer-assisted proof, or Lean run supplied a step. This
session's rereading is a self-check, not an independent review.
Only this research file changes; queue, registry, audit and science status
files remain untouched.

The next scientific decision is whether a local stability theorem can be
proved from the *unpinned* O(4) input for the transverse plaquette
perturbation. The present argument neither supplies nor refutes that
theorem. Its first required conclusion is a strictly positive interval
in (17), with constants independent of transverse size; no amount of
reusing (15) changes its shrinking interval.

RESULT: PROVED the transverse-torus face reduction and longitudinal reflection positivity, the residual-group Ward port (5)–(8), and explicit failures (9), (12) of the independent-sheet and conditional-ferromagnet ports; PROVED given OpenAI the anchor and finite-cylinder bound (15), whose common perturbative interval is only {0}; a positive size-uniform interval and the rest of FACE-SG-T remain OPEN, with no isotropic or continuum mass gap claimed.
