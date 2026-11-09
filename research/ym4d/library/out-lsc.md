# A normalization correction and the last-scale constants in Chapter 6

Your Chapter 1 bare density is incompatible with the vacuum-energy substitution in 4.33(h4)(a).
Definition 1.1 sets $`\rho_0=e^{-g_0^{-2}A}`$ at CA-I:477–481.
Definition 1.5 starts its recursion from that density at CA-I:924–933.
But 4.33(h4)(a), CA-I:157039–157041, uses an energy initialized with the vacuum constant of CA-I:159153–159160.
The missing term in the bare convention is $`E_{\rm vac}`$, as (N5) below shows.

The repair uses your existing vacuum-normalized convention:

```math
\widehat\rho_0=e^{-x_0A-E_{\rm vac}},\qquad
\widehat Z=e^{-E_{\rm vac}}Z_{\rm bare},\qquad
\widetilde Z=e^{-\mathcal E}\widehat Z.
```

You write this convention explicitly at CA-II:140916–140926 and outline lines 23405–23415,23515–23527.
At CA-II:140922–140923, you call the corrected density “the density $`\rho_0`$ of Definition 1.5”.
The lower bound concerns $`\widehat Z(0)`$; its bare form retains $`e^{E_{\rm vac}}`$.
This correction leaves probability expectations and source cumulants unchanged.

All account and outline references below are source-file lines at commit `31a47c543775`.
I and II mean CA-I and CA-II, your complete-account parts.
SA means your outline, `YM4_sketch_500.tex`.
Balaban's inputs are read through your quotations and the available literature record; his papers were not independently inspected.
This is a conditional research proof for your review. It is not an audit and grants no scientific status.

## 1. Reconstructed statement

At II:63365–63367, `6.3:lem-last-scale-constants` says:
“The statement of this lemma is not written out here; parts of its proof are printed below.”
The statement below reconstructs what its checked Chapter 6 consumers require.
It is not a claim of literal equality with an unwritten statement.

Your printed proofs already supply (b) at II:63369–63526, (c) at II:63568–63689,
(d) at II:63691–63798, and (e) at II:63800–63833.
Your floor calculation appears at II:109918–109975 and SA:23504–23539.
Your Chapter 4 supplies the normalized vacuum remainder and density bound.
We reproduce these arguments below, retaining their inputs.

The additions are the short offset proof for (a), the explicit common constants on the terminal coupling window,
the normalization reconciliation, and the completion under the original torus floor.
The normalization reconciliation is taken from a separate Codex check of the normalization.
The application is limited to the Chapter 6 uses listed in §6.5 and the original torus floor of clause (iii-b).

**Lemma (reconstruction of `6.3:lem-last-scale-constants`).** Work in dimension four with SU(2) and normalized trace. Fix odd $`L`$, the auxiliary tuple $`\mathfrak p`$, $`\gamma`$, $`\gamma_H<1`$, and $`\varrho>0`$ in your prescribed order. Retain clause (0), the identification $`b_{k+1}(0)=\beta_{k+1}`$, and the correlation theorem's construction and estimates. In particular, retain its source-free representation, real-background, and sourced majorant inputs, specified in §2 below. Use the vacuum-energy convention of I:159153–159160 and II:140916–140926, with the correction to the bare reading of (h4)(a) proved in §3. Do not assume the last-scale conclusion or volume-free correlations.

Write

```math
X=g^{-2},\quad x_0=g_0^{-2},\quad
\lambda=c_0/2,\quad c_5=2c_2,\quad b_+=3\lambda+2c_2,
\quad g_-(g)=(X+B^\sharp)^{-1/2}.
```

The common numerical flow has

```math
K=\min\{k:x_k\le X+B^\sharp\},\qquad
K_J=\max\{k:x_j>X\text{ for all }j\le k\}.
```

Clause (0) gives $`X<x_K\le X+B^\sharp`$, $`K\to\infty`$ as $`g_0\downarrow0`$, and the flow up to $`K`$. The correlation theorem gives

```math
\lambda(j-i)-2c_2\le x_i-x_j\le3\lambda(j-i)+2c_2,
\qquad X<x_{K_J}\le X+b_+ .                         \tag{1}
```

The flow inequality holds for $`0\le i<j\le K_J`$. The numerical flow and its coefficients are independent of the torus.

Let $`R_J(x)`$ be the least integer power of $`L`$ at least $`(\log x)^r`$, with the radius exponent of the common admitted parameter tuple. Define

```math
N_{\mathbb T}(g,m)=L^{11}M\sup_{u\ge0,\ u\in\mathbb Z}
L^{-u}R_J\bigl(X+b_++4c_2+3\lambda(m+u)\bigr),
\quad m_J=m^J_{\mathbb T}(g)=\min\{m\ge0:L^m\ge N_{\mathbb T}(g,m)\}.
\tag{2}
```

The radius exponent $`r`$ here is $`r_{\rm pr}`$ in Chapter 5; that chapter's source-disc radius $`r`$ is our $`\varrho`$. Chapter 5 restricts its radius powers to nonnegative exponents (II:688–699). The conventions agree on the admitted range: $`\gamma_J\le(8c_2+4)^{-1/2}\le1/2`$ (II:2865–2868), so every argument of $`R_J`$ used here is at least $`X\ge4`$.

Distinguish this $`m_J`$ from the physical torus floor

```math
m_{\mathbb T}(g_-)=11+m'+\log_LR(g_-),\qquad M=L^{m'}.
```

Put

```math
\mathcal A=\{0\}\cup\{a\in\mathbb Z_{\ge1}:\lambda a<B^\sharp+c_5\},
\qquad a^\natural=\max\mathcal A .                         \tag{3}
```

Choose $`0<g\le\min\{\gamma_H,\gamma_J,\gamma_D\}`$, where $`\gamma_D`$ ensures

```math
m_{\mathbb T}(g_-),m_J\ge a^\natural.
```

Take any integer $`m_1\ge m_{\mathbb T}(g_-)`$, any $`0<g_0\le g_-(g)`$, and the bare lattice of spacing $`L^{-K}`$ in the torus of side $`2L^{m_1}`$. For real Lipschitz sources, let $`S^T_n`$ be the joint cumulant of

```math
\mathcal O(f)=\sum_p f(x(p))[1-\operatorname{Re}\operatorname{tr}U(\partial p)],
\qquad \|f\|_\sharp=\max\{\|f\|_\infty,40M\operatorname{Lip}f\}.
```

**(a) Bounded offset.** $`K\le K_J`$ and $`a=K_J-K\in\mathcal A`$.

**(b) Last-scale constants.** If $`K_J\ge m_J`$, set

```math
K'=K_J-m_J=K-b,\quad b=m_J-a,\quad
N_T=2L^{m_1-a},\quad N=N_TL^{m_J}=2L^{m_1+b}.                \tag{4}
```

These are admissible correlation-theorem data. Dilation to its side-one torus identifies the bare lattices, Wilson probability measures and source cumulants. Its source norm is no larger than $`\|f\|_\sharp`$. Moreover

```math
X<x_{K'}\le x^*(g):=X+b_++3\lambda m_J+2c_2,
\quad E_+^\sharp+C_{\rm low}\le E_*(L,\mathfrak p,g,\varrho)<\infty. \tag{5}
```

The bound is uniform in $`K,g_0,m_1,a,N_T,N`$ and source positions. Each exponent has a separate uniform bound, given in (21)–(22).
For an admitted source $`w=\sum_i z_if_i`$, with $`\sum_i|z_i|\|f_i\|_\sharp<\varrho`$, write

```math
Z_{\rm bare}(w)=\int e^{-A(x_0-w,U)}\,dU,\qquad
\widehat Z(w)=e^{-E_{\rm vac}}Z_{\rm bare}(w),\qquad
\widetilde Z(w)=e^{-\mathcal E(w)}\widehat Z(w),\quad \mathcal E(0)=0.
\tag{5a}
```

Here $`E_{\rm vac}`$ is the real, source-independent vacuum constant of the same zero-source construction. The constants in (5) are chosen to satisfy

```math
|\widetilde Z(w)|\le e^{E_+^\sharp N^4},\qquad
\widetilde Z(0)=\widehat Z(0)\ge e^{-C_{\rm low}N^4}.
\tag{5b}
```

