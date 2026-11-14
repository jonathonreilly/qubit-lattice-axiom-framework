## Repo search

**ARGUED — reading record.** This note addresses FINISH row 771, at
`90650434f231480ba54381c5476ac5cdc0017ebf`. The target-specific prior note
`prior/gap-channel-astra.md` was absent. The November 8 repository-search
digest concerns earlier RG obligations, not this channel decomposition.
Its snapshot copies are not independent evidence. The task row contains no
additional “Repo prior work” hit. No matching channel owner was found in
`open-registry.md`, `open-core.md`, or `l17c.md`. Row 772 owns the separate
literature search; this note does not take over that work.

The close prior results are:

| Source | Closeness and use |
|---|---|
| `gap-transfer.md` Sections 8, 9.3 | Claude Opus 5.5's finite-volume transfer and centre decomposition, crediting the earlier Codex/Astra construction. Reused, not reproved. |
| `gap-flux-exercise.md` Sections 8.2–8.4 | Claude Fable 5.2's reduction of local observables to the centre-even sector; crossing uses larger flux sets. Reused. |
| `gap-means-max.md` Sections 4.1–4.6 | Claude Fable 5.2's Theorem R, crossed weights, and the definition of (ES). Inputs to this note. |
| `gap-es1-opus.md` Sections 2, 5 | Claude Opus 5.5's exact crossed-trace identity, flux-variance bounds, and conditional fusion criterion. Reused without repeating those proofs. |
| `gap-skeleton-final.md` Section 13.20 | Locates the open quantitative seed and the earlier failed linear bound. Its summaries are not additional premises. |
| PR #10114, `MASS_GAP_CONSTRUCTION_ASTRA.md` Sections 1.1–1.2 | Codex/Astra's finite Wilson transfer, injectivity, and finite-volume gap. Source read at `f76f6c649cff7dffbab664d8976e680e8f287fe9`. This gives no uniform seed or channel comparison. |
| PR #10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149 | A positive one-step loop witness and a local convolution inequality. Not a bound on the full thermal trace. |
| Main, `docs/HIGGS_MASS_WILSON_LOOP_SPECTROSCOPY_BOUNDED_NOTE_2026-05-10_higgsH3.md` 27–115, 135–159, 314–332 | Already constructs the spatial plaquette sum and cites Morningstar–Peardon. It is a numerical SU(3) diagnostic with named limitations, not the SU(2) seed proof. No number is imported. |
| PR #10133, `REVIEW_FLOW_S11.md` 268–286 | Charge-conjugation covariance of fine quadratic operators, not physical transfer channels. |
| PR #10134, `docs/KOIDE_MASSIVE_DOUBLING_REDUCES_TO_TRANSFER_POSITIVITY_NOTE_2026-06-02.md` 22–63, 183–201 | Finite Dirac-transfer algebra; its “doubling” is spinor doubling, not a change of torus size. |
| `twisted-order-calculus.md` 1–38 | Magnetic translations of a constant-background covariant Laplacian. Different operator from the gauge-invariant twisted transfer used here. |

Current-main rules were read at `a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc`.
The science baseline stays pinned. The main workflow now points to RULES,
SETTINGS, and the research procedure. This is the assigned research note,
not a new campaign, audit, or status change.

**ARGUED — search boundary.** Targeted follow-ups used
“Billoire”, “Morningstar”, “symmetry channel”, “little group”,
“glueball … irrep”, and “charge conjugation”.
The PR heads fetched were #10114 at `f76f6c649c`, #10133 at `89faef229f`,
#10134 at `1e70c7211a`, and #10141 at `fb99b4dddc`.
The last differs from the older digest's snapshot.
The main YM4D paths and #10141 snapshot paths supplied no matching
channel proof under these terms. Broader hits included the two main
documents above and unrelated spinor/Koide notes. These are bounded
searches, not a claim of exhaustive absence. No hit read supplies this
channel form of (ES), so the assigned work was not stopped as a duplicate.

### Source and status contract

Author: **Codex gpt-6-astra max**, row 771, slot repo2f, 2026-11-12.
Research text; no independent check and no scientific status granted.
**PROVED** below means a written argument from the explicitly named inputs,
not a repository grade. **ARGUED** identifies an unverified application;
**GUIDE** identifies physical motivation; **OPEN** identifies a missing estimate.
No numerical proof, enumeration, fitted spectrum, or computer certificate is used.

**ARGUED — source record.** Credit Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text. Their outline and CA-I were each
fetched once at `31a47c543775`. Index rows and neighbours were read before
the source excerpts. Outline 2313–2336 supplies the positive transfer trace;
25675–25689 supplies symmetry covariance, including
`V_w U_x V_w^{-1}=U_{wx}`. These are already their results.
Outline 588–599 and 31860–31882 explicitly keep a positive mass gap separate.
The CA-I 4.12–4.19 index search found no physical channel-spectrum result.
This is a bounded search record, not an assertion that the entire account
lacks one. CA-I 2670–2714 was also read using the port-map locator:
its Theorem 0 gives a unitary spatial signed-permutation action and
explicitly does not assert a mass gap. Berg and Billoire (1983), and
Morningstar and Peardon (1999),
are the task's spectroscopy precedents; no uninspected numerical or
theorem claim from those papers is used. The permitted paper directory
`/Users/jonBridger/ym4d-papers` was absent.

### Checkpoint

**PROVED given the stated inputs — completed written result.** Sections
1–5 construct the channels and exact trace identities. Section 6 tests
their proposed uses. **OPEN:** the quantitative (ES) estimates at one
physical size. The next input is stated in Section 7; it remains with
the existing owners. No second-model check was requested or performed.

## 1. The correct symmetry labels

**PROVED given the transfer inputs — conventions.** Initially the lattice
spacing and time step are one. Thus $a\geq3$ is an integer side length.
All transfers are for Wilson SU(2) at the same $\beta>0$; every spatial
side length is an integer at least three.
For a rectangular spatial torus $B$, write

$$
R_{B,m}=\frac{T_{B,m}}{\lambda_0(B)},\qquad
e(B)=\log\lambda_0(B),\qquad E_0(B)=-e(B).
\tag{1}
$$

Here $\lambda_0(B)$ always belongs to the *periodic* box. The inputs
(TM-tw), (F1), (S3) of Theorem R imply $0\leq R_{B,m}\leq1$.
We use its positive eigenvalues, with multiplicity. A zero eigenvalue
contributes zero to every trace below; give it energy $+\infty$.
No assertion about an unbounded logarithm's domain is needed.
These conventions preserve the absolute normalization needed by $\delta$.

