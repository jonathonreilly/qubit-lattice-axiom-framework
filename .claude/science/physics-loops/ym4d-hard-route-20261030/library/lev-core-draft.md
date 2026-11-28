# LEV and CORE in four dimensions: pass 1 (long draft)

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), one session, 2026-11-04. Pass 1 of the method "Claude drafts at length, Codex distils, a fresh session referees, then the part is frozen". Research text, not an audit. It grants no status, and no other model has checked it.

Credit. Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the three-dimensional manuscript `YM3/YM3_I.tex` ("YM3") and the four-dimensional outline `YM4_sketch_500.tex` ("SA"), both at commit `31a47c543775`: the pinned levelling (YM3 Proposition II-85-34), the outer-core substitution (YM3 Propositions I-93-98(g2) and II-16-69), the hereditary core (SA (R4)-(R6)), the averaging formula with its contour mean, straightened average, block factor and node factor (SA L7065-7106), and the four-dimensional remark that the inverse node factor "is continued into each pillar by means of a smooth bump" (SA L7913). Tadeusz Balaban for the averaging operations and their estimates (CMP 98, 99) and the background-field method (CMP 99, 102, 109). Jonathan Dimock for his expositions of Balaban's renormalization group (arXiv 1108.1335, 1212.5562, 1304.0705). The library notes cited below are by Codex and Claude; each credits its own sources.

Sources read in this session, in bounded ranges: YM3 L42080-42480, L49560-49700, L54627-55130, L55869-55930, L56440-56650; SA L5663-5800, L6559-6665, L7063-7108, L9690-9712, L9667, and the single lines L7741, L7747, L7913; library: `st1-draft2.md` (Sections 0, 2-4, 7.1, 7.8, 11.3-11.4, 15), `st1.md` L45-242, L313-340, L400-425, `a1-balaban.md` L325-456, L1705-1900, `a3-derivative.md` L421, L461-466, `c1-repr.md` L1-25, L148-220, `shift-map.md` L1540-1580, `ym4-assembly.md` L214-285, `in1-draft.md` L798-812. YM3_II was not needed: the statement and the full proof of II-85-34 are in `YM3_I.tex` (L54729-54785 and L54787-55118), so it was not fetched.

---

## 0. Summary

| Target | Result here | Inputs |
|---|---|---|
| **LEV** (pinned levelling, YM3 II-85-34) | **proved in four dimensions**, as an implication (Theorem LEV, Section 9; ST1 interface Corollary LEV-ST1, Section 10) | SA's averaging formula and its main-rule domain (SA L7065-7106, definitions); the real curvature averaging estimate **CURV** on pillars (`a1-balaban.md` §3.5, (3.6) and L358-366; the content of ST1's import AV-conv, SA L9667). Everything else is proved here: the Federbush mean (Lemma FM), the comb gauge (Lemma CG), the one-step straightened map (Lemma ONE), the pillar recursion (Proposition REC, the four-dimensional form of YM3 (II-155-25)), and the levelling itself. |
| **CORE** (outer-core substitution, YM3 II-16-69) | **proved in four dimensions**, as an implication (Theorem CORE, Section 12), with the constants of ST1's (16): $C_{\rm os}=18$, $K^\sharp=e^{3\delta_T}K_T$ | Route B (main): ST1's Theorem T and Corollary T′ (`st1-draft2.md` §7.8; an implication there from AV, AX, TH4, PROF, BG), so CORE adds **no new import** to ST1. Route A (alternative, YM3's argument): the uniform tower estimate (ER7) (SA L6571-6582, assumed there; `c1-repr.md` §8, proposed by Codex, not checked by the other model). |

**No statement internal to LEV or CORE is Outstanding.** Both end as complete proofs of implications. No step stops at a lemma, so no attacks are recorded (Section 14 says what remains open upstream, in the imports).

Three findings that change the inputs of ST1:

1. **CORE needs no α₁² structure and no new import.** YM3 proves its tower clause by Schwarz's lemma from a size bound $K^\sharp_{\rm tw}(\alpha_0+\alpha_1^2)$ (YM3 L42437-42447). In four dimensions ST1 already has a Lipschitz tower estimate, Corollary T′ (`st1-draft2.md` L563-569), whose normalisation coincides exactly with the core's (R6) normalisation (Section 12.3). The tower clause follows from it in two lines. The hypothesis $b_1^2\le c_\natural b_0$ of (16) is then not used.
2. **LEV needs no pillar folding in four dimensions, and its averaging input reduces to CURV.** Every object the pin reads lies in the pillar's own level-$(q-1)$ sublattice and its block factor at the top (Lemma LOC). The four-dimensional pillar recursion (the analogue of YM3 (II-155-25), which YM3 imports from its own averaging theory) is proved here from SA's formula (Section 6). As a by-product, the node-factor bound of ST1's import AX ($|v_q^{\pm1}-1|\le K_v\xi_q\sup|H|$) is proved here at real references, with $K_v=16$ (Proposition PT4 (P4)).
3. **A geometric constant in ST1.** `st1-draft2.md` Lemma TG(iv) states that a site and its pillar top are within weighted distance $3/2$, citing YM3 L55661. That is the three-dimensional value for coordinate paths. In four dimensions a coordinate path from a site to its top has weighted length less than $2$ (Lemma G4(a)); the value $3/2$ holds if path length is Euclidean. This changes only the factor $e^{3\delta_T}$ of Corollary T′ to at most $e^{4\delta_T}$; I use $e^{4\delta_T}$ below to be safe.

Constants. Every constant introduced here is fixed before $\kappa$ and is independent of $M$ and $\bar\kappa$. Each one depends only on $L$, absolute numbers, the CURV threshold $c_{\rm cv}$, DR's decay rate $\mu$, and (for CORE) Theorem T's $K_T,\delta_T,a_T$. The table is in Section 13; each constant is also marked where it is introduced.

---

## 1. What ST1 uses: the exact statements

### 1.1 LEV

ST1's distil states the import (`st1.md:223-229`):

> pinned levelling on a supplied regular triple domain $D_{\rm LEV}$, with its local gauge requirements on turning cells. It gives the gauge $u$, the transformed pair, and the bounds in Definition 5. With the current already in the shift's units, $e^{i\eta H^\delta}\mathbf U=(e^{i\eta H}\mathbf U)^u$, $K^\delta=\operatorname{Ad}u(\mathbf J+K)-\mathbf J$ (17). It is holomorphic only where every endpoint pillar used by the read remains levelled. It must preserve the actual stored transports at their pinnable sites and give the common-center continuation used for complex ties. Pointwise bounds on $u,u^{-1}$ alone do not suffice.

The bounds of Definition 5 (`st1.md:165-170`; `st1-draft2.md` L180-190 adds the factor $E_{\bar\kappa}$): for a pinned read, $\|(\lambda h_Y)^\delta\|_w\le C_{\rm lev}|\lambda|C_{\rm src}E_{\bar\kappa}C_{\mathcal A}\delta_{\rm src}Q_X$ whenever the endpoint pillars are levelled, "the full profile loss $C_me^{C_m\delta_{\rm prof}}$" included in $C_{\rm lev}$; and the pillar-size functional of the unpinned shift is at most $K_{\rm pin}|\lambda|C_{\rm src}E_{\bar\kappa}C_{\mathcal A}\delta_{\rm src}E_X$. The pinning vocabulary is fixed at `st1.md:198` (pillars $B^q(y)$, tops in $Y$, pinnable, read sets $\operatorname{Rd}_Y(y)$, $\widehat\varepsilon_y(H)=\xi_q\sup_{\operatorname{Rd}_Y(y)}|H|$, levelled when $\widehat\varepsilon_y<\epsilon_{\rm lev}$; "Preservation of a stored transport means equality of its ordered path product before and after the pinned response").

Round 2 uses LEV at every transition. Its uses, with line numbers in `st1-draft2.md`:

- L46 and L879 (Theorem 1 hypothesis 5): "pinned levelling preserves the stored transports as in LEV".
- L832 (after Lemma ST): "the pinned levelling of LEV preserves every stored transport that a carried term reads ... provided the tops are levelled. Levelling at the physical point holds by the pin term of (12)".
- L846 (Proposition 7): the gauge $u_\delta$ "is $\mathbf1$ off the endpoints of $\operatorname{Bd}(Y)$ and satisfies $u_\delta(y)v^\sharp_q(y)=\mathbf1$ at levelled tops (YM3 L54737)", and "preserves the stored transports at pinnable levelled tops (YM3 L54741-54745)". The pinned pair is then a gauge transform of $(E,J(E))$; this is the return of the transition.
- L875 (hypothesis 3): LEV's triple domain, with "the turning-cell gauges of LEV's (eq:levelling-regular-triple) supplied by restricting the natural-cube witnesses".
- L877 (hypothesis 4) and L711-752 (Theorem S): the endpoint-pillar bound $K_{\rm pin}$ and the pinned bound $C_{\rm lev}$ enter $a_X$ of (12).
- L237 (constants, step 2): $C_{\rm lev},K_{\rm pin},\epsilon_{\rm lev},c_{rt}$ are LEV's constants.
- L934 (open imports): "LEV in four dimensions (YM3 L54627-55124 is the three-dimensional model)".

So the four-dimensional LEV must supply: the construction of $u$ and $h^\delta$ on $D_{\rm LEV}$; (17); $u=\mathbf1$ off the endpoints of $\operatorname{Bd}(Y)$; the top identity $u(y)v^\sharp_q(y)=\mathbf1$ at levelled tops; preservation of stored transports at pinnable levelled tops; the local bound and the profile bound that give $C_{\rm lev}$ and $K_{\rm pin}$; holomorphy where the relevant tops are levelled; locality, real gauge covariance, conjugation, Borel dependence; restriction; and the common-centre clause for ties. Theorem LEV and Corollary LEV-ST1 state exactly these.

### 1.2 CORE

ST1's distil states the import (`st1.md:216-222`):

> CORE (NL1): the stated cores, their gauge clauses, and outer substitution. Precisely, for $0<\tau<1$, $0<b_0\le b_1$, $b_1^2\le c_\natural b_0$, $2(b_0+b_1)\le a^\sharp$, a shift satisfying $|H|,|\nabla^{\mathbf U}H|<\tau b_0/(C_{\rm os}K^\sharp(1+c_\natural))$, $|\mathbf J+K|<b_0$ (16) sends the core at $((1-\tau)b_0,(1-\tau)b_1)$ into the core at $(b_0,b_1)$. The derivative convention and separate current condition matter. YM3 42287-42325 gives $C_{\rm os}=18$ there. The four-dimensional outer-core substitution remains an open import.

The core is SA (R4)-(R6), as spelled out at `st1.md:110`: $|\partial U-I|,|\partial\mathbf U-I|<b_0\eta_i^2$, $|A'|,|\nabla^UA'|<b_1$, $|\mathbf J|<b_0$; real gauges on contained cubes of side at most $C_{\rm box}LM$ with $|A|,|\nabla A|<C_{\rm pot}Mb_0$; every subtower (every allowed subdomain, both erosion rules, $1\le q\le p\le i$) has curvature $<b_0L^{-(i-p)}\eta_p^2$ and current $<b_0L^{-(i-p)}L^{2(q-p)}$ in level-$q$ units, also for $U$; all towers exist on their open branches.

Round 2 uses CORE in Proposition 6 (`st1-draft2.md` L652-674): the midpoint core at $(1-\tau_a)b^{\rm mid}$ is sent into the core at $b^{\rm mid}$, with $K_{\rm core}=8L^3C_{\rm os}K^\sharp(1+c_\natural)/c_{\min}$ (L655). Its constants $C_{\rm os},K^\sharp,c_\natural$ enter step 2 of the order (L237) and the ceilings $b_1^2\le c_\natural b_0$, $2(b_0+b_1)\le a^\sharp$ of step 10 (L251). It is open item 4 of `st1-draft2.md` L935: "CORE's outer-core substitution in four dimensions (YM3 L42287-42325 in three)". Theorem CORE states exactly this.

---

## 2. What the sources prove, with line numbers

**YM3 II-85-34.** The setting is at YM3 L54636-54729: step $t=k+1$, mesh $\xi=\eta_k$, pillars $B^q(y)$, tops in $Y$, pinnable tops (L54649-54651: "pinnable if $q\ge2$, or if $q=1$ and every bare site within $2\xi$ of $B^1(y)$ lies in a pillar of level zero or one"), turning cells (L54652-54656), the regular-triple domain $\mathfrak T_k(Y;c)$ (L54660-54674), admitted shifts and their local size (II-79-5) (L54676-54691), neighbours and read sets (L54692-54708), the bump $\phi$ and the constants (II-85-3) (L54711-54726). The statement is L54729-54785. The proof is L54787-55118. It rests on (II-155-25) (YM3 L49647-49662), which YM3 proves from its own three-dimensional averaging iteration (L49664-49700: "the extra estimates needed beyond the real reference iteration"). Its three-dimensional features are: the comb counts and $L^{-3}$ block means inside (II-155-25); the bump $\prod_{\mu=1}^3$ (L54915); the path length $3(L^o-1)/2$ giving $|T|\le5/2$ (L54894-54895); the weighted lengths $3$, $6$, $12$ (L55104-55115); the folding extension (L54798-54805).

**YM3 II-16-69.** Statement L42287-42325, proof L42327-42452. The proof has two parts: a pointwise estimate (II-16-52) (L42333-42340, proved L42344-42412, with the plaquette step through YM3's (I-10-121)), and the tower clause by Schwarz's lemma on a disc, using the size bound I-93-98(f) (statement L42171-42204, proof L42205-42234). I-93-98(f) is three-dimensional through its input I-93-83.

**SA.** The hereditary core is SA L5663-5729: (R4) at L5672-5680, the box gauges at L5683-5685, the derivative convention at L5689-5692, (R5) at L5698-5703, (R6) at L5705-5716 (read on "$Z$ with two layers of the $M$-cubes of level $p-1$ removed", L5707-5708), and the logarithmic substitution (R8) at L5747-5755. SA *assumes* the uniform tower estimate (ER7) at L6571-6582 ("Assume the following uniform tower estimate"); it does not prove it. The averaging formula is SA L7065-7106: the Federbush mean "the solution, close to the family, of $\sum_i\log(V_iV^{-1})=0$", the path family $\mathcal G(y,x)$ of at most $4!$ members and the comb $\Gamma_{y,x}$ of order $4,3,2,1$ (L7065); the average $\mathcal M(U)(c)=\exp(L^{-4}\sum_{x\in B(c_-)}\log W_x)U[c]$ on $\mathrm{Dom}(c)=\{\varpi_c<cL^{-2}\}$ (L7066-7072); the linear averages $Q^{\rm s}$, $\sigma$, $Q^{\rm pl}$ (L7076-7086; "$Q^{\rm pl}$ is the derivative of $\mathcal M$ at $\mathbf1$"); the straightened average and block factor $\mathsf u(y)=\exp(L^{-4}\sum_{x\in B(y)}\log[\mathbf W(y,x)W_0(y,x)^{-1}])$, $e^{i\mathcal Q^1(W_0,\mathsf a)(c)}\mathcal M(W_0)(c)=\mathsf u(c_-)^{-1}\mathcal M(\mathbf W)(c)\mathsf u(c_+)$ (L7092-7097); the recursion $\mathsf a_{n+1}=\mathcal Q^1(W_{0,n},\mathsf a_n)$, $v_{n+1}=v_n\mathsf u(W_{0,n},\mathsf a_n)$, and "the product $v_k=v_k[A]$ of the $k$ block factors is the node factor" (L7101-7108). SA L9667 defines the axial gauge by comb transports, "$(\mathcal M^nU)(\Gamma_{z,x})=\mathbf1$", and states the converse curvature estimate used as AV-conv. SA L9702 is the Landau top condition $u_Bv_j[\mathcal H(B)]=\mathbf1$. SA L7913 says, for 1a.3.9-1a.3.11: "At sites that carry stored fields but have ceased to be tops, $\mathsf n^{-1}$ is continued into each pillar by means of a smooth bump, and in this way the stored data are not acted on", and "1a.3.11 is a matter of covariance only: $(\mathcal M^iU^w)(y,x)=w(y)(\mathcal M^iU)(y,x)w(x)^{-1}$". This is SA's one-sentence four-dimensional statement of the levelling idea; no construction or estimate accompanies it.

**Library.** `a1-balaban.md` §3.5 (L325-456) rebuilds Balaban's curvature recursion $v_{m+1}\le L^2v_m+C(L^2v_m)^2$ (3.6) and its uniformity (L358-366: "Induction then gives $w_m<2\alpha$ at every step"); §7.6 (L1705-1900) gives the one-step straightened bounds (7.11), the identity (7.14) and the bootstrap, at real references with the local gauge hypothesis (7.10). `c1-repr.md` §8 (L148-211) proposes a proof of (ER7) in four dimensions from A1 (9.2), AV and Definition A; its last line says the argument is "by Codex, not yet checked by the other model" (L220). `ym4-assembly.md` L282 lists "⟦open: NL-ER7⟧ the estimate (ER8u) = (ER7)". `st1-draft2.md` §7.8 proves Theorem T and Corollary T′ as implications from AV, AX, TH4, PROF, BG (L503-569). `shift-map.md` (67b) (L1556-1576) is an exact example: pointwise small complex gauges $r_t=e^{t\epsilon sT}$ with $\|\rho\|_\infty\le\epsilon$ give returned links $e^{\pm2t\epsilon T}$, hence potentials of size $2t\epsilon/\eta$; "a small pointwise complex return does not give a mesh-uniform potential bound". This is why the levelling turns must be smooth on cells of positive order, and why singleton cells are allowed only where the read scale is at most $L\eta$ (Section 9.4, Remark).

---

## Part I. Conventions and elementary lemmas

## 3. Conventions

Work on a finite periodic four-dimensional lattice with numerical bare mesh $\eta$; $\xi_l=L^l\eta$; $L\ge13$ odd. Real configurations take values in $SU(2)$, complex ones in $SL(2,\mathbb C)$. The real Lie algebra $\mathfrak h$ is the traceless Hermitian $2\times2$ matrices, its complexification $\mathfrak g_{\mathbb C}=\mathfrak{sl}(2,\mathbb C)$; configurations near the identity are written $e^{iX}$. On $2\times2$ matrices $|\cdot|$ is the operator norm; on finite arrays $\|\cdot\|$ (or $\|\cdot\|_\infty$) is the maximum of these norms. On real endomorphisms of $\mathfrak h$ (used for frames, Section 9.3) $|\cdot|$ is the Euclidean operator norm for the Hilbert-Schmidt inner product. A gauge acts by $W^g(b)=g(b_-)W(b)g(b_+)^{-1}$ and on a current or a left increment at $b$ by $\operatorname{Ad}g(b_-)$. Write $\operatorname{cn}(g)=|g|\,|g^{-1}|$ (pointwise maximum for a gauge field). The involution is $X^{\mathfrak c}=(X^*)^{-1}$ on $SL(2,\mathbb C)$ and $Z^{\mathfrak c}=Z^*$ on $\mathfrak g_{\mathbb C}$, so that $(e^{iZ})^{\mathfrak c}=e^{iZ^{\mathfrak c}}$; its fixed points are $SU(2)$ and $\mathfrak h$.

The covariant difference is ST1's (4): $(\nabla^W_\mu A)_\nu(x)=\eta^{-1}[\operatorname{Ad}W_\mu(x)A_\nu(x+\eta e_\mu)-A_\nu(x)]$, for $W=U$ or $W=\mathbf U$. A *stencil* at a bond $b=\langle x,x+\eta e_\nu\rangle$ in direction $\mu$ is the pair of bonds $b$ and $b'=\langle x+\eta e_\mu,x+\eta e_\mu+\eta e_\nu\rangle$ ($\mu=\nu$ allowed); it is contained in a bond set if both bonds are.

Lattice levels. $\mathbb T^{(n)}$ is the level-$n$ lattice (spacing $\xi_n$, sites at the centres of the level-$n$ blocks, nested because $L$ is odd; SA L7070-7072). For $z\in\mathbb T^{(n+1)}$, $B(z)=B^{n+1}(z)\cap\mathbb T^{(n)}$ is the set of $L^4$ level-$n$ sites of its block, and $B^{n+1}(z)$ also denotes the set of bare sites of the block. A level-$n$ bond has length $\xi_n$; as a path of the level-$(n-1)$ lattice it is a straight segment $[c]$ of $L$ bonds. For $z\in\mathbb T^{(n+1)}$ and $x\in B(z)$, $\mathcal G(z,x)$ is the family of shortest level-$n$ paths from $z$ to $x$ that complete the displacement in one direction before the next (at most $4!=24$ members), and $\Gamma_{z,x}$ is its member with order $4,3,2,1$ (SA L7065). Every member has $\sum_\mu|x_\mu-z_\mu|/\xi_n\le4(L-1)/2=2(L-1)$ bonds.

Pillars. Fix a top $y$ of level $q\ge1$. The pillar is the set of bare sites $B^q(y)$, of side $\xi_q$; its bonds $\mathsf P(B^q(y))$ are the bare bonds with both endpoints in it. Put $t_n=L^{n-q}=\xi_n/\xi_q$ for $0\le n\le q$. **Geometric convention (G0).** As in YM3's setting (YM3 L54636-54656), each determining member $\Omega_l$ is a union of level-$l$ blocks, and the sites of a level-$q$ pillar lie in layer $q$, so $l(x)=\xi_q$ on $B^q(y)$. Since level-$(q+1)$ blocks are unions of level-$q$ blocks, a level-$q$ block lies inside $\Omega_{q+1}$ or is disjoint from it, so the convention is a statement about tops only. (If a reader prefers pillars whose scale is within a factor $L$ of $\xi_q$, as `a3-derivative.md:461` allows, every weighted length in Lemma G4 is multiplied by at most $L$; only the constants $24$ and $10$ of Section 9.9 change.)

## 4. Elementary lemmas

Each lemma below is an inequality about finitely many $2\times2$ matrices or a finite-dimensional holomorphic map. Each is proved by power series, the triangle inequality, or the one-variable maximum principle. All are Lean-formalizable (Mathlib has the matrix exponential, normed algebras, the Cauchy estimate, and the identity theorem for analytic functions on connected sets).

**Lemma E1 (exponential).** [proved here] For $X,Y,X_k\in M_2(\mathbb C)$: $|e^X-1|\le e^{|X|}-1\le|X|e^{|X|}$; $|e^X-e^Y|\le|X-Y|e^{\max(|X|,|Y|)}$; $|\prod_ke^{X_k}-1|\le e^{\sum_k|X_k|}-1$; and if $W_1,\dots,W_N$ are unitary, $|\prod W_k-1|\le\sum_k|W_k-1|$.

*Proof.* The first from the series. The second from $e^X-e^Y=\int_0^1e^{sX}(X-Y)e^{(1-s)Y}ds$. The third by induction: $\prod_{k\le m+1}e^{X_k}-1=(\prod_{k\le m}e^{X_k}-1)e^{X_{m+1}}+(e^{X_{m+1}}-1)$, so $d_{m+1}\le d_me^{|X_{m+1}|}+e^{|X_{m+1}|}-1$, and $d_m\le e^{\sum_{k\le m}|X_k|}-1$ satisfies this. The fourth by the telescoping identity $\prod W_k-1=\sum_k(\prod_{h<k}W_h)(W_k-1)$ and unitarity. ∎

**Lemma E2 (logarithm).** [proved here] For $|X-1|\le\kappa<1$ define $\log X=\sum_{n\ge1}(-1)^{n+1}(X-1)^n/n$. Then $e^{\log X}=X$; $|\log X|\le-\log(1-\kappa)\le\kappa/(1-\kappa)$; $|\log X-\log Y|\le|X-Y|/(1-\kappa)$ if also $|Y-1|\le\kappa$; $\log e^Z=Z$ if $|Z|<\log2$; and $\log(gXg^{-1})=g(\log X)g^{-1}$ whenever $\operatorname{cn}(g)\,|X-1|<1$. Also $\log(X^*)=(\log X)^*$ and $\log X^{-1}=-\log X$ on this ball.

*Proof.* The bounds and $e^{\log X}=X$, $\log e^Z=Z$ are identities of absolutely convergent power series (for $\log e^Z$, $\sum_n|Z|^n/n!=e^{|Z|}-1<1$ allows rearrangement). The derivative of $\log(1+Z)$ in direction $H$ is a sum of words with $n-1$ factors $Z$ and one $H$, of norm at most $\sum_n|Z|^{n-1}|H|=|H|/(1-|Z|)$; integrate along the segment. The conjugation identity holds term by term, since $(g(X-1)g^{-1})^n=g(X-1)^ng^{-1}$ and both series converge. The last two hold term by term. ∎

**Lemma E3 (adjoint).** [proved here] $|\operatorname{Ad}(g)Z|\le\operatorname{cn}(g)|Z|$, with equality of norms for unitary $g$; $|\operatorname{Ad}(e^X)-1|\le e^{2|X|}-1$; $|\operatorname{Ad}(e^X)-\operatorname{Ad}(e^Y)|\le2|X-Y|e^{2\max(|X|,|Y|)}$; and $|\operatorname{Ad}(X)-1|\le2|X^{-1}|\,|X-1|$.

*Proof.* $\operatorname{Ad}(e^X)=e^{\operatorname{ad}X}$ and $|\operatorname{ad}X|\le2|X|$; apply E1 to $\operatorname{ad}X,\operatorname{ad}Y$. For the last, $XZX^{-1}-Z=(X-1)ZX^{-1}+Z(X^{-1}-1)$ and $X^{-1}-1=X^{-1}(1-X)$. ∎

**Lemma E4 (BCH remainder).** [proved in `st1.md` Lemma 3 (L313-338), restated] Put $\ell(X,Z)=\log(e^Xe^Z)-X-Z$. For all arguments of norm at most $1/16$, $|\ell(X,Z)-\ell(X,Z')|\le96|X||Z-Z'|$ and $|\ell(X,Z)-\ell(X',Z)|\le96|Z||X-X'|$. In particular $|\ell(X,Z)|\le96|X||Z|$, and $|\log(e^Xe^Z)|\le1.01(|X|+|Z|)$ when $|X|,|Z|\le10^{-4}$.

*Proof.* The first inequality is `st1.md` (26), proved at L336-338 by Schwarz's lemma in the first variable and a Cauchy circle in the second. The second follows from the first and the identity $\ell(X,Z)=-\ell(-Z,-X)$, which holds because $\log(e^{-Z}e^{-X})=\log((e^Xe^Z)^{-1})=-\log(e^Xe^Z)$ (E2). The third is the first with $Z'=0$, since $\ell(X,0)=0$. The last: $|\ell|\le96\cdot10^{-4}\max(|X|,|Z|)\le0.01(|X|+|Z|)$. ∎

**Lemma E5 (Schwarz and Cauchy, vector-valued).** [proved here] Let $V,W$ be finite-dimensional complex normed spaces, $F$ holomorphic on the open ball $\{\|z\|<R\}\subset V$ with $\|F\|\le M$. (i) If $F(0)=0$, then $\|F(z)\|\le M\|z\|/R$. (ii) For $\|z\|<R$, $\|DF(z)\|\le M/(R-\|z\|)$. (iii) If $F$ is holomorphic on $\{\|z\|<2R\}$, bounded by $M$, then for $\|z\|,\|z'\|\le R/2$, $\|DF(z)-DF(z')\|\le 2M\|z-z'\|/R^2$.

*Proof.* (i) For a unit $e$ and a norm-one functional $\ell$ on $W$, $g(\zeta)=\ell(F(\zeta e))/\zeta$ is holomorphic on $|\zeta|<R$; the maximum principle on $|\zeta|=r<R$ gives $|g|\le M/r$; let $r\to R$ and take the supremum over $\ell$ (Hahn-Banach in finite dimension). (ii) Cauchy's formula on the disc $\zeta\mapsto F(z+\zeta h)$, $|\zeta|<R-\|z\|$, $\|h\|=1$. (iii) By (ii) on the ball of radius $2R$, $\|DF(w)\|\le M/R$ for $\|w\|\le R$. Fix a unit $h$; $G=DF(\cdot)h$ is holomorphic and bounded by $M/R$ on $\{\|w\|<R\}$. For $\|w\|\le R/2$, (ii) for $G$ on the ball of radius $R/2$ about $w$ gives $\|DG(w)\|\le(M/R)/(R/2)=2M/R^2$. Integrate $DG$ along the segment $[z',z]$, which stays in $\{\|w\|\le R/2\}$. ∎

**Lemma E6 (mixed exponential difference).** [proved here; YM3 L55024-55031] For $\theta_0,\theta_1,\theta_2,\theta_{12}\in M_2(\mathbb C)$ with $|\theta_j|\le r$, put $d_i=|\theta_i-\theta_0|$, $s=|\theta_{12}-\theta_1-\theta_2+\theta_0|$. Then
\[
 |e^{\theta_{12}}-e^{\theta_1}-e^{\theta_2}+e^{\theta_0}|\le e^{3r}s+e^{5r}d_1d_2 .
\]
*Proof.* Put $\delta_i=\theta_i-\theta_0$, $\sigma=\theta_{12}-\theta_1-\theta_2+\theta_0$. Split the left side as $[e^{\theta_0+\delta_1+\delta_2+\sigma}-e^{\theta_0+\delta_1+\delta_2}]+[e^{\theta_0+\delta_1+\delta_2}-e^{\theta_0+\delta_1}-e^{\theta_0+\delta_2}+e^{\theta_0}]$. The first bracket is at most $se^{3r}$ by E1, since $|\theta_1+\theta_2-\theta_0|\le3r$. The second is $\int_0^1\int_0^1D^2\exp(\theta_0+t_1\delta_1+t_2\delta_2)[\delta_1,\delta_2]dt_1dt_2$; the second derivative of $\theta\mapsto\theta^n$ is a sum of $n(n-1)$ words, so $|D^2\exp(\theta)[h,k]|\le e^{|\theta|}|h||k|$, and $|\theta_0+t_1\delta_1+t_2\delta_2|\le5r$. ∎

**Lemma LD (logarithmic differences).** [proved here; YM3 (eq:levelling-log-differences), YM3 L54990-54998, with the proof rebuilt in a smaller regime] Let $|\theta_0|,|\theta_1|,|\theta_2|,|\theta_{12}|\le r\le1/20$ and $|\alpha_0|,|\alpha_1|\le\rho\le1/20$; put $X_0=e^{-i\theta_0}e^{i\alpha_0}e^{i\theta_2}$, $X_1=e^{-i\theta_1}e^{i\alpha_1}e^{i\theta_{12}}$, and $d_i,s$ as in E6. Then $|X_j-1|\le1/5$ and
\[
 |\log X_0|\le3|\alpha_0|+3d_2,\qquad
 |\log X_1-\log X_0|\le3|\alpha_1-\alpha_0|+5s+7d_1d_2+6\rho d_1 .
 \tag{LD}
\]
*Proof.* Write $u_j=e^{-i\theta_j}$, $a_j=e^{i\alpha_j}$, so $X_0=u_0a_0u_2^{-1}$, $X_1=u_1a_1u_{12}^{-1}$. Then $X_0-1=u_0(a_0-1)u_2^{-1}+(u_0-u_2)u_2^{-1}$, so by E1 $|X_0-1|\le e^{2r}(\rho e^\rho+d_2)\le e^{2r}(\rho e^\rho+2r)\le1.106(0.053+0.1)<1/5$; the same for $X_1$, with $|\theta_{12}-\theta_1|\le2r$. On the $1/5$-ball the logarithm has $|\log X|\le\frac54|X-1|$ and Lipschitz constant $\frac54$ (E2). Hence $|\log X_0|\le\frac54e^{2r}(e^{\rho}|\alpha_0|+d_2)\le1.47(|\alpha_0|+d_2)$. Next, expanding $a_j=1+(a_j-1)$,
\[
\begin{split}
 X_1-X_0={}&[(u_1-u_{12})-(u_0-u_2)]u_{12}^{-1}+(u_0-u_2)(u_{12}^{-1}-u_2^{-1})\\
 &+(u_1-u_0)(a_1-1)u_{12}^{-1}+u_0(a_1-a_0)u_{12}^{-1}+u_0(a_0-1)(u_{12}^{-1}-u_2^{-1}),
\end{split}
\]
which is checked by expanding: the first two terms sum to $u_1u_{12}^{-1}-u_0u_2^{-1}$, the last three to $u_1(a_1-1)u_{12}^{-1}-u_0(a_0-1)u_2^{-1}$. The bracket in the first term is minus the mixed difference of $\theta\mapsto e^{-i\theta}$, bounded by E6 by $e^{3r}s+e^{5r}d_1d_2$. By E1, $|u_0-u_2|\le e^rd_2$, $|u_1-u_0|\le e^rd_1$, $|u_{12}^{-1}-u_2^{-1}|\le e^r|\theta_{12}-\theta_2|\le e^r(d_1+s)$, $|a_1-1|,|a_0-1|\le\rho e^\rho$, $|a_1-a_0|\le e^\rho|\alpha_1-\alpha_0|$, $|u^{\pm1}|\le e^r$. So
\[
 |X_1-X_0|\le e^{4r}s+(e^{6r}+e^{2r})d_1d_2+e^{2r}d_2s+2e^{2r+\rho}\rho d_1+e^{2r+\rho}|\alpha_1-\alpha_0|+e^{2r+\rho}\rho s .
\]
With $r,\rho\le1/20$ and $d_2\le2r$: the coefficient of $s$ is at most $1.222+0.111+0.059$, of $d_1d_2$ at most $2.456$, of $\rho d_1$ at most $2.324$, of $|\alpha_1-\alpha_0|$ at most $1.162$. Multiply by $\frac54$: $1.74\le5$, $3.07\le7$, $2.91\le6$, $1.45\le3$. ∎

**Lemma TRU (totally real uniqueness).** [proved here] Let $D\subset\mathbb C^N$ be open and connected, and $f$ holomorphic on $D$ with values in a finite-dimensional space. If $f=0$ on a nonempty open subset of $D\cap\mathbb R^N$, then $f=0$ on $D$.

*Proof.* At a point $x_0$ of that real open set, every real partial derivative of every order vanishes. For holomorphic $f$, $\partial f/\partial z_j=\partial f/\partial x_j$ on real points, so all complex derivatives at $x_0$ vanish; the power series of $f$ at $x_0$ is zero, so $f=0$ near $x_0$; the identity theorem on the connected set $D$ gives $f=0$. ∎

## 5. Four-dimensional geometry of pillars and cells

**Definitions (four-dimensional transcription of YM3 L54636-54708).** Fix a localization domain $Y$ and the sequence $\Omega_\bullet$. Put $\mathfrak e_Y=\operatorname{Bd}(Y)\cap\operatorname{Bd}^\circ(\Omega_0)$ and $S_Y=\{$endpoints of bonds in $\operatorname{Bd}(Y)\}$. For a positive bond $b$ let $y(b)$ and $n(b)$ be the top and level of the pillar containing $b_-$, and $\xi_{y(b)}=\xi_{n(b)}$. A top $y$ of level $q\ge1$ is a *top in $Y$* if $B^q(y)\subset Y$; $\mathsf{Tp}(Y)$ is the set of these. It is *pinnable* if $q\ge2$, or $q=1$ and every bare site within $\infty$-distance $2\eta$ of $B^1(y)$ lies in a pillar of level zero or one. *Turning cells:* for a pinnable top, the cells $\mathsf C(a)=B^{q-1}(a)$, $a\in B(y)$, of order $o(a)=q-1$; for a nonpinnable top (necessarily $q=1$), the single cell $\mathsf C(y)=B^1(y)$ of order $1$. $\mathsf{Ct}(Y)$ is the set of centres, $y(a)$ the top of $a$. The cells are disjoint and partition the pillars of $\mathsf{Tp}(Y)$, since level-$(q-1)$ blocks tile level-$q$ blocks. A cell of order $0$ is a singleton. Its *inner third* is $\{x\in\mathsf C(a):|x_\mu-a_\mu|<\xi_o/3\ \forall\mu\}$.

**Lemma G4.** [proved here] Let $d_{\mathbf B}$ be the weighted distance with density $l(x)^{-1}$, path lengths measured along coordinate paths (an upper bound for Euclidean length).

(a) Two sites of one level-$q$ pillar are at weighted distance less than $4$; a site and its top are at distance less than $2$.

(b) Two bare sites at $\infty$-distance at most $2\eta$ are at weighted distance at most $8$.

(c) If $o\ge1$ and $L^o\ge13$, the two-step neighbourhood ($\infty$-distance at most $2\eta$) of the inner third of a cell of order $o$ is contained in the cell.

(d) If $y'$ is a pinnable level-one top whose pillar is within $\infty$-distance $2\eta$ of $B^{q}(y)$, $x\in B^q(y)$, and $x'$ lies in $B^1(y')$ or within $\infty$-distance $2\eta$ of it, then $d_{\mathbf B}(x,x')\le4+8+4+8=24$; if $x'\in B^1(y')$ the bound is $16$.

(e) If $u\ne\mathbf1$ is possible only at sites of inner thirds of positive-order cells and at singleton cells (Section 9), a bond outside $\mathfrak e_Y$ has $u=\mathbf1$ at both endpoints; more precisely every bond with an endpoint in such a site belongs to $\mathsf P$ of that cell's pillar, or (singletons) to $\operatorname{Rd}_Y(y')$ of the singleton's top $y'$.