These statements do not bound $`E_{\rm vac}/N^4`$. A common change of normalization shifts the two exponents oppositely, so their sum and the normalized source quotient are unchanged.

**(c) Change of units.** Let $`n\ge2`$, $`R,d>0`$, and let $`\ell(n,R)`$ be the least power of $`L`$ at least $`8n(R+1)`$. Also require $`L^{m_1}\ge L^{m_J}\ell(n,R)`$. Let $`\mathfrak S(n,R,d)`$ consist of real Lipschitz source tuples supported in radius-$`R`$ balls. Require pairwise support distance at least $`d`$, as at II:63098–63118. In Case A, $`K_J\ge m_J`$,

```math
|S^T_n(\vec f)|\le C^*_n(d;R)\prod_i\|f_i\|_\sharp,\qquad
C^*_n(d;R)=\max_{b\in\mathcal B(g)}\Phi_{n,dL^b,RL^b}(E_*),       \tag{6}
```

where $`\mathcal B(g)=\{m_J-a:a\in\mathcal A\}\subset[0,m_J]`$ and

```math
\Phi_{n,d',R'}(t)=\left[2C_{\rm UV}(d';R')+
(\log2)\mathfrak r^n
\left(2e^{n[t\ell(n,R')^4+2C_{\rm face}(R')]}+2\right)^n\right]
\left(\frac n\varrho\right)^n .                              \tag{7}
```

These are your coefficients at II:63633–63640 and `6.4:eq-per-ball-bound-b`. Their definitions appear in (24); take $`\mathfrak r=2`$ for finite source lists. $`C^*_n`$ depends only on the fixed data and $`n,d,R`$, and is non-increasing in $`d`$.

**(d) Remaining cutoffs.** Let $`\mathfrak S(n,R)`$ consist of real bounded source tuples supported in radius-$`R`$ balls. In Case B, $`K_J<m_J`$, for $`n\ge1`$ and $`\vec f\in\mathfrak S(n,R)`$,

```math
|S^T_n(\vec f)|\le C^B_n(R)\prod_i\|f_i\|_\infty,
\quad C^B_n(R)=c_n[12(2R+3)^4]^nL^{4nm_J},
\quad c_n=\sum_{\pi\in\operatorname{Part}(n)}(|\pi|-1)!.        \tag{8}
```

Thus, under part (c)'s torus floor, the maximum of (6) and (8) applies at every bare coupling, uniformly in the physical torus. Section 6.4 also proves the bound under the original floor of (iii-b).

**(e) Limits.** At fixed $`g,m_1`$, every sequence $`g_0\downarrow0`$ eventually lies in Case A. It has a subsequence with fixed $`a,N_T,m_J,b`$, along which the correlation theorem's fixed-data limit clauses apply. The estimates hold in their respective cases along the full sequence; their combined bound needs no extraction.

The declaration of dependence on $`L,\mathfrak p,g,\varrho`$ follows your convention that $`\gamma`$ and its choices are already fixed. It does not assert uniformity while varying that earlier window.

## 2. Retained inputs

The statement retains the following inputs. Their hypotheses and their standing in your account remain unchanged.
None is supplied merely by reconstructing the missing statement.

1. **Flow and identification.** Retain clause (0), I:2533–2542, and `4.2:lem-first-passage`, I:3636–3721.
   Retain the correlation flow bounds, II:2875–2884, and its torus-independent numerical recursion, II:2958–2966.
   Retain $`b_{k+1}(0)=\beta_{k+1}`$ as the standing identification at II:63072–63081.
   Equality of numerical flows does not identify the effective energies.
2. **Correlation construction.** Retain all admitted inputs of `5.1:thm-correlation-theorem`, II:2791–2812,
   and its parameter restrictions, II:2814–2867.
   These include Balaban's source-free construction, configuration maps, domains, operators, random-walk and far-field statements,
   quadratic-form bounds, and the source-free identities and estimates from Balaban CMP 116 listed there.
   Retain the finer-zone boundary summation, preparatory resummation geometry, and preparatory window-data statement.
   Your text calls the last statement's proof outstanding at II:2810–2812.
   Retain source holomorphy, locality, induction estimates and mass preservation at II:2921–2935.
   Use the torus estimate and fixed-data limit clauses at II:2937–2959 after supplying their floor below.
3. **Positive representation and exact mass.** Retain 4.33(h1)–(h3) and (h7)–(h11), I:157030–157078.
   Thus each real history is positive and finite, and its field-dependent exponent has the stated bound.
   The block map is Borel with unit fibre mass. Each reference normalizer is finite and positive.
   Replacement uses the conditional mass times a probability law.
   Reversed gauge fixing, removal of the specified characteristic function, and the finite decomposition preserve integrals.
   These are your hypotheses on Balaban's operations, not new proofs of those operations.
4. **Vacuum energies.** Retain the energy definition I:159153–159160 and all hypotheses at I:159288–159309.
   These specify Balaban CMP 119's format, the local-term bounds from Balaban CMP 109 and CMP 119,
   label locality, $`0<g_j\le\gamma<1`$, bounded increments, and the one-step normalization ceiling.
   Retain the density-constants inputs (A)–(D) at I:159511–159520.
   The one-step estimate and remainder argument are reproduced below from I:159412–159443.
   Also retain the identification of the zero-source Chapter 5 energies with these Chapter 4 energies.
   This includes the zero-source local terms and source-independent logarithms in II:25233–25238.
   Your convention at II:140916–140926 uses that identification. The numerical flow alone does not prove it.
5. **Real backgrounds and tests.** Retain Balaban CMP 102b, Theorem 1, (7)–(8), in the form I:154052–154058.
   Retain your characteristic-function admission, I:155039–155096, for Balaban CMP 119's tests (2.16)–(2.17).
   It applies on each determining box, including the stated alternative datum factor $`C_Q`$.
6. **Eight sourced upper-bound inputs.** In II:59645–59680, retain items 1–7 and 9.
   Item 1 is the sourced induction format, including clauses (c), (d), (f), at every local level.
   Item 2 is the sourced real and complex versions of Balaban CMP 119 (2.43)–(2.46), and sup-norm bounds (2.47)–(2.48).
   Item 3 controls complex plaquette weights through $`\theta_W`$.
   Item 4 gives the per-zone-cell value bound and its volume ceiling.
   Item 5 gives the modification estimate on the flat domain class, including $`-\kappa_{\mathfrak d}d_k(X)`$.
   Item 6 bounds the live-component gas and its polymer partition function under both coupling ceilings.
   Item 7 counts complementary cells in the history indexing.
   Item 9 supplies the history indexing and its reserved half-factor payments.
   Only item 8, the unsourced floor, is replaced by the proof in §5.
7. **Per-ball ingredients.** Retain the placement lemma, II:61417–61432, and the periodized-weight lemma, II:61517–61565.
   Retain your chessboard estimate, used at II:64152–64183, on the same torus and cutoff.
   Retain locality, analyticity and term bounds, II:60715–60731.
   Retain Balaban CMP 116 (1.26), in the form II:62030–62067, and your ultraviolet and face estimates,
   II:62127–62157,62293–62314. These apply to the required subfamilies of domains.

Choose all construction constants and the source radius before the final coupling ceiling, as in II:2814–2867.
Then fix $`g`$ and $`m_J(g)`$. The integration radius and exponents below are subsequent choices.
They do not change an earlier construction constant or ceiling.

## 3. Normalization and the estimates used at the last lattice

**One vacuum convention throughout.** Chapter 1 starts with $`\rho^{\rm bare}_0=e^{-x_0A}`$ and propagates that mass (I:477–487,924–933). We distinguish it from

```math
\widehat\rho^{\rm sf}_j=e^{-E_{\rm vac}}\rho^{\rm bare}_j,
\qquad
\widehat\rho^{\rm sf}_0=e^{-x_0A-E_{\rm vac}}.
\tag{N1}
```

The superscript $`\rm sf`$ means source-free; it does not restrict to one history. Fix the vacuum endpoint of this run, and denote it by $`H`$ to avoid confusing it with $`K'`$ or $`K_J`$. On the original source-free run one may take $`H=K`$, since $`K'=K-b\le K`$. Use that same initial scalar in the sourced run. Nothing below compares vacuum constants chosen with different endpoints.

Put $`v_j=E^{(j)}(T,T)`$ and, for a history $`h`$, use your definition