### 1.1 Periodic boxes

**PROVED.** Let $A_B=\prod_{i=1}^3\mathbb Z/L_i\mathbb Z$ be the translation
group. Let $K_B$ be the signed permutations preserving the three lengths.
For a cube, $K_B=O_h$. Write $U_x,U_R,C_s$ for translations, spatial
isometries, and the centre flips, with $s\in\mathbb F_2^3$.
Each commutes with the periodic transfer, but

$$
U_RU_xU_R^{-1}=U_{Rx},\qquad
U_RC_sU_R^{-1}=C_{Rs}.
\tag{2}
$$

Translations commute with the flips on gauge-invariant functions: moving
a flip plane changes it by a site gauge transformation. Consequently
the relevant group is $(A_B\times\mathbb F_2^3)\rtimes K_B$.
It is not a direct product of momentum and cubic labels.

The simultaneous momentum and centre projectors are

$$
Q_p=\frac1{|A_B|}\sum_{x\in A_B}e^{-ip\cdot x}U_x,\qquad
P_q=\frac18\sum_{s\in\mathbb F_2^3}(-1)^{q\cdot s}C_s .
\tag{3}
$$

Here $p_i=2\pi n_i/L_i$ modulo $2\pi$, and $q_i\in\mathbb F_2$.
Character orthogonality proves that these are orthogonal projections
resolving the identity. Equation (2) maps $(p,q)$ to $(Rp,Rq)$.
At fixed $(p,q)$ use the little group

$$
K_{B;p,q}=\{R\in K_B:Rp=p\pmod{2\pi},\ Rq=q\}.
\tag{4}
$$

Its irreducible representations, or equivalently representations induced
over the orbit of $(p,q)$, are the correct remaining labels.
Parity sends $p$ to $-p$. A parity eigenvalue and a fixed momentum are
simultaneous labels only when inversion preserves that momentum block.
At $p=0,q=0$ on a cube the labels are
$A_1^\pm,A_2^\pm,E^\pm,T_1^\pm,T_2^\pm$.
At generic momentum they must be replaced by little-group labels.
Using all individual $(p,q)$ blocks counts an orbit once per pair; using
an induced representation counts it once with the orbit multiplicity.
These two conventions must not be mixed.

*Proof of covariance.* Pullback by a lattice isometry permutes links,
inverting a variable when its orientation reverses. It preserves Haar
measure, the Wilson potential, the temporal convolution, and gauge averaging.
The centre-flip argument is Section 9.3 of the transfer note.
Composing these pullbacks gives (2). A flip plane can be translated back
by flipping the sites in the intervening slab. This proves the commuting
translation/centre assertion on the physical space. The finite character
sums in (3), followed by (2), prove the remaining claims.

**PROVED — SU(2) has no physical $C=-$ block here.** Charge conjugation
acts linearly on functions by pullback, $(\mathcal C f)(U)=f(U^*)$.
For $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\in SU(2)$,
$U^*=JUJ^{-1}$. Simultaneous complex conjugation of all links is therefore
the constant site gauge transformation $J$. Thus $\mathcal C=1$ on the
gauge-invariant Hilbert space, also with a central twist.
The projector $(1-\mathcal C)/2$ is zero.
This is distinct from anti-linear conjugation of a wavefunction.

### 1.2 Magnetic twists

**PROVED — the blanket cubic assertion in the task needs a restriction.**
A rotation maps $T_{B,m}$ to $T_{B,Rm}$, after identifying the two boundary
conventions. At fixed $m$, only the stabilizer of $m$ can act.
For example the SU(2) magnetic vector $(1,0,0)$ is changed by exchanging
the first two spatial axes. That exchange does not commute with a transfer
operator on that one fixed twisted box. Full cubic covariance is restored
on the direct sum over the orbit of twists.

**PROVED — a finite group that avoids assuming untwisted momenta.**
Represent the spatial twist by a closed plaquette cochain
$b\in C^2(B;\mathbb F_2)$, with class $m$. The spatial Wilson term contains
$(-1)^{b_p}\operatorname{tr}U_p$. A centre change on links,
$U_e\mapsto(-1)^{\eta_e}U_e$, changes $b$ by $d\eta$.
If a lattice isometry $g$ preserves $[b]$, choose $\eta$ with

$$
d\eta=b+g b .
\tag{5}
$$

The combined isometry and link change preserves the twisted action,
Haar measure, temporal convolution, and gauge projection. Pairs $(g,\eta)$
compose by $(g,\eta)(h,\xi)=(gh,\eta+g\xi)$.
Quotient by exact link cochains, which are site centre gauges.
This gives a finite symmetry group $\widetilde K_{B,b}$ with

$$
1\longrightarrow H^1(B;\mathbb F_2)
\longrightarrow\widetilde K_{B,b}
\longrightarrow (A_B\rtimes K_B)_{[b]}
\longrightarrow1 .
\tag{6}
$$

The kernel is the group of winding flips. Equation (5) has a solution
precisely because the cohomology classes agree. This proves surjectivity;
closed link cochains modulo exact ones give the stated kernel.
The induced unitaries commute with $T_{B,m}$.

One may use irreducible representations of this finite group. At fixed
$q$, use the subgroup preserving its character. This suffices for every
trace decomposition below. Equation (6) does not assume a split extension.

**PROVED — an explicit twisted momentum convention.** Let
$\mathfrak m_{ij}\in\mathbb F_2$ be the magnetic flux through the $ij$
plane, with $\mathfrak m_{ji}=\mathfrak m_{ij}$ modulo two.
Choose $b_{ij}(x)=\mathfrak m_{ij}$ on the plaquettes with
$x_i=L_i-1,\ x_j=L_j-1$, and zero elsewhere.
For translation by $e_i$, take the compensating cochain $\eta_i$ on
$j$-links at $x_i=0,\ x_j=L_j-1$, with coefficient $\mathfrak m_{ij}$,
for every $j\ne i$. Its derivative is $b+\tau_i b$: in the $ij$ plane
the two nonzero rows are $x_i=L_i-1$ and $x_i=0$.
Let $S_i$ be this lifted translation.