*Proof.* (a) By (G0) the density on the pillar is $\xi_q^{-1}$. A coordinate path between two sites of the pillar has at most $\sum_\mu(L^q-1)=4(L^q-1)$ bare steps of length $\eta$, inside the pillar; its weighted length is at most $4(L^q-1)\eta/\xi_q<4$. From a site to the centre $y$ there are at most $4(L^q-1)/2$ steps, giving less than $2$. (b) At most $8$ bare steps, and $l(x)\ge\eta$ everywhere, so each step has weight at most $1$. (c) In lattice steps from the centre, inner-third sites have $|k|<L^o/3$, so $|k|\le\lceil L^o/3\rceil-1\le(L^o-1)/3$; the cell has $|k|\le(L^o-1)/2$; and $(L^o-1)/3+2\le(L^o-1)/2$ iff $L^o\ge13$. (d) $x$ to a site $s$ of $B^q(y)$ near $B^1(y')$: less than $4$ by (a); $s$ to a site $s'$ of $B^1(y')$: at most $8$ by (b); $s'$ to any site of $B^1(y')$: less than $4$; and at most $8$ more to a site within $2\eta$. (e) If $x$ is in the inner third of a positive-order cell of a top $y$, every bond at $x$ has its other endpoint within $\eta$ of $x$, hence in the cell by (c); so the bond is in $\mathsf P(B^q(y))\subset\mathfrak e_Y$ (the pillar lies in $Y$ and in $\Omega_0$). If $x$ is a singleton of a pinnable level-one top $y'$, every bond at $x$ has both endpoints within $\eta$ of $B^1(y')$; the far endpoint lies in a pillar (pinnability), hence in $\Omega_0$, so the bond is in $\mathfrak e_Y$ and in $\operatorname{Rd}_Y(y')$. ∎

*Read sets and neighbours* (YM3 L54692-54708, verbatim in content). For $y\in\mathsf{Tp}(Y)$ of level $q$, $\operatorname{Rd}_Y(y)=\mathsf P(B^q(y))$, except at pinnable level-one tops, where it is the set of bonds of $\mathfrak e_Y$ with both endpoints within $2\eta$ of $B^1(y)$. The neighbours $\operatorname{nb}_Y(y)$ of a top are $y$ and the pinnable level-one tops $y'$ in $Y$ whose pillars are within $2\eta$ of $B^q(y)$.

---

## Part II. The four-dimensional pillar averaging package

YM3's proof of II-85-34 imports the bounds (II-155-25) of its own averaging theory (YM3 L49647-49662, "the relative recursion and accumulated factors"). This part proves their four-dimensional form from SA's averaging formula. The only averaging estimate imported is CURV, the real curvature recursion.

## 6. SA's average, and the elementary objects

### 6.1 The formula

Everything below is SA's definition (SA L7065-7106), restricted to its main rule. Let $W$ be a complex configuration on the level-$n$ bonds of a region.

- *Contour variable:* for $z\in\mathbb T^{(n+1)}$, $x\in B(z)$, $W(z,x)=\operatorname{av}\bigl(W(\Gamma)\bigr)_{\Gamma\in\mathcal G(z,x)}$, the Federbush mean (Lemma FM) of the path products; $W(x,z)=W(z,x)^{-1}$, $W(z,z)=\mathbf1$.
- *Comb transport:* $W(\Gamma_{z,x})$, the ordered product along the comb.
- *Average:* for a level-$(n+1)$ bond $c$ with $x'=x+(c_+-c_-)$, $W_x=W(c_-,x)\,W([x,x'])\,W(x',c_+)\,W[c]^{-1}$ and $\mathcal M(W)(c)=\exp\bigl(L^{-4}\sum_{x\in B(c_-)}\log W_x\bigr)W[c]$ (SA L7066-7069), where $W[c]$ and $W([x,x'])$ are the straight products of $L$ level-$n$ bonds.
- *Block factor and straightened average* of $\mathbf W=e^{i\mathsf a}W$ relative to $W$ (SA L7092-7097): $\mathsf u_W(\mathsf a)(z)=\exp\bigl(L^{-4}\sum_{x\in B(z)}\log[\mathbf W(z,x)W(z,x)^{-1}]\bigr)$ and $\mathcal Q^1(W,\mathsf a)(c)=i^{-1}\log\bigl[\mathsf u(c_-)^{-1}\mathcal M(\mathbf W)(c)\mathsf u(c_+)\mathcal M(W)(c)^{-1}\bigr]$, so that, by Lemma E2,
\[
 \mathcal M(e^{i\mathsf a}W)=\bigl(e^{i\mathcal Q^1(W,\mathsf a)}\mathcal M(W)\bigr)^{\mathsf u_W(\mathsf a)} .
 \tag{6.1}
\]
- *Logarithmic increments:* $\zeta_W(\mathsf a)(z,x)=i^{-1}\log[\mathbf W(z,x)W(z,x)^{-1}]$ and $\zeta^{\rm c}_W(\mathsf a)(z,x)=i^{-1}\log[\mathbf W(\Gamma_{z,x})W(\Gamma_{z,x})^{-1}]$. Thus $\mathsf u_W(\mathsf a)(z)=e^{i\bar\zeta(z)}$, $\bar\zeta(z)=L^{-4}\sum_{x\in B(z)}\zeta_W(\mathsf a)(z,x)$.
- *Iteration* (SA L7101-7106): $\mathcal M^n$ is the iterate. Along $R_n=\mathcal M^nR_0$ and an increment $\mathsf a_0$: $\mathsf a_{n+1}=\mathcal Q^1(R_n,\mathsf a_n)$, $v_0=\mathbf1$, $v_{n+1}=v_n\,\mathsf u_{R_n}(\mathsf a_n)$; "the product $v_k=v_k[A]$ of the $k$ block factors is the node factor".