```math
E_{\rm vac}=\sum_{j<H}v_j,\qquad
E^{\rm vac}_k[h]=E_{\rm vac}-\sum_{j<k}E^{(j)}(\Omega_{j+1},\Lambda_{j+1}),
\qquad E^{\rm bare}_k[h]=E^{\rm vac}_k[h]-E_{\rm vac}.
\tag{N2}
```

This is I:159153–159160, with its endpoint $`K`$ renamed $`H`$. The zero-source format and its vacuum theorem are retained inputs; matching numerical flow coefficients alone would not establish them.

Here is your vacuum theorem’s proof from I:159412–159443 at SU(2). Let $`\mathsf V_j=|T|_j`$. Its one-step normalization and local-term estimates give

```math
v_j=-\frac92(L^4-1)\mathsf V_{j+1}\log x_j+r_j,
\qquad |r_j|\le D_0\mathsf V_{j+1},\quad
D_0=(L^4-1)c_G^\sharp+K_*(E_0+1).
\tag{N3}
```

Here $`E_0`$ is your local-term bound, not an initial vacuum energy. The coefficient is $`\frac12(d-1)\dim SU(2)=9/2`$. The other letters are fixed construction constants. For the never-large history $`h=\varnothing`$, (N2) leaves the sum over $`k\le j<H`$. Therefore

```math
E^{\rm vac}_k[\varnothing]=-\mathfrak l_k+\mathfrak r_k,\quad
\mathfrak l_k=\frac92(L^4-1)\sum_{j=k}^{H-1}\mathsf V_{j+1}\log x_j\ge0,
\quad |\mathfrak r_k|\le\frac{D_0}{L^4-1}\mathsf V_k=:C_{\mathfrak r}\mathsf V_k.
\tag{N4}
```

Indeed $`\mathsf V_{j+1}=L^{-4(j+1-k)}\mathsf V_k`$ and the geometric sum is $`1/(L^4-1)`$. Each $`x_j>1`$ in the admitted run. The empty sums at $`k=H`$ obey the same inequalities. This proves the required uniformity of the vacuum remainder without any bound on $`E_{\rm vac}`$ itself.

Thus the bare version of I:157039–157041 is

```math
-E^{\rm bare}_k[\varnothing]
=E_{\rm vac}+\mathfrak l_k-\mathfrak r_k.
\tag{N5}
```

The missing term is $`E_{\rm vac}`$. In the normalized convention (N1), the printed (h4)(a) holds as (N4). This is the correction from the separate Codex normalization check. It imposes no bound on the bare vacuum number.

The discrepancy is substantive already at one step. From (N3),

```math
E^{\rm bare}_1[\varnothing]=-v_0
\ge\left[\frac92(L^4-1)\log x_0-D_0\right]\mathsf V_1.
```

For $`\log x_0>(D_0+C_{\mathfrak r})/[\frac92(L^4-1)]`$, this exceeds $`C_{\mathfrak r}\mathsf V_1`$.
But (h4)(a), if applied to the bare energy, implies $`E^{\rm bare}_1\le C_{\mathfrak r}\mathsf V_1`$.
Thus the substitution fails under the stated one-step inputs.
The lower-member proof from a correctly normalized (h4)(a) remains valid.

Every exact operation preserves the common scalar. Block push-forward is linear. The finite decomposition sums to one. The replacement $`\tau\mapsto m_\tau\mathfrak s`$ is positively homogeneous because $`m_{c\tau}=c m_\tau`$ and $`\mathfrak s`$ is a probability law. The remaining integration identities preserve it too (I:157204–157222). Hence

```math
\int\widehat\rho^{\rm sf}_k\,dV_k
=e^{-E_{\rm vac}}\int\rho^{\rm bare}_0\,dU
=\widehat Z(0),\qquad k\le H.
\tag{N6}
```

Choose $`E=E_{\rm vac}`$ in II:730–739. The sourced integral identity II:2933–2935 then gives $`Z^J(w)=\widehat Z(w)`$ after the lattice identification (15). In particular $`Z^J(0)`$ equals (N6). Pointwise identification of the two effective densities is unnecessary.

**Lower density and real background.** We reproduce your lower-member proof of `4.33:thm-stability`, I:157114–157129, using (N4). Positivity permits keeping only the never-large term. Its field-dependent exponent is at least $`-C_E\mathsf V_k`$, by (h2); its constant part is at least $`-C_{\mathfrak r}\mathsf V_k`$, by (N4). Consequently

```math
\widehat\rho_k^{\rm sf}\,dV\ \ge\ \chi_k\exp[-x_kA(U_k(V))-E_-\mathsf V_k]\,dV,
\quad E_-=C_E+C_{\mathfrak r},\quad
C_E=E_1^\sharp(1-L^{-\beta_T})^{-1}+1 .                    \tag{9}
```

Here $`\mathsf V_k`$ denotes the number of level-$`k`$ sites, not a field coordinate. The constants in (9) are independent of $`x_k,k,H`$ and the torus. In bare variables the right side carries $`e^{E_{\rm vac}}`$. The same convention is explicit in `4.36:cor-density-constants`, I:159530–159537,159571–159593. The density theorem retains its positivity, representation, irrelevance and one-step vacuum-energy hypotheses. This note does not prove those hypotheses.

The real-background input is Balaban CMP 102b, Theorem 1, (7)–(8), in your form `4.31:eq-standing-inputs-e`, I:154052–154058. In level-$`k`$ units, $`\eta=L^{-k}`$. If

```math
\sup_p\|V(\partial p)-1\|<w\le a_1,
```

then its real minimizing background obeys

```math
\sup_p\|U_k(V,\partial p)-1\|<B_3w\eta^2.                 \tag{10}
```

The same estimate on each determining box gives the characteristic-function implication of `4.31:lem-window-characteristic`, I:155039–155096:

```math
\sup_p\|V(\partial p)-1\|<w\le a_1,\quad B_3w\le\varepsilon(x_k)
\quad\Longrightarrow\quad\chi_k(V)=1,
\qquad \varepsilon(x)=A_0x^{-1/2}(\log x)^{p_0}.            \tag{11}
```

Your proof applies Balaban’s estimate (10) to each factor of the actual $`\chi_k`$, whose threshold is $`\varepsilon(x_k)\eta^2`$. The determining box contains the tested plaquettes. This is why the estimate concerns the minimizing background and its tests, not just the coarse Wilson action. Both $`a_1`$ and $`B_3\ge1`$ are fixed before $`g`$, independently of the torus. Under the alternative datum convention at I:155092–155095, put $`Q_0=\max\{1,C_Q\}`$ and use $`a_1/Q_0`$ and $`Q_0B_3`$ in our bounds, including (17). These conservative replacements ensure both that the datum is below the background theorem's threshold and that its curvature is below the characteristic-function threshold. Your account uses the operator norm here (I:153575–153583). At $`k=0`$, use $`U_0=V`$; the same inequalities hold with $`B_3\ge1`$.

**Sourced upper majorant in the same convention.** We reproduce your accounting in `5.12:prf-torus-bound-proof`, II:59645–59821. Its nine hypotheses are listed in §2, item 6. They include the sourced versions of Balaban CMP 119 (2.43)–(2.48). We replace only the floor hypothesis by the proof in §5. The other eight retain their standing in your account, with the initial constant set to $`E_{\rm vac}`$ before bounding histories.

This setting of the constant is visible in the formula, not inferred from normalization invariance of cumulants. The sourced exponent contains $`-E_k^w`$ (II:25040–25043), and $`E_k^w`$ contains the initial $`E`$ with coefficient one (II:25233–25238). Keep all local families and logarithms in that formula fixed. Replacing $`E=0`$ by $`E=E_{\rm vac}`$ multiplies **each** history measure by $`e^{-E_{\rm vac}}`$. The local energy differences $`e_j(X;w)`$ and $`\mathcal E(w)`$ are unchanged. After their subtraction, the residual source-free energy is $`E_k^{\rm vac}[h]`$ of (N2); missing source shares are the additional costs at II:59727–59739. In particular the all-small source-free residual is (N4), not $`E_k^{\rm bare}[\varnothing]`$.

The upper argument uses no floor. In its notation:

1. Subtract $`\mathcal E(z)=\sum_{j,X}[e^{(j)}(X;w)-e^{(j)}(X;0)]`$. The missing shares cost $`O(1)\sum_j|Z_j|`$, paid by the existing history charges (II:59718–59739).
2. The retained sourced versions of Balaban's CMP 119 bounds (2.43)–(2.48) and clause (c) of your complex-weight lemma bound the Wilson part by $`-(1-\theta_W)A\le0`$. The extra zone-cell term is at most $`2^{-4}(C_\sharp O(1)+1)\log x_j`$ per zone cell (II:59741–59764).
3. Below $`k=K'`$, this joins the already paid logarithmic charges. A live arrested pile is paid in its own large-field region, never the top zone (II:59766–59799).
4. Only the top-zone contribution must remain extensive at the last lattice. Balaban’s modulus-integration argument, with the retained live-component gas sum, gives the upper bound (II:59801–59813).

To expose all dependence, the source-free part can be read from I:157046–157105 and I:157133–157181. Its summation is

```math
\sum_{\mathcal S}\mathfrak M_k(\mathcal S)e^{q_k(\mathcal S)}
\le e^{c_M\mathsf V_k},\qquad |\Gamma_k|\le\mathsf V_k,
```

```math
C_\Gamma(x)=\frac92(\log x+B_\sharp\gamma^2)+C_{\mathfrak r},
\qquad E_+(x)=C_\Gamma(x)+C_{\rm maj}+c_M.                  \tag{12}
```

The coefficient $`9/2`$ is the SU(2) value of $`\frac32\dim SU(N)`$. The letter $`B_\sharp`$ in (12) is the constant of I:157049. Your text writes the clause-(0) slope with the same symbol (I:641–667); this note writes that slope as $`B^\sharp`$ in the first-passage formulas. No step needs the two to differ. All energies and history masses in this calculation are normalized as in (N2).

There is also an explicit source for the logarithmic coefficient in that convention: I:159538–159550 bounds $`-E_k^{\rm vac}[h]`$ by

```math
\left[\frac92(\log x_k+B_{\rm vac}\gamma^2)+C_{\mathfrak r}\right]\mathsf V_k
+\sum_{j=1}^k(C_{\log}\log x_{j-1}+C_{\rm loc}^{\rm lab})|Z_j^+|_j.
\tag{12b}
```

Here take $`B_{\rm vac}=\max\{B_\sharp,C_\beta+1,c_5\}`$. This fixed enlargement covers both the constant in (12) and the absolute-increment bound used in I:159292,159540; compare I:158119–158129. Formula (12b) is the normalized vacuum theorem's label bound, with its stated hypotheses. Its first term uses the whole current volume; this harmless enlargement avoids requiring a top-zone improvement. The remaining terms are precisely large-field charges. Their payment is an upstream hypothesis, retained below.

The comparison constant introduces no hidden last-scale dependence: II:7992–8073 defines $`C_\sharp`$ uniformly over the admitted reference sequences and bounds it by the fixed number $`\bar C_\sharp`$ before the coupling ceiling is chosen. The per-cell calculation II:14644–14772 bounds the current chain's contribution by $`C_\sharp[\mathsf K_{\rm cell}^0+3(\mathsf N_0(\log x_j)+3)C_0^\sharp]`$. Its admitted volume ceiling gives the logarithmic bound used in item 2 above. Its live arrested terms are expressly excluded from that top-cell charge and are paid separately, as in item 3.

Here is the corresponding sourced summation, with the payments exposed. After subtracting $`\mathcal E`$, apply the eight retained upper-bound hypotheses to each **normalized** history at level $`k=K'`$. Let $`C_{\rm maj}^J`$ be the source-budget replacement of the fixed nonlogarithmic majorant constant in (12). Let $`c_{\rm gas}`$ be the fixed exponent from the live-gas and history-label summation after the charges are paid. The extra top coefficient is $`c_{\rm top}=2^{-4}(\bar C_\sharp C_{\rm zone}+1)`$, with the fixed geometric counting factor included in $`C_{\rm zone}`$. These are the constants of the retained estimates, not newly assumed functions of the last coupling.

Apply (12b) before this summation. Put its large-field charges, the lower-zone terms, the missing source shares and the live arrested piles into the paid majorant $`\mathfrak M^J_k(h)`$. The top nonlogarithmic cost is at most $`C_{\rm maj}^J\mathsf V_k`$; the top source cost is at most $`c_{\rm top}\log x\,\mathsf V_k`$. Thus we may choose

```math
a_\Gamma=\frac92B_{\rm vac}\gamma^2+C_{\mathfrak r}+C_{\rm maj}^J,
\qquad b_\Gamma=\frac92.
\tag{12c}
```

Balaban’s modulus-integration argument, in your form at II:59801–59813, and the retained gas sum now give

```math
\begin{split}
\left|\int e^{-\mathcal E(z)}\widehat\tau^J_h(z)\right|
&\le \mathfrak M^J_k(h)
\exp\{[a_\Gamma+(b_\Gamma+c_{\rm top})\log x]\mathsf V_k\},\\
\sum_h\mathfrak M^J_k(h)&\le \exp(c_{\rm gas}\mathsf V_k).
\end{split}                                                   \tag{12a}
```

Here $`\widehat\tau^J_h=e^{-E_{\rm vac}}\tau^{J,\rm bare}_h`$ is the history measure before the source subtraction. The first inequality separates top and non-top costs, using $`|\Gamma_k|\le\mathsf V_k`$. The second is where the retained live-gas, modification and history-count hypotheses are used. The gas term $`e^{-p_0(g_k)}|\mathbb L_k|`$ is at most $`\mathsf V_k`$; the history-label payments change its coefficient by fixed $`(d,L)`$-numbers. The missing shares and live piles have already been paid before summing. This is the conditional use of those sourced hypotheses, not a deduction of a complex-source majorant from the source-free upper bound alone.

Consequently, with $`A_J=a_\Gamma+c_{\rm gas}`$ and $`B_J=b_\Gamma+c_{\rm top}`$, a valid sourced exponent satisfies

```math
\left|e^{-\mathcal E(w)}\widehat Z(w)\right|
\le e^{(A_J+B_J\log x)\mathsf V_k},\qquad
E_+^\sharp(x):=A_J+B_J\log x.                            \tag{13}
```

The finite history sum and triangle inequality prove (13) directly from (12a). The coefficients in (12c), the source budget and the gas payment depend on the admitted construction and source radius. They contain neither $`N_T`$ nor the number of levels. This supplies the logarithmic dependence at the standing of the eight retained upper hypotheses. It does not assume the last-scale conclusion or claim to prove those hypotheses. In bare variables the very same estimate is

```math
\left|e^{-\mathcal E(w)}Z_{\rm bare}(w)\right|
\le e^{E_{\rm vac}+(A_J+B_J\log x)\mathsf V_k}.
\tag{13a}
```

The factor $`e^{E_{\rm vac}}`$ must remain here. Multiplying an already weakened bare estimate, such as $`Z_{\rm bare}(0)\le1`$, by $`e^{-E_{\rm vac}}`$ would not prove (13).

This also clarifies II:63531–63565. The single *additional* member is the top-zone logarithm; the original Balaban constants already contain a logarithm, as II:59766–59769 states. All logarithmic members can be collected into one dominating term of the displayed $`2^{-4}(C_\sharp O(1)+1)\log x`$ form by enlarging its fixed constant. The consumers need the resulting upper bound, not a unique decomposition of the exponent.

**Changing convention after both bounds are proved.** If $`\widetilde Z`$ is multiplied by $`e^{-h}`$, replace $`E_+^\sharp`$ by $`E_+^\sharp-h/\mathsf V_k`$ and $`C_{\rm low}`$ by $`C_{\rm low}+h/\mathsf V_k`$. Their sum is unchanged. The shifted exponents need not individually be nonnegative or uniform; their sum is the quotient exponent. This observation transports valid estimates. It cannot supply a missing upper or lower estimate. The estimates used here are established in the common convention (N1)–(N6), before this observation is applied.

## 4. The offset, floors and lattice identification

**Existence of the floor in (2).** This reproduces your proof at II:62887–62983. Set $`D_g=X+b_++4c_2+3\lambda+e`$. For $`m,u\ge0`$,

```math
X+b_++4c_2+3\lambda(m+u)\le D_g(1+m)(1+u).
```