The lift commutator for $i,j$ is the site centre gauge whose site sign
is negative at $x_i=x_j=0$, if $\mathfrak m_{ij}=1$.
Indeed its coboundary has precisely the four link rows from
$\eta_i+\tau_i\eta_j+\eta_j+\tau_j\eta_i$.
Other plane contributions cancel. Thus the $S_i$ commute on physical
states. Composing $L_i$ translations sweeps the compensating row through
all $x_i$, giving a full flip plane in each relevant $j$ direction:

$$
S_i^{L_i}=\prod_{j\ne i}C_j^{\mathfrak m_{ij}},\qquad
e^{ip_iL_i}=(-1)^{\sum_j\mathfrak m_{ij}q_j},\qquad
p_i=\frac{2\pi}{L_i}
\left(n_i+\frac12\left[\sum_j\mathfrak m_{ij}q_j\right]_2\right).
\tag{6a}
$$

Here $n_i$ runs modulo $L_i$, and $[\,]_2$ is reduction to zero or one.
This also proves the allowed phases by diagonalizing the commuting finite
order unitaries. The projector at fixed $q$ is the product of
$L_i^{-1}\sum_{r=0}^{L_i-1}e^{-ip_ir}S_i^r$.
Orthogonality follows from the differences $2\pi(n_i-n_i')/L_i$;
the phase in $S_i^{L_i}$ makes each factor idempotent.
Different choices of lift can relabel phases by centre characters.
Equation (6a) states our convention explicitly. In the centre-even sector
the shifts vanish. For charged twisted sectors they need not vanish.
Use the stabilizer of this joint translation/centre character in (6)
for its point-group label.

## 2. Loop operators for the channels

### 2.1 Projection, including the signs

**PROVED.** Let $W_\ell(U)=\tfrac12\operatorname{tr}\prod_{e\in\ell}U_e$
be a spatial closed-loop function; products of such functions are also
allowed seeds. Its centre charge is its winding vector modulo two:

$$
C_s W_\ell=(-1)^{s\cdot w(\ell)}W_\ell.
\tag{7}
$$

Each intersection with a flip plane supplies one sign. Backtracking
intersections cancel modulo two. Thus a contractible loop has $q=0$;
a once-winding loop along axis $i$ has $q_i=1$.
A product has the sum of its charges.

For a finite symmetry group $G$ acting within a fixed block, choose unitary
irreducible matrices $D^\alpha$ of dimension $d_\alpha$. Define

$$
E^\alpha_{ij}=\frac{d_\alpha}{|G|}
\sum_{g\in G}\overline{D^\alpha_{ij}(g)}\,U_g,\qquad
\Pi_\alpha=\sum_iE^\alpha_{ii}.
\tag{8}
$$

Schur orthogonality gives
$E^\alpha_{ij}E^\gamma_{kl}
=\delta_{\alpha\gamma}\delta_{jk}E^\alpha_{il}$ and
$(E^\alpha_{ij})^*=E^\alpha_{ji}$.
In particular $\Pi_\alpha$ is an orthogonal isotypic projector.
It commutes with the transfer.
These identities follow by substituting $gh=k$ in the two finite sums
and applying matrix-coefficient orthogonality.

For the periodic cube at $p=q=0$, use proper rotations $O$ of order 24,
then project inversion $\mathcal I$ and charge conjugation:

$$
\mathcal O^{\Gamma,\eta,c}_{ij}[\ell]
=Q_0P_0\,\frac{1+\eta\mathcal I}{2}
\,\frac{1+c\mathcal C}{2}
\,\frac{d_\Gamma}{24}
\sum_{R\in O}\overline{D^\Gamma_{ij}(R)}\,W_{R\ell}.
\tag{9}
$$

Here $\eta,c\in\{+1,-1\}$; $c=-1$ gives zero for SU(2).
At nonzero $(p,q)$ apply (8) for $K_{B;p,q}$ to $Q_pP_qW_\ell$.
Inversion is part of that irrep only when it preserves the block;
otherwise omit the separate parity projector of (9).
For a twist use (8) for the group in (6), restricted at fixed $q$,
or its little groups after (6a). Its loop images include the signs in (5).
Formula (9) is a sum of rotated loop shapes, with relative signs or
matrix coefficients; (3) adds spatial Fourier phases. Higher-dimensional
irreps require matrix coefficients, not one list of scalar signs.

**PROVED — explicit cubic choices.** The five proper-rotation matrices can
be defined by their action on these polynomial spaces:

| Irrep | Dimension | Basis defining the matrices |
|---|---:|---|
| $A_1$ | 1 | $1$ |
| $A_2$ | 1 | $xyz$ |
| $E$ | 2 | $2z^2-x^2-y^2,\ x^2-y^2$ |
| $T_1$ | 3 | $x,y,z$ |
| $T_2$ | 3 | $yz,zx,xy$ |

Use an invariant inner product to orthonormalize each basis.
These give the five irreps: the diagonal sign subgroup distinguishes
the three coordinate lines in each $T$ representation, and permutations
act transitively; $E$ is the irreducible sum-zero plane of the permutation
representation on $x^2,y^2,z^2$. The two $T$ representations differ on a
quarter turn. The two one-dimensional characters are distinct.
Finally $1^2+1^2+2^2+3^2+3^2=24$, so the list is complete.
Parity in (9) can be chosen independently of the polynomial degree.

For a concrete first seed, let $L_i$ be the sum over all plaquettes normal
to axis $i$. Orientation reversal has no effect on its SU(2) trace.
Then $L_x+L_y+L_z$ is $A_1^+$, and
$(2L_z-L_x-L_y,\ L_x-L_y)$ is $E^+$.
Subtract the vacuum mean in the $A_1^+$ channel.
Plaquettes alone supply neither a $T$ irrep nor negative parity at zero
momentum: their three-dimensional permutation representation is
$A_1\oplus E$. Use further shapes and (9); a projection may be zero
if a shape has too much symmetry. Odd parity requires a shape combination
not identified with its inversion by rotations and loop reversal.

**PROVED — two further concrete loop constructions.** Let
$B_i(x)=\tfrac12\sum_\ell(U_\ell-U_\ell^{-1})$, where the sum runs over
the four elementary plaquettes touching $x$, based at $x$, with normal
$+e_i$. This is the anti-Hermitian clover field, used here only as a
bounded loop polynomial. It transforms by site gauge conjugation and as
an axial vector under spatial signed permutations.
Consequently

$$
\left(\sum_x\operatorname{tr}B_yB_z,\quad
      \sum_x\operatorname{tr}B_zB_x,\quad
      \sum_x\operatorname{tr}B_xB_y\right)
\quad\hbox{transforms as }T_2^+.
\tag{9a}
$$

Each term expands into signed traces of concatenated plaquette loops.
For a parity-odd scalar, define the centred covariant difference

$$
(\nabla_jB_k)(x)=\tfrac12\big[
U_j(x)B_k(x+e_j)U_j(x)^{-1}
-U_j(x-e_j)^{-1}B_k(x-e_j)U_j(x-e_j)\big].
$$

It has one polar spatial index and one axial index. Hence

$$
\sum_{x,i,j,k}\varepsilon_{ijk}
\operatorname{tr}\big(B_i(x)\nabla_jB_k(x)\big)
\quad\hbox{transforms as }A_1^- .
\tag{9b}
$$

Gauge invariance follows from the displayed parallel transports.
A proper rotation preserves the contraction; inversion changes the
difference's sign and preserves each axial field. These facts prove
the stated channels. Expanding again gives closed-loop words with signs.
The claim is their transformation law, not a spectral overlap lower bound.
Together with (9), these constructions make the “standing-wave shape”
choice explicit beyond the scalar plaquette sum.

### 2.2 What these operators do and do not span

**PROVED.** In a fixed magnetic background its positive ground state
$\Omega_m$ is invariant under the group in (6). Indeed a measure-preserving
configuration symmetry takes it to another positive normalized ground
state; simplicity makes these equal. Therefore

$$
\Pi_\alpha(M_W\Omega_m)=M_{\Pi_\alpha W}\Omega_m .
\tag{10}
$$

This is a state-creation formula within that background. A Wilson-loop
multiplication operator does not change $m$. The magnetic crossed sectors
in Theorem R require their own twisted transfers, or a separately defined
operator between boundary-condition spaces. Symmetrizing periodic loops
does not create all those sectors.

**PROVED — completeness requires the whole loop algebra.** On a finite
connected graph fix a spanning tree. Gauge orbits are simultaneous
conjugacy classes of the remaining based holonomies $V_1,\ldots,V_k$.
Write $V_j=s_j1+i\,v_j\cdot\sigma$.
Traces of words of length one determine $s_j$; words of length two
determine $v_i\cdot v_j$; length three also determine the oriented triple
products. Equal such data give an orthogonal map between the vector
families. If their span is three-dimensional, the triple products fix its
orientation. If the span has lower dimension, choose its extension with
positive determinant. Hence an $SO(3)$ map, lifted to SU(2), conjugates
the two families. Loop traces therefore separate gauge orbits.

The unital real algebra generated by all loop traces is dense in
continuous functions on the compact orbit space, by Stone–Weierstrass.
Continuous functions are dense in its finite Haar $L^2$ space.
$\Omega_m$ is continuous with a positive minimum on the compact
configuration space, so multiplication by it preserves density.
Applying bounded projectors gives density in each channel.
This proves completeness for projected *loop polynomials*, with arbitrary
shapes. It proves no completeness for a finite spectroscopy basis.

**GUIDE.** Selecting shapes with large overlap can make a variational
calculation efficient, as in the spectroscopy precedents named above.
Neither a large overlap nor a finite loop basis supplies a lower spectral
bound or counts states omitted from that basis.

## 3. The two seed numbers and the crossed weights

### 3.1 Positive channel traces

**PROVED given the transfer inputs.** Fix $z=(q;m)$ and decompose its
Hilbert space by the actual symmetry projectors of Sections 1–2.
Let $\alpha$ range over those blocks, and let $j$ count every eigenvector,
including representation multiplicity. Set

$$
E_{z,\alpha,j}(B)=-\log\frac{\lambda_{z,\alpha,j}(B)}
                                     {\lambda_0(B)}\geq0,\qquad
F_{z,\alpha}(t;B)=\sum_j e^{-tE_{z,\alpha,j}(B)} .
\tag{11}
$$

Thus $F_{z,\alpha}=\operatorname{Tr}(\Pi_{z,\alpha}R_{B,m}^{\,t})$.
All summands are nonnegative and the sum is finite for integer $t\geq1$.
In a block with representation dimension $d_\alpha$, one can instead
sum eigenvalues on the multiplicity space and multiply by $d_\alpha$.
This follows because an operator commuting with an irreducible finite
group action is the identity on its representation factor.

For the periodic cube the unique vacuum lies in

$$
\alpha_{\rm vac}=(p=0,\ q=0,\ A_1^+,\ C=+).
\tag{12}
$$

The same positive-ground-state argument as (10) proves (12).
Only its one vacuum eigenvector is removed, not the whole $A_1^+$ block.
The exact thermal number of (ES) is

$$
\boxed{\displaystyle
\epsilon(a)=
\sum_{\alpha}\sum_{j:\,(z,\alpha,j)\ne{\rm vac}}
e^{-aE_{0,\alpha,j}(a^3)} ,
\qquad z=0=(0;0).}
\tag{13}
$$

The sum includes all allowed momenta and all little-group irreps in the
centre-even periodic sector. There is no cancellation between channels.
The definition of (ES) is

$$
\epsilon(a)\leq10^{-7},\qquad
\delta(a)=a\{E_0((2a)^3)-8E_0(a^3)\}\leq10^{-7}.
\tag{14}
$$

Both numbers are nonnegative by the cited transfer and doubling inputs.

### 3.2 Heavy crossed weights

**PROVED.** Use the sixteen crossed sectors $X$ of Theorem R:
$q=(0,x_1,x_2)$ and $m=(0,x_3,x_4)$, $x\in\mathbb F_2^4$.
For $A=(a,c,d)$, put $\epsilon_A=S_{\rm ev}(a;A)$ and

$$
p_z=\frac{Z_z(a;A)}{Z_0(a;A)}
=\sum_\alpha w_{z,\alpha},\qquad
w_{z,\alpha}=\frac{F_{z,\alpha}(a;A)}{1+\epsilon_A}.
\tag{15}
$$

The prior crossing lemma gives $0\leq p_z\leq1$ and $\sum_Xp_z=4$.
For any choice of four sectors $L\subset X$, the heavy weight is exactly

$$
\boxed{\displaystyle
H_L=\sum_{z\notin L}\sum_\alpha w_{z,\alpha}
=\frac{\sum_{z\notin L}\sum_{\alpha,j}
                e^{-aE_{z,\alpha,j}(A)}}{1+\epsilon_A}.}
\tag{16}
$$

Without (ES), “heavy” only names this complement. It asserts no energy
bound. Under Theorem R's smallness hypothesis, $L=\{p_z>1/2\}$ is its
four-element isotropic group; that group construction is prior work.

Rotations can equate terms in (15) only when they preserve the geometry
and the relevant set of sectors. A general cubic rotation can leave the
crossed slice $X$. A fixed-$z$ operator sees the stabilizer of $z$.
An arbitrary chosen $L$ need not be a union of full cubic orbits.
Use the subgroup preserving $X$ and $L$ before replacing sums by orbit
multiplicities. No extra factor of 24 or 48 is automatic.

### 3.3 An exact channel form of the vacuum defect

**PROVED — a logarithm of channel sums, not a sum of channel ground
energies.** For $A=(a,c,d)$ and $A'=(2a,c,d)$, let

$$
\Delta_A=a\{2e(A)-e(A')\},\qquad
\epsilon'_A=S_{\rm ev}(a;A').
$$

Lemma 2.1 of the Opus note is the already proved crossing identity

$$
e^{-\Delta_A}(1+\epsilon'_A)
=\frac14\sum_{z\in X}\sum_{\alpha,j}
                   e^{-2aE_{z,\alpha,j}(A)} .
\tag{17}
$$

It immediately gives

$$
\boxed{\displaystyle
\Delta_A=
\log(1+\epsilon'_A)
-\log\!\left(\frac14
\sum_{z,\alpha,j}e^{-2aE_{z,\alpha,j}(A)}\right).}
\tag{18}
$$

Use the three shapes
$A_1=(a,a,a)$, $A_2=(a,2a,a)$, $A_3=(a,2a,2a)$, each doubled in
its first coordinate. Permuting coordinates identifies the intermediate
boxes of Theorem R. Then

$$
\boxed{\delta=4\Delta_{A_1}+2\Delta_{A_2}+\Delta_{A_3}.}
\tag{19}
$$

Every term in the sums in (18) is a channel trace. The logarithm must stay.
A direct-sum decomposition of a Hamiltonian does not make its ground
energy the sum of the channel ground energies.

There is also a nonnegative channel sum *inside* this exact expression.
Define, for every eigenvector counted in (11),

$$
v_{z,\alpha,j}=\frac{e^{-aE_{z,\alpha,j}(A)}}{1+\epsilon_A},\qquad
D_{z,\alpha}=\sum_j v_{z,\alpha,j}(1-v_{z,\alpha,j}),\qquad
D_A=\sum_{z,\alpha}D_{z,\alpha}.
\tag{20}
$$

Since $\sum_{\alpha,j}v_{z,\alpha,j}=p_z\leq1$, each $v$ lies in
$[0,1]$, and every $D_{z,\alpha}\geq0$. Also $\sum_{z,\alpha,j}v=4$.
Substitution into (17) proves

$$
1-\frac{D_A}{4}
=\frac{e^{-\Delta_A}(1+\epsilon'_A)}{(1+\epsilon_A)^2}>0,
\qquad
\boxed{\Delta_A=
-\log(1-D_A/4)+\log(1+\epsilon'_A)-2\log(1+\epsilon_A).}
\tag{21}
$$

Equations (13), (16), and (19)–(21) are the requested channel
decompositions. Equation (21) does not assign positive additive pieces
of $\delta$ to independent glueball species.

**PROVED — relation to the existing flux variance.** Write

$$
Q_A=\sum_zp_z(1-p_z),\qquad
J_z=p_z^2-\sum_{\alpha,j}v_{z,\alpha,j}^{\,2}\geq0 .
$$

Then

$$
D_A=Q_A+\sum_zJ_z.
\tag{22}
$$

Indeed $J_z$ is the sum of $v_iv_k$ over ordered distinct eigenvectors
in sector $z$. Thus it includes pairs within one irrep and between irreps.
The Opus flux-variance lower bound drops these nonnegative terms.
Keeping them gives an exact refinement of that identity, not a replacement
proof of its crossing lemma. A refinement of $p_z$ into cubic channels
does not give a separate crossing equation for each refined label.

### 3.4 Information forced by an already small seed

**PROVED — a necessary restriction, not a way to prove (ES).** Equation
(21), $\epsilon'_A\geq0$, and $\Delta_A\geq0$ imply

$$
0\leq D_A\leq
4\{1-e^{-\Delta_A}(1+\epsilon_A)^{-2}\}
\leq4(\Delta_A+2\epsilon_A).
\tag{23}
$$

For any sector with $p_z>1/2$, let $v_{\max}$ be its largest individual
eigenvector weight. Compactness ensures that it exists. Since
$\sum v_i^2\leq v_{\max}p_z$,

$$
p_z-v_{\max}\leq \frac{J_z}{p_z}\leq 2D_A .
\tag{24}
$$

If its top eigenvalue had multiplicity at least two, then
$v_{\max}\leq p_z/2$ and $J_z\geq p_z^2/2>1/8$.
Thus $D_A<1/8$ forces a simple top eigenvalue in every such sector.
Its eigenspace is then a one-dimensional representation of the symmetries
preserving that sector. The remaining spectral weight is bounded by (24).

For $A_1$ under (ES), $\Delta_{A_1}\leq\delta/4$ and
$D_{A_1}\leq9\,10^{-7}<1/8$. Hence each of Theorem R's four light
crossed sectors has this single-state dominance. This does not determine
its parity or momentum, and does not identify which sectors are light
before the seed is established. It is information symmetry can extract
from a quantitative bound; symmetry does not supply that bound.

## 4. Doubling the box: new modes and the vacuum channel

### 4.1 The exact kinematic inclusion

**PROVED for spatial functions, not for interacting energy eigenstates.**
On $\mathbb Z_{2a}^3$, Fourier momenta are $p_i=\pi n_i/a$ with
$n_i\in\mathbb Z_{2a}$. The pullback of a function on $\mathbb Z_a^3$
is invariant under the three half-period translations $x\mapsto x+ae_i$.
Conversely that invariance makes it a function on $\mathbb Z_a^3$.
A Fourier function has this property exactly when all $n_i$ are even.
With counting-measure norms the isometric pullback is
$f(x)\mapsto2^{-3/2}f(x\bmod a)$.

More explicitly, the eight orthogonal projections are

$$
\mathsf Q_r=\frac18\sum_{s\in\mathbb F_2^3}
                 (-1)^{r\cdot s}\tau_{as},
\qquad r\in\mathbb F_2^3 .
\tag{25}
$$

Their Fourier supports are $n\bmod2=r$. Each contains $a^3$ Fourier
modes. The old modes are $r=0$; seven new classes have at least one odd
component. Cubic rotations group them by Hamming weight:

| Odd components | Number of classes | Smallest nonzero $\lVert p\rVert$ in a class |
|---:|---:|---:|
| 1 | 3 | $\pi/a$ |
| 2 | 3 | $\sqrt2\,\pi/a$ |
| 3 | 1 | $\sqrt3\,\pi/a$ |

These are momenta, not proved energies. Even the old $r=0$ class contains
nonzero momenta. Cubic irreps and the parity vector $r$ are different
decompositions.

**PROVED — distinction on the transfer Hilbert space.** Equation (25)
also decomposes the periodic $2a$-box Hilbert space, now by *total*
momentum modulo these half translations. Its $r=0$ subspace is not
identified with the Hilbert space of the $a$-box by the preceding map.
Repeating a small link configuration constrains distinct Haar link
variables to equality, a set of measure zero in the large configuration
space. Pulling a small-box function from a chosen subset of links instead
does not intertwine the actions across the old seams.
Neither construction proves $T_{2a}J=JT_a$.

Eight independent periodic boxes and one periodic doubled box have
different seam identifications and gauge constraints. Their Fourier
labels do not identify their spectra. A spectral inclusion, trial-state
gluing estimate, or comparison of their ground energies is an additional
statement. None is supplied by the kinematic inclusion.

### 4.2 Which channel carries the defect?

**PROVED.** In its original frame both ground states in (14) have the
vacuum label (12). In that precise sense $\delta$ is a difference in
the scalar, zero-momentum, centre-neutral, parity-even channel.
It is not a sum of the lowest nonzero-momentum energies newly allowed
by doubling. Equations (17)–(21), in a crossed frame, express this scalar
number through every allowed channel of the sixteen flux sectors.

**PROVED — scalar does not mean one elementary mode.** If an operator
$A$ commutes with a symmetry group and $\Omega$ is invariant, then
$A\Omega$ is invariant. Thus its vacuum-to-state matrix elements vanish
in nontrivial *total* representations of that group.
However, for every unitary irrep $V$, $V\otimes V^*$ contains the invariant
vector $\sum_i e_i\otimes e_i^*$. Opposite momenta add to zero, equal
SU(2) centre charges add to zero, and equal parities multiply to plus.
Pairs of modes from any nontrivial channel can therefore have the
vacuum quantum numbers. Two modes with odd $n$ can have total $r=0$.

**ARGUED — physical reading, not a spectral construction.** Interacting
vacuum energy can be sensitive to such neutral composites and to winding
objects. No particle or oscillator decomposition of the Wilson vacuum is
assumed here. If a gluing interpolation breaks translations or rotations,
its selection rule is only that of its common unbroken subgroup.
It cannot inherit the full cubic selection rule by naming its endpoints.
Symmetry alone removes no additional term from (18) or (20).

## 5. Reflection positivity and the quantitative estimates it would need

### 5.1 Positivity survives the projection

**PROVED given reflection positivity.** A spatial symmetry preserving
the action and commuting with time reflection acts unitarily on the
reflection-positive quotient. Its finite character projectors are
orthogonal there. Equivalently, on the transfer space, for a projected
vector $\psi_\alpha$ and integer $t\geq1$,

$$
\langle\psi_\alpha,R^t\psi_\alpha\rangle
=\sum_j|\langle j,\psi_\alpha\rangle|^2e^{-tE_j}\geq0.
\tag{26}
$$

At $t=0$ use $\langle\psi_\alpha,\psi_\alpha\rangle\geq0$ directly;
no convention for $0\cdot\infty$ or missing kernel eigenvector is needed.
Different orthogonal blocks have zero mixed matrix elements.
The same expansion makes every matrix
$[\langle\psi_i,R^{t_i+t_j}\psi_j\rangle]_{ij}$ positive semidefinite:
its quadratic form is $\|\sum_iR^{t_i}\psi_i c_i\|^2$.
In the periodic vacuum block use $(1-|\Omega\rangle\langle\Omega|)\psi$
for a connected correlation.

Thus the minus signs in (9) do not destroy temporal positivity.
They also do not create negative contributions which could cancel
the positive terms in (13).
This argument concerns Hilbert-space positivity. It does not assert a
pointwise positive kernel for every symmetry projector or signed twist sum.

**PROVED — the useful inequality and its limit.** In each positive
trace-class block, for integer $t\geq1$,

$$
\operatorname{Tr}(S_\alpha^{\,2t})
\leq\{\operatorname{Tr}(S_\alpha^{\,t})\}^2,\qquad S_\alpha\geq0.
\tag{27}
$$

The difference is the sum of products of distinct eigenvalues to power
$t$. Summing (27) gives
$\sum_\alpha\operatorname{Tr}S_\alpha^{2t}
\leq\sum_\alpha(\operatorname{Tr}S_\alpha^t)^2$,
which retains more information than squaring the sum over $\alpha$.
It supplies no small upper bound for any trace at time $t$.

Crossing in (17) exchanges the time direction with a spatial direction.
A fixed spatial momentum or cubic projector before that exchange is
not the same spatial projector after it. Consequently (27) does not
produce Lemma K, or a separate copy of Theorem R, in each cubic channel.
The given crossing formula is the flux sum (17). Any formula with a new
symmetry insertion needs its own transformed boundary insertion.

### 5.2 A lower energy bound needs a state count

**PROVED — a sufficient certificate with its missing inputs visible.**
For the periodic centre-even block let $Q_\alpha^{\rm ex}$ remove the
vacuum only when necessary. Suppose its spectrum has $E_j\geq m_\alpha$.
For integers $1\leq t_0<a$, define
$B_\alpha=\operatorname{Tr}(Q_\alpha^{\rm ex}R^{t_0})$.
Then termwise in the spectrum,

$$
\epsilon(a)\leq
\sum_\alpha B_\alpha e^{-(a-t_0)m_\alpha}.
\tag{28}
$$

The same argument applies to a heavy sector, without removing any
state, if $m_{z,\alpha}$ bounds energies *relative to the periodic
vacuum*, as in (11):

$$
H_L\leq\frac1{1+\epsilon_A}
\sum_{z\notin L,\alpha}
B_{z,\alpha}e^{-(a-t_0)m_{z,\alpha}},
\quad
B_{z,\alpha}=\operatorname{Tr}(\Pi_{z,\alpha}R_{A,m}^{t_0}).
\tag{29}
$$

These are genuine sufficient estimates once the right sides are bounded.
They can reduce a proof to a finite collection of troublesome channels
only if a summable bound already controls the omitted channels.
A bound on the lowest energy alone gives no such $B_\alpha$.
Continuous gauge links leave infinitely many states even on a finite graph.

**PROVED — explicit failure of “gap plus positivity bounds the trace”.**
On $N$ points with the uniform measure, let $P$ project onto constants
and let $R=P+r(1-P)$, $0<r<1$. Its matrix entries are
$r\delta_{ij}+(1-r)/N>0$, its vacuum is simple, and it is a positive
trace-class transfer with excited energy $-\log r$.
Let the spatial symmetries act trivially on this extra state space.
All its states then belong to the scalar, even, neutral channel, but

$$
\operatorname{Tr}R^a-1=(N-1)r^a .
\tag{30}
$$

The gap can be fixed while (30) is arbitrarily large.
This is a counterexample to an inference from symmetry, positivity and
a lowest-energy bound alone. It is not a replacement Wilson action or
a counterexample to a criterion that also uses Wilson state-count estimates.

**PROVED — symmetry gives necessary multiplicities.** If a nonvacuum
level has full symmetry multiplicity $g$ and energy $E$, then
$\epsilon\geq g e^{-aE}$ whenever that level is in the even periodic sum.
Thus (ES) requires $aE\geq\log(g\,10^7)$.
Momentum-star and irrep degeneracies strengthen this necessary condition.
They give no upper estimate on the rest of the sum and no ordering of
the lowest energies of different irreps.

**PROVED — a finite operator basis has the opposite variational direction.**
Compress $R$ to a finite span $V$ of projected loop states, orthogonal
to the vacuum. Its largest Rayleigh quotient is at most the norm of
$R$ on the whole channel. Taking minus its logarithm therefore gives
an *upper* bound on the channel's lowest energy.
Unseen states can have lower energy and arbitrarily small overlap with $V$.
To prove a lower bound, one needs
$\langle\psi,R\psi\rangle\leq e^{-m_\alpha}\|\psi\|^2$ on a dense
set in the entire projected channel, or another estimate on its complement.
Section 2.2 supplies density only when all loop polynomials are admitted;
it supplies no quantitative inequality on them.

### 5.3 Why the vacuum defect needs an additional comparison

**PROVED — normalized channel data alone do not fix $\delta$.**
Multiplying all $T_{B,m}$ at each fixed box by the same $e^{-c_B}$
preserves every normalized eigenvalue, every channel, and positivity.
It changes
$E_0(B)$ to $E_0(B)+c_B$, and changes the defect by
$a(c_{(2a)^3}-8c_{a^3})$.
This proves the stated logical insufficiency of normalized spectral data.
Arbitrary such rescalings need not preserve Wilson locality or crossing;
they are not counterexamples under those additional hypotheses.
For Wilson theory the normalization is fixed, and its cross-volume
comparison remains necessary.

**PROVED — sector gaps and sector offsets are different.** Put
$\mu_z=\|T_{A,m}P_q\|$ and, when $\mu_z>0$, define

$$
d_z=-\log\frac{\mu_z}{\lambda_0(A)},\qquad
s_z=\frac{Z_z(a;A)}{\mu_z^a}-1 .
$$

Then the exact sector weight is

$$
p_z=e^{-ad_z}\frac{1+s_z}{1+\epsilon_A}.
\tag{31}
$$

An internal gap above $\mu_z$ bounds neither its offset $d_z$ from the
periodic ground state nor its thermal multiplicity $s_z$ by itself.
In particular an internally well-gapped twisted box can still have a
light ground state in (31).

**PROVED as a use of the prior theorem, not a new fusion proof.**
Theorem V in the Opus note supplies the actual sufficient bridge.
For four sectors $L$, if
$u_A=\tfrac12H_L+\tfrac12\sum_{z\in L}s_z<1$, it gives

$$
\Delta_A\leq-\log(1-u_A)+\log(1+\epsilon'_A)
                         -2\log(1+\epsilon_A).
\tag{32}
$$

Channel estimates (28)–(29) can feed (32). They must also control
the light-sector $s_z$ and the enlarged-box $\epsilon'_A$.
The bounds are needed at the three shapes in (19).
Equivalently, (18) requires a sufficiently large crossed trace at time
$2a$, not merely nonnegativity of its terms.
The open fusion assumption of Section 5 of the Opus note is another
way to supply these numbers. Decomposing its states into irreps does
not prove that assumption.

**OPEN — the quantitative obligation.** No estimate here supplies the
right side of (28) below $10^{-7}$, or the three right sides of (32)
with weighted sum below $10^{-7}$, at an order-one running coupling.
For physical size $\ell$, restore lattice spacing $h$ and set $a=\ell/h$.
Then $e^{-aE}=e^{-\ell(E/h)}$. The bounds, their summed state counts,
and the absolute vacuum comparison must hold uniformly as $h\to0$
along the prescribed coupling trajectory. The number of momentum blocks
grows in this limit. A finite-cutoff block decomposition is not this bound.

## 6. The U(1) test, applied to each proposed use

**PROVED — the logical test used here is T1–T3 of the first-principles
note, Section 3b.3.** A method valid also for U(1) is not thereby false.
Its hypotheses must fail in any comparison regime where its claimed
seed is false. No Coulomb-phase numerical threshold is used below.

| Candidate | Test and disposition |
|---|---|
| Spatial symmetry projections and temporal positivity imply a seed | **PROVED false at that level of generality.** They also hold for a massless Gaussian gauge field; the explicit even scalar state below prevents the required thermal bound. |
| The absence of SU(2) $C=-$ states removes the massless obstruction | **PROVED insufficient as a symmetry argument.** The comparison field has a neutral $C=+$ two-photon state in $A_1^+$ at zero total momentum. |
| Lowest energy in each channel suffices, without state counts | **PROVED false for general positive transfers**, by (30); U(1) has the same need for a thermal state count. |
| A lower energy bound plus the summed bounds in (28)–(29) suffices for those traces | **PROVED valid conditional estimate.** Its combined smallness hypotheses cannot hold where its conclusion fails. Applying it to strongly coupled U(1) is not a defect. |
| Internal twisted-sector gaps also bound $\delta$ | **PROVED missing the required inputs**, by (31) and the exact comparison (18). Symmetry does not supply offsets or the light-sector thermal sums. |
| Projection to zero momentum and $A_1^+$ is enough to prove the full even seed | **PROVED unjustified.** The omitted even channels in (13) are nonnegative and need upper bounds; even the retained channel admits the comparison obstruction below. |
| The extra single-state restriction (24) proves a seed | **PROVED circular as proposed.** It follows from the already small deficit and thermal sum; it cannot supply them. |

### A hand-checkable scalar obstruction

**PROVED for the stated free model; GUIDE for the interacting U(1)
Wilson theory.** Take the nonzero oscillator modes of free Maxwell
theory on a periodic spatial cube of side $a$, in its zero electric and
magnetic flux sector. Their stipulated free energies are $|p|$,
$p=2\pi n/a$. This defines a positive free Hamiltonian; its thermal
trace is finite at positive time after the zero modes have been removed.
Indeed $\sum_{n\ne0}e^{-t|2\pi n/a|}<\infty$, and the logarithm of the
bosonic product trace is bounded by a constant times this sum.
The positive-time kernel is reflection positive: each oscillator has
kernel proportional to $e^{-\omega(t+s)}$ for reflected times, whose
quadratic form is a positive constant times
$|\sum_i c_i e^{-\omega t_i}|^2$; the Gaussian field inherits this form.

Create two photons of momenta $p,-p$ with $|p|=2\pi/a$.
Contract their vector indices and sum over the cubic orbit. For example,
the two-creation part of
$\sum_{|p|=2\pi/a,i}B_i(p)B_i(-p)$ gives a nonzero such vector.
It has total momentum zero, trivial winding charge, $C=+$, parity plus,
and irrep $A_1$. Its energy is $4\pi/a$. Hence at time $a$

$$
\epsilon_{\rm even}(a)\ \geq\
\epsilon_{A_1^+,\,p=0}(a)\ \geq e^{-4\pi}\ >10^{-7}
\quad\hbox{for every }a.
\tag{33}
$$

The strict inequality needs no decimal computation:
$4\pi<14$, $e<3$, and $3^{14}=4\,782\,969<10^7$.
Two-particle states are essential to this example; deleting a single
photon's channel does not remove (33).
It already defeats a claimed seed, so no Casimir-energy computation
is needed for its vacuum defect.

**ARGUED — scope of the comparison.** This is a free-field example,
not a proof of a Coulomb phase for the compact Wilson measure.
For that measure the large-coupling gapless input has the external
standing recorded in Section 3b.3 of the first-principles note.
Conditional on failure of its seed, T3 gives the same diagnostic:
a successful SU(2) criterion must have a quantitative hypothesis which
fails there. Symmetry and reflection positivity themselves do not fail.
For full U(1) centre symmetry, centre projectors are Fourier integrals
with integer flux labels; its $\mathbb Z_2$ subgroup can also be used.
None of those changes excludes the neutral pair in (33).

## 7. What moved, and the precise remaining task

| Statement | Mark | Consequence |
|---|---|---|
| Correct little groups, twist stabilizers, and trivial SU(2) charge conjugation | **PROVED** from the finite lattice action and gauge invariance | Corrects the proposed labels; removes only forbidden or duplicate labels. |
| Projected loop construction and density of the whole loop algebra | **PROVED** | Provides operators for every nonzero block, including loops within each fixed magnetic background. A finite basis still has an uncontrolled complement. |
| Equations (13), (16), (18)–(22) | **PROVED given the cited transfer and crossing inputs** | Resolves the two seed numbers and heavy weights into actual spectral blocks. Keeps the logarithm and the within-sector terms. |
| Equations (23)–(24) | **PROVED given those inputs** | A small seed forces single-state dominance in the four light crossed sectors. This is new conditional information, not a seed estimate. |
| Half-period modes and the vacuum selection rule | **PROVED** | Separates the seven new Fourier classes from total quantum numbers; establishes no interacting spectral embedding. |
| Channel RP and conditional thermal bounds | **PROVED** | Preserves positivity and gives useful estimates only with quantitative energy and state-count inputs. |
| A smaller unestimated set, such as only the lowest $0^{++}$ state | **OPEN; not justified by symmetry** | All omitted terms still need an upper bound. |
| (ES) at one physical size at order-one running coupling | **OPEN** | Neither number has been bounded by this work. No mass gap is proved. |

**OPEN — next input, with no reassignment.** A useful next channel result
would bound the *complete* heat trace in (28), with a summable remainder,
and provide the offsets and light-sector control required by (32).
The existing fusion and cross-volume lanes retain those obligations.
A claim that one irrep suffices must first provide the bound for its
complement. A list of loop shapes or measured lowest masses is not that
bound.

**ARGUED — verification record.** The equations above are hand arguments.
No numerical job or machine enumeration was run. This is an author
self-check, not an independent check. Only this output file was edited
by this session. Mechanical checks concerned whitespace, display delimiters,
the single final RESULT line, and file identity only; none is proof evidence.

**ARGUED — recovery record.** During the session the supplied checkout's
HEAD moved to `f95704b9f4`, with an unrelated deletion of
`library/gap-pag-grow-astra.md`. The committed diff of this lane from the
requested pin only added that note; the inputs used above did not change.
That work was left untouched. The final text was prepared in the isolated
`/tmp/gap-channel-astra-20261112/worktree` on
`research/gap-channel-astra-20261112`, based at `90650434f`, and copied
back to the requested lane path. No commit or push was made by this session.

RESULT: PROVED by hand from the cited transfer and crossing inputs, not independently checked: the correct symmetry blocks and loop projectors, exact channel forms of epsilon, the heavy weights and delta through (18)–(22), and single-state dominance of light sectors conditional on a small seed; symmetry and channel positivity supply neither quantitative number of (ES), and channel energy bounds also need summed state counts and a vacuum/flux comparison. OPEN: (ES) at one physical size at order-one running coupling. No mass gap or scientific status is claimed.