SA uses two cruder rules for real configurations off $\mathrm{Dom}(c)=\{\varpi_c<cL^{-2}\}$ (SA L7070-7080). They never occur below: every configuration in this part is, in a suitable gauge, within $10^{-2}$ of the identity link by link on the relevant blocks (Lemma ONE (i)), and real data there have plaquettes far below $cL^{-2}$ (CURV).

**Locality (Lemma LOC).** [proved here, from the formula] $\mathsf u_W(\mathsf a)(z)$, $\zeta(z,x)$, $\zeta^{\rm c}(z,x)$ and the contour and comb transports at $z$ read only the level-$n$ bonds of $B^{n+1}(z)$. $\mathcal M(W)(c)$ and $\mathcal Q^1(W,\mathsf a)(c)$ read only the level-$n$ bonds of the double block $D(c)=B^{n+1}(c_-)\cup B^{n+1}(c_+)$. Consequently, for a top $y$ of level $q$: the averages $\mathcal M^nW$ on the level-$n$ bonds inside $B^q(y)$ ($n\le q-1$), the recursion $\mathsf a_n$ on those bonds, the block factors $\mathsf u_n$ at the level-$(n+1)$ sites of $B^q(y)$ ($n\le q-1$), the node factors $v_n$ at the level-$n$ sites of $B^q(y)$ and $v_q(y)$, and the transports $W_{q-1}(\Gamma_{y,a})$, $W_{q-1}(y,a)$, $a\in B(y)$, read only $\mathsf P(B^q(y))$.

*Proof.* The first two sentences read off the formula: every path in $\mathcal G(z,x)$ and the comb lie in $B^{n+1}(z)$; $W_x$ uses $B^{n+1}(c_-)$, the segment $[x,x']$ and $B^{n+1}(c_+)$. For the consequence, use induction on $n$: a level-$(n+1)$ bond $c$ with both endpoints in $B^q(y)$, $n+1\le q-1$, has $D(c)\subset B^q(y)$, because level-$(n+1)$ blocks tile level-$q$ blocks ($L$ odd, centred nesting). The top factor $v_q(y)=v_{q-1}(y)\mathsf u_{q-1}(y)$ uses $\mathsf u_{q-1}(y)$, which reads $B^q(y)$; it never uses a level-$q$ average. ∎

*Remark (no folding).* YM3 extends the configuration by coordinate folding to an adjacent double block (YM3 L54798-54805) because its recursion is formulated on double blocks. Lemma LOC shows that the pillar objects never read a level-$q$ double block, so no extension is needed in four dimensions.

### 6.2 The Federbush mean

**Lemma FM.** [proved here; SA L7065 defines the mean as "the solution, close to the family, of $\sum_i\log(V_iV^{-1})=0$"] Let $V_1,\dots,V_N\in GL(2,\mathbb C)$, $N\le24$, with spread $\sigma=\max_i|V_iV_1^{-1}-1|\le1/500$.

(a) The equation $\sum_i\log(V_iV^{-1})=0$ has exactly one solution $V$ with $|VV_1^{-1}-1|<1/100$; write $V=\operatorname{av}(V_\bullet)$. It has the form $V=e^XV_1$ with $|X|\le1.26\sigma$.

(b) $\operatorname{av}$ is holomorphic in $(V_1,\dots,V_N)$ on this set.

(c) If $\sigma\le1/2000$ and $g,h\in GL(2,\mathbb C)$ with $\operatorname{cn}(g)\le4$, then $\operatorname{av}(gV_\bullet h)=g\operatorname{av}(V_\bullet)h$.

(d) $\operatorname{av}(V,\dots,V)=V$; $\operatorname{av}(V_\bullet^{\mathfrak c})=\operatorname{av}(V_\bullet)^{\mathfrak c}$; a unitary family has a unitary mean.

(e) If $V_i=e^{X_i}V_0$, $|X_i|\le r\le1/2000$, then $\operatorname{av}(V_\bullet)=e^YV_0$ with $|Y-\bar X|\le102r^2$, $\bar X=N^{-1}\sum_iX_i$.

(f) If $V'_i=e^{D_i}V_i$ with $|D_i|\le d\le1/2000$ and both families have spread at most $1/500$, then $|\log(\operatorname{av}(V'_\bullet)\operatorname{av}(V_\bullet)^{-1})|\le6d$.

*Proof.* (a) Put $W_i=V_iV_1^{-1}$, $w_i=\log W_i$, so $|w_i|\le1.01\sigma\le0.00202$ (E2). Write a candidate as $V=e^XV_1$, $|X|\le1/16$. Then $V_iV^{-1}=e^{w_i}e^{-X}$, and with $\ell$ of Lemma E4 the equation reads $\sum_i(w_i-X+\ell(w_i,-X))=0$, i.e.
\[
 X=\Theta(X):=\bar w+N^{-1}\textstyle\sum_i\ell(w_i,-X).
\]
By E4, $|\Theta(X)-\Theta(X')|\le96\max_i|w_i|\,|X-X'|\le0.194|X-X'|$ and $|\Theta(X)|\le0.00202+0.194/16<1/16$ on $|X|\le1/16$. So $\Theta$ is a contraction of that ball and has exactly one fixed point there, with $|X|\le1.01\sigma/(1-0.194)\le1.26\sigma$. A solution $V$ with $|VV_1^{-1}-1|<1/100$ has $X=\log(VV_1^{-1})$ of norm at most $0.0102<1/16$, so it is this fixed point. All logarithms used are within their series balls ($|e^{w_i}e^{-X}-1|\le e^{0.065}-1<1$).

(b) The iterates $\Theta^k(0)$ are holomorphic in $(w_i)$, hence in $(V_i)$, and converge uniformly (contraction constant $0.194$); a uniform limit of holomorphic maps is holomorphic.

(c) The family $gV_ih$ has $(gV_ih)(gV_1h)^{-1}=gW_ig^{-1}$, so spread at most $4\sigma\le1/500$. The candidate $gVh$ has $(gVh)(gV_1h)^{-1}=ge^Xg^{-1}$, within $4(e^{1.26\sigma}-1)<1/100$ of $\mathbf1$. And $(gV_ih)(gVh)^{-1}=g(V_iV^{-1})g^{-1}$, so by E2 (the conjugated elements are within $4\cdot0.07<1$ of $\mathbf1$) $\sum_i\log(gV_iV^{-1}g^{-1})=g(\sum_i\log V_iV^{-1})g^{-1}=0$. Uniqueness in (a) gives the claim.

(d) The first: $V$ solves, with $X=0$. The second: $\mathfrak c$ is a real-analytic involution with $(AB)^{\mathfrak c}=A^{\mathfrak c}B^{\mathfrak c}$ and $\log(A^{\mathfrak c})=-(\log A)^*$ by E2; hence $\sum_i\log(V_i^{\mathfrak c}(V^{\mathfrak c})^{-1})=\sum_i\log((V_iV^{-1})^{\mathfrak c})=-(\sum_i\log V_iV^{-1})^*=0$, and $V^{\mathfrak c}(V_1^{\mathfrak c})^{-1}=(VV_1^{-1})^{\mathfrak c}$ is within $1/100$ of $\mathbf1$ (it is within $|VV_1^{-1}-1|/(1-|VV_1^{-1}-1|)$). Uniqueness gives $\operatorname{av}(V_\bullet^{\mathfrak c})=V^{\mathfrak c}$. For a unitary family, $V_\bullet^{\mathfrak c}=V_\bullet$, so $V^{\mathfrak c}=V$.

(e) The family has spread $\max_i|e^{X_i}e^{-X_1}-1|\le e^{2r}-1\le2.01r\le1/500$ (E1). Seek $V=e^YV_0$: the equation is $Y=\bar X+N^{-1}\sum_i\ell(X_i,-Y)$, a contraction with constant $96r\le0.048$ on $|Y|\le1/16$; so $|Y|\le r/0.952\le1.06r$ and $|Y-\bar X|\le96r\cdot1.06r\le102r^2$. The solution is within $1/100$ of $V_1$ relative to $V_1$ ($|e^Ye^{-X_1}-1|\le e^{2.06r}-1$), so it is $\operatorname{av}$.

(f) Let $X,X'$ be the fixed points of (a) for the two families, with $w'_i=\log(e^{D_i}W_ie^{-D_1})$. By E1, $|e^{D_i}W_ie^{-D_1}-W_i|\le2.01d$, so $|w'_i-w_i|\le2.02d$ (E2 on the $0.002$-ball). Then
\[
 |X'-X|\le|\bar w'-\bar w|+\max_i\bigl(|\ell(w'_i,-X')-\ell(w'_i,-X)|+|\ell(w'_i,-X)-\ell(w_i,-X)|\bigr)
 \le2.02d+0.194|X'-X|+96|X|\,2.02d ,
\]
by both inequalities of E4. With $|X|\le1.26\cdot0.002$ this gives $|X'-X|\le3.12d$. Finally $\operatorname{av}(V')\operatorname{av}(V)^{-1}=e^{X'}e^{D_1}e^{-X}$, and $|e^{X'}e^{D_1}e^{-X}-1|\le|e^{X'}(e^{D_1}-1)e^{-X}|+|(e^{X'}-e^X)e^{-X}|\le1.006d+3.14d$, whose logarithm is at most $4.2d\le6d$. ∎

### 6.3 The comb gauge

**Lemma CG.** [proved here] Let $U$ be real on the bonds of a box of a lattice of spacing $\xi$, with at most $m$ bonds in each direction, and let every plaquette of the box satisfy $|\partial U-1|\le\varpi$. There is a real gauge $g$ on the box, equal to $\mathbf1$ at a corner, such that $|U^g(b)-1|\le3m\varpi$ for every bond $b$ of the box.