Also $`R_J(x)\le L\max\{1,(\log x)^r\}`$. Taking logarithms in the preceding inequality bounds the logarithm of its left side by a fixed multiple, depending on $`g`$, of $`\log(2+m)\log(2+u)`$. Indeed, each of $`\log D_g,\log(1+m),\log(1+u)`$ is at most

```math
(\log2)^{-2}\log D_g\log(2+m)\log(2+u).
```

Therefore

```math
N_{\mathbb T}(g,m)\le C(g)(\log(2+m))^r
\sup_{u\ge0}L^{-u}(\log(2+u))^r<\infty.                 \tag{14}
```

The ratio of consecutive terms in the last supremum tends to $`L^{-1}<1`$. Choose any fixed number strictly between $`L^{-1}`$ and one. Beyond a finite index it bounds the ratio, so a geometric sequence bounds the tail. This proves finiteness and decay without evaluation. The same ratio argument shows that $`L^m/(\log(2+m))^r\to\infty`$. Hence (2) has an admissible integer $`m`$, and a least one.

The terms in its defining supremum have the form $`L^v`$, $`v\in\mathbb Z`$, and tend to zero. Only finitely many are at least the positive $`u=0`$ term. Their maximum attains the supremum. Keeping that term gives

```math
L^{m_J}\ge L^{11}M R_J(X),
```

since $`b_+,c_2,\lambda\ge0`$. Thus $`m_J\to\infty`$ as $`g\downarrow0`$. The physical floor also diverges, since $`g_-\downarrow0`$. The finite set $`\mathcal A`$ is fixed before $`g`$. The definition of a limit therefore supplies $`\gamma_D>0`$ making both floors at least $`a^\natural`$ for *every* $`g\le\gamma_D`$. Monotonicity of $`m_J(g)`$ is not needed.

**Part (a): added offset argument.** Clause (0) and equality of the two recursions give $`x_j>X`$ for every $`j\le K`$. The definition of $`K_J`$ implies $`K\le K_J`$. If $`a=0`$, (3) applies. If $`a>0`$, apply (1) at $`i=K,j=K_J`$:

```math
\lambda a-c_5\le x_K-x_{K_J}<(X+B^\sharp)-X=B^\sharp.
```

Hence $`\lambda a<B^\sharp+c_5`$, which proves (a), including its strict inequality. No sign for individual increments was used.

**Part (b): your printed identification argument.** The floors give $`m_1\ge a`$ and $`m_J\ge a`$. Thus $`N_T=2L^{m_1-a}`$ is a positive integer and $`b=m_J-a\ge0`$. In Case A, $`K'=K_J-m_J\ge0`$. Moreover

```math
L^{K_J}N_T=2L^{m_1+K},\qquad
2L^{m_1}\frac{L^{j-K_J}}{N_T}=L^{j-K}.                    \tag{15}
```

The first equality matches the bare lattice. The second matches every later spacing. At $`j=K'`$ it gives $`L^{-b}`$. The correlation floor is satisfied by (2); all its other numerical hypotheses have been retained.

For $`\widetilde f(y)=f(2L^{m_1}y)`$,

```math
\|\widetilde f\|^J_\sharp
=\max\{\|f\|_\infty,40ML^{-b}\operatorname{Lip}f\}
\le\|f\|_\sharp .                                       \tag{16}
```

Dilation preserves the finite bond-indexed Haar product and plaquette products. It also preserves each source value at the corresponding barycentre. Thus

```math
A(x_0-\textstyle\sum_i z_i\widetilde f_i,U)
=x_0A(U)-\sum_i z_i\mathcal O(f_i).
```

With $`E=E_{\rm vac}`$, the correlation partition function is $`Z^J=\widehat Z=e^{-E_{\rm vac}}Z_{\rm bare}`$. Near zero their logarithms differ by the constant $`-E_{\rm vac}`$, so all positive-order cumulants agree. This identifies probability laws and cumulants; it does not equate the two unnormalized masses. There is no field rescaling or Jacobian factor in this relabelling of bond variables.

Finally, $`x_{K'}>X`$. If $`m_J>0`$, (1) gives

```math
x_{K'}\le x_{K_J}+3\lambda m_J+2c_2\le x^*(g).
```

For $`m_J=0`$, use $`x_{K'}=x_{K_J}\le X+b_+\le x^*(g)`$. This proves the coupling part of (5).

## 5. Your floor calculation and the added common-window constants

Set $`\mathsf V=N^4`$, $`x=x_{K'}\in(X,x^*]`$, and $`\eta=L^{-K'}`$. We reproduce your lower-half argument at II:109918–109975. It uses Balaban’s minimizing-background bound.
The added choice is one radius for the whole bounded interval, respecting both $`a_1`$ and the small-field threshold.
Your full lemma there also assumes reserve-weight estimates and $`x_{K'}\le2X`$. Those are not invoked here. At fixed $`g`$, define

```math
\varepsilon_*(g)=A_0(x^*)^{-1/2}(\log X)^{p_0}>0,
\quad
s_*(g)=\min\left\{\frac12,\frac{a_1}{8},
\frac{\varepsilon_*}{8B_3},\frac{1}{8B_3\sqrt{x^*}}\right\}>0. \tag{17}
```

All logarithms are positive since $`X>1`$. Since $`p_0\ge0`$, $`\varepsilon(x)\ge\varepsilon_*`$ throughout the interval. These definitions are made after $`g`$; they impose no new condition on an earlier construction constant.

Restrict the last block field to $`\mathcal B=\{V:\|V_b-1\|<s_*\text{ for every independent bond }b\}`$. A product of four unitary matrices satisfies

```math
\|V_1V_2V_3V_4-1\|\le\sum_{j=1}^4\|V_j-1\|<4s_*.
```

This follows by telescoping the product and using that multiplication by a unitary preserves the operator norm. An inverse bond has the same distance from one. Consequently Balaban’s background estimate (10) and the test admission (11), with $`w=4s_*`$, imply

```math
\chi_{K'}=1\text{ on }\mathcal B,\qquad
\|U_{K'}(\partial p)-1\|<4B_3s_*\eta^2.                  \tag{18}
```

The thresholds have a factor-two margin: $`4s_*\le a_1/2`$ and $`4B_3s_*\le\varepsilon_*/2`$. This uses your actual small-field test, not an assumption that its history tests are empty.

For $`W\in SU(2)`$, its eigenvalues are $`e^{\pm i\theta}`$. Thus

```math
1-\operatorname{Re}\operatorname{tr}W
=1-\cos\theta=\tfrac12\|W-1\|^2.
```

There are exactly $`6\mathsf V\eta^{-4}`$ fine plaquettes. Combining this count with (18) gives

```math
A(U_{K'}(V))\le48B_3^2s_*^2\mathsf V,
\qquad xA(U_{K'}(V))\le\tfrac34\mathsf V.                       \tag{19}
```

The powers $`\eta^4`$ and $`\eta^{-4}`$ cancel. This is the dimensional step in the floor argument. It is the curvature estimate for the minimizing background in (10) that permits it.

For normalized SU(2) Haar measure and $`0<s\le1`$,

```math
\operatorname{Haar}\{W:\|W-1\|<s\}\ge c_Hs^3,
\qquad c_H=\frac{8}{3\pi^3}.                             \tag{20}
```

Here is the hand calculation, following SA:23504–23513. Parametrize $`W=\cos\theta\,1+i\sin\theta\,n\cdot\sigma`$, $`n\in S^2`$. Haar measure is normalized spherical volume on $`S^3`$, with density $`(2\pi^2)^{-1}\sin^2\theta\,d\theta\,d\Omega`$. Left multiplication is an orthogonal transformation of unit quaternions, so this probability is Haar. The interval $`0<\theta<s`$ lies in the operator ball, since $`2\sin(\theta/2)\le\theta`$. Concavity of sine on $`[0,\pi/2]`$ gives $`\sin\theta\ge2\theta/\pi`$ for $`0\le\theta\le1`$. Integrating and using $`|S^2|=4\pi`$ yields (20). Endpoints have measure zero.

There are $`4\mathsf V`$ independent last-lattice bonds. Integrate the **normalized** lower member (9) over $`\mathcal B`$, use (19), and multiply their independent Haar masses. By (N6),

