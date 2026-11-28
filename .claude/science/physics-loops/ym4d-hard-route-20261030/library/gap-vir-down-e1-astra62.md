# Repo search

Research at `5aab5b0d56b1`, row 1631. The target-specific prior file is absent. I searched `origin/main` (8b11ae2bb95e), `pr/10114` (f76f6c649cff), `pr/10133` (89faef229ff6), `pr/10134` (1e70c7211a2c) and `pr/10141` (c73ad7b177d9). VIR-down, visible virial or thermal energy, delay closure, adverse hidden trace, magnetic-placement spin tails, banded plaquette spin shifts and boundary-link boosts gave no target hits. The pinned checkout outside the lane also returned none.

**ON FILE (external hits).** Searches including one-step loop correlation, observed slopes, electric-spin score, marked resolvents and toron Hamiltonians found pointers in main's `research/mass-gap/library/{gap-fp-astra,gap-limit-astra,gap-sh-astra,gap-transfer-check}.md`. Their source on PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` (7), bounds simple-loop convolution below by $(1+v_N/\rho)^{-1}|F\rangle\langle F|$, $\rho=(I_2/I_1)^{|C|}$. Its (11) gives the one-step correlation bound $C_F(a)\ge v_N^2 e^{-4\beta(p_B+|C|)}/(1+v_N/\rho)$ for every $\beta>0$, uniformly in the spatial volume. E1 asks for a signed derivative at periods of order $n$. Main's `research/mass-gap/library/gap-vir-sc.md`, row 710 Theorem U(ii), gives the raw eigenstate derivative used below. [November 8 digest, §11](prior/repo-search-2026-11-08.md)

**ON FILE (closest lane hits).** Row 860 Lemma DS bounds the joint thermal probability of specified electric spins on plaquette-separated edges by the all-zero probability times $\prod_e(k_e+1)^2 r_{k_e/2}(\beta)r_{k_e/2}(5\beta)$. It supplies the staple and separation arguments. Row 875 boosts electric spin counts. Row 1617 (6) controls large electric spins in the score of each eigenstate. Row 1626 (4) truncates a single-delay response in *energy* and its (8) counts Wilson Taylor degree. Row 1618 Proposition 6 uses coldness at half time to truncate a thermal energy sum. [Row 860](gap-hs-max.md) · [Row 875](gap-exc-astra.md) · [Row 1617](gap-vir-down-astra62.md) · [Row 1626](gap-vir-down-dom-astra62.md) · [Row 1618](gap-vir-down-neon.md)

**ON FILE (target).** VIR-DOWN lists E1 open. Row 1628 (17), (19), (23) identifies exact visibility inside each eigenspace and prices hidden adverse slopes. Row 1629 (2.12)–(2.13) bounds the signed mark using within-cell covariance. Check 1630 §3.3 leaves open the lower bound for the observed numerator at a fixed positive rate. [Registry](open-registry.md) · [Row 1628](gap-vir-down-twoside-astra62.md) · [Row 1629](gap-vir-down-twoside-neon.md) · [Check 1630](gap-vir-down-twoside-check-opus.md)

**ON FILE (outline index, row 244).** The chunk and obligation searches for transfer, Peter–Weyl, Clebsch–Gordan bandwidth, staples and spectral gap lead to Sussman and Alpoge's outline with Claude and Codex, revision `31a47c543775`. Lines 2197–2243 give GL3–GL4's Bessel multipliers, 2259–2280 give the spin bandwidth of polynomial multiplication, and 2315–2335 give the positive transfer and its periodic trace. Lines 3717–3720 leave the spectral gap open, and CA-I 2703–2711 excludes it from Theorem 0. [Index, chunk 02](sa-index/chunk-02.md) · [Obligations](sa-index/obligations.md)

## The observed Wilson score