*Proof.* Coordinates $0\le x_\mu\le m_\mu\le m$ with the corner at $0$. The tree: for each $x$, the path $P(x)$ from $0$ goes first along $e_4$ to $x_4$, then $e_3$, $e_2$, $e_1$. Its bonds are the $(z,z+e_k)$ with $z_1=\dots=z_{k-1}=0$. Set $g(x)=U(P(x))^{-1}$, so $U^g=\mathbf1$ on tree bonds. Let $b=(x,x+e_\mu)$ and $N(b)=\sum_{j<\mu}x_j$. If $N(b)=0$, $b$ is a tree bond. Otherwise let $k<\mu$ be the least index with $x_k>0$, and $p$ the plaquette $x-e_k\to x\to x+e_\mu\to x-e_k+e_\mu\to x-e_k$. Its two $e_k$-bonds start at $x-e_k$ and $x-e_k+e_\mu$, whose coordinates below $k$ vanish ($\mu>k$), so they are tree bonds. Hence $\partial U^g(p)=U^g(b)U^g(b')^{-1}$ with $b'=(x-e_k,x-e_k+e_\mu)$, and $N(b')=N(b)-1$. By induction $U^g(b)$ is a product of $N(b)\le3m$ plaquette holonomies of $U^g$, each a unitary conjugate of a plaquette holonomy of $U$. Lemma E1 (unitary telescoping) gives $|U^g(b)-1|\le3m\varpi$. ∎

### 6.4 The imported real estimate

**CURV (import).** There is $c_{\rm cv}>0$, depending only on $L$, such that: if $U$ is real on $\mathsf P(B^q(y))$, $q\ge1$, and every bare plaquette there has $|\partial U-1|\le c\,t_0^2$ with $c\le c_{\rm cv}$, then for $0\le n\le q-1$ the averages $\mathcal M^nU$ on the level-$n$ bonds inside $B^q(y)$ are given by SA's main rule, and every level-$n$ plaquette inside $B^q(y)$ has $|\partial(\mathcal M^nU)-1|\le2c\,t_n^2$.

*Source and status.* `a1-balaban.md` §3.5 rebuilds Balaban's curvature recursion, CMP 98 (48), as $v_{m+1}\le L^2v_m+C(L^2v_m)^2$ (3.6), and proves its uniformity: "suppose initially $v_0\le\alpha L^{-2n}$ ... Induction then gives $w_m<2\alpha$ at every step" (`a1-balaban.md` L358-366), $w_m=L^{2(n-m)}v_m$. With $n\leftrightarrow q$ this is CURV, since $t_m^2=L^{-2(q-m)}$; the recursion reads only the four blocks under a coarse plaquette (L366, "The argument uses only the four underlying blocks"), so it is pillar-local by Lemma LOC. It is also the content of ST1's import AV-conv (SA L9667: "if $U$ is any configuration whose plaquettes are regular at a small radius $\varepsilon\le cL^{-2}$, then the tests of $M_{\mathbf B}(U)$ are within $2\varepsilon$ of $\mathbf 1$ in the interior of a layer"). Status: [C] in the library (`a1-balaban.md` §3.5). It is an import here, not proved.

**Corollary RR (real reference in a gauge).** [proved here, from CURV and Lemma CG] Under CURV's hypothesis, for each $n\le q-1$ and each level-$(n+1)$ block or double block $D$ inside $B^q(y)$ there is a real gauge $g$ on the level-$n$ sites of $D$ with $(\mathcal M^nU)^g=e^{i\omega_0}$ on the level-$n$ bonds of $D$, $\|\omega_0\|\le13c\,t_n$.

*Proof.* $D$ has at most $m=2L-1$ level-$n$ bonds per direction, and its plaquettes have defect at most $2ct_n^2$ (CURV). Lemma CG gives $|(\mathcal M^nU)^g(b)-1|\le6(2L-1)ct_n^2\le12c\,t_n$, using $Lt_n\le1$ for $n\le q-1$. Lemma E2 gives $|\omega_0|\le1.01\cdot12ct_n$. ∎

## 7. One straightened step

Fix $c_1:=5\cdot10^{-5}$ and $r_1:=c_1/L$ (absolute, resp. depending only on $L$; fixed before $\kappa$; independent of $M,\bar\kappa$). For a level-$(n+1)$ block or double block $D$, let $\mathcal D_f(D)$ (the *formula domain*) be the set of pairs $(W,\mathsf a)$ of a complex configuration and an increment on the level-$n$ bonds of $D$ for which there is a complex gauge $h$ on the level-$n$ sites of $D$ with
\[
 \operatorname{cn}(h)\le4,\qquad W^h=e^{i\omega},\qquad \|\omega\|<r_1,\qquad \|\operatorname{Ad}(h)\mathsf a\|<r_1 ,
\]
and let $\mathcal D_1(D)$ be the subset where this holds with $h=\mathbf1$.

**Lemma ONE.** [proved here, from the formula, Lemmas E1-E5 and FM]

(i) *Definition and holomorphy.* On $\mathcal D_f(D)$ every object of Section 6.1 attached to $D$ (contour variables and combs of $W$ and $e^{i\mathsf a}W$, the loops $W_x$, $\mathcal M(W)$, $\mathcal M(e^{i\mathsf a}W)$, $\mathsf u$, $\zeta$, $\zeta^{\rm c}$, $\mathcal Q^1$) is defined by SA's main rule, with every logarithm in its series ball and every mean in the domain of Lemma FM(a). Each is holomorphic in $(W,\mathsf a)$ and is real (unitary, respectively Hermitian) at real data.

(ii) *Covariance.* If $(W,\mathsf a)\in\mathcal D_f(D)$ through a gauge $h$ with $\operatorname{cn}(h)\le2$, and $g$ is a complex gauge with $\operatorname{cn}(g)\le2$, then $(W^g,\operatorname{Ad}(g)\mathsf a)\in\mathcal D_f(D)$ and $W^g(z,x)=g(z)W(z,x)g(x)^{-1}$, $W^g(\Gamma_{z,x})=g(z)W(\Gamma_{z,x})g(x)^{-1}$, $\mathcal M(W^g)(c)=g(c_-)\mathcal M(W)(c)g(c_+)^{-1}$, $\mathsf u_{W^g}(\operatorname{Ad}g\,\mathsf a)(z)=g(z)\mathsf u_W(\mathsf a)(z)g(z)^{-1}$, $\zeta^{(\rm c)}_{W^g}(\operatorname{Ad}g\,\mathsf a)(z,x)=\operatorname{Ad}(g(z))\zeta^{(\rm c)}_W(\mathsf a)(z,x)$, and $\mathcal Q^1(W^g,\operatorname{Ad}g\,\mathsf a)(c)=\operatorname{Ad}(g(c_-))\mathcal Q^1(W,\mathsf a)(c)$. The same holds with $\mathfrak c$: the objects at $(W^{\mathfrak c},\mathsf a^{\mathfrak c})$ are the $\mathfrak c$-images.

(iii) *Zero increment.* $\mathsf u_W(0)=\mathbf1$, $\zeta=\zeta^{\rm c}=0$, $\mathcal Q^1(W,0)=0$.

(iv) *Block factor and increments.* On $\mathcal D_1(D)$: $|\zeta^{\rm c}_W(\mathsf a)(z,x)|\le2.2L\|\mathsf a\|$, $|\zeta_W(\mathsf a)(z,x)|\le12.6L\|\mathsf a\|$, $|\mathsf u_W(\mathsf a)(z)^{\pm1}-1|\le13.2L\|\mathsf a\|$.

(v) *The straightened step.* On $\mathcal D_1(D)$ with $\delta:=\|\omega\|+\|\mathsf a\|\le r_1/4$,
\[
 \|\mathcal Q^1(W,\mathsf a)\|\le L\|\mathsf a\|\,(1+C_1L\delta),\qquad C_1:=8/c_1^2 .
 \tag{7.1}
\]

*Proof.* (i) First on $\mathcal D_1(D)$, $W=e^{i\omega}$. Each link of $W$ or of $e^{i\mathsf a}W$ is $e^{i\chi}$ with $|\chi|\le1.01\cdot2r_1$ (E4). A product of $N$ links is within $e^{2.02Nr_1}-1$ of $\mathbf1$ (E1). Paths of $\mathcal G(z,x)$ have $N\le2(L-1)$: their products are within $4.1c_1$ of $\mathbf1$, so the family's spread is at most $8.3c_1\le1/2000$ and Lemma FM applies; the contour variable is within $e^{1.26\cdot8.3c_1+4.1c_1}-1\le15c_1$ of $\mathbf1$. The loop $W_x$ is a product of two contour variables and $2L$ links, within $e^{2\cdot15.2c_1+4.1c_1}-1\le35c_1$ of $\mathbf1$; its logarithm is defined, of norm at most $36c_1$; so $|\mathcal M(W)(c)-1|\le39c_1$, and the same for $e^{i\mathsf a}W$. Similarly $|\mathsf u-1|\le33c_1$, and the argument of the logarithm in $\mathcal Q^1$ is within $150c_1\le1/100$ of $\mathbf1$, so $|\mathcal Q^1|\le155c_1\le1$. Every step is a polynomial, a convergent series or a Federbush mean, so holomorphic (FM(b)); at real data every factor is unitary, every mean unitary (FM(d)), and the logarithms of unitary elements near $\mathbf1$ are $i$ times Hermitian. On $\mathcal D_f(D)$, by (ii) applied with the gauge $h^{-1}$, each object is a conjugate of the corresponding object at $(e^{i\omega},\operatorname{Ad}h\,\mathsf a)\in\mathcal D_1(D)$ by elements of condition number at most $4$: all spreads are at most $4\cdot8.3c_1\le1/500$, all loop arguments within $4\cdot35c_1<1/2$ of $\mathbf1$, so the formulas are defined directly at $(W,\mathsf a)$.

(ii) Path products are exactly covariant: $W^g(\Gamma)=g(z)W(\Gamma)g(x)^{-1}$. Means: both $W=(e^{i\omega})^{h^{-1}}$ and $W^g=(e^{i\omega})^{gh^{-1}}$ are gauge images of the base configuration $e^{i\omega}$, whose path families have spread at most $8.3c_1\le1/2000$ (proof of (i)); Lemma FM(c), applied to the base families with the conjugations $h^{-1}$ and $gh^{-1}$ (condition numbers at most $2$ and $4$), gives the covariance of the means at $W$ and at $W^g$, hence between them. Loops: $W^g_x=g(c_-)W_xg(c_-)^{-1}$; Lemma E2 conjugates the logarithm (the conjugated loop is within $4\cdot35c_1<1$ of $\mathbf1$); the mean of logarithms and the exponential conjugate; and $W^g[c]=g(c_-)W[c]g(c_+)^{-1}$. The block factor: $\mathbf W^g(z,x)W^g(z,x)^{-1}=g(z)\mathbf W(z,x)W(z,x)^{-1}g(z)^{-1}$, with $\mathbf W^g=e^{i\operatorname{Ad}g\,\mathsf a}W^g$. Then $\mathcal Q^1$ conjugates by $g(c_-)$. Membership of $(W^g,\operatorname{Ad}g\,\mathsf a)$ in $\mathcal D_f(D)$ holds with the gauge $hg^{-1}$, of condition number at most $4$. The $\mathfrak c$ statement follows in the same way from $(AB)^{\mathfrak c}=A^{\mathfrak c}B^{\mathfrak c}$, E2 and FM(d).

(iii) At $\mathsf a=0$, $\mathbf W=W$; every ratio is $\mathbf1$.

(iv) For a path $\Gamma$ of $N\le2(L-1)$ bonds, moving the exponentials to the left gives $(e^{i\mathsf a}W)(\Gamma)=\bigl[\prod_ke^{i\operatorname{Ad}(P_k)\mathsf a_k}\bigr]W(\Gamma)$, $P_k$ the product of the first $k-1$ links of $W$, $\operatorname{cn}(P_k)\le e^{2Nr_1}\le1.0002$. So $|(e^{i\mathsf a}W)(\Gamma)W(\Gamma)^{-1}-1|\le e^{1.0002N\|\mathsf a\|}-1\le2.01(L-1)\|\mathsf a\|\cdot1.001$, and its logarithm $D_\Gamma$ has $|D_\Gamma|\le2.1L\|\mathsf a\|\le2.1c_1\le1/2000$. This is the bound for $\zeta^{\rm c}$ (with $2.2$). For $\zeta$, apply Lemma FM(f) with $d=2.1L\|\mathsf a\|$: $|\zeta|\le12.6L\|\mathsf a\|$. Then $\mathsf u=e^{i\bar\zeta}$ with $|\bar\zeta|\le12.6L\|\mathsf a\|$, and E1 gives $|\mathsf u^{\pm1}-1|\le e^{12.6L\|\mathsf a\|}-1\le13.2L\|\mathsf a\|$.

(v) Let $F(\omega,\mathsf a)=\mathcal Q^1(e^{i\omega},\mathsf a)(c)$, holomorphic on the ball $\{\max(\|\omega\|,\|\mathsf a\|)<r_1\}$ and bounded by $1$ there (by (i)). *Its derivative at $(0,0)$.* At $\omega=0$, $\mathbf W=e^{i\mathsf a}$. Each path product is $\exp(i\mathsf a(\Gamma)+O(\|\mathsf a\|^2))$, $\mathsf a(\Gamma)=\sum_k\mathsf a_k$ (E4). By FM(e), $\log\mathbf W(z,x)=i\bar{\mathsf a}(z,x)+O(\|\mathsf a\|^2)$, $\bar{\mathsf a}(z,x)$ the arithmetic mean of $\mathsf a(\Gamma)$ over $\mathcal G(z,x)$, and $W(z,x)=\mathbf1$. Hence $\log\mathsf u(z)=i\sigma(z)+O(\|\mathsf a\|^2)$, $\sigma(z)=L^{-4}\sum_{x\in B(z)}\bar{\mathsf a}(z,x)$. Next $\log\mathbf W_x=i[\bar{\mathsf a}(c_-,x)+\mathsf a([x,x'])-\bar{\mathsf a}(c_+,x')-\mathsf a[c]]+O(\|\mathsf a\|^2)$, and since $x\mapsto x'$ is a bijection $B(c_-)\to B(c_+)$, $\log\mathcal M(\mathbf W)(c)=i[\sigma(c_-)+(Q^{\rm s}\mathsf a)(c)-\sigma(c_+)]+O(\|\mathsf a\|^2)$, with $(Q^{\rm s}\mathsf a)(c)=L^{-4}\sum_{x\in B(c_-)}\mathsf a([x,x'])$ (SA L7076-7086: $Q^{\rm pl}=\sigma(c_-)+Q^{\rm s}-\sigma(c_+)$ "is the derivative of $\mathcal M$ at $\mathbf1$"). Conjugating by $\mathsf u(c_\mp)^{\mp1}$ removes $\sigma$: $F(0,\mathsf a)=Q^{\rm s}\mathsf a+O(\|\mathsf a\|^2)$. The $O(\cdot)$ terms are bounded by explicit multiples of $\|\mathsf a\|^2$ (E4, FM(e)), so $D_{\mathsf a}F(0,0)=Q^{\rm s}$, whose norm as a map from bond increments (sup norm) to the value at $c$ is at most $L^{-4}\cdot L^4\cdot L=L$. *The estimate.* Lemma E5(iii) with $2R=r_1$ and $M=1$: for $\max(\|\omega\|,\|\mathsf a\|)\le r_1/4$, $\|D_{\mathsf a}F(\omega,\mathsf a)-Q^{\rm s}\|\le8\max(\|\omega\|,\|\mathsf a\|)/r_1^2\le8L^2\delta/c_1^2$. Since $F(\omega,0)=0$, $F(\omega,\mathsf a)=\int_0^1D_{\mathsf a}F(\omega,s\mathsf a)[\mathsf a]\,ds$, so $|F|\le(L+8L^2\delta/c_1^2)\|\mathsf a\|$. ∎

## 8. The pillar recursion

**Proposition REC.** [proved here, from Lemma ONE] Fix a top $y$ of level $q\ge1$. Let $R_0$ be a complex configuration on $\mathsf P(B^q(y))$ and $\mathsf a_0$ an increment there with $\|\mathsf a_0\|\le\epsilon\,t_0$. Put $k_0:=c_1^2/1000$ (absolute). Assume: for each $n\le q-1$ the averages $R_n=\mathcal M^nR_0$ on the level-$n$ bonds inside $B^q(y)$ are defined, and for each level-$(n+1)$ block or double block $D$ inside $B^q(y)$ there is a complex gauge $h_{n,D}$ on its level-$n$ sites with
\[
 \operatorname{cn}(h_{n,D})\le1+\kappa_n,\qquad R_n^{h_{n,D}}=e^{i\omega},\ \|\omega\|\le K_0t_n ,
\]
where $K_0\le k_0$, $\epsilon\le k_0$, $\kappa_n\le1/100$ and $\sum_n\kappa_n\le1/100$. Define $\mathsf a_{n+1}=\mathcal Q^1(R_n,\mathsf a_n)$ ($n\le q-2$), $\mathsf u_n=\mathsf u_{R_n}(\mathsf a_n)$ ($n\le q-1$), $v_{n+1}=v_n\mathsf u_n$, $v_0=\mathbf1$. Then:

(i) all these are defined (on the bonds and sites inside $B^q(y)$), and $\|\mathsf a_n\|\le1.04\,\epsilon\,t_n$ for $n\le q-1$;

(ii) $|\mathsf u_n^{\pm1}-1|\le14\,\epsilon\,t_{n+1}$;

(iii) $|v_n(x)^{\pm1}-1|\le16\,\epsilon\,t_n$ at the level-$n$ sites $x$ of $B^q(y)$, $1\le n\le q$ (at $n=q$, at $y$);

(iv) $\mathcal M^n(e^{i\mathsf a_0}R_0)=(e^{i\mathsf a_n}R_n)^{v_n}$ on the level-$n$ bonds inside $B^q(y)$, $n\le q-1$;

(v) everything is holomorphic in the data on the set where the hypotheses hold, real at real data, $\mathfrak c$-equivariant, covariant under real gauges $g$ of the pillar ($\mathsf a_n\mapsto\operatorname{Ad}g\,\mathsf a_n$, $\mathsf u_n\mapsto g\mathsf u_ng^{-1}$, $v_n\mapsto gv_ng^{-1}$ at the corresponding sites), and reads only $\mathsf P(B^q(y))$.

*Proof.* (i) Put $p_n=\|\mathsf a_n\|/t_n$, so $p_0\le\epsilon$. Suppose $p_m\le1.04\epsilon$ for $m\le n$, $n\le q-2$. Fix a level-$(n+1)$ bond $c$ inside $B^q(y)$ and the gauge $h=h_{n,D(c)}$. Then $(R_n^h,\operatorname{Ad}h\,\mathsf a_n)=(e^{i\omega},\tilde{\mathsf a})$ with $\|\tilde{\mathsf a}\|\le1.01\cdot1.04\epsilon t_n$, and $\delta=\|\omega\|+\|\tilde{\mathsf a}\|\le(K_0+1.06\epsilon)t_n\le2.06k_0/L^2<r_1/4$. So $(R_n,\mathsf a_n)\in\mathcal D_f(D(c))$, $\mathcal Q^1(R_n,\mathsf a_n)(c)=\operatorname{Ad}(h(c_-))^{-1}\mathcal Q^1(e^{i\omega},\tilde{\mathsf a})(c)$ (ONE (ii)), and by (7.1)
\[
 \|\mathsf a_{n+1}\|\le(1+\kappa_n)^2L\|\mathsf a_n\|\bigl(1+C_1(K_0+1.06\epsilon)Lt_n\bigr),\qquad
 p_{n+1}\le p_n(1+\kappa_n)^2\bigl(1+2.06\,C_1k_0Lt_n\bigr),
\]
since $t_{n+1}=Lt_n$. Iterating from $p_0\le\epsilon$, with $C_1k_0=8/1000$ and $L\sum_{m\le q-2}t_m\le1/(L-1)\le1/12$:
\[
 p_{n+1}\le\epsilon\exp\Bigl(2\sum_m\kappa_m+2.06\cdot0.008/12\Bigr)\le\epsilon e^{0.0214}\le1.04\epsilon .
\]
This closes the induction (first exit cannot occur).

(ii) In the gauge $h=h_{n,D}$ of the block $D=B^{n+1}(z)$, ONE (ii) and (iv) give $\mathsf u_n(z)=h(z)^{-1}\mathsf u_{e^{i\omega}}(\tilde{\mathsf a})(z)h(z)$, so $|\mathsf u_n^{\pm1}-1|\le1.01\cdot13.2L\cdot1.01\cdot1.04\epsilon t_n\le14\epsilon t_{n+1}$. (At $n=q-1$ the same holds: $\|\tilde{\mathsf a}\|\le1.06\epsilon/L<r_1$.)

(iii) A level-$n$ site $x$ is a level-$(m+1)$ site for every $m<n$, and $v_n(x)=\mathsf u_0(x)\cdots\mathsf u_{n-1}(x)$. By E1-type telescoping, $|\prod_m(1+Y_m)-1|\le\prod_m(1+|Y_m|)-1$, so $|v_n^{\pm1}-1|\le\exp(14\epsilon\sum_{m<n}t_{m+1})-1\le\exp(14\cdot1.09\,\epsilon t_n)-1\le16\epsilon t_n$, using $\sum_{k\le n}t_k\le t_n/(1-L^{-1})$.

(iv) Induction on $n$. For $n=0$ it is trivial. Assume it at $n\le q-2$ and let $c$ be a level-$(n+1)$ bond inside $B^q(y)$. The configuration $X=e^{i\mathsf a_n}R_n$ satisfies $X^{h}=e^{i\tilde{\mathsf a}}e^{i\omega}=e^{i\omega'}$, $\|\omega'\|\le1.01(\|\tilde{\mathsf a}\|+\|\omega\|)<r_1$ (E4), with $\operatorname{cn}(h)\le1.01$; and $\operatorname{cn}(v_n)\le(1+16\epsilon)^2\le1.01$. By ONE (ii) with $g=v_n$ and by (6.1),
\[
 \mathcal M^{n+1}(e^{i\mathsf a_0}R_0)(c)=\mathcal M(X^{v_n})(c)=v_n(c_-)\mathcal M(X)(c)v_n(c_+)^{-1}
 =v_n(c_-)\mathsf u_n(c_-)e^{i\mathsf a_{n+1}(c)}R_{n+1}(c)\mathsf u_n(c_+)^{-1}v_n(c_+)^{-1},
\]
which is $(e^{i\mathsf a_{n+1}}R_{n+1})^{v_{n+1}}(c)$, since $(Y^{\mathsf u})^{v}=Y^{v\mathsf u}$.

(v) Holomorphy: compositions of the holomorphic maps of ONE (i). Reality, $\mathfrak c$ and real covariance: ONE (i)-(ii) at each step, by induction (for real $g$, $\operatorname{cn}(g)=1$). Locality: Lemma LOC. ∎

**Proposition PT4 (the four-dimensional form of YM3 (II-155-25) and (II-85-19)).** [proved here, from CURV and Proposition REC] Put $c_{\rm gf}:=\min\{k_0/20,\ c_{\rm cv},\ 1/1024\}$ and $C_{\rm gf}:=31$ (depending only on $L$ through $c_{\rm cv}$; fixed before $\kappa$; independent of $M,\bar\kappa$). Let $y$ be a top of level $q\ge1$, $U$ real on $\mathsf P(B^q(y))$, $A',\mathbf A$ complex forms there, $\mathbf U=e^{i\eta A'}U$, $E=e^{i\eta\mathbf A}\mathbf U$, and
\[
 L^{2q}\varpi_{B^q(y)}(U)\le c_{\rm gf},\qquad \epsilon':=\xi_q\sup|A'|<c_{\rm gf},\qquad \varepsilon_y:=\xi_q\sup|\mathbf A|<c_{\rm gf},
\]
$\varpi_{B^q(y)}$ the maximal bare plaquette defect on the pillar. Then:

(P1) $W_{0,n}=\mathcal M^nU$, $R_n=\mathcal M^n\mathbf U$, $E_n=\mathcal M^nE$ ($n\le q-1$) are defined on the level-$n$ bonds inside $B^q(y)$, holomorphic in $(A',\mathbf A)$ for fixed $U$, real at real data, and read only $\mathsf P(B^q(y))$.

(P2) The recursion of REC with $R_0=\mathbf U$, $\mathsf a_0=\eta\mathbf A$ is defined, with $E_n=(e^{i\mathsf a_n}R_n)^{v_n}$, $\|\mathsf a_n\|\le1.04\varepsilon_yt_n$, $|v_n^{\pm1}-1|\le16\varepsilon_yt_n$. Define the **relative node factor** $v^\sharp_q[\mathbf U;\mathbf A](y):=v_q(y)=v_{q-1}(y)\mathsf u_{q-1}(y)$. It satisfies $|v^\sharp_q(y)^{\pm1}-1|\le16\varepsilon_y$ and depends only on the pair $(\mathbf U,\mathbf A)$ on the pillar.

(P3) For $a\in B(y)$ put $T_W(a)=W_{q-1}(\Gamma_{y,a})$ (comb transport; $W_{q-1}=\mathcal M^{q-1}W$) and $S=T_{\mathbf U}(a)$. Then $\operatorname{cn}(S)\le1.01$ and
\[
 T_E(a)=v_{q-1}(y)\,e^{i\zeta(a)}\,S\,v_{q-1}(a)^{-1},\qquad v^\sharp_q(y)=v_{q-1}(y)e^{i\bar\zeta},
 \tag{8.1}
\]
with $\zeta(a)=\zeta^{\rm c}_{R_{q-1}}(\mathsf a_{q-1})(y,a)$, $\bar\zeta=L^{-4}\sum_{x\in B(y)}\zeta_{R_{q-1}}(\mathsf a_{q-1})(y,x)$, $|\zeta(a)|\le2.4\varepsilon_y$, $|\bar\zeta|\le14\varepsilon_y$, $|v_{q-1}(a)^{\pm1}-1|\le2\varepsilon_y$. The same holds for the contour-variable transport $T'_W(a)=W_{q-1}(y,a)$ with $\zeta(a)$ replaced by $\zeta_{R_{q-1}}(\mathsf a_{q-1})(y,a)$, $|\zeta|\le14\varepsilon_y$.

(P4) At a real reference ($A'=0$), $v^\sharp_q[U;\mathbf A](y)$ is SA's node factor $v_q[\cdot]$ (SA L7106) of the increment, and $|v_q^{\pm1}-1|\le16\,\xi_q\sup_{B^q(y)}|\mathbf A|$: this is the bound of ST1's import AX with $K_v=16$.

*Proof.* (P1)-(P2). *First the real reference.* By Corollary RR (with $c=c_{\rm gf}\le c_{\rm cv}$), REC applies to $R_0=U$, $\mathsf a_0=\eta A'$ with real gauges, $\kappa_n=0$, $K_0=13c_{\rm gf}\le k_0$, $\epsilon=\epsilon'$ (as $\|\eta A'\|\le\eta\sup|A'|=\epsilon't_0$). So $\mathbf U$'s averages exist and $R_n=(e^{i\mathsf a'_n}W_{0,n})^{v'_n}$ with $\|\mathsf a'_n\|\le1.04\epsilon't_n$, $|v'^{\pm1}_n-1|\le16\epsilon't_n$. *Then the complex reference.* On each block or double block $D$ inside the pillar take $h_{n,D}=g\,(v'_n)^{-1}$, $g$ the real gauge of Corollary RR. Then $R_n^{h}=(e^{i\mathsf a'_n}W_{0,n})^g=e^{i\operatorname{Ad}g\,\mathsf a'_n}e^{i\omega_0}=e^{i\omega}$ with $\|\omega\|\le1.01(1.04\epsilon'+13c_{\rm gf})t_n\le0.72k_0t_n$ (E4), and $\operatorname{cn}(h)\le(1+16.1\epsilon't_n)^2\le1+33\epsilon't_n=:1+\kappa_n$, $\sum\kappa_n\le36\epsilon'\le1/100$. REC applies to $R_0=\mathbf U$, $\mathsf a_0=\eta\mathbf A$, $\epsilon=\varepsilon_y$ (as $\|\eta\mathbf A\|\le\varepsilon_yt_0$), and gives (P2) and $E_n$'s existence via REC (iv). Holomorphy, reality and locality: REC (v). The node factor is a formula value of $(\mathbf U,E)$ alone, so it depends only on the pair; the gauges $h$ only certify the domains.

(P3) Apply REC (iv) at $n=q-1$ and multiply along the comb: the gauge factors telescope, so $T_E(a)=v_{q-1}(y)(e^{i\mathsf a_{q-1}}R_{q-1})(\Gamma_{y,a})v_{q-1}(a)^{-1}=v_{q-1}(y)e^{i\zeta(a)}Sv_{q-1}(a)^{-1}$ by the definition of $\zeta^{\rm c}$; and $\mathsf u_{q-1}(y)=e^{i\bar\zeta}$ by definition. In the gauge $h=h_{q-1,B^q(y)}$, ONE (ii) and (iv) give $|\zeta(a)|\le1.01\cdot2.2L\cdot1.01\cdot1.04\varepsilon_yt_{q-1}\le2.4\varepsilon_y$ and $|\bar\zeta|\le1.01\cdot12.6L\cdot1.06\varepsilon_y/L\le14\varepsilon_y$; REC (iii) gives $|v_{q-1}^{\pm1}-1|\le16\varepsilon_y/L\le2\varepsilon_y$. For $\operatorname{cn}(S)$: $S=v'_{q-1}(y)(e^{i\mathsf a'_{q-1}}W_{0,q-1})(\Gamma)v'_{q-1}(a)^{-1}$, and $(e^{i\mathsf a'}W_{0,q-1})(\Gamma)=\prod_ke^{i\operatorname{Ad}(P_k)\mathsf a'_k}\,W_{0,q-1}(\Gamma)$ with unitary $P_k$, so $\operatorname{cn}(S)\le(1+33\epsilon')\,e^{2\cdot2(L-1)\cdot1.04\epsilon'/L}\le1.01$. The contour-variable version is identical, with Lemma FM(c) for the telescoping of the gauge factors and ONE (iv) for $\zeta$.

(P4) At $A'=0$, $R_n=W_{0,n}$ and the recursion is SA's (L7101-7106) with $U_0=U$. ∎

---
## Part III. LEV in four dimensions

## 9. The pinned levelling

### 9.0 Data, domain and constants

Units are ST1's: one numerical bare mesh $\eta$; a triple $P=(U,A',\mathbf J)$ with $\mathbf U=e^{i\eta A'}U$; a shift $\mathfrak h=(\mathbf A,\mathbf K)$ acts by $E=e^{i\eta\mathbf A}\mathbf U$ and $\mathbf J\mapsto\mathbf J+\mathbf K$ ("the current already in the shift's units", `st1.md:225`). YM3 works at step $t=k+1$ with $\mathbf U=e^{i\eta_tA'}U$, $\eta_t=\xi/L$ and currents $L^{-3}\mathbf J+\mathbf K$; its factors $L^{-1},L^{-3}$ in (eq:levelling-regular-triple) (YM3 L54663-54665) are this change of units and disappear here.

**The regular triple domain $\mathfrak T(Y;c)$** (four-dimensional form of YM3 L54660-54674). $P\in\mathfrak T(Y;c)$ when:

- (T1) for $b\in\mathfrak e_Y^+$ and contained stencils, $\xi_{y(b)}|A'(b)|<c$, $\xi_{y(b)}^3|\mathbf J(b)|<c$, $\xi_{y(b)}^2|(\nabla^U_\mu A'_\nu)(b_-)|<c$;
- (T2) $L^{2q}\varpi_{B^q(y)}(U)\le c$ for every $y\in\mathsf{Tp}(Y)$ of level $q$;
- (T3) on each cell $\mathsf C(a)$ of order $o\ge1$ there are a real gauge $w$ and a real potential $A^{\rm g}$ with $U^w=e^{i\eta A^{\rm g}}$ on $\mathsf P(\mathsf C(a))$, $\xi_o|A^{\rm g}|\le c$, $\xi_o^2|\nabla A^{\rm g}|\le c$, where $\nabla$ is the covariant difference of the configuration $e^{i\eta A^{\rm g}}$.

ST1 supplies (T1)-(T2) from its absolute ceilings and (T3) by restricting natural-cube witnesses (`st1-draft2.md` L875).

**Admitted shifts and sizes** (YM3 L54676-54708, verbatim in content). An admitted shift is a pair of complex one-forms on $\operatorname{Bd}(Y)$, zero off $\mathfrak e_Y$. Its local size is
\[
 |\mathfrak h|_{\mathbf U,Y}(b)=\max\bigl\{\xi_{y(b)}|\mathbf A(b)|,\ \xi_{y(b)}^2\max_\mu|(\nabla^{\mathbf U}_\mu\mathbf A_\nu)(b_-)|,\ \xi_{y(b)}^3|\mathbf K(b)|\bigr\},
\]
the inner maximum over stencils contained in $\mathfrak e_Y$ (empty maxima zero). $\|\mathfrak h\|_y$ is its maximum over bonds with $y(b)=y$, and $\|\mathfrak h\|^+_y=\max_{y'\in\operatorname{nb}_Y(y)}\|\mathfrak h\|_{y'}$. For $y\in\mathsf{Tp}(Y)$ of level $q$: $\varepsilon_y(\mathbf A)=\xi_q\sup_{\mathsf P(B^q(y))}|\mathbf A|$, $\widehat\varepsilon_y(\mathbf A)=\xi_q\sup_{\operatorname{Rd}_Y(y)}|\mathbf A|$. Then $\mathsf P(B^q(y))\subset\operatorname{Rd}_Y(y)\subset\mathfrak e_Y$ and $\varepsilon_y\le\widehat\varepsilon_y$, $\varepsilon_y\le\|\mathfrak h\|_y$. A top is **levelled** when $\widehat\varepsilon_y(\mathbf A)<\epsilon$.

**Constants** (four-dimensional form of (II-85-3), YM3 L54718-54726). With $c_{\rm gf},C_{\rm gf}$ of Proposition PT4 and $\phi(s)=(1-9s^2)^3$ for $|s|<1/3$, $0$ otherwise:
\[
 b_\phi=54,\qquad c_{\rm m}=64,\qquad c_{\rm rt}=\min(c_{\rm gf},1/20)=c_{\rm gf},\qquad
 \varepsilon_{\rm m}={c_{\rm gf}\over100c_{\rm m}},\qquad C_{\rm m}=200b_\phi^2L^2c_{\rm m},
 \qquad 0<\epsilon\le\varepsilon_{\rm m}.
 \tag{9.0}
\]
$\phi$ is even and $C^2$, $0\le\phi\le1$, $\phi(0)=1$; with $t=9s^2$, $\phi'(s)=-54s(1-t)^2$ and $\phi''(s)=54(1-t)(5t-1)$, so $|\phi'|\le5.2$ and $|\phi''|\le54$ on $[0,1/3]$, and $\phi=\phi'=\phi''=0$ at $|s|=1/3$; so $|\phi'|,|\phi''|\le b_\phi$ (YM3's example, L54715-54717, checked). All constants in (9.0) depend only on $L$ and $c_{\rm cv}$; they are fixed before $\kappa$ and independent of $M$ and $\bar\kappa$. ($c_{\rm m}=64$ replaces YM3's $10C_{\rm gf}^2e^{4C_{\rm gf}}$; only the inequality $|p^{\pm1}-1|\le\frac12c_{\rm m}\varepsilon_y$ of Step 1 is used.)

### 9.1 Theorem LEV

**Theorem LEV (four-dimensional pinned levelling).** [proved here, as an implication from CURV and SA's averaging formula] Let $L\ge13$ be odd, $P\in\mathfrak T(Y;c_{\rm rt})$, and $\mathfrak h=(\mathbf A,\mathbf K)$ an admitted shift. The construction of Sections 9.2-9.6 defines a gauge $u=u^\delta_Y[P;\mathbf A]$ on all bare sites, equal to $\mathbf1$ off $S_Y$ (indeed off the pillars of $\mathsf{Tp}(Y)$), and an admitted shift $\mathfrak h^\delta[P]=(\mathbf A^\delta,\mathbf K^\delta)$, with:

(L1) *Top identity and size.* At a levelled top $y$ of level $q$: $u(y)\,v^\sharp_q[\mathbf U;\mathbf A](y)=\mathbf1$, and $|u(x)^{\pm1}-\mathbf1|\le C_{\rm m}\varepsilon_y(\mathbf A)$ for $x\in B^q(y)$.

(L2) *Stored transports.* At a pinnable levelled top, for every $a\in B(y)$, $T_{(e^{i\eta\mathbf A}\mathbf U)^u}(a)=T_{\mathbf U}(a)$, both for the comb transport $T$ and for the contour-variable transport $T'$ of (P3).

(L3) *The pinned pair.* $\operatorname{cn}(u)\le5/4$, and on positive bonds
\[
 e^{i\eta\mathbf A^\delta(b)}\mathbf U(b)=u(b_-)e^{i\eta\mathbf A(b)}\mathbf U(b)u(b_+)^{-1},\qquad
 \mathbf J(b)+\mathbf K^\delta(b)=\operatorname{Ad}(u(b_-))\bigl(\mathbf J(b)+\mathbf K(b)\bigr),
 \tag{17}
\]
which is ST1's (17). The shift is unchanged at $b$ when $u(b_-)=u(b_+)=\mathbf1$.

(L4) *Local bound.* $|\mathfrak h^\delta[P]|_{\mathbf U,Y}(b)\le C_{\rm m}\|\mathfrak h\|^+_{y(b)}$.

(L5) *Dependence.* The construction is local on the pillars and read sets, commutes with real gauge transformations and with $\mathfrak c$, and is Borel in all its data. For fixed $U$, its values on given pillars are holomorphic in $(A',\mathbf J,\mathbf A,\mathbf K)$ on the open set where their tops are levelled; its value at a bond is holomorphic where every top in $Y$ whose pillar contains an endpoint of the bond is levelled.

(L6) *Profile.* If $\mathsf s\ge0$ on the bare sites of $\Omega_0$ satisfies $\mathsf s(x)\le e^{\delta d_{\mathbf B}(x,x')}\mathsf s(x')$ and $|\mathfrak h|_{\mathbf U,Y}(b)\le\mathsf s(b_-)$, then $\|\mathfrak h\|^+_{y(b)}\le e^{16\delta}\mathsf s(b_-)$ and $\widehat\varepsilon_{y'}(\mathbf A)\le Le^{24\delta}\mathsf s(b_-)$ for $y'\in\operatorname{nb}_Y(y(b))\cap\mathsf{Tp}(Y)$.

(L7) *Restriction.* All bounds persist after restriction to $\operatorname{Bd}(X)$, $X^\uparrow\subset Y$, using only the stencils contained there.

(L8) *Common centres.* The bounds (L3)-(L4) hold for every assignment of centre values $\zeta(a)$ with $|\zeta(a)|<2c_{\rm m}\varepsilon_{y(a)}(\mathbf A)$ at centres over levelled tops and $\zeta(a)=0$ elsewhere, in place of the pins. The values of $u$ at all centres (in particular at all tops and at every site of $B(y)$, $y$ pinnable) depend only on the pair $(\mathbf U,\mathbf A)$, not on the splitting $(U,A')$.

The proof occupies Sections 9.2-9.9. It follows YM3 L54787-55118 step by step; every three-dimensional count is replaced, and the averaging input is Proposition PT4 instead of YM3 (II-155-25).

### 9.2 Step 1: the prescribed values

Fix a levelled $y\in\mathsf{Tp}(Y)$ of level $q$. Its data satisfy Proposition PT4's hypotheses: $L^{2q}\varpi\le c_{\rm rt}=c_{\rm gf}$ by (T2); $\epsilon'=\xi_q\sup_{\mathsf P(B^q(y))}|A'|<c_{\rm rt}$ by (T1), since every pillar bond $b$ has $y(b)=y$; and $\varepsilon_y\le\widehat\varepsilon_y<\epsilon\le\varepsilon_{\rm m}<c_{\rm gf}$. For $a\in B(y)$ define the **pin**
\[
 p(a)=T_{\mathbf U}(a)^{-1}\,v^\sharp_q(y)^{-1}\,T_E(a),\qquad E=e^{i\eta\mathbf A}\mathbf U .
\]
By (8.1), $p(a)=S^{-1}e^{-i\bar\zeta}e^{i\zeta(a)}S\,v_{q-1}(a)^{-1}$. Put $X=e^{-i\bar\zeta}e^{i\zeta(a)}$. By E1, $|X-1|\le e^{16.4\varepsilon_y}-1\le16.5\varepsilon_y$; by E3, $|S^{-1}XS-1|\le\operatorname{cn}(S)|X-1|\le16.7\varepsilon_y$; so
\[
 |p(a)-1|\le|S^{-1}XS-1|\,|v_{q-1}(a)^{-1}|+|v_{q-1}(a)^{-1}-1|\le16.7\varepsilon_y(1+2\varepsilon_y)+2\varepsilon_y\le18.8\varepsilon_y ,
\]
and the same for $p(a)^{-1}=v_{q-1}(a)S^{-1}X^{-1}S$. For the contour-variable transport $T'$, (P3) gives $|\zeta|\le14\varepsilon_y$ and the same computation gives $|p^{\pm1}-1|\le31\varepsilon_y$. In either case
\[
 |p(a)^{\pm1}-1|\le\tfrac12c_{\rm m}\varepsilon_y<\tfrac12c_{\rm m}\varepsilon_{\rm m}=c_{\rm gf}/200<1/200 .
\]
At $a=y$, $T_W(y)=\mathbf1$ (empty comb, and $W(y,y)=\mathbf1$ by definition), so $p(y)=v^\sharp_q(y)^{-1}$. The **pin logarithm** $\zeta^{\rm pin}(a)=i^{-1}\log p(a)^{-1}$ has $|\zeta^{\rm pin}(a)|\le1.006\cdot\frac12c_{\rm m}\varepsilon_y\le c_{\rm m}\varepsilon_y$ (E2). Put this logarithm at every centre over a levelled top and zero at every other centre. The choice of comb or contour variable is fixed once for all by the stored-coordinate convention of ST1 (`st1.md:198`: "equality of its ordered path product", i.e. the comb; SA L9667 defines the axial gauge by combs).

*Pair dependence.* $T_{\mathbf U}$, $T_E$ and $v^\sharp_q$ are formula values of the configurations $\mathbf U$ and $E$ on the pillar (P2), so $p(a)$ depends only on the pair $(\mathbf U,\mathbf A)$. The levelled condition reads only $\mathbf A$. This is the first half of (L8).

### 9.3 Step 2: covariance under the turn, and the stored transports

Let $u$ be any complex gauge on the bare sites of $B^q(y)$ with $\operatorname{cn}(u)\le5/4$ and $u(a)=p(a)$, $u(y)=p(y)$. The averages are covariant under $u$: by induction on $n\le q-1$, $\mathcal M^n(E^u)=(\mathcal M^nE)^{u|}$, $u|$ the restriction to the level-$n$ sites. Indeed $E_n=(e^{i\mathsf a_n}R_n)^{v_n}$ (P2), so $E_n^{hv_n^{-1}}=(e^{i\mathsf a_n}R_n)^h=e^{i\operatorname{Ad}h\,\mathsf a_n}R_n^h=e^{i\omega'}$ with $\|\omega'\|<r_1$, $h=h_{n,D}$ of PT4, and $\operatorname{cn}(hv_n^{-1})\le1.03\le2$ (here $(X^a)^b=X^{ba}$); so ONE (ii) applies to $E_n$ with the gauge $g=u|$ ($\operatorname{cn}\le5/4\le2$). The comb (and the contour variable, FM(c)) is covariant: $T_{E^u}(a)=u(y)T_E(a)u(a)^{-1}$. Hence
\[
 T_{E^u}(a)=p(y)\,T_E(a)\,p(a)^{-1}=v^\sharp_q(y)^{-1}T_E(a)\cdot T_E(a)^{-1}v^\sharp_q(y)T_{\mathbf U}(a)=T_{\mathbf U}(a).
\]
This is the identity of YM3 L54854-54864 ("The choice $h(y)=v_q(y)^{-1}$, $h(a)=p(a)$ makes this equal to $\operatorname{ax}_{\mathbf U}(a)$"), now proved from the four-dimensional formula. It uses only the values of $u$ at $y$ and at the centres $a\in B(y)$. The actual $u$ of Step 4 has these values (Step 4, "values at centres") and $\operatorname{cn}(u)\le5/4$, and $E^u=e^{i\eta\mathbf A^\delta}\mathbf U$ on the pillar by (17) and the proviso of Step 5. This proves (L2), and $u(y)v^\sharp_q(y)=p(y)v^\sharp_q(y)=\mathbf1$ proves the first part of (L1).

### 9.4 Step 3: frames on cells

On a cell $\mathsf C(a)=B^o(a)$, $o\ge1$, consider real endomorphism fields $T(x)\in\operatorname{End}_{\mathbb R}(\mathfrak h)$, mapping the fibre at $a$ to the fibre at $x$, with $T(a)=1$ and
\[
 \xi_o|\nabla^U_\varsigma T|\le1,\qquad \xi_o^2|\nabla^U_{\varsigma'}\nabla^U_\varsigma T|\le1
\]
for all eight signed directions $\varsigma,\varsigma'$ and all stencils contained in the cell, where $(\nabla^U_\varsigma T)(x)=\eta^{-1}[\operatorname{Ad}(U(x,x+\eta\varsigma))T(x+\eta\varsigma)-T(x)]$. Let $T$ be the minimizer of $\sum_{x\in\mathsf C(a)}|T(x)|_{\rm HS}^2$ over this set.

*Nonempty, with a strict feasible point.* Let $w,A^{\rm g}$ be the cell gauge of (T3), $c=c_{\rm rt}\le1/20$, and $T_0(x)=\operatorname{Ad}(w(x)^{-1}w(a))$. With $D_\varsigma(x)=\operatorname{Ad}(e^{i\eta A^{\rm g}_\varsigma(x)})-1$ (for a negative direction, $A^{\rm g}_{-\varsigma}(x)=-A^{\rm g}_\varsigma(x-\eta\varsigma)$, the transported link being $e^{-i\eta A^{\rm g}_\varsigma(x-\eta\varsigma)}$), direct substitution of $U(x,x+\eta\varsigma)=w(x)^{-1}e^{i\eta A^{\rm g}_\varsigma(x)}w(x+\eta\varsigma)$ gives
\[
 (\nabla^U_\varsigma T_0)(x)=\eta^{-1}\operatorname{Ad}(w(x)^{-1})D_\varsigma(x)\operatorname{Ad}(w(a)),\quad
 (\nabla^U_{\varsigma'}\nabla^U_\varsigma T_0)(x)=\eta^{-2}\operatorname{Ad}(w(x)^{-1})\bigl[(1+D_{\varsigma'}(x))D_\varsigma(x+\eta\varsigma')-D_\varsigma(x)\bigr]\operatorname{Ad}(w(a)).
\]
$\operatorname{Ad}w$ is orthogonal. By E3, $|D_\varsigma|\le e^{2\eta|A^{\rm g}|}-1\le2.1\eta c/\xi_o$, so $\xi_o|\nabla T_0|\le2.1c\le0.11<1/2$. For the second difference, $|D_\varsigma(x+\eta\varsigma')-D_\varsigma(x)|\le2e^{2c/L}\eta|A^{\rm g}_\varsigma(x+\eta\varsigma')-A^{\rm g}_\varsigma(x)|$ (E3), and $|A^{\rm g}(x+\eta\varsigma')-A^{\rm g}(x)|\le\eta|\nabla A^{\rm g}|+|\operatorname{Ad}(e^{i\eta A^{\rm g}})-1||A^{\rm g}|\le1.11\,\eta c/\xi_o^2$ (for negative directions two such steps, $2.22\,\eta c/\xi_o^2$); together with $|D_{\varsigma'}||D_\varsigma|\le(2.1\eta c/\xi_o)^2$ this gives $\xi_o^2|\nabla\nabla T_0|\le2.01\cdot2.22c+4.5c^2\le0.24<1/2$.

*Existence, uniqueness, bounds.* The feasible set is finite-dimensional, closed and convex; the objective is strictly convex and coercive. So the minimizer exists and is unique. Along a coordinate path from $a$ to $x$ inside the cell, with at most $4(L^o-1)/2=2(L^o-1)$ steps, each step changes $|T|$ by at most $\eta/\xi_o=L^{-o}$ (orthogonality of $\operatorname{Ad}U$), so $|T(x)|\le1+2(L^o-1)L^{-o}<3$. Its complex-linear extension $T_{\mathbb C}$ to $\mathfrak g_{\mathbb C}=\mathfrak h\oplus i\mathfrak h$ satisfies $|T_{\mathbb C}Z|_{\rm HS}\le|T|\,|Z|_{\rm HS}$ (the two parts are Hilbert-Schmidt orthogonal), hence, in the operator norm of $2\times2$ matrices, $|T_{\mathbb C}|\le\sqrt2|T|<5$, and its first and second differences are at most $\sqrt2\xi_o^{-1}\le2\xi_o^{-1}$ and $2\xi_o^{-2}$. (In three dimensions YM3 L54894-54898 has $|T|\le5/2$ and the same final bounds $5$, $2\xi_o^{-1}$, $2\xi_o^{-2}$.)

*Continuity in $U$.* Let $U_k\to U$ and $T_k$ the minimizers. For $\theta\in(0,1)$, $(1-\theta)T+\theta T_0$ satisfies every constraint for $U$ strictly (the constraints are convex, $T$ is feasible and $T_0$ strictly feasible, and $T(a)=T_0(a)=1$). The constraint functions are continuous in $U$, so this field is feasible for $U_k$ when $k$ is large. So $\limsup_k\min_k\le\|(1-\theta)T+\theta T_0\|^2$ for every $\theta$, hence $\le\|T\|^2$. The $T_k$ are bounded ($|T_k|<3$); a subsequential limit is feasible for $U$ (closed constraints) with objective at most the minimum, so it equals $T$ by uniqueness. Hence $T_k\to T$.

*Covariance.* A real gauge $g$ acts on feasible fields by $T(x)\mapsto\operatorname{Ad}(g(x))T(x)\operatorname{Ad}(g(a))^{-1}$, preserving the constraints and the objective; by uniqueness the minimizer is covariant. The definition commutes with lattice translations of the cell.

### 9.5 Step 4: bumps and turns

For a cell of order $o\ge1$ set $b_a(x)=\prod_{\mu=1}^4\phi((x_\mu-a_\mu)/\xi_o)$ and $\mu(x)=b_a(x)T_{\mathbb C}(x)\zeta(a)$ for $x\in\mathsf C(a)$; on a singleton cell set $\mu(a)=\zeta(a)$; set $\mu=0$ off the pillars of $\mathsf{Tp}(Y)$; and put $u=e^{-i\mu}$. Here $\zeta(a)$ is the centre value: the pin logarithm of Step 1, or (for (L8)) any value in the polydisc
\[
 |\zeta(a)|<2c_{\rm m}\varepsilon_{y(a)}\ \text{at centres over levelled tops with }\varepsilon_{y(a)}>0,\qquad\zeta(a)=0\ \text{elsewhere}.
 \tag{9.1}
\]
*Values at centres.* $T(a)=1$ and $b_a(a)=1$, so $\mu(a)=\zeta(a)$ and, for the pins, $u(a)=e^{-\log p(a)^{-1}}=p(a)$. In particular $u(y)=p(y)$ at every levelled top (the top is the centre of its own cell, $y\in B(y)$). A top, or a site of $B(y)$ for a pinnable $y$, is a centre. So the identities of Step 2 do not depend on the frames.

*Turn differences.* Let $z=|\zeta(a)|$. Then, at every site and for every contained stencil,
\[
 |\mu|\le5z,\qquad |\eta\nabla^U_\varsigma\mu|\le7b_\phi L^{-o}z,\qquad |\eta^2\nabla^U_{\varsigma'}\nabla^U_\varsigma\mu|\le11b_\phi^2L^{-2o}z .
 \tag{9.2}
\]
*Proof.* $|b_a|\le1$ and $|T_{\mathbb C}|<5$ give the first. For the second, $\eta\nabla_\varsigma\mu(x)=[b_a(x+\eta\varsigma)-b_a(x)]\operatorname{Ad}(U_\varsigma)T_{\mathbb C}(x+\eta\varsigma)\zeta+b_a(x)\,\eta(\nabla_\varsigma T_{\mathbb C})(x)\zeta$; one factor of $b_a$ changes, by at most $b_\phi\eta/\xi_o$ (mean value theorem), so the bound is $(5b_\phi+2)L^{-o}z\le7b_\phi L^{-o}z$. For the third, let $\tau_0,\tau_1,\tau_2,\tau_{12}$ be the values of $T_{\mathbb C}\zeta$ at $x,x+\eta\varsigma,x+\eta\varsigma',x+\eta\varsigma'+\eta\varsigma$, transported to $x$ (in the order of the second covariant difference), and $b_0,b_1,b_2,b_{12}$ the bump values. Then $\eta^2\nabla_{\varsigma'}\nabla_\varsigma\mu(x)=b_{12}\tau_{12}-b_1\tau_1-b_2\tau_2+b_0\tau_0$, and
\[
 b_{12}\tau_{12}-b_1\tau_1-b_2\tau_2+b_0\tau_0=b_{12}(\tau_{12}-\tau_1-\tau_2+\tau_0)+(b_{12}-b_1)(\tau_1-\tau_0)+(b_{12}-b_2)(\tau_2-\tau_0)+(b_{12}-b_1-b_2+b_0)\tau_0 ,
\]
checked by expansion. The four terms are at most $2$, $2b_\phi$, $2b_\phi$ and $5b_\phi^2$ times $L^{-2o}z$: $|\tau_{12}-\tau_1-\tau_2+\tau_0|=\eta^2|\nabla\nabla T_{\mathbb C}\zeta|\le2L^{-2o}z$; $|b_{12}-b_1|\le b_\phi L^{-o}$, $|\tau_1-\tau_0|\le2L^{-o}z$; and $|b_{12}-b_1-b_2+b_0|\le b_\phi^2L^{-2o}$ (for $\varsigma'\ne\pm\varsigma$ it is a product of two one-factor differences; for $\varsigma'=\varsigma$ a second difference of $\phi$, at most $b_\phi L^{-2o}$; for $\varsigma'=-\varsigma$, $b_{12}=b_0$ and it is minus a second difference). The sum is at most $(2+4b_\phi+5b_\phi^2)L^{-2o}z\le11b_\phi^2L^{-2o}z$. ∎

*Extension by zero.* A nonzero bump value lies in the inner third, whose two-step neighbourhood lies in the cell (Lemma G4(c), $L^o\ge L\ge13$). So every stencil containing a site where $\mu\ne0$ in a positive-order cell lies in that cell, and (9.2) holds for all stencils. At a singleton, pinnability makes its two-step neighbourhood consist of level-zero and level-one sites; this is used in Step 6.

*Size of the turns.* On (9.1), $z<2c_{\rm m}\varepsilon_{\rm m}=c_{\rm gf}/50\le1/51200$. So $|\mu|\le5z<10^{-4}$, $|u^{\pm1}-1|\le|\mu|e^{|\mu|}\le5.01z$, and $\operatorname{cn}(u)\le e^{2|\mu|}\le5/4$. For the actual pins $z\le c_{\rm m}\varepsilon_y$, so $|u(x)^{\pm1}-1|\le5.01c_{\rm m}\varepsilon_y\le C_{\rm m}\varepsilon_y$ on $B^q(y)$ (cells partition the pillar and $\mu$ on $B^q(y)$ comes from its own cells only). This completes (L1) and the first part of (L3).

*Where $u\ne\mathbf1$.* If $u$ is nontrivial at an endpoint of a bond $b$, then $b$ lies in $\mathsf P(B^q(y))\subset\operatorname{Rd}_Y(y)$ for a levelled top $y$ with a positive-order cell, or in $\operatorname{Rd}_Y(y')$ for a levelled pinnable level-one top $y'$ (Lemma G4(e)). In both cases $\eta|\mathbf A(b)|<\epsilon/L\le\epsilon$ (levelled: $\xi_q|\mathbf A(b)|<\epsilon$ with $\xi_q\ge L\eta$).

*Remark (why smooth turns; `shift-map.md` (67b)).* A pointwise small complex gauge of size $\epsilon$ that varies at the bare scale produces potentials of size $\epsilon/\eta$, hence local sizes $\xi_y\epsilon/\eta$ (`shift-map.md` L1556-1576). On cells of positive order the bump varies on the scale $\xi_o$, which is what (9.2) records: covariant first and second differences are smaller by $L^{-o}$ and $L^{-2o}$. On singletons the turn does vary at the bare scale; there the read scale is $\xi_{y(b)}\le\xi_1=L\eta$ by pinnability, so the loss $\xi_{y}/\eta$ is at most $L$. This is the factor $L$ in the bounds $(3+15Lc_{\rm m})$, $42L^2c_{\rm m}$ of Step 6 and in $\widehat\varepsilon$ of (L6). Pointwise bounds on $u,u^{-1}$ alone would not suffice (`st1.md:229`).

### 9.6 Step 5: the pinned shift

On positive bonds define
\[
 \mathbf A^\delta(b)={1\over i\eta}\log\bigl(u(b_-)e^{i\eta\mathbf A(b)}\mathbf U(b)u(b_+)^{-1}\mathbf U(b)^{-1}\bigr),\qquad
 \mathbf K^\delta(b)=\operatorname{Ad}(u(b_-))(\mathbf J+\mathbf K)(b)-\mathbf J(b),
\]
and $\mathbf A^\delta(b)=\mathbf A(b)$ when $u(b_-)=u(b_+)=\mathbf1$. Extend both forms oddly to reversed bonds. The proviso is essential: on an untouched bond the original shift need not be small (YM3 L54964-54967). On a touched bond the argument of the logarithm is $e^{-i\mu(b_-)}e^{i\eta\mathbf A(b)}e^{i\operatorname{Ad}(\mathbf U(b))\mu(b_+)}$, within $e^{10^{-4}+\epsilon+1.01\cdot10^{-4}}-1<1/100$ of $\mathbf1$, so the series logarithm is defined, and $e^{\log X}=X$ gives (17). Where both turns are $\mathbf1$ but the bond lies in a read set of a levelled top (so $\eta|\mathbf A(b)|<\epsilon<\log2$), the logarithmic formula gives $\mathbf A(b)$ by E2; so the two definitions agree on every bond where the logarithmic formula is used in an estimate below. *Admissibility:* by Lemma G4(e), bonds outside $\mathfrak e_Y$ are untouched, so $\mathfrak h^\delta$ vanishes off $\mathfrak e_Y$. This completes (L3).

### 9.7 Step 6: the local bound (L4)

*The $\mathbf U$-transported turn differences.* (9.2) uses $\nabla^U$; Lemma LD will use $\mathbf U$-transports. Put $E_\mu=\operatorname{Ad}(e^{i\eta A'_\mu(x)})$ and let $\widehat E_\nu$ be the $\nu$-analogue at $x+\eta e_\mu$ transported to $x$ with $U_\mu(x)$, i.e. $\widehat E_\nu=\operatorname{Ad}(e^{i\eta\operatorname{Ad}(U_\mu(x))A'_\nu(x+\eta e_\mu)})$. On a stencil in a level-$q$ pillar, (T1) gives $\eta|A'|<L^{-q}c_{\rm rt}$ and $\eta^2|\nabla^UA'|<L^{-2q}c_{\rm rt}$, so by E3
\[
 |E_\mu|\le1.008,\qquad |E_\mu-1|\le\tfrac18L^{-q},\qquad |\widehat E_\nu-E_\nu|\le\tfrac18L^{-2q}.
\]
Let $\theta_0=\mu(x)$, $\theta_1=\operatorname{Ad}(\mathbf U_\mu(x))\mu(x+\eta e_\mu)$, $\theta_2=\operatorname{Ad}(\mathbf U_\nu(x))\mu(x+\eta e_\nu)$, $\theta_{12}=\operatorname{Ad}(\mathbf U_\mu(x)\mathbf U_\nu(x+\eta e_\mu))\mu(x+\eta e_\mu+\eta e_\nu)$, and hats for the $U$-transported values. Then $\theta_1=E_\mu\widehat\theta_1$, $\theta_2=E_\nu\widehat\theta_2$, $\theta_{12}=E_\mu\widehat E_\nu\widehat\theta_{12}$, and
\[
 \theta_{12}-\theta_1-\theta_2+\theta_0=E_\mu\widehat E_\nu\widehat s+E_\mu(\widehat E_\nu-1)\widehat d_1+(E_\mu\widehat E_\nu-E_\nu)\widehat d_2+[(E_\mu-1)(\widehat E_\nu-1)+(\widehat E_\nu-E_\nu)]\theta_0
\]
(checked by expansion; YM3 L55050-55055), with $\widehat d_i,\widehat s$ the hatted differences. With (9.2) and $o\le q$:
\[
 d_1,d_2\le1.008\cdot7b_\phi L^{-o}z+\tfrac18L^{-q}5z\le9b_\phi L^{-o}z,\qquad
 s\le(1.017\cdot11+2\cdot0.136\cdot7+0.71)b_\phi^2L^{-2o}z\le15b_\phi^2L^{-2o}z .
\]
Also $|\theta_j|\le1.017\cdot5z\le1/20$.

*The stencil estimate.* Fix a stencil at $b=\langle x,x+\eta e_\nu\rangle$ in direction $\mu$, contained in $\mathfrak e_Y$, with $b'=\langle x+\eta e_\mu,x+\eta e_\mu+\eta e_\nu\rangle$. Put $H=\|\mathfrak h\|_{y(b)}$, $H_+=\|\mathfrak h\|^+_{y(b)}$, $\alpha_0=\eta\mathbf A_\nu(x)$, $\alpha_1=\operatorname{Ad}(\mathbf U_\mu(x))\eta\mathbf A_\nu(x+\eta e_\mu)$. With $X_0,X_1$ as in Lemma LD, $\eta\mathbf A^\delta(b)=i^{-1}\log X_0$ and $\eta^2(\nabla^{\mathbf U}_\mu\mathbf A^\delta_\nu)(x)=i^{-1}(\log X_1-\log X_0)$, because $\operatorname{Ad}(\mathbf U_\mu(x))$ commutes with the logarithm (E2). Three cases (YM3 L55059-55095).

*Case 1: $\mu$ vanishes at the four sites.* The shift is unchanged at $b$ and $b'$ (proviso), and (L4) holds with constant $1$.

*Case 2: a nonzero value lies in a cell of positive order.* Then the whole stencil lies in that cell (Step 4), all four sites lie in the pillar of $y=y(b)$, of level $q$ with $o\le q\le o+1$, and the cell's top is levelled. So $z\le2c_{\rm m}\varepsilon_y\le2c_{\rm m}H$, and $b,b'\in\mathsf P(B^q(y))\subset\operatorname{Rd}_Y(y)$ give $|\alpha_j|\le1.008L^{-q}\epsilon\le1/20$ and $|\alpha_0|\le L^{-q}H$, $|\alpha_1-\alpha_0|=\eta^2|\nabla^{\mathbf U}_\mu\mathbf A_\nu(x)|\le L^{-2q}H$. Lemma LD with $r=\rho=1/20$ and multiplication by $\xi_q/\eta=L^q$, $\xi_q^2/\eta^2=L^{2q}$:
\[
 \xi_q|\mathbf A^\delta(b)|\le3H+27b_\phi L^{q-o}z\le(3+54b_\phi Lc_{\rm m})H,
\]
\[
 \xi_q^2|\nabla^{\mathbf U}_\mu\mathbf A^\delta_\nu(x)|\le3H+L^{2q}\bigl(75b_\phi^2L^{-2o}z+7\cdot81b_\phi^2L^{-2o}z^2+6\rho\cdot9b_\phi L^{-o}z\bigr)\le3H+(150b_\phi^2+1)L^2c_{\rm m}H+b_\phi LH\le160b_\phi^2L^2c_{\rm m}H ,
\]
using $z\le2c_{\rm m}H$ in the linear term, $z\le c_{\rm gf}/50$ in the quadratic term, and $\rho\le1.008L^{-q}H$ (both $b,b'$ have top $y$) with $z\le c_{\rm gf}/50$ in the last: $6\cdot1.008\cdot9b_\phi L^{q-o}z\,H\le b_\phi LH$. Lemma LD is applied with $\rho=\max_j|\alpha_j|\le1/20$.

*Case 3: the nonzero turns lie at singletons.* Every nonzero-turn site $s$ of the stencil is a singleton of a levelled pinnable level-one top $y'$; the four sites are within $\infty$-distance $\eta$ of $s$, so (pinnability) all four have levels at most one, and $y'\in\operatorname{nb}_Y(y(b))$ (its pillar is within $\eta$ of the pillar containing $b_-$). Both $b$ and $b'$ have their endpoints within $\eta$ of $B^1(y')$, so they lie in $\operatorname{Rd}_Y(y')$ and $|\alpha_j|\le1.008\epsilon/L\le1/20$. Here $\mu=\zeta$ at the nonzero sites (no frame), so with $z_\bullet=\max|\zeta|\le2c_{\rm m}H_+$ over these singletons: $|\theta_j|\le1.008z_\bullet$, $d_i\le2.02z_\bullet$, $s\le4.04z_\bullet$. With $\xi_{y(b)}\le L\eta$ and $|\alpha_0|\le(\eta/\xi_{y(b)})H$, $|\alpha_1-\alpha_0|\le(\eta/\xi_{y(b)})^2H$:
\[
 \xi_{y(b)}|\mathbf A^\delta(b)|\le3H+3L\cdot2.02z_\bullet\le(3+15Lc_{\rm m})H_+,\qquad
 \xi_{y(b)}^2|\nabla^{\mathbf U}\mathbf A^\delta(x)|\le3H+L^2(20.2+0.01+0.61)z_\bullet\le42L^2c_{\rm m}H_+ .
\]
*The current.* $\mathbf K^\delta=\operatorname{Ad}(u(b_-))\mathbf K+(\operatorname{Ad}(u(b_-))-1)\mathbf J$, with $|\operatorname{Ad}u|\le\operatorname{cn}(u)\le5/4$ and $|\operatorname{Ad}u-1|\le2|u^{-1}||u-1|\le10.1z$ (E3), $z\le2c_{\rm m}H$ at the cell of $b_-$, and $\xi_{y(b)}^3|\mathbf J(b)|<c_{\rm rt}\le1/20$ (T1): $\xi_{y(b)}^3|\mathbf K^\delta(b)|\le\frac54H+10.1\cdot2c_{\rm m}H/20\le2c_{\rm m}H$.

All bounds are at most $C_{\rm m}H_+=200b_\phi^2L^2c_{\rm m}H_+$. This proves (L4) for the pins, and for every centre assignment in (9.1), since only $z<2c_{\rm m}\varepsilon_{y(a)}$ was used; this is the second half of (L8).

### 9.8 Step 7: dependence (L5)

*Locality and covariance.* The pin at $y$ reads only the averages over its pillar (Lemma LOC, (P1)); the levelled test reads only $\operatorname{Rd}_Y(y)$; the frame reads only the real configuration on its cell. Real gauge covariance: the pins satisfy $p\mapsto g(a)pg(a)^{-1}$ (REC (v), PT4, and covariance of the transports, ONE (ii)); $\zeta^{\rm pin}\mapsto\operatorname{Ad}(g(a))\zeta^{\rm pin}$; the frame is covariant (Step 3); so $\mu\mapsto\operatorname{Ad}(g)\mu$, $u\mapsto gug^{-1}$ pointwise, and $\mathbf A^\delta,\mathbf K^\delta$ transform as $\mathbf A,\mathbf K$. The levelled test is invariant ($|\operatorname{Ad}(g)\mathbf A|=|\mathbf A|$).

*Holomorphy.* For fixed $U$ the frames and bumps are constants. On the open set where a given set of tops is levelled (open: $\widehat\varepsilon_y$ is a maximum of finitely many continuous functions), the pins are holomorphic in $(A',\mathbf A)$ (PT4 (P1)-(P3); the inverse, product and series logarithm are holomorphic); $u=e^{-i\mu}$ is holomorphic; the series logarithm defining $\mathbf A^\delta$ and the polynomial $\mathbf K^\delta$ are holomorphic in $(A',\mathbf J,\mathbf A,\mathbf K)$. Where both turns at a bond equal $\mathbf1$, the logarithmic formula agrees with the inert definition (Step 5), so no branch arises there. The value at a bond depends on the pins of the tops whose pillars contain its endpoints; it is holomorphic where these are levelled.

*Borel.* On each of the finitely many sets defined by "this set of tops is levelled", the construction is jointly continuous in all data (continuity of the frames, Step 3, and of the averages, ONE (i)); these sets are Borel. So the construction is Borel.

*Conjugation.* At real data all factors are unitary and $\mathfrak c$-fixed. Each ingredient commutes with $\mathfrak c$: the averages and node factors (ONE (ii), REC (v)), the pins, the real frames and bumps, the exponential, and the series logarithm ($\log(X^{\mathfrak c})=(\log X)^{\mathfrak c}$ in the convention $e^{iZ}$, by E2). Hence $u(\overline P,\overline{\mathfrak h})=u(P,\mathfrak h)^{\mathfrak c}$ and the shift transforms accordingly. (YM3 L55098-55102 argues by holomorphic reflection; here the equivariance is checked ingredient by ingredient, which needs no identity theorem.)

### 9.9 Step 8: profile (L6), restriction (L7), common centres (L8)

*Profile.* Let $y'\in\operatorname{nb}_Y(y(b))$ and $b'$ a bond with $y(b')=y'$. By Lemma G4(a),(d), $d_{\mathbf B}(b_-,b'_-)\le16$ (if $y'=y(b)$, less than $4$). So $|\mathfrak h|(b')\le\mathsf s(b'_-)\le e^{16\delta}\mathsf s(b_-)$, which is the first bound. For the second, let $b''\in\operatorname{Rd}_Y(y')$. If $y'$ has level $q'\ge2$, then $y'=y(b)$ (the other neighbours have level one), $b''\in\mathsf P(B^{q'}(y'))$, $y(b'')=y'$ and $\xi_{q'}|\mathbf A(b'')|\le|\mathfrak h|(b'')\le\mathsf s(b''_-)\le e^{4\delta}\mathsf s(b_-)$. If $y'$ is pinnable of level one, $b''_-$ is within $2\eta$ of $B^1(y')$, so it lies in a level-zero or level-one pillar, $\xi_1\le L\xi_{y(b'')}$, and $d_{\mathbf B}(b''_-,b_-)\le24$ (G4(d)); so $\xi_1|\mathbf A(b'')|\le L|\mathfrak h|(b'')\le Le^{24\delta}\mathsf s(b_-)$. Taking the supremum gives $\widehat\varepsilon_{y'}\le Le^{24\delta}\mathsf s(b_-)$. (YM3 L55104-55117 has $3+6+3=12$ and $C_{\rm m}\ge18$ in three dimensions; the four-dimensional lengths are $4+8+4=16$ and $24$, and $C_{\rm m}\ge24$.)

*Restriction.* Restricting to $\operatorname{Bd}(X)$, $X^\uparrow\subset Y$, keeps a subset of the stencils, of the bonds and of the read sets used above; every bound is a maximum over these, so it persists.

*Common centres and ties.* The bounds of Steps 4-6 used only (9.1). For two input triples with one pair $(\mathbf U,\mathbf J)$ and one real shift, the pins coincide (Step 1, pair dependence) and the turns at all centres coincide (Step 4, values at centres). At real data the turns are unitary, so $w=\widetilde uu^{-1}$ is a real gauge equal to $\mathbf1$ at every centre, hence at every top and at every site of $B(y)$, $y$ pinnable. This is the property used for complex ties at YM3 L56636-56650 ("Turns agree there for inputs with one pair"); for ST1's stored slots it is used with Lemma ST (`st1-draft2.md` L820-830), under the reading that the initial site of a stored slot of level $l$ is a level-$l$ lattice site, so that a stored site over a pinnable top $y$ of level $l+1$ is a point of $B(y)$, i.e. a centre (SA L6160-6173 records the slot's bond, initial site and formation level). This completes (L8) and the proof of Theorem LEV. ∎

### 9.10 What is four-dimensional in the proof

| YM3 (3D) | here (4D) | where |
|---|---|---|
| (II-155-25), (II-85-19) imported from YM3's averaging theory | Proposition PT4, proved from SA's formula, Lemmas FM, CG, ONE, REC, and the import CURV | Sections 6-8 |
| folding to a double block | not needed (Lemma LOC) | 6.1 |
| block means $L^{-3}\sum$, families of $3!$ paths | $L^{-4}\sum$, families of $4!$ paths, combs of $\le2(L-1)$ bonds | 6.1, 7 |
| $|T|\le5/2$ (path $3(L^o-1)/2$) | $|T|<3$ (path $2(L^o-1)$); $|T_{\mathbb C}|<5$ unchanged | 9.4 |
| bump $\prod_{\mu=1}^3\phi$ | $\prod_{\mu=1}^4\phi$; (9.2) unchanged | 9.5 |
| weighted lengths $3,6,12$, $C_{\rm m}\ge18$ | $4,8,16$ and $24$, $C_{\rm m}\ge24$ | 9.9 |
| $c_{\rm m}=10C_{\rm gf}^2e^{4C_{\rm gf}}$ | $c_{\rm m}=64$ with $C_{\rm gf}=31$ | 9.0, 9.2 |
| units $\eta_t=\xi/L$, $L^{-3}\mathbf J$ | ST1's single units | 9.0 |
| Lemma LD for $r\le1/8$, $\rho\le1/12$ | proved for $r,\rho\le1/20$ (all uses are far inside) | 4 |

## 10. The ST1 interface

**Corollary LEV-ST1.** [proved here, from Theorem LEV] Take $D_{\rm LEV}=\mathfrak T(Y;c_{\rm rt})$ and $\epsilon_{\rm lev}=\epsilon$. Let $h_Y$ be a regional shift satisfying ST1's (S), $\mathfrak n(h_Y)(b)\le C_{\rm S}e^{-\mu d(b,\mathcal S_v)}$ with $C_{\rm S}=C_{\rm src}E_{\bar\kappa}C_{\mathcal A}\delta_{\rm src}$ and $d(b,\mathcal S_v)=d_{\mathbf B}(b_-,\mathcal S_v)$, where $\mathfrak n$ is the numerator of ST1's (10). Put
\[
 C_{\rm tr}=1+2.1Lc_{\rm rt}\ (\le2),\qquad C_{\rm lev}=C_{\rm tr}^2C_{\rm m}e^{18\mu},\qquad K_{\rm pin}=C_{\rm tr}Le^{11\mu}.
\]
Then for every complex $\lambda$:

(a) the pillar-size functional of the unpinned shift obeys $\widehat\varepsilon_y(\lambda\mathbf A_Y)\le K_{\rm pin}|\lambda|C_{\rm S}E_X$ for every endpoint pillar $y$ of $X$;

(b) whenever every endpoint pillar of $X$ is levelled for $\lambda h_Y$, $\|\rho_X(\lambda h_Y)^\delta\|_w\le C_{\rm lev}|\lambda|C_{\rm S}Q_X$;

(c) (17) holds, $u=\mathbf1$ off the endpoints of $\operatorname{Bd}(Y)$, $u(y)v^\sharp_q(y)=\mathbf1$ at levelled tops, and the stored transports are preserved at pinnable levelled tops;

(d) on the disc $|\lambda|<(2a_X)^{-1}$ of ST1's (12), every endpoint pillar is levelled, and $\lambda\mapsto\rho_X(\lambda h_Y)^\delta$ is holomorphic there for fixed real data.

These are the hypotheses on LEV in ST1's Definition 5 (`st1.md:165-170`) and in hypotheses 3-5 of `st1-draft2.md` (L875-879), with "the full profile loss" in $C_{\rm lev}$. $C_{\rm tr},C_{\rm lev},K_{\rm pin}$ depend only on $L,c_{\rm cv},\mu$; they are fixed before $\kappa$ and independent of $M$ and $\bar\kappa$ ($\mu$ is DR's rate, fixed in step 2 of ST1's order).

*Proof.* *Conversion between the two sizes.* ST1's numerator uses $l(b)=\xi_{y(b)}$ (by (G0)) and $\nabla^U$; LEV's uses $\nabla^{\mathbf U}$. Their difference at a stencil is $\eta^{-1}(\operatorname{Ad}(e^{i\eta A'_\mu(x)})-1)\operatorname{Ad}(U_\mu(x))H_\nu(x+\eta e_\mu)$, of norm at most $2.1|A'_\mu(x)||H(b')|$ (E3). Since $\xi_{y(b)}|A'_\mu(x)|<c_{\rm rt}$ (T1) and $\xi_{y(b)}\le L\xi_{y(b')}$ (adjacent sites differ by at most one layer, by separation), $\xi_{y(b)}^2|\nabla^{\mathbf U}H-\nabla^UH|\le2.1Lc_{\rm rt}\,\xi_{y(b')}|H(b')|$. Hence $|\mathfrak h|_{\mathbf U,Y}(b)\le C_{\rm tr}\max\{\mathfrak n(b),\mathfrak n(b')\}$ and $\mathfrak n(h^\delta)(b)\le C_{\rm tr}\max\{|\mathfrak h^\delta|_{\mathbf U}(b),|\mathfrak h^\delta|_{\mathbf U}(b')\}$, with $d_{\mathbf B}(b_-,b'_-)\le1$.

*The profile.* For $\lambda h_Y$, put $\mathsf s(x)=C_{\rm tr}e^{\mu}|\lambda|C_{\rm S}e^{-\mu d_{\mathbf B}(x,\mathcal S_v)}$. The triangle inequality gives $\mathsf s(x)\le e^{\mu d_{\mathbf B}(x,x')}\mathsf s(x')$, and the conversion gives $|\lambda\mathfrak h_Y|_{\mathbf U,Y}(b)\le\mathsf s(b_-)$. So (L6) applies with $\delta=\mu$.

(b) By (L4) and (L6), $|(\lambda\mathfrak h_Y)^\delta|_{\mathbf U}(b)\le C_{\rm m}e^{16\mu}\mathsf s(b_-)$, and by the conversion $\mathfrak n((\lambda h_Y)^\delta)(b)\le C_{\rm tr}C_{\rm m}e^{17\mu}\mathsf s(b_-)=C_{\rm lev}|\lambda|C_{\rm S}e^{-\mu d(b,\mathcal S_v)}$. Divide by $w(b)$ and take the maximum over the bonds read by $X$; $e^{-\mu d}\le e^{-\mu d/2}$ gives $Q_X$. Restriction: (L7).

(a) For an endpoint pillar $y$ and $b''\in\operatorname{Rd}_Y(y)$: $\xi_q|\lambda\mathbf A(b'')|\le L\,|\lambda\mathfrak h_Y|_{\mathbf U}(b'')\le L\mathsf s(b''_-)$ (the factor $L$ only for pinnable level-one $y$), and $d_{\mathbf B}(b''_-,y)\le8+2=10$ (Lemma G4(a),(b)). So $\widehat\varepsilon_y\le Le^{10\mu}\mathsf s(y)=C_{\rm tr}Le^{11\mu}|\lambda|C_{\rm S}e^{-\mu d(y,\mathcal S_v)}\le K_{\rm pin}|\lambda|C_{\rm S}E_X$.

(c) (L1)-(L3).

(d) By (12), $|\lambda|<(2a_X)^{-1}$ gives $K_{\rm pin}|\lambda|C_{\rm S}E_X<\epsilon_{\rm lev}/2$, so by (a) every endpoint pillar is levelled; then (L5) gives holomorphy. ∎

---
## Part IV. CORE in four dimensions

## 11. The core, the pointwise estimate, and the towers

### 11.1 The core

Work at a core address $(\sigma'',i,X)$, $X\subset\Lambda_i\subset\Omega_i$, $i\ge1$, in level-$i$ units: bare mesh $\eta=\eta_i=L^{-i}\le1/13$. Following SA (R4)-(R6) (SA L5672-5716) and `st1.md:110`, a triple $P=(U,A',\mathbf J)$ on $X$ lies in the **core** $\mathcal U^\circ_i(X;b_0,b_1)$ when:

- (C1) $|\partial U-I|,|\partial\mathbf U-I|<b_0\eta^2$ at every plaquette of $X$; $|A'|,|\nabla^UA'|<b_1$; $|\mathbf J|<b_0$;
- (C2) on every cubical box in $X$ of side at most $C_{\rm box}LM$ there is a real gauge with $U=e^{i\eta A}$, $|A|,|\nabla A|<C_{\rm pot}Mb_0$;
- (C3) for every subdomain $Z\subset X$ of level $p\le i$, both erosion rules, and $1\le n\le p$: the tower $U_n(Z;P)$ of (R5) exists in its open continuation domain, and on $Z^{\wr p}$ (two layers of level-$(p-1)$ $M$-cubes removed, SA L5707-5708)
\[
 |\partial U_n(Z;P)-I|<b_0\lambda_p\eta_p^2,\qquad |J(U_n(Z;P))|<b_0\lambda_pL^{2(n-p)}\quad(\text{level-}n\text{ units}),\qquad \lambda_p=L^{-(i-p)},
\]
and the same with $\mathbf U$ replaced by $U$.

The **outer substitution** of a shift $(H,K)$ on the active bonds of $X$ is SA (R8), ST1's (8): $P\dotplus(H,K)=(U,A'',\mathbf J+K)$, $A''=(i\eta)^{-1}\log(e^{i\eta H}e^{i\eta A'})$ on the active bonds, unchanged elsewhere (so we may set $H=0$ off the active bonds).

*Geometric reading (GEO-core).* The subdomains $Z$ of (C3) at level $p$ are localization regions of level $p-1$ (unions of level-$(p-1)$ $M$-cubes of the aligned partitions, ST1 step 8: "$M_1\mid M$ (aligned partitions)"), and $Z^{\wr p}$ is as in ST1's Definition 1. This is how SA L5698-5708 and `st1.md:110` read; I record it because Lemma TWR uses it.

### 11.2 The pointwise estimate

**Lemma PW (YM3 (II-16-52), YM3 L42333-42412, rebuilt).** [proved here] Let $\eta\le1/13$; $U$ real; $\mathbf U=e^{i\eta A'}U$ with $|A'|,|\nabla_UA'|<\beta_1$ and $|\partial\mathbf U-I|<\beta_0\eta^2$; and $f$ a complex form with $|f|,|\nabla_{\mathbf U}f|<s$ at every bond and contained stencil, where $\beta_0,\beta_1,s\le1/60$. Put $A^f=(i\eta)^{-1}\log(e^{i\eta f}e^{i\eta A'})$. Then all logarithms are defined ($\eta(s+\beta_1)\le1/390$), and
\[
 |A^f-A'|<\tfrac{11}{10}s,\qquad |\nabla_U(A^f-A')|<\tfrac{11}{10}s,\qquad |\partial(e^{i\eta f}\mathbf U)-\partial\mathbf U|<\tfrac94s\eta^2 .
 \tag{PW}
\]
*Proof.* Put $\epsilon_*=1/380$, $q_*=(1+\epsilon_*)/(1-\epsilon_*)=381/379<51/50$.

*Potential.* $P=e^{i\eta f}e^{i\eta A'}$ and $Q=e^{i\eta A'}$ lie within $e^{1/390}-1<\epsilon_*$ of $\mathbf1$ (E1). $|P-Q|\le(e^{\eta s}-1)e^{\eta\beta_1}\le\eta s(1+\epsilon_*)$. The logarithm is $(1-\epsilon_*)^{-1}$-Lipschitz on the $\epsilon_*$-ball and $\log Q=i\eta A'$ (E2). So $|A^f-A'|\le q_*s<\frac{11}{10}s$.

*Derivative.* At a stencil $(x;\mu,\nu)$ let $u=U_\mu(x)$ (real) and
\[
 a_1=i\eta f_\nu(x),\ a_2=i\eta\operatorname{Ad}(u)f_\nu(x+\eta e_\mu),\ c_1=i\eta A'_\nu(x),\ c_2=i\eta\operatorname{Ad}(u)A'_\nu(x+\eta e_\mu),
\]
$E_j=e^{a_j}e^{c_j}$, $H_j=e^{c_j}$, $D_j=E_j-H_j$. Since $\operatorname{Ad}(u)$ commutes with the logarithm, $\Delta:=(\log E_2-\log H_2)-(\log E_1-\log H_1)=i\eta^2\nabla_U(A^f-A')_\nu(x)$. Bounds on the inputs: $|c_2-c_1|=\eta^2|\nabla_UA'|<\eta^2\beta_1$. Since $\nabla_{\mathbf U}$ uses $\operatorname{Ad}(e^{i\eta A'_\mu(x)}u)$, $\operatorname{Ad}(u)f(x+\eta e_\mu)-f(x)=\eta\nabla_{\mathbf U}f-(\operatorname{Ad}(e^{i\eta A'_\mu(x)})-1)\operatorname{Ad}(u)f(x+\eta e_\mu)$, so by E3 $|a_2-a_1|<\eta^2s(1+\omega_*)$, $\omega_*=2\beta_1(1+\epsilon_*)<1/29$. *Telescoping inequality:* with $X_j=E_j-1$, $Y_j=H_j-1$ (norms at most $\epsilon_*$), $\log E_j-\log H_j=\sum_n(-1)^{n+1}(X_j^n-Y_j^n)/n$ and $X^n-Y^n=\sum_{k=0}^{n-1}X^k(X-Y)Y^{n-1-k}$. Differencing $j=2$ and $j=1$ term by term leaves either the increment $D_2-D_1$ (multiplicity $n$, weight $\epsilon_*^{n-1}$) or one increment of $X$ or $Y$ times $D_1$ (multiplicity $n(n-1)/2$ each, weight $\epsilon_*^{n-2}$); summing,
\[
 |\Delta|\le{|D_2-D_1|\over1-\epsilon_*}+{(|E_2-E_1|+|H_2-H_1|)|D_1|\over2(1-\epsilon_*)^2}.
\]
By E1, $D_2-D_1=(e^{a_2}-e^{a_1})e^{c_2}+(e^{a_1}-1)(e^{c_2}-e^{c_1})$, so $|D_2-D_1|\le(1+\epsilon_*)(|a_2-a_1|+\eta s|c_2-c_1|)$; $|D_1|\le(1+\epsilon_*)\eta s$; $|E_2-E_1|\le(1+\epsilon_*)(|a_2-a_1|+|c_2-c_1|)$; $|H_2-H_1|\le(1+\epsilon_*)|c_2-c_1|$. Hence
\[
 |\Delta|\le q_*(|a_2-a_1|+\eta s|c_2-c_1|)+\tfrac12q_*^2\eta s(|a_2-a_1|+2|c_2-c_1|)
 <\eta^2s\bigl\{q_*(1+\omega_*)+q_*\eta\beta_1+\tfrac12q_*^2\eta[s(1+\omega_*)+2\beta_1]\bigr\}<1.05\,\eta^2s ,
\]
the three terms being at most $1.0389$, $0.0013$, $0.0020$. So $|\nabla_U(A^f-A')|<\frac{11}{10}s$.

*Plaquette.* For the plaquette $(x;\mu,\nu)$ write $\mathbf U_1=\mathbf U_\mu(x)$, $\mathbf U_2=\mathbf U_\nu(x+\eta e_\mu)$, $\mathbf U_3=\mathbf U_\mu(x+\eta e_\nu)$, $\mathbf U_4=\mathbf U_\nu(x)$, $\partial\mathbf U=\mathbf U_1\mathbf U_2\mathbf U_3^{-1}\mathbf U_4^{-1}$, and $f_1,\dots,f_4$ correspondingly. Moving the exponentials to the left,
\[
 \partial(e^{i\eta f}\mathbf U)=e^{i\eta g_1}e^{i\eta g_2}e^{i\eta g_3}e^{i\eta g_4}\,\partial\mathbf U,\quad
 g_1=f_1,\ g_2=\operatorname{Ad}(\mathbf U_1)f_2,\ g_3=-\operatorname{Ad}(\partial\mathbf U\,\mathbf U_4)f_3,\ g_4=-\operatorname{Ad}(\partial\mathbf U)f_4,
\]
using $\mathbf U_1\mathbf U_2\mathbf U_3^{-1}=\partial\mathbf U\,\mathbf U_4$. Their sum is
\[
 \textstyle\sum_kg_k=\eta(D_{\mathbf U}f)(x;\mu,\nu)+(1-\operatorname{Ad}(\partial\mathbf U))\bigl(\operatorname{Ad}(\mathbf U_4)f_3+f_4\bigr),\qquad D_{\mathbf U}f=\nabla_{\mathbf U,\mu}f_\nu-\nabla_{\mathbf U,\nu}f_\mu ,
\]
since $\operatorname{Ad}(\mathbf U_1)f_2-f_4=\eta\nabla_{\mathbf U,\mu}f_\nu(x)$ and $\operatorname{Ad}(\mathbf U_4)f_3-f_1=\eta\nabla_{\mathbf U,\nu}f_\mu(x)$. Here $|D_{\mathbf U}f|<2s$, $|1-\operatorname{Ad}(\partial\mathbf U)|\le2.01\beta_0\eta^2$ (E3), $|\operatorname{Ad}\mathbf U_4|\le e^{2\eta\beta_1}\le1.003$; so $|\sum g_k|\le\eta s(2+4.1\beta_0\eta)$. Each $|g_k|\le\varkappa s$ with $\varkappa\le e^{6\eta\beta_1}(1+3\beta_0\eta^2)\le1.01$. The expansion of $\prod_ke^{X_k}-1-\sum_kX_k$ has only terms of degree at least two, majorized by $e^{\sum|X_k|}-1-\sum|X_k|\le\frac12(\sum|X_k|)^2e^{\sum|X_k|}$; with $X_k=i\eta g_k$ this is at most $8.1\eta^2\varkappa^2s^2$. Therefore
\[
 |\partial(e^{i\eta f}\mathbf U)-\partial\mathbf U|\le|\partial\mathbf U|\bigl(\eta|\textstyle\sum g_k|+8.1\eta^2\varkappa^2s^2\bigr)\le(1+\beta_0\eta^2)\eta^2s(2+4.1\beta_0\eta+8.3s)<2.15\,\eta^2s .\qquad∎
\]
The proof is dimension-free: it reads one bond, one stencil, one plaquette. (YM3 uses its product expansion (I-10-121), YM3 L41985, for the plaquette step; the direct expansion above replaces it.)

### 11.3 The core's towers are Theorem T's towers

**Lemma TWR.** [proved here, from Theorem T (i),(iii), SA Theorem 3, Lemma TRU and GEO-core] At a core address as in 11.1, let $Z\subset X$ be a subdomain of level $p\le i$, $\mathfrak r$ an erosion rule and $1\le n\le p$. Let $U$ be real and $A'$ complex on $Z$ with
\[
 L^{2p}|\partial U-I|<a_T,\qquad \max\{\lambda_p|A'|,\lambda_p^2|\nabla_UA'|\}<a_T ,
 \tag{11.1}
\]
which is Theorem T's domain $\mathcal Q^{\rm T}(a_T)$ for the ambient sequence truncated at level $p$, whose scale on $Z$ is $l=\eta L^p=\lambda_p$ (as $Z\subset\Omega_i\subset\Omega_p$). Then:

(a) The (R5) tower $U_n(Z;P)$ is defined and equals the localized tower $U_{n,Z}(U,A')$ of Corollary T′, applied with Corollary T′'s $(i,p,X)$ equal to $(p,n,Z)$, as holomorphic functions of $A'$ for fixed $U$.

(b) At every inner plaquette or full bond $e$ of $Z^{\wr p}$, Corollary T′'s normalized quantity is
\[
 G_{n,Z}(U,A';e)=L^{2p}\bigl(\partial U_n(Z;P)(e)-I\bigr)\ \ \text{or}\ \ L^{2(p-n)}J(U_n(Z;P))(e)\ (\text{level-}n\text{ units}),
\]
so the bounds of (C3) for $(Z,p,n)$ read $|G_{n,Z}|<b_0\lambda_p$.

*Proof.* (a) *The sequences agree.* Corollary T′ localizes by $\Omega'_q=\Omega^\flat_q\cap Z_{[q]}$, $q\le n$. Since $Z\subset X\subset\Lambda_i\subset\Omega_i\subset\Omega_q$, this is $Z_{[q]}$, the erosion tower of $Z$ that (R5) uses; the determining set $\mathbf B'$ is a function of the sequence (ST1 Definition 1), so both constructions read the same datum $D(A')=M_{\mathbf B'}(e^{i\eta A'}U)$. *Both are defined and holomorphic on the convex set $\mathcal C=\{A':(11.1)\}$.* Theorem T (i) gives this for $U_{n,Z}$. For (R5): by AV-row, $D(A')=e^{i\beta}M_{\mathbf B'}(U)$ with $\|\beta\|\le C_QLa_T\le\delta_B/4<r_B$ (Theorem T's ceiling $\bar a\le\delta_B/(4C_QL)$, `st1-draft2.md` L507), so $B=i^{-1}\log(D(A')M_{\mathbf B'}(U)^{-1})=\beta$ lies in SA Theorem 3's ball and $\Phi_{M_{\mathbf B'}(U)}(B)$ is defined and holomorphic. *They agree at real $A'$.* For real $A'$, SA Theorem 3 (SA L9696: "exactly one holomorphic map $\Phi$ ... that agrees with $U^\circ(e^{iB}\mathbf V_0)$ for real $B$") gives $U_n(Z;P)=U^\circ(D(A'))$, and Theorem T (iii) gives that $U_{n,Z}$ at real $A'$ is "the real axial representative of its averaged datum", $U^\circ(D(A'))$. The real points of $\mathcal C$ form a nonempty open subset of the real form. Lemma TRU on the connected set $\mathcal C$ gives equality. The currents of equal configurations are equal.

(b) Corollary T′ defines $G$ with $n_i(x)=\min\{\lambda^\flat(x),i\}$, here $\min\{\lambda^\flat(x),p\}=p$ on $Z$ since $\lambda^\flat\ge i\ge p$ there; the plaquette member is $L^{2p}(\partial U_{n,Z}-I)$ and the current member is $L^{2p+\min\{n,p\}-3n}J=L^{2(p-n)}J$ with $J$ in level-$n$ units (`st1-draft2.md` L563-566; YM3 L55882-55889). Every element of $Z^{\wr p}$ has its base within $2\xi_n$ of $Z^{\wr n}$, because $Z^{\wr p}\subset Z^{\wr n}$ for aligned partitions ($n\le p$; GEO-core). Then (C3) in level-$i$ units reads $L^{2p}|\partial U_n-I|<b_0\lambda_pL^{2p}\eta_p^2=b_0\lambda_p$ and $L^{2(p-n)}|J|<b_0\lambda_p$. ∎

## 12. The outer-core substitution

**Theorem CORE.** [proved here, as an implication from Theorem T and Corollary T′ of `st1-draft2.md`, with Lemmas PW and TWR] Let $i\ge1$, $L\ge13$, and put
\[
 C_{\rm os}=18,\qquad K^\sharp=\max\{1,e^{4\delta_T}K_T\},\qquad a^\sharp=\min\{1/60,a_T\},
\]
with $K_T,\delta_T,a_T$ of Theorem T. Let $0<\tau<1$, $c_\natural\ge1$, $0<b_0\le b_1$, $2(b_0+b_1)\le a^\sharp$, and $b_2=\tau b_0/(C_{\rm os}K^\sharp(1+c_\natural))$. If $P=(U,A',\mathbf J)\in\mathcal U^\circ_i(X;(1-\tau)b_0,(1-\tau)b_1)$ (with any current) and the shift satisfies ST1's (16),
\[
 |H|,|\nabla^{\mathbf U}H|<b_2,\qquad |\mathbf J+K|<b_0 ,
\]
then $P\dotplus(H,K)\in\mathcal U^\circ_i(X;b_0,b_1)$. The substitution is locally holomorphic, and its pair is $(e^{i\eta H}\mathbf U,\mathbf J+K)$. The hypothesis $b_1^2\le c_\natural b_0$ of ST1's statement is not needed.

*Proof (Route B).* Write $P''=P\dotplus(H,K)=(U,A'',\mathbf J+K)$.

*Simple clauses (C1).* Apply Lemma PW with $\beta_\iota=(1-\tau)b_\iota\le1/120$, $f=H$ and $s=b_2\le\tau b_0/36\le1/60$. The real curvature is unchanged. The complex curvature: $|\partial(e^{i\eta H}\mathbf U)-I|<((1-\tau)b_0+\frac94b_2)\eta^2\le b_0\eta^2$, since $\frac94b_2\le\tau b_0/16$. The potential: $|A''|<(1-\tau)b_1+\frac{11}{10}b_2<b_1$ and $|\nabla_UA''|\le|\nabla_UA'|+|\nabla_U(A''-A')|<(1-\tau)b_1+\frac{11}{10}b_2<b_1$, since $\frac{11}{10}b_2<\tau b_0\le\tau b_1$. The current: $|\mathbf J+K|<b_0$ by hypothesis.

*Gauge clause (C2).* It concerns $U$ alone, which is unchanged; the bound $C_{\rm pot}M(1-\tau)b_0$ implies $C_{\rm pot}Mb_0$.

*Tower clauses (C3).* For $U$: unchanged, and the input bounds at $(1-\tau)b_0$ imply those at $b_0$. For $\mathbf U''=e^{i\eta A''}U$: fix $(Z,p,n,\mathfrak r)$. Both $A'$ and $A''$ satisfy (11.1): $L^{2p}|\partial U-I|<(1-\tau)b_0L^{-2(i-p)}<a_T$, and $\lambda_p|A'|,\lambda_p^2|\nabla_UA'|<b_1<a_T$, the same for $A''$ by the simple clauses. By Lemma TWR the towers exist on their open branches (Theorem T (i)) and the (C3) quantities are $G_{n,Z}$. Corollary T′, with the site-to-top factor $e^{4\delta_T}$ (Lemma G4(a): two endpoints, each at weighted distance less than $2$ from its top), gives at every element of $Z^{\wr p}$
\[
 |G_{n,Z}(U,A'';e)-G_{n,Z}(U,A';e)|\le e^{4\delta_T}K_T\max_b\max\{\lambda_p|A''-A'|(b),\lambda_p^2|\nabla_U(A''-A')|(b)\}
 \le e^{4\delta_T}K_T\lambda_p\tfrac{11}{10}b_2\le\tfrac{11}{10}\cdot\tfrac{\tau}{18(1+c_\natural)}\lambda_pb_0<\tfrac{\tau}{2}\lambda_pb_0 ,
\]
by Lemma PW ($\lambda_p\le1$). The input core gives $|G_{n,Z}(U,A';e)|<(1-\tau)\lambda_pb_0$. Hence $|G_{n,Z}(U,A'';e)|<(1-\tau/2)\lambda_pb_0<\lambda_pb_0$, which is (C3) at radius $b_0$ by Lemma TWR (b).

*Holomorphy and the pair.* The series logarithm is holomorphic in $(A',H)$ on its ball, and $e^{i\eta A''}=e^{i\eta H}e^{i\eta A'}$ by E2, so $e^{i\eta A''}U=e^{i\eta H}\mathbf U$. Restriction to the active bonds commutes with (R8) (`st1.md:410-413`). ∎

*Why no $\alpha_1^2$.* YM3 bounds the tower quantity on a whole disc of substituted triples by $K^\sharp_{\rm tw}(\gamma_0+\gamma_1^2)$ and applies Schwarz (YM3 L42437-42447). A bound linear in $\gamma_1$ would not do there, because $b_1$ may be of order $b_0^{1/2}$. Corollary T′ is a Lipschitz bound in the first-order norm of the *difference* $A''-A'$, which is of size $b_2\propto\tau b_0$; so the size of $b_1$ never enters, beyond $b_1<a_T$.

**Route A (alternative; YM3's argument, conditional on (ER7)).** [proved here, as an implication from (ER7)] *(ER7) in the form needed.* There are $a_7>0$ and $K_7\ge1$ such that, if $P$ satisfies (C1)'s curvature and potential bounds at radii $(\alpha_0,\alpha_1)$ with $\alpha_0+\alpha_1\le a_7$, then for every $(Z,p,n,\mathfrak r)$ the towers exist, are holomorphic in $A'$ for fixed $U$ on the open set of such triples, and on $Z^{\wr p}$ satisfy $|\partial U_n-I|\le K_7(\alpha_0+\alpha_1^2)\lambda_p\eta_p^2$, $|J(U_n)|\le K_7(\alpha_0+\alpha_1^2)\lambda_pL^{2(n-p)}$. (SA L6571-6582 assumes it; YM3 I-93-98(f), L42171-42204, proves it in three dimensions; `c1-repr.md` §8, L148-211, proposes a four-dimensional proof, with the factor $L^{-2(j-p)}\le\lambda_p$ at subdomains, L211, "not yet checked by the other model", L220.) With $K^\sharp=K_7$, $a^\sharp=\min\{1/60,a_7\}$, $C_{\rm os}=18$ and $b_1^2\le c_\natural b_0$: put $\beta_\iota=(1-\tau)b_\iota$, $\gamma_\iota=2b_\iota$, $s=\frac49(1+\tau)b_0$, $R=s/b_2=8(1+\tau)K^\sharp(1+c_\natural)/\tau>2$. For $|z|<R$, Lemma PW with $f=zH$ gives triples with simple radii $(\beta_0+\frac94s,\beta_1+\frac{11}{10}s)=(2b_0,\le2b_1)$, and $\gamma_0+\gamma_1\le a^\sharp$. Each normalized tower quantity $F(z)$ is holomorphic on $|z|<R$, bounded by $\lambda_pK^\sharp(\gamma_0+\gamma_1^2)\le4\lambda_pK^\sharp(1+c_\natural)b_0$, with $|F(0)|<(1-\tau)\lambda_pb_0$. Lemma E5(i) for $F-F(0)$ gives $|F(1)-F(0)|\le8\lambda_pK^\sharp(1+c_\natural)b_0\,b_2/s=\lambda_p\tau b_0/(1+\tau)<\lambda_p\tau b_0$. The simple clauses at $z=1$ are those of Route B. This is YM3 L42412-42452 with the four-dimensional (ER7); the arithmetic $C_{\rm os}=18$ is dimension-free. ∎

*Which route ST1 should use.* Route B: it adds no import (Theorem T and Corollary T′ are already ST1's own, used for its tower reads (L3)), it does not need $b_1^2\le c_\natural b_0$, and its constant $K^\sharp$ is Theorem T's. Route A needs (ER7), listed as open at `ym4-assembly.md` L282 (⟦open: NL-ER7⟧).

---
## Part V. Constants, status, and what the referee should check

## 13. Constants in order of choice

IN1 requires the constants of the stage, background and response bounds to be fixed before $\kappa$ and independent of $M$ and $\bar\kappa$, with $M$ entering only through lower bounds (`in1-draft.md:807-808`; its Theorems A.5-A.7 build the order on this). Every constant below meets this requirement. None depends on $M$, $\bar\kappa$, the depth, the volume, or the shapes of regions.

| Constant | Value or definition | Depends on | Where fixed in ST1's order (`st1-draft2.md` §4) |
|---|---|---|---|
| $c_1$, $r_1$ | $5\cdot10^{-5}$, $c_1/L$ | absolute, $L$ | step 1 ($L$) |
| $C_1$, $k_0$ | $8/c_1^2$, $c_1^2/1000$ | absolute | step 1 |
| FM constants | spread $1/500$, radius $1/100$, $C_{\rm FM}=6$ | absolute | step 1 |
| $c_{\rm cv}$ | CURV's threshold | $L$ (import AV) | step 2 |
| $c_{\rm gf}$ | $\min\{k_0/20,c_{\rm cv},1/1024\}$ | $L$ | step 2 |
| $C_{\rm gf}$ | $31$ | absolute | step 2 |
| $b_\phi$, $c_{\rm m}$ | $54$, $64$ | absolute | step 2 |
| $c_{rt}$ | $c_{\rm gf}$ | $L$ | step 2 (LEV) |
| $\varepsilon_{\rm m}$, $\epsilon_{\rm lev}=\epsilon$ | $c_{\rm gf}/(100c_{\rm m})$, any $\epsilon\le\varepsilon_{\rm m}$ | $L$ | step 2 (LEV) |
| $C_{\rm m}$ | $200b_\phi^2L^2c_{\rm m}$ | $L$ | step 2 |
| $K_v$ (AX, by-product) | $16$ | absolute | step 2 |
| $C_{\rm tr}$ | $1+2.1Lc_{rt}\le2$ | $L$ | step 2 |
| $C_{\rm lev}$ | $C_{\rm tr}^2C_{\rm m}e^{18\mu}$ | $L$, $\mu$ (DR) | step 2 (after DR's $\mu$) |
| $K_{\rm pin}$ | $C_{\rm tr}Le^{11\mu}$ | $L$, $\mu$ | step 2 |
| $C_{\rm os}$ | $18$ | absolute | step 2 |
| $K^\sharp$ (Route B) | $\max\{1,e^{4\delta_T}K_T\}$ | Theorem T's constants: $L,\rho_0$, AV, AX, TH4, PROF, BG | step 4 (with Theorem T) |
| $a^\sharp$ (Route B) | $\min\{1/60,a_T\}$ | as $a_T$ | step 4 |
| $c_\natural$ | any $\ge1$ (unused in Route B) | — | step 2 |
| $K^\sharp$, $a^\sharp$ (Route A) | $K_7$, $\min\{1/60,a_7\}$ of (ER7) | (ER7)'s inputs | step 2 |

ST1 lists $C_{\rm os},K^\sharp,c_\natural$ in step 2 (`st1-draft2.md` L237). With Route B, $K^\sharp$ and $a^\sharp$ are known only after Theorem T's constants (step 4). They enter only $K_{\rm core}$ and $r_*$ (step 6) and the ceilings $2(b_0+b_1)\le a^\sharp$ of step 10, all chosen later, so the order is unchanged: move $C_{\rm os},K^\sharp$ from step 2 to step 4. The rate $\mu$ is DR's, fixed in step 2; $C_{\rm lev},K_{\rm pin}$ come after it in the same step. The factor $E_{\bar\kappa}$ of (S) enters $C_{\rm S}$ in Corollary LEV-ST1, not $C_{\rm lev}$ or $K_{\rm pin}$; as in `st1-draft2.md` §4 it is absorbed by the ceilings on $A_1/A_0$ and $\gamma$, chosen after $\bar\kappa$.

## 14. Status

| Item | Status here |
|---|---|
| Lemmas E1-E6, LD, TRU | [proved here] |
| Lemma G4 (four-dimensional pillar and cell geometry) | [proved here], under (G0) |
| Lemma LOC (pillar locality; no folding) | [proved here], from SA's formula |
| Lemma FM (Federbush mean: existence, uniqueness, holomorphy, covariance, first order, Lipschitz) | [proved here] |
| Lemma CG (comb gauge) | [proved here] |
| CURV | **import**, [C] in `a1-balaban.md` §3.5 (L325-366); the content of ST1's AV-conv (SA L9667) |
| Corollary RR | [proved here], from CURV and CG |
| Lemma ONE (one straightened step) | [proved here], from SA's formula (SA L7065-7097) |
| Proposition REC (pillar recursion) | [proved here], from ONE |
| Proposition PT4 (four-dimensional (II-155-25), (II-85-19); AX's node-factor bound with $K_v=16$) | [proved here], from CURV and REC |
| **Theorem LEV** (four-dimensional II-85-34) | **[proved here]**, as an implication from CURV, under (G0) and the stored-site reading of 9.9 |
| **Corollary LEV-ST1** ($C_{\rm lev}$, $K_{\rm pin}$, (17), top identity, stored transports, holomorphy on the $\lambda$-disc) | **[proved here]**, from Theorem LEV and ST1's (S) |
| Lemma PW (pointwise substitution estimate) | [proved here] |
| Lemma TWR (core towers are Theorem T's towers; normalisations agree) | [proved here], from Theorem T (i),(iii), SA Theorem 3, TRU, GEO-core |
| **Theorem CORE**, Route B | **[proved here]**, as an implication from ST1's Theorem T and Corollary T′ (with $e^{4\delta_T}$) |
| Theorem CORE, Route A | [proved here], as an implication from (ER7) |

**No statement internal to LEV or CORE is Outstanding.** Both targets end at complete proofs of implications, so no stopped lemma and no attacks are recorded.

**What remains open upstream, on these two paths** (none of it is new, and none is promoted here):

1. LEV rests on **CURV** (status [C], `a1-balaban.md` §3.5). It is the real curvature averaging estimate, part of ST1's import AV.
2. CORE (Route B) rests on **Theorem T and Corollary T′** of `st1-draft2.md` §7.8, which are implications there from AV, AX, TH4, PROF, BG. Of these, TH4 rests on P81, P82° and M1 (`a3-derivative.md` §§6-7, 12), and P82° is "the first point of failure" (`st1-draft2.md` L932, open item 1). So the first open statement under CORE is P82°, as for every other use of Theorem T in ST1.
3. CORE (Route A) rests on **(ER7)** (⟦open: NL-ER7⟧, `ym4-assembly.md` L282; Codex's proposed proof `c1-repr.md` §8 is unchecked).

**Consequences for ST1's import list** (`st1-draft2.md` L928-941). Item 3 (LEV) and item 4 (CORE) can be removed as separate imports: LEV is proved from CURV (inside AV), and CORE from Theorem T (inside ST1). AX's node-factor bound is proved at real references (PT4 (P4)); AX's remaining content (the axial definition and the Landau top condition, SA L9667, L9702) is unchanged. Two corrections to ST1: Lemma TG(iv)'s $3/2$ should read "less than $2$" for coordinate paths (Lemma G4(a)), so Corollary T′'s $e^{3\delta_T}$ becomes $e^{4\delta_T}$; and $C_{\rm os},K^\sharp$ move from step 2 to step 4 of ST1's order.

**Points for the referee to check first** (where this draft is most likely to be wrong):

1. *Lemma ONE (v)*: that $D_{\mathsf a}\mathcal Q^1(\mathbf1,0)=Q^{\rm s}$ exactly (the derivation from SA's formula in the proof), and that the operator norm of $Q^{\rm s}$ is $L$. The uniformity of REC in the depth rests on this exact first-order constant; a constant $CL$ with $C>1$ would make $p_n$ grow like $C^n$.
2. *Lemma TWR (a)*: that SA's (R5) tower and Theorem T's tower are the same function of $A'$ — the argument uses only that both are holomorphic on a convex set and agree at real $A'$ with the real axial representative (SA L9696, Theorem T (iii)).
3. *GEO-core*: that the core's subdomains are localization regions of level $p-1$ for aligned partitions, so that $Z^{\wr p}\subset Z^{\wr n}$ and Corollary T′ covers every element read by (C3).
4. *(G0)* and the stored-site reading of 9.9 (initial sites of level-$l$ stored slots are level-$l$ lattice sites, hence centres $a\in B(y)$).
5. *Step 2 of LEV*: the covariance $\mathcal M^n(E^u)=(\mathcal M^nE)^{u|}$ for the complex turn $u$; it uses only formula-level covariance (ONE (ii)) and $\operatorname{cn}(u)\le5/4$, never the closeness of $E^u$ to $U$ link by link (which fails at singletons, `shift-map.md` (67b)).
6. *Corollary LEV-ST1*: the conversion $C_{\rm tr}$ between $\nabla^U$ and $\nabla^{\mathbf U}$ and the use of $\xi_{y(b)}\le L\xi_{y(b')}$ for adjacent sites.

No computer-assisted step is used. Every argument is a finite inequality, a power-series identity, a contraction on a finite-dimensional ball, Cauchy's estimate, the identity theorem, or strict convexity on a finite-dimensional set; each is Lean-formalizable.

---

## Result

**LEV is proved in four dimensions**, as an implication (Theorem LEV and Corollary LEV-ST1). The proof follows YM3's Proposition II-85-34 (YM3 L54729-55118) step by step, with every three-dimensional count replaced. Its averaging input, which YM3 imports as (II-155-25), is proved here from SA's four-dimensional averaging formula (SA L7065-7106): the Federbush mean, the comb gauge, one straightened step with the exact first-order constant $L$, and the pillar recursion. The only imported estimate is CURV, the real curvature averaging recursion of `a1-balaban.md` §3.5 (inside ST1's AV). No folding is needed in four dimensions. The construction gives ST1 everything its Definition 5 and Proposition 7 ask of LEV: (17), $u=\mathbf1$ off the endpoints of $\operatorname{Bd}(Y)$, the top identity $u(y)v^\sharp_q(y)=\mathbf1$, preservation of stored transports at pinnable levelled tops, the constants $C_{\rm lev}=C_{\rm tr}^2C_{\rm m}e^{18\mu}$ and $K_{\rm pin}=C_{\rm tr}Le^{11\mu}$, holomorphy where the relevant tops are levelled, and the common-centre clause for ties. A by-product: AX's node-factor bound, $K_v=16$.

**CORE is proved in four dimensions**, as an implication (Theorem CORE), with ST1's (16) and $C_{\rm os}=18$, $K^\sharp=e^{4\delta_T}K_T$. Route B uses ST1's own Corollary T′ (a Lipschitz tower estimate whose normalisation is exactly the core's), so CORE adds no import to ST1 and does not need $b_1^2\le c_\natural b_0$. Route A is YM3's Schwarz argument and needs (ER7).

**First remaining Outstanding statement:** none internal to LEV or CORE. Upstream, LEV rests on CURV ([C]); CORE (Route B) rests on Theorem T, whose first open input is P82° (through TH4).

This is research text. It grants no status, and no other model has checked it.