```math
\begin{split}
\widetilde Z(0)=\widehat Z(0)=e^{-E_{\rm vac}}Z_{\rm bare}(0)
&=\int\widehat\rho_{K'}^{\rm sf}\,dV\\
&\ge e^{-(E_-+3/4)\mathsf V}(c_Hs_*^3)^{4\mathsf V}\\
&=e^{-C_{\rm low}^*(g)\mathsf V},\\
C_{\rm low}^*(g)&=E_-+\frac34+4\log(c_H^{-1})+12\log(s_*^{-1}).
\end{split}                                                \tag{21}
```

The first equality uses $`\mathcal E(0)=0`$. The mass identity is (N6), not equality with the unshifted Chapter 1 integral. In particular the corrected bare floor is

```math
Z_{\rm bare}(0)\ge
\exp\{E_{\rm vac}-C_{\rm low}^*(g)\mathsf V\}.
\tag{21a}
```

This is the corrected form from that normalization check, also explicit in SA:23515–23527. For $`K'=0`$, use $`U_0=V`$ and $`-E_{\rm vac}\ge-C_{\mathfrak r}\mathsf V_0`$ from (N4); hence the same normalized calculation applies even if the vacuum endpoint is later. Every constant in (21) is independent of $`K,g_0,m_1,N_T,a`$. The scalar $`E_{\rm vac}`$ itself need not have any such bound.

Your more specific dependence on the single last-scale coupling can also be retained. For any admitted $`x`$, use

```math
s(x)=\min\left\{\frac12,\frac{a_1}{8},
\frac{\varepsilon(x)}{8B_3},\frac{1}{8B_3\sqrt x}\right\},\qquad
C_{\rm low}(x)=E_-+\frac34+4\log(c_H^{-1})+12\log(s(x)^{-1}).
```

The preceding integral proof works with $`s(x)`$ at that coupling. Moreover $`s(x)\ge s_*`$ for $`X<x\le x^*`$, by the componentwise bounds used in (17). Hence $`C_{\rm low}(x)\le C_{\rm low}^*`$. This produces an actual single-coupling floor function and proves its boundedness on the required interval.

For the upper bound, insert $`x\le x^*`$ into (13):

```math
|\widetilde Z(z)|=|e^{-E_{\rm vac}-\mathcal E(z)}Z_{\rm bare}(z)|
\le e^{C_+^*(g,\varrho)\mathsf V},\qquad
C_+^*(g,\varrho)=A_J+B_J\log x^* .                        \tag{22}
```

The source radius and norm are those already admitted by the correlation theorem. The same estimate applies to the transported and periodized source lists used by Chapter 6; their admissibility is its periodized-weight lemma, not a new analytic continuation here.

We may therefore choose the common dominating exponent

```math
\boxed{E_*=A_J+B_J\log x^*+E_-+\frac34+
4\log(c_H^{-1})+12\log(s_*^{-1}).}                        \tag{23}
```

This proves the second assertion of (5), in the normalization (5a). Constants in upper bounds can be enlarged to (21)–(22). Thus this proves existence of the constants that the consumers require, rather than bounding arbitrary unnecessarily large choices of them. At the retained upper hypotheses' standing, the coupling dependence is displayed in (12b)–(13), (17), (21), (22). No conclusion is inferred just from saying that an unspecified function depends on a bounded coupling.

## 6. The printed conclusions and their consumers

### 6.1 The per-ball deduction with a symbolic exponent

There is an apparent circle if part (c) cites the *uniformity conclusion* of the per-ball theorem. Your proof has no circle. It keeps $`t=E_+^\sharp+C_{\rm low}`$ as a numerical parameter throughout the proof of 6.4. Only its final paragraph invokes the uniform last-scale conclusion.

Here are the ingredients of your proof at II:63964–64283, with their retained antecedents:

- The placement lemma, II:61417–61432, places each ball a distance at least $`R+2`$ from cell faces using a lattice translation.
- The periodized-weight lemma, II:61517–61565, supplies the admissible copied source lists and the chessboard identity. Choose your reading $`\mathfrak r=2`$ for the literal finite-source polydisc; $`\mathfrak r=1`$ is also available under its class reading.
- Locality, analyticity and the term bound are II:60715–60731. They are independent of last-scale normalization.
- The ultraviolet and face estimates, II:62127–62157 and 62293–62314, hold for arbitrary relevant subfamilies. Their constants are

```math
\begin{split}
C_{\rm UV}(d;R)&=C_eC_{(1.26)}
\sum_{i\ge0}\mathfrak a(R,i)e^{-c_\kappa[dL^i/(4M)-4]_+},\\
C_{\rm face}(R)&=C_eC_{(1.26)}
\sum_{i\ge0}\mathfrak a(R,i)e^{-c_\kappa[RL^i/(4M)-3]_+},\\
\mathfrak a(R,i)&=\left(2(R+2)L^i/M+6\right)^4 .
\end{split}                                                    \tag{24}
```

The tree estimate underlying (24) is Balaban 116 (1.26), in the form of II:62030–62067. It is a retained input here. Each series is finite: beyond a fixed index, its terms are bounded by $`C L^{4i}e^{-cL^i}`$ for positive fixed $`C,c`$. The ratio of this majorant at $`i+1`$ and $`i`$ is $`L^4e^{-c(L-1)L^i}`$, eventually at most $`1/2`$. This is an existence estimate, not a computation. The first series is non-increasing in $`d`$.

Let $`\mathcal C`$ be the cells and $`q\le n`$ the occupied-cell count.
Let $`I_c`$ index the sources in cell $`c`$, and let $`\mathfrak G_\ell`$ be your reflection group acting simply transitively on the cells.
For $`\sigma\in\mathfrak G_\ell`$, let $`\epsilon(\sigma)\in\{+,-\}`$ record its reflection parity.
Use $`\xi^{(+)}=\xi`$, $`\xi^{(-)}=\overline\xi`$, and set

```math
u_{c,\sigma,z}=\sum_{i\in I_c}z_i(f_i\circ\sigma^{-1}),\qquad
w^{\rm ch}_{c,z}=\sum_{\sigma\in\mathfrak G_\ell}u_{c,\sigma,z}^{(\epsilon(\sigma))}.
```

Split the local energy into bulk terms belonging to cells and terms meeting a face.
Your counterterm is

```math
\mathcal E''(z)=
\sum_{c\ {\rm occupied}}\frac1{|\mathcal C|}
\sum_{\sigma\in\mathfrak G_\ell}
\left[\mathcal E^{\rm bulk}_{\sigma c}
\bigl(u_{c,\sigma,z}^{(\epsilon(\sigma))}\bigr)\right]^{(\epsilon(\sigma))}
+\mathcal E^\partial(w_z).
```

The transported sources preserve the norm and lie in their admitted source balls.
For even parity each bulk summand is a holomorphic composition.
For odd parity it has the form $`\overline{\Phi(\bar z)}`$ with $`\Phi`$ holomorphic.
Conjugating the coefficients of its locally convergent power series proves holomorphy and conjugates its derivatives at zero.
The face sum is holomorphic by the same source hypothesis. All sums are finite at fixed cutoff.
Each local energy vanishes at zero source, so $`\mathcal E''(0)=0`$.

If at least two cells are occupied, every bulk summand omits one of the $`n`$ variables. Its full mixed derivative vanishes. If one cell is occupied, its transported bulk terms have the original support radii and separations. Apply the ultraviolet estimate to each, then take their average. Apply it once more to the face subfamily. Hence

```math
|\partial_1\cdots\partial_n\mathcal E''(0)|
\le2C_{\rm UV}(d;R)(n/\varrho)^n\prod_i\|f_i\|_\sharp.       \tag{25}
```

The original bare integral makes $`Z_{\rm bare}(z)`$ entire, by compactness of the finite product of bond groups and linearity of the source exponent. Thus
$`h''=e^{-\mathcal E''}\widehat Z/\widehat Z(0)=e^{-\mathcal E''}Z_{\rm bare}/Z_{\rm bare}(0)`$ is holomorphic on the admitted ball. The chessboard estimate at a copied source, followed by the normalized upper bound (22) and floor (21), gives a cost $`tN^4/|\mathcal C|=t\ell^4`$ per occupied cell. Section 6.5 spells out the vacuum cancellation before this root. For a bulk domain in $`\sigma c`$, its relevant plaquettes lie within $`2\varepsilon`$ of that cell, where $`\varepsilon\le1`$ is the lattice spacing used in your proof at II:64117–64120. Other copied balls lie at least $`R+2`$ from its faces, so at distance at least $`R+2-2\varepsilon\ge R`$ from those plaquettes.
Thus no other copy contributes at those plaquettes. Locality gives