**ON FILE (rows 710, 1617, 1624, 1628 and check 1630).** Write $d=3n^3$ for the number of spatial links. Work in product Haar coordinates on the neutral space. Let $V=\sum_p(1-W_p)$, where $W_p=\tfrac12\operatorname{tr}U_p$ also denotes the corresponding multiplication operator. Let $T=MCM$, with $M=e^{-\beta V/2}$ and $C$ the product of temporal convolutions. Gauge and centre projections can be suppressed on invariant vectors. For any unit eigenvector $\psi$ at $\lambda=r\lambda_0>0$, put $m=-\log r$ and $w=C^{1/2}M\psi/\sqrt{\lambda}$. The electric spin label on a link is $k=2j$. With all Bessel functions evaluated at $\beta$,

$$
 g_\beta(k)=\frac{k}{\beta}+\frac{I_{k+2}}{I_{k+1}}-1,\qquad
 D_\psi=\frac{\langle\psi,T'\psi\rangle}{\lambda}
       =\mathbb E_w\sum_e g_\beta(k_e)-\langle\psi,V\psi\rangle .
$$

Write $\Omega$ for the positive normalized vacuum and $b_\psi=D_\psi-D_\Omega$. Let $F_r$ project onto the eigenspace of $T/\lambda_0$ at $r$ in the centre-neutral, gauge-invariant space. The loop cells bin the three orientations of squares of side $n/32$ on the $n/32$ grid after spatial Wilson flow for $(n/128)^2$, with normalized trace bins of width $1/8$. Row 1628 (17) identifies the visible subspace at $r$ with the span of $F_r(\Omega\mathbf1_C)$ over these cells $C$. Let $J_r$ project onto this span and choose an orthonormal basis there. Put $G(t)=\sum_{0<r<1}r^t\operatorname{rank} F_r$ and $W_t=\sum_{0<r<1}m r^t\operatorname{rank} F_r$. The sum of $r^t b_\psi$ over those excited basis vectors is the E1 numerator $N(t,\beta)$, including at multiple eigenvalues. Set $W_{\rm obs}=\sum_{0<r<1} m r^t\operatorname{rank}J_r\le W_t$. E1 asks for $N\ge(\kappa_0+\epsilon)W_t$ with fixed positive constants. I take $\kappa_0=1/16$, with the depth shift fixed as in check 1630 before $K$. [Eigenstate score](gap-vir-sc.md) · [All-coupling formula](gap-vir-down-astra62.md) · [Loop cells, line 45](gap-vir-down-tool-astra62.md)

## A bound for large spins in the spatial slice

**PROVED.** Let $n$ be even, $n\ge4$, $\beta>0$, and $\Pi_{e,k}$ the Haar spin projection acting on link $e$. Here $\mathbb E_\psi$ is the joint law of these commuting projections in $\psi$, including when $\psi$ is the vacuum. For $t>1$, $0<c<1$, $a=\log(1/c)$, $0<\delta\le1$, take the integer

$$
 q=\left\lceil\max\left\{2,\ 6e^2\beta,
       \frac{8\beta+\log(2dt/(a\delta))}{\log 2}\right\}\right\rceil .
 \tag{1}
$$

Any larger integer also works. Before any coldness assumption, every unit eigenvector satisfies

$$
 \sum_e \Pr_\psi(k_e\ge q)\ \le\ \frac{6m+\delta a/t}{q}.
 \tag{2}
$$

The $m$ on the right is the excitation energy relative to the neutral vacuum. In particular the extensive raw vacuum energy never enters (2).

*Proof.* Use the positive unprojected kernel $T(x,y)$ in temporal gauge. It commutes with simultaneous slice gauge transformations and centre translations. Its top eigenfunction is positive and simple by strict kernel positivity. Each symmetry preserves this normalized eigenfunction, so the full operator norm equals the neutral $\lambda_0$. Fix a set $S$ of spatial links with no common spatial plaquette between any two. With $x$ the left endpoint and all other links fixed, the dependence of $T(x,y)$ on $(x_e:e\in S)$ is a product of factors $\exp[s_e\,\tfrac12\operatorname{tr}(x_e v_e)]$ times a positive factor independent of those links. Indeed one temporal plaquette has coefficient $\beta$ and four spatial plaquettes have coefficient $\beta/2$ at that endpoint. Each normalized trace, including a reversed link, is a real linear functional on the unit quaternion $x_e$ with coefficient of norm one. Their weighted sum has norm $0\le s_e\le3\beta$ and some direction $v_e\in SU(2)$. At $s_e=0$ the factor is constant.

For $k\ge1$ the spin-$k/2$ projection of the single factor, divided in absolute value by the original factor at the same link, is bounded by

$$
 A_k=(k+1)^2 e^{6\beta}\frac{(3\beta/2)^k}{(k+1)!}.
 \tag{3}
$$

In fact GL3 gives the projected factor $(k+1)[2 I_{k+1}(s_e)/s_e]\chi_{k/2}(x_e v_e)$. The character has absolute value at most $k+1$. The constant coefficient $2I_1(s_e)/s_e$ is a Haar mean bounded by $e^{s_e}$, and the factor itself is at least $e^{-s_e}$. The positive Bessel series gives $I_{k+1}(s)/I_1(s)\le (s/2)^k/(k+1)!$ term by term, with the limiting interpretation at zero. This proves (3).

For prescribed labels $k_e\ge1$, let $R=\prod_{e\in S}\Pi_{e,k_e}$. Applying the projections at the left endpoint gives the pointwise inequality $|(RT)(x,y)|\le (\prod A_{k_e})T(x,y)$. Therefore $|\langle\psi,RT\psi\rangle|\le(\prod A_{k_e})\langle|\psi|,T|\psi|\rangle\le\lambda_0\prod A_{k_e}$. The left side equals $\lambda\Pr_\psi(k_e\text{ prescribed},\,e\in S)$. This is where the eigenstate costs one $e^m$ for the entire set.

Give a link of direction $i$ based at $x$ the colour $(i,\sum_{j\ne i}x_j\bmod 2)$. Even $n$ makes the colouring periodic. Parallel edges on the same plaquette have opposite transverse parity. There are six classes, each plaquette-separated. In one class $H$ put $U_H=\sum_{e\in H}k_e{\bf1}_{k_e\ge q}$ and $B_q=\sum_{k\ge q}(e^k-1)A_k$. Expanding the product for $e^{U_H}$, using the joint bound on every nonempty subset and summing the positive terms, gives

$$
 \mathbb E_\psi e^{U_H}\le 1+e^m\{(1+B_q)^{|H|}-1\}
       \le e^m(1+B_q)^{|H|}.
$$

For $k\ge q$, $k!\ge(k/e)^k$ gives $e^k A_k\le e^{6\beta}(k+1)[3e^2\beta/(2k)]^k\le e^{6\beta}2^{-k}$, using $k+1\le2^k$. Thus $dB_q\le 2d e^{6\beta}2^{-q}\le \delta a/t$. Jensen's inequality on each class gives $\mathbb E_\psi U_H\le m+|H|B_q$. Summing over the classes and dividing by $q$ proves (2). The proof also applies to $m=0$.

## Which part of the slope this controls

**PROVED.** In the magnetic Haar space set $Q_p^j=\prod_{e\in\partial p}{\bf1}_{k_e\le j}$ and $W_p^{[q]}=Q_p^q W_p Q_p^q$. Every factor acts on the four-link plaquette Hilbert space and extends by the identity on exterior links. Define the uncut and cut magnetic contributions to the log-multiplier slope by

$$
 B_M(\psi)=\sum_p\big(\langle W_p\rangle_\psi-\langle W_p\rangle_\Omega\big),
 \qquad B_M^{[q]}(\psi)=\sum_p\big(\langle W_p^{[q]}\rangle_\psi-
                                      \langle W_p^{[q]}\rangle_\Omega\big).
$$

The sign is fixed by the minus sign in front of $V$. At every cold point $G(t)\le c$, every excited unit eigenvector satisfies

$$
 |B_M(\psi)-B_M^{[q]}(\psi)|\ \le\ \frac{8(6+2\delta)}{q}\,m .
 \tag{4}
$$

This compresses the *spatial insertion itself*, including its off-diagonal matrix elements. In particular all the spins of an observed eigenstate outside the four marked links may fluctuate freely.

*Proof.* Multiplication by a fundamental matrix element acts on spin $k/2$ through the tensor product with spin $1/2$, giving only labels $k-1,k+1$, with the negative label omitted. The dual fundamental on a reversed link has the same rule. Each edge occurs just once in $W_p$. Consequently $W_p Q_p^{q-1}=Q_p^q W_p Q_p^{q-1}$. The self-adjoint error $W_p-W_p^{[q]}$ vanishes on both sides of $Q_p^{q-1}$, and its norm is at most two because $\|W_p\|\le1$. Thus

$$
 |\langle W_p-W_p^{[q]}\rangle_\psi|
 \le 2\langle I-Q_p^{q-1}\rangle_\psi
 \le 2\sum_{e\in\partial p}\Pr_\psi(k_e\ge q).
$$

This estimate includes transitions from label $q$ to label $q+1$. Dropping those transitions using Cauchy–Schwarz alone would give a square root of the rare-event probability. Summing the bound uses four plaquettes per link. Apply (2) to the eigenstate and the vacuum. Coldness gives $e^{-tm}\le G(t)\le c$, hence $a/t\le m$. These facts give (4).

**ON FILE (row 1617 (5)–(6), checked in 1621).** With $q$ from (1) let $B_E^{[q]}(\psi)$ be the difference of the expectations of $\sum_e g_\beta(\min(k_e,q))$ in $w$ and $w_0=C^{1/2}M\Omega/\sqrt{\lambda_0}$. For the full electric contribution $B_E$, row 1617 (6), including its clamped version following (12), gives
$-\delta m/\beta\le B_E-B_E^{[q]}\le(1+\delta)m/\beta$.
Its cutoff conditions $q\ge e^2\beta$ and $d e^{8\beta}2^{-q}\le\delta a/t$ follow from (1). Subtracting the constant $g_\beta(q)$ from the clamped operator makes it supported on $k<q$ without changing the vacuum-subtracted score. This earlier estimate uses $w$, while (4) is in $\psi$. The two placements are linked by the eigenvalue equation. [Row 1617](gap-vir-down-astra62.md) · [Check 1621](gap-vir-down-astra62-check-opus.md)

**PROVED (uniform error for E1).** Denote by $N_q$ the same observed sum as $N$, replacing $b_\psi$ by $B_E^{[q]}(\psi)+B_M^{[q]}(\psi)$. Put $h_q=8(6+2\delta)/q$. For every cold point,

$$
 -(\delta/\beta+h_q)W_{\rm obs}
 \ \le\ N-N_q\ \le\
 ((1+\delta)/\beta+h_q)W_{\rm obs}.                                      \tag{5}
$$

Indeed (4) and the electric estimate hold for *every* unit vector of a fixed eigenspace. Sum them in an orthonormal basis of its visible subspace with the positive weights $r^t$. The vacuum-subtracted scores are quadratic forms there, since the map from $\psi$ to $w$ is a linear isometry on that eigenspace. The cut scores are bounded at each fixed box. Absolute convergence follows from $G(t)<\infty$, $W_t<\infty$ and the error per state. This proof freezes the true Wilson eigenvectors and true visibility projectors, even at crossings or for arbitrarily small nonzero overlaps.

**PROVED (quantifiers on the long window).** Fix $b,g_0,L_h$, the depth $s$ of check 1630, and $\ell=L_h b^s$, all before $K$. In (1) take $\delta=1$ and fix the cold threshold $0<c<1$, for example $c=1/2$ for the aspect-512 consumer. By check 1453 and row 1618 Theorem 3, $\beta\asymp\log n$ uniformly on $[\beta_K,\beta_{K+s}]$, that interval has bounded width, and $t=(n/512)e^{(\beta-\beta_K)/16}$ is between two fixed positive multiples of $n$. Thus $q=O(\log n)$ uniformly there, and $q\ge6e^2\beta$. For every $\eta>0$ there is $K_\eta$ such that for all $K\ge K_\eta$ and **every** cold point of that characteristic,

$$
 |N-N_q|\le\eta W_{\rm obs}\le\eta W_t.                                   \tag{6}
$$

At the calibrated points $\beta_{K+s-i}$, the fixed lattice has physical side $L_h b^i$ for $0\le i\le s$. Equation (6) also covers the intervening cold points in the weak part, the band and the infrared stretch. Only coldness at the stated period enters. In particular the entire discarded contribution is smaller in magnitude than $W_t/16$ at every sufficiently late cold point. At any late cold point with $N_q\le0$, taking $\eta<1/16$ would rule out E1 there. Existence of such points on the prescribed Wilson trajectory is open. Conversely, (6) identifies which terms must carry a positive slope if E1 holds. A strict surplus with a fixed margin for $N_q$ is equivalent up to a vanishing rate error to a strict surplus for $N$. The new estimate is the bound on the error. The transport still needs HOT and a characteristic consistent with the running budget of check 1630 §1.3(d).

## A check using Taylor degree on overlapping plaquettes

**PROVED (second derivation of the spatial error at logarithmic cutoff).** The following estimate works for every subset of links, including the whole boundary of a plaquette. It gives (2)–(6) for a possibly larger $q$ of the same order, without using the single-link Bessel estimate (3) or the six-colour factorization.

Let $R_e={\bf1}_{k_e\ge q}$, $R_S=\prod_{e\in S}R_e$. Conditional on the other left-end links and on $y$, keep only those factors in the kernel whose left variables meet $S$, writing them as $\exp(\sum_f\alpha_f W_f)$. The exterior factor is positive. Here $W_f$ is a normalized plaquette trace, or a normalized temporal link-pair trace, with $|W_f|\le1$. Counting incident factors with multiplicity gives $\sum_f\alpha_f\le3\beta|S|$. In the absolutely convergent Taylor expansion, the monomial with powers $h_f$ has degree at most $\sum_{f\ni e}h_f$ at $e$. A product of $j$ fundamental or dual entries has only spin labels $k\le j$, by the tensor product rule. A monomial can survive $R_S$ only when $q|S|\le4\sum_f h_f$. The factor four allows a single plaquette to meet all four selected edges.

The integral kernel of the one-link projection onto label $k$ has modulus at most $(k+1)^2$, so $\|R_e\|_{\infty\to\infty}\le1+\sum_{k<q}(k+1)^2\le1+q^3$. Multiply each surviving Taylor bound by $2^{4\sum h_f-q|S|}\ge1$ and sum the series. Division by the original kernel costs at most $e^{\sum_f\alpha_f}$ after cancelling the exterior factor. This proves

$$
 |(R_ST)(x,y)|/T(x,y)
 \ \le\ [(1+q^3)2^{-q}e^{51\beta}]^{|S|},
$$

since $(1+2^4)3=51$. The full norm comparison used in (2) now gives $\langle R_S\rangle_\psi\le e^m[(1+q^3)2^{-q}e^{51\beta}]^{|S|}$. Expand $\prod_e[1+(e^\theta-1)R_e]$ on *all* links and apply Jensen with $\theta=q\log2/2$. The result is

$$
 \sum_e\Pr_\psi(k_e\ge q)\ \le\
 \frac{2}{q\log2}\{m+d(1+q^3)e^{51\beta}2^{-q/2}\}.                    \tag{7}
$$

For the same cutoff in both proofs, take $q$ satisfying (1) and also
$q\ge128$, $q\ge4[51\beta+\log(4dt/(a\delta))]/\log2$.
For $q\ge128$, $1+q^3\le2^{q/4}$, as seen at 128 and from $3/q<(\log2)/4$ thereafter. Hence the term after $m$ in braces is at most $a\delta/(4t)$. Since $\log2\ge1/2$, (7) implies (2). This checks the $m$-dependence, vacuum subtraction and error order in (6) by a different bound on the boundary kernel. Only the spatial mark is truncated in this check. No numerical evaluation enters either proof.

## Testing the sign left by the cutoff

**PROVED (necessary local signal).** Put $S_o=\sum_{0<r<1}r^t\operatorname{rank}J_r$. It is positive for the specified nonconstant loop partition by row 1624 (14) and row 1628 (17). Let $\langle\cdot\rangle_o$ average the unit visible vectors with weights $r^t/S_o$, using their magnetic or electric placements as indicated. Define $q+1$ signed numbers

$$
 A_j=\frac1d\sum_e\{\Pr_o^{\rm el}(k_e\ge j)-\Pr_0^{\rm el}(k_e\ge j)\},
 \quad 1\le j\le q,\qquad
 A_M=\frac1d\sum_p\{\langle W_p^{[q]}\rangle_o-\langle W_p^{[q]}\rangle_\Omega\}.
$$

There are $d$ spatial plaquettes. For $0<\eta<1/16$, if E1 holds at a cold point with $K\ge K_\eta$ from (6), then

$$
 \max(A_M,A_1,\ldots,A_q)
 \ \ge\ \frac{(1/16+\epsilon-\eta)\,W_t}{d S_o(1+g_\beta(q)-g_\beta(0))}
 \ \ge\ \frac{(1/16-\eta)a}{d t(1+g_\beta(q)-g_\beta(0))}.               \tag{8}
$$

In the specified windows this last lower bound is at least a fixed positive constant times $n^{-4}$ for the cutoff (1). Thus at least one of the retained *signed* averages must be positive on this scale, even when the visible occupation is small.

*Proof.* Use the clamped electric score in (5). Telescoping gives $N_q/(d S_o)=A_M+\sum_{j=1}^q[g_\beta(j)-g_\beta(j-1)]A_j$. Each coefficient is positive by row 1617 (12), the log derivative of the adjacent Bessel ratio. Hence the right side is at most $(1+g_\beta(q)-g_\beta(0))$ times the maximum. E1 and (6) give the first bound in (8). The second uses $W_t\ge W_{\rm obs}\ge S_o a/t$. Finally $g_\beta(q)-g_\beta(0)\le q/\beta+1$, using GL4 at $q\ge\beta$. This is bounded on the window because $q=O(\log n)$ and $\beta\asymp\log n$. The averages in (8) still use the exact observed thermal state.

**PROVED (what spin probabilities miss).** The compressed plaquette reads coherences between different spin labels. For example, in the actual neutral Haar slice space take one elementary plaquette with fundamental character $\chi_p$ and the unit trial vectors $\phi_\pm=(1\pm\chi_p)/\sqrt2$. The holonomy is Haar by integration over one link. Character orthogonality gives $\int\chi_p=0,\ \int\chi_p^2=1$, and the Haar substitution sending one link of the plaquette to its negative gives $\int\chi_p^3=0$. The two terms of $\phi_\pm$ occupy disjoint joint spin sectors, so *all* simultaneous spin-label probabilities in this placement agree. Yet $\langle W_p^{[q]}\rangle_{\phi_\pm}=\pm1/2$ for $q\ge1$, by $W_p=\chi_p/2$ and $Q_p^q\phi_\pm=\phi_\pm$. These are trial vectors. The example identifies the information lost by dephasing a low-spin local density matrix. It supplies no counterexample about Wilson eigenvectors. I obtain no lower bound on the signed combination in the proof of (8) from (2) or from spin probabilities alone.

## Comparison laws and scope

**ON FILE (rows 1618, 1626, 1628 (22), check 1630 §3.1).** For the free transverse photon the normalized multipliers are independent of $\beta$ in rescaled coordinates. Thus $b_r=0$ on every eigenspace, and at **every** $t>0$ $N=0<W_t/16$. For the compact Gaussian $U(1)$ law with zero monopoles and zero magnetic flux, all contractible flowed-loop cells are invariant under flat shifts. Their delay closure lies in the $Q=0$ photon sector. The even rotors at $Q\ne0$ have energy $|Q|^2/(2\beta n)$ and positive slope, but none contributes to $N$. On the observed sector the same zero-slope calculation gives $N=0$, including at a degeneracy with a charged level. A unitary change of coordinates adds a commutator whose compression to a transfer eigenspace vanishes. Thus the positive pointwise lower bound fails for both Gaussian laws at every period, in particular at any point satisfying the cold restriction. This comparison does not establish that a specified characteristic enters the cold region. Flat-shift invariance uses symmetry. The vanishing photon slope uses the Gaussian law. The Wilson staple formula (3) and the one-unit bandwidth of the cosine plaquette have no literal counterpart for a noncompact quadratic Maxwell action. [Gaussian spectra](gap-vir-down-neon.md) · [Visible sector](gap-vir-down-dom-astra62.md) · [Convention check](gap-vir-down-twoside-check-opus.md)

**PROVED (scope of the approximation).** For a *cosine* compact $U(1)$ weight, the proof by Taylor degree goes through with Fourier label $k=|j|$, since each coordinate factor changes the integer charge by one and its spin-$k$ projection has kernel bounded by two for $k>0$. Row 1617 supplies the corresponding electric cutoff. In five-dimensional Wilson $SU(2)$, use $4n^4$ links, eight colours, six spatial plaquettes incident on each link, and a boundary-link coefficient at most $4\beta$. Using $s_e\le4\beta$ in (3), the product proof gives the analogue of (2) with eight classes and $q=O(1+\beta+\log(dt/(a\delta)))$ for fixed cold threshold. This is logarithmic in $n$ when the same bare-coupling and period scalings are imposed. The factor eight in (4) becomes twelve. These counts change constants. The sign for the interacting five-dimensional law remains open.

**PROVED (the truncation estimate is compatible with failure of the seed).** Use the neutral spectator test of row 1553. Tensor the Wilson transfer with a coupling-independent oscillator with normalized multipliers $e^{-h/n}$, $h=0,1,\ldots$, observing only the Wilson loops. In ground-state coordinates every delayed reading is a Wilson delayed reading tensored with the spectator vacuum, so $N,N_q,W_{\rm obs}$ agree with their Wilson values. Product coldness implies Wilson coldness by factorization of the partition function. Hence (5)–(6) still hold there. At $u=n/512$ the oscillator has purity $(1-x)/(1+x)$, $x=e^{-1/512}>1/2$, by summing two geometric series. Multiplication by the Wilson purity, which is at most one, leaves the product below $1/3$ at every $K$. Thus (6) alone is compatible with seed failure even with the four-dimensional Wilson factor intact. The small-tail conclusion uses a property of the local Wilson weight. Selectivity at physical times would have to enter in the retained signed response. I cannot establish its sign on the weak part, the band or the infrared stretch, or establish a converse on pure Wilson fields. [Lemma ALG, row 1553](gap-mech-direction4-fable.md)

**RESULT (d) — a first piece of E1 on actual Wilson boxes.** **PROVED** (2) and (4) bound large spatial-link spins in each Wilson eigenstate in magnetic placement and their contribution to its vacuum-subtracted plaquette score.
With row 1617's electric estimate, (5)–(6) give an $O(1/\log n)\,W_{\rm obs}$ error for the full observed slope at all cold points of every prescribed fixed-depth window.
Equation (7) checks the spatial estimate by a different hand derivation.
**PROVED** (8) gives a necessary signed local discrepancy of order at least $n^{-4}$ for the trial rate $1/16$.
The sign and size of the retained response are open throughout the required window. No proof or refutation of E1, the seed or the mass gap follows.
These are written arguments, with no Lean or numerical calculation used as a proof step.