```math
\mathcal E^{\rm bulk}_{\sigma c}(w^{\rm ch}_{c,z})
=\mathcal E^{\rm bulk}_{\sigma c}
\bigl(u_{c,\sigma,z}^{(\epsilon(\sigma))}\bigr).
```

Real parts are unchanged by outer conjugation. Summing over the simply transitive group therefore gives

```math
\operatorname{Re}\mathcal E''(z)=
\sum_{c\ {\rm occupied}}|\mathcal C|^{-1}
\operatorname{Re}\mathcal E^{\rm bulk}(w^{\rm ch}_{c,z})
+\operatorname{Re}\mathcal E^\partial(w_z).
```

These bulk terms cancel those from the chessboard bound, term by term.
The copied source for cell $`c`$ has $`|\mathcal C||I_c|`$ ball copies.
The face estimate gives

```math
|\mathcal C|^{-1}|\mathcal E^\partial(w^{\rm ch}_{c,z})|
\le |I_c|C_{\rm face}(R),\qquad
|\mathcal E^\partial(w_z)|\le nC_{\rm face}(R).
```

Since $`\sum_c|I_c|=n`$, the two face contributions cost at most $`2nC_{\rm face}(R)`$.
The occupied-cell count is at most $`n`$. Thus

```math
|h''|\le\exp\{n[t\ell^4+2C_{\rm face}(R)]\}=Q,\qquad h''(0)=1. \tag{26}
```

Here $`t\ge0`$, since the upper and lower bounds hold at zero, so $`Q\ge1`$. All of (25)–(26) holds before any assertion that $`t`$ is uniform.

For completeness, your final analytic step is elementary. On the source ball
$`\rho(z)=\varrho^{-1}\sum_i|z_i|\|f_i\|_\sharp<1/\mathfrak r`$, apply Schwarz's lemma on the complex line through $`z`$ to $`(h''-1)/(Q+1)`$. It gives
$`|h''(z)-1|\le(Q+1)\mathfrak r\rho(z)`$. On the smaller ball
$`\rho<1/[2\mathfrak r(Q+1)]`$, the logarithm has modulus at most
$`\sum_{j\ge1}2^{-j}/j=\log2`$. Cauchy's formula on coordinate circles approaching radii
$`\varrho/[2n\mathfrak r(Q+1)\|f_i\|_\sharp]`$ gives

```math
|\partial_1\cdots\partial_n\log h''(0)|
\le(\log2)(2Q+2)^n\mathfrak r^n(n/\varrho)^n\prod_i\|f_i\|_\sharp .
```

If a source norm is zero, that source is zero and the mixed cumulant vanishes; no division is then needed. Adding (25) proves (7), with $`t`$ still symbolic. This reproduces your Chapter 6 argument. It assumes neither a zero-free original source ball nor an independent cell-covariance assertion.

### 6.2 Your printed part (c): transport and maximum

In Case A, the last-lattice radius is $`RL^b`$ and its separation is $`dL^b`$. Equation (16) controls its source norms. Since $`L^b\ge1`$,

```math
8n(RL^b+1)\le L^b\,8n(R+1)\le L^b\ell(n,R).
```

The last quantity is a power of $`L`$. By minimality,

```math
\ell(n,RL^b)\le L^b\ell(n,R)\le L^{m_J}\ell(n,R)\le L^{m_1}. \tag{27}
```

Thus the printed floor suffices for every possible $`b`$. The raw deduction above gives
$`\Phi_{n,dL^b,RL^b}(t)`$. The map $`t\mapsto\Phi_{n,d',R'}(t)`$ is non-decreasing, since every coefficient is nonnegative. Replace $`t`$ by (23), then maximize over the finite set $`\mathcal B(g)`$. This proves (6). Only $`C_{\rm UV}`$ depends on $`d`$, and it is non-increasing. A finite maximum preserves that property.

### 6.3 Your printed parts (d) and (e)

In Case B, part (a) gives $`0\le K\le K_J<m_J`$. Let $`\epsilon=L^{-K}\le1`$. A plaquette whose barycentre lies in a radius-$`R`$ ball has its base site within sup-distance $`R+\epsilon`$ of the ball's centre. On each coordinate circle there are at most $`2R/\epsilon+3`$ such sites. This remains an upper bound when the interval covers the circle: then count all sites, which is no larger. There are six direction pairs. Hence

```math
\#\{p:x(p)\in\operatorname{supp}f_i\}
\le6(2R+3)^4L^{4K}\le6(2R+3)^4L^{4m_J}=:P_R.
```

Since $`0\le a_p\le2`$, $`|\mathcal O(f_i)|\le2P_R\|f_i\|_\infty`$.
For bounded random variables $`Y_i`$, expanding $`\log\langle e^{\sum z_iY_i}\rangle`$ at zero gives

```math
\kappa(Y_1,\ldots,Y_n)=
\sum_{\pi\in\operatorname{Part}(n)}(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}\left\langle\prod_{i\in B}Y_i\right\rangle .
```

Indeed, the term with $`j`$ factors of the nonconstant part of the moment generating function orders the $`j`$ nonempty blocks in $`j!`$ ways. Its logarithmic coefficient is $`(-1)^{j-1}/j`$, leaving $`(-1)^{j-1}(j-1)!`$. This finite coefficient identity is not a computer enumeration. Each moment product is at most $`\prod_i\|Y_i\|_\infty`$. The displayed local count therefore proves (8). No total-torus plaquette count occurs.

For part (e), your clause (0), I:2533–2537 (where $`B^\sharp`$ is written $`B_\sharp`$), gives

```math
K(g_0,g)\ge\frac{g_0^{-2}-X}{B^\sharp}-1\longrightarrow\infty .
```

Part (a) implies $`K_J\ge K`$, so Case A eventually holds. An infinite sequence taking values in a finite set has an infinite constant subsequence: otherwise it is a finite union of finite sets. Apply this to $`a\in\mathcal A`$. At fixed $`g,m_1`$, (4) then fixes $`N_T,m_J,N,b`$, while $`K_J\to\infty`$. These are precisely the fixed-data hypotheses of the correlation theorem's subsequential-limit clause. Its conclusions apply. The bounds need no such extraction, since all possible $`a`$ were already covered.

### 6.4 Added completion under the original torus floor of (iii-b)

Part (c) follows the stronger printed floor at II:63275–63280. The principal statement (I:2610–2620) asks only

```math
m_1\ge m_{\mathbb T}(g_-),\qquad L^{m_1}\ge\ell(n,R).
```

We must not silently replace this by the stronger floor. The remaining physical torus exponents form a finite set depending only on the fixed data, $`n,R`$. They are covered by the original torus bound.

Set

```math
J=\max\{m_{\mathbb T}(g_-),\,m_J+\log_L\ell(n,R)\},\qquad
N_{\max}=2L^{J+m_J},\qquad \Delta=d/(2L^J).
```

For $`m_1\ge J`$, parts (c) and (d) apply. For $`m_1<J`$ in Case A, (4) gives $`N\le N_{\max}`$. On the side-one torus the source separation is at least $`d/(2L^{m_1})\ge\Delta`$. The norm is bounded by (16). Clause (iv) of the correlation theorem, II:2937–2959, therefore yields

```math
|S^T_n(\vec f)|\le C^{\rm bd}_n(d;R)\prod_i\|f_i\|_\sharp,
```

```math
C^{\rm bd}_n(d;R)=
\left[
C\,\Delta^{-4}(1+\log^+\Delta^{-1})
+(\log2)\left(2e^{E_*N_{\max}^4}+2\right)^n
\right](n/\varrho)^n .                                    \tag{28}
```

Here $`C`$ is that theorem's ultraviolet constant, already fixed independently of cutoff and torus. We used its displayed decreasing majorant, so (28) is non-increasing in $`d`$. If a nonzero separated tuple cannot fit on a small torus, there is simply no such tuple; the estimate still applies to every tuple that does fit. Case B is covered by (8). Consequently

```math
C^\infty_n(d;R)=
\max\{C^*_n(d;R),\,C^B_n(R),\,C^{\rm bd}_n(d;R)\}             \tag{29}
```

proves the consumer's bound with its original floor. This finite-torus completion uses the already established (5) and the torus theorem, not (iii-b) itself. The simpler constant $`\max(C^*_n,C^B_n)`$ suffices under part (c)'s printed floor.

### 6.5 The checked Chapter 6 consumers

Chapter 1's $`Z_{\rm bare}`$ omits the vacuum constant. Chapter 5's $`Z`$, and Chapter 6's $`Z`$, include the source-independent initial constant $`E`$. With the choice $`E=E_{\rm vac}`$ made in §3, their $`Z=\widehat Z`$; their $`\widetilde Z`$ also subtracts the source energy and is exactly (5a). Chapter 6 writes the initial $`E`$ explicitly at II:60370–60374, and proves its cancellation in the probability quotient at II:60414–60422. The definitions of (S) and (F), II:60705–60741, use that $`Z`$. The passages permit this common choice; they do not establish individually uniform upper and lower exponents for an arbitrary initial $`E`$.

Here is the cancellation with the signs retained. Put $`A=C_+^*`$, $`B=C_{\rm low}^*`$ and $`\mathsf V=N^4`$. Equations (13a), (21a), (22) give

```math
\begin{aligned}
|e^{-\mathcal E(w)}Z_{\rm bare}(w)|&\le e^{E_{\rm vac}+A\mathsf V},\\
Z_{\rm bare}(0)&\ge e^{E_{\rm vac}-B\mathsf V},\\
\left|e^{-\mathcal E(w)}\frac{Z_{\rm bare}(w)}{Z_{\rm bare}(0)}\right|
&=\frac{|\widetilde Z(w)|}{\widetilde Z(0)}
\le e^{(A+B)\mathsf V}.
\end{aligned}
\tag{30}
```

Equivalently $`A_{\rm bare}=A+E_{\rm vac}/\mathsf V`$ and $`B_{\rm bare}=B-E_{\rm vac}/\mathsf V`$. Their sum is $`A+B\le E_*`$. No estimate on either vacuum shift is taken.

For the periodized weight $`w^{\rm ch}_{c,z}`$, numerator and denominator live on the **same torus**, at the same cutoff. They use the same $`E_{\rm vac}`$, even though the copied source depends on $`c`$ and $`z`$. Your chessboard identity gives a nonnegative quotient. Applying (30) before taking its $`|\mathcal C|`$th root yields

```math
\|F_{c,z}\|_{\rm ch}
\le\exp\left\{|\mathcal C|^{-1}\operatorname{Re}\mathcal E(w^{\rm ch}_{c,z})
+(A+B)\frac{N^4}{|\mathcal C|}\right\}
=\exp\left\{|\mathcal C|^{-1}\operatorname{Re}\mathcal E(w^{\rm ch}_{c,z})
+(A+B)\ell^4\right\}.
\tag{31}
```

This is II:64157–64183 in the corrected notation. In particular there is no leftover $`E_{\rm vac}/|\mathcal C|`$.

| Checked consumer | Source identification and effect of the correction |
|---|---|
| **II:63531**, read through 63565 | It uses the upper and lower last-scale assertions from II:63195–63226. The density is the sourced one with initial $`E`$ at II:63382–63393. Set $`E=E_{\rm vac}`$; then these are exactly (13) and (21). The explicit identity $`Z_{\rm bare}=e^E Z^J`$ at II:63474–63490 confirms that the proof identifies cumulants, not unshifted masses. No extra vacuum term enters (5). |
| **II:63907–63920**, read through 63935 | It uses the sum $`E_+^\sharp+C_{\rm low}`$ in the per-ball quotient and then a finite maximum over $`b`$. That sum is the invariant exponent in (30). Each $`b`$ may have its own run and vacuum number; cancellation occurs within that run before the maximum. The finite maximum (6) therefore has no vacuum term. |
| **II:64272**, read with 64157–64183 and 64246–64282 | The proof applies (S) and (F) to the same $`\widetilde Z`$, then replaces $`N^4/\vert \mathcal C\vert `$ by $`\ell^4`$. Equation (31) checks that step. This passage also needs $`C_{\rm low}`$ separately uniform; (21) supplies that bound. Finally $`\log Z(0)`$ has zero source derivative, so the cumulant bound (7), and hence (29), are unchanged. |
| **II:68364**, read with 68362–68367 | This is a dependency statement for clause (ii), not a new unnormalized floor. The actual infinite-volume theorem takes probability expectations, cumulants and centered moments (II:66418–66430,66436–66452,66460–66477). Its per-ball input is (29). Multiplication of each finite-cutoff density by its positive vacuum scalar leaves those objects and reflection positivity exactly unchanged. The cancellation precedes every subsequence limit; convergence or uniformity of $`E_{\rm vac}`$ across cutoffs or tori is unnecessary. |

The convention itself is not conjectured here. II:140880–140886 defines an explicitly bare $`Z_m`$; II:140916–140926 writes $`\widetilde Z_m=e^{-E_m-\mathcal E_m}Z_m`$. This is (5a). That later volume-transfer argument retains $`e^{E_m}`$ in its bare lower bound (II:141703–141708). It concerns a different use, where two torus sizes can require a vacuum-density comparison. The four consumers above need only the same-torus cancellation (30)–(31). We use the later passage only to identify your convention. Its stability and volume-transfer assumptions are outside this proof.

## 7. Constant order, scope and check record

The earlier choices remain fixed throughout. In particular,
$`B_{\rm vac},C_{\mathfrak r},C_{\rm maj}^J,c_{\rm top},c_{\rm gas},a_1,B_3`$
are construction constants fixed before the target $`g`$.
The vacuum number is evaluated separately for each run. No ceiling is selected from that number.
After fixing $`g`$, choose $`m_J`$, $`x^*`$, $`s_*`$ and the exponents in that order.
After fixing $`n,R,d`$, choose the cell length and torus floor. Then vary $`m_1,g_0`$ and source positions.

Equations (21)–(23) give separately uniform lower and upper exponents in last-lattice volume $`N^4`$.
Uniformity is in the physical torus exponent $`m_1`$, with the omitted-step exponent fixed at $`m_J(g)`$.
It does not allow $`m_J`$ to vary independently. It does not assert that $`b`$ is constant across bare couplings.
Part (e) makes $`b`$ constant only after subsequence extraction.
For $`K_J<m_J`$, part (d) gives a bounded-observable estimate. It gives no partition-function floor for a correlation run.

The application proved here is the checked Chapter 6 assembly and (29), under the original floor of clause (iii-b).
The same-torus cancellation in (30)–(31) is exact before any limit.
No uniform bound on $`E_{\rm vac}`$, or on its density, is needed for those divisions.

This note does not replace every later use of the last-scale constants.
In unit-lattice volume the conversion is $`N^4=L^{4b}(2L^{m_1})^4`$.
A comparison between different tori retains a vacuum-density difference.
Your formula at II:141688–141725 displays that difference explicitly.
Neither its bound nor a logarithmic bound per unit-lattice site is proved here.
No later-use repair or additional ceiling is included in this claim.

The representation, vacuum-energy hypotheses, sourced upper estimates, and Balaban's real-background input remain assumptions of this implication.
The preparatory window-data statement remains outstanding at II:2810–2812.
This note establishes neither an unconditional stability theorem nor an unconditional main-theorem conclusion.
It supplies no factorial growth estimate, clustering result or rotation result.

**Who wrote and checked.** Codex wrote the working proof; its exact model variant was not recorded.
A fresh Claude session checked the first version line by line. It rejected the identification with the bare mass.
It accepted the offset, lattice matching, local count and subsequence arguments.
It also accepted the per-ball deductions conditional on a valid common exponent.
A separate Codex check identified the missing vacuum term and the repair in your existing convention.
That check also corrected the first checker's stronger claim that no normalization could work.

A fresh Claude session then checked the repaired changes line by line, keeping the accepted parts of the first version.
Its report says: “First failing step: none.”
It checked the normalized floor, the upper bound in the same convention, the separate constants,
and the four consumer cancellations. It explicitly retained the common-energy identification as an assumption.
This acceptance is conditional on the inputs in §2.

Codex wrote this outward version against the checked working proof and read the cited source ranges. Claude (Opus 5.5) checked this version line by line against the working proof and the cited account lines; its fixes are applied.
The recorded checks are model readings, not human review or an audit. They grant no scientific status.
Every proof step above is a written argument. Source searches and file checks do not discharge any mathematical claim.
