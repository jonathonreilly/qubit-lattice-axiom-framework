# Repo search

I searched Markdown and TeX on `origin/main` (8b11ae2bb95e), `pr/10114` (f76f6c649cff), `pr/10133` (89faef229ff6), `pr/10134` (1e70c7211a2c) and `pr/10141` (c73ad7b177d9). Search terms included channel projector, noncommuting channel, Haar sewing, half-spin commutator, Casimir filter, two triangles, signed inclusion, Oeckl–Pfeiffer, spin foam and recoupling. The broad projector search also found quark and gravity projectors. The target-specific prior is absent at lane commit `2adba8cfa914`. The November 8 digest identifies the soft-route loop witness below. The registry has entries for Bałaban's last-scale estimates and no match for this inclusion or projector test. FINISH row 1421 has no separate “Repo prior work” line.

| Source | Statement and relevance |
|---|---|
| Main, `docs/BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md` 13–30 and `docs/GAUGE_VACUUM_PLAQUETTE_WINDOW_INTERTWINER_BASIS_DISPLACEMENT_BOUNDED_NOTE_2026-06-12.md` 267–283 | The SU(3) calculation tests character coefficients and a 2D benchmark. The four-fundamental basis and four-link Schur normalization are available. A normalized external-label lift and four-corner contraction remain open for that window. |
| Main, `research/mass-gap/library/prior/gap-crux-lit-nonab.md` 160–172 | The dual expansion represents the partition function. The cited literature search found no volume-uniform monotone bound from those signed amplitudes. |
| PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149, located by the [November 8 digest](prior/repo-search-2026-11-08.md) | For a centered simple loop the one-step convolution satisfies a positive rank-one **lower** form bound, with the exterior convolution retained. The requested upper estimate concerns a different operator. |
| Lane, [two-filter test](gap-tree-astra.md) (G8)–(G11), (G18)–(G19), and [its check](gap-tree-check-opus.md) §3 | The two singlet lines have overlap of modulus one half. Two pair rotations contract. The bare four-strand Wilson Haar tensor acts as the identity on its invariant plane, ruling out the proposed unit-cost one-link factorization. |
| Lane, [row 1341](gap-blockstep-astra62.md) (13)–(18), (22) and [check 1344](gap-blockstep-check-opus.md) §§1–5 | The exact open cube has 49 resolved face modes. Its interior polynomial has absolute error below \(2^{-24}\) for \(0\le\beta\le7/3\). The cost bound is \(6.6\cdot10^{14}\) arithmetic gates. Shared-boundary gluing still needs its own estimate. |
| Lane, [row 1418](gap-rg-step-sizing-astra62.md), sections on the 166-row minor, pair Gram matrices and (t1)–(t2) | Disjoint external columns realize pairs of triangles meeting one link. The norm of a fused pair is the trace of a product of bond Grams. Row 1418 leaves the signs inside that very contraction to be tested. [Row 1386](gap-mech-direction2-fable.md) §§4.3–4.5 requires a signed carry against the classical dimension factor. |
| Lane, [Lemma FOREST](gap-ps-disint-max.md) §3.4, [sparse cycle readings](gap-solve45-astra62.md) at line 19, and PRs 10114/10133, <code>RD_LOG.md</code> 316 | A gauge-invariant law has product Haar marginals on forests. One cycle retains its holonomy up to conjugation. The soft-route forest change of variables preserves product Haar with its anchors fixed. These give the orbit reduction used below. |

The targeted five-ref query for the row name, the noncommuting-channel test, Haar sewing, two-triangle Gram/minor/commutator, antipodal intertwiner and exposed Wilson triangle returned no hits. The broad projector search also located the trivial-channel transfer at zero coupling and the numerical SU(3) \(8\otimes8\) channel projectors on main, respectively in <code>NATIVE_GAUGE_TRANSFER_STRONG_COUPLING_GAP_NARROW_THEOREM_NOTE_2026-06-12.md</code> 97–104 and <code>SU3_WIGNER_INTERTWINER_BLOCK1_THEOREM_NOTE_2026-05-03.md</code> 157–173. Their operators and coupling regimes differ from this block.

The [outline index](sa-index/README.md), chunks 01, 02 and 04, and [obligations](sa-index/obligations.md) locate GL3 (“The Bessel recurrence gives (GL3)”) and GL4, proved in SA 2195–2243. I use these formulas with their character-dimension factor. SA 394–416 distinguishes mass preservation from transport of a specified observable. C4 at SA 4075–4084 asks for “one nonempty class” preserved through the steps. The CA index identifies CA-I 4209–4239 as a cited ultraviolet theorem with every effective coupling below the small ceiling. This row treats an intermediate-coupling tensor question. Credit for the outline and complete account belongs to Ethan Sussman and Levent Alpoge, writing with Claude and Codex. The Bałaban source used here is the quotation in the account. [Lane quotation record](lit-balaban.md)

## Result

**The group test passes for an exact first-pair estimate. The four-dimensional drift test fails for the one-link mechanism.** With \(b=2I_2(\beta)/I_1(\beta)\), two mismatched fundamental triangle pairings subtract \(3b^6/32\) from the squared-norm upper bound at each four-spin pattern. The same subtraction vanishes in compact U(1). In 4D any two reflection-invariant endpoint reductions commute on each fixed half-spin pattern. In the complete, vacuum-normalized \(2^4\) block, a whole boundary sector retains its bare triangle weights for every \(\beta\in I=[2,2+1/256]\). Its variation forces a radius greater than \(1/4\) around any single centre in the unscaled Hilbert–Schmidt norm after any fixed isometry with the transported vacuum. An estimate using two independently routed cycles remains open.

## Plan and checkpoint

1. Check the target-specific prior, owner rules, row 1418, the blockstep checks, and existing ownership of the signed gate.
2. Identify the linear functional or contraction in the Haar-integrated block that could benefit from different channel projectors. Compute the signed contribution on the half-spin core, test its abelian specialization, and trace its dimension dependence against the classical factor.
3. Decide the gate in the variables of the block. If it passes, attempt the specified four-direction inclusion and measure the cost. If it fails, prove the obstruction for a precisely stated class.
4. Record exact derivations, any computations and their trusted base, remaining obligations, and the next two rows with decisive outcomes.

Row 1421, author-only mathematical argument at the requested pin. This is research text and grants no status.

## The first Wilson pair

Take the ordered bond and vacuum normalization of row 1418. A face of spin \(n/2\) has normalized character coefficient \(b_n=(n+1)I_{n+1}(\beta)/I_1(\beta)\) with \(b_0=1\). Each corner carries \(b_n^{1/4}\). Each bond carries the incident spins and an orthonormal invariant-tensor label, with dual bases on its two ends. Put \(b=b_1\) and \(u=b^{3/4}/\sqrt{2}\). Fix four occupied transverse plaquettes at the common bond of two bare sites. A column with two fundamental triangles has value \(u^2p_m\) up to its orientation sign, where \(p_m\) is the unit product of the two singlets in matching \(m\). This follows from the cycle evaluation of row 1418, leaving its common leg open. The two triangles require the members of each matched pair to belong to different axes. In four dimensions there are exactly two such matchings. At least one opposite pair occurs in any four of the six transverse directions. Pairing its ends to each other excludes one matching, and each of the other two is admissible.

Choose phases so that the two matching vectors \(p,q\) have \(\langle p,q\rangle=1/2\), using (G8) of the two-filter test. Sewing the internal bond gives the actual exterior minor

\[
Y=u^4\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}.
\]

The exterior labels distinguish the two patterns at each end. They fix every corner spin, so higher spins cannot change these four coefficients. Rows and columns may be rephased independently. The determinant in the reflected, positive Gram convention is \(3u^8/4\). The basis-invariant squared-norm saving against the product of the two endpoint squared norms is

\[
4u^8-\|Y\|_{\rm HS}^2=\tfrac32u^8=\tfrac{3}{32}b^6.
\]

Indeed, for the two ordered mismatches the unit Cauchy–Schwarz deficit is \(1-|\langle p,q\rangle|^2=3/4\). In a fixed compact U(1) charge sector the invariant space has dimension at most one and every such exterior-square deficit is zero, including when a vector vanishes. This is a genuine group-dependent improvement in the *pair norm*. The two individual singlet projectors also have \([P,Q]^*[P,Q]=(3/16)I\) on their plane. To price a four-dimensional step requires deciding which operators the Wilson sum actually presents to its two endpoints and testing the normalized outgoing channels over the full block.

The signed term in the minor is \(-2\det Y\) in \(\|Y\|_{\rm HS}^2=(\operatorname{tr}Y)^2-2\det Y\), in the reflected Gram convention above. Its basis-independent version embeds with a fixed sign in the *entire* first fusion. For each ordered spin pattern \(S\) on the cut, write \(x_i,y_j\) for the two sites' column vectors in its common invariant space. The other external legs fix \(S\), so the squared norm of the pair adds over \(S\). Relative to the sectorwise Cauchy–Schwarz upper bound it is reduced by

\[
 \sum_{S,i,j}\left(\|x_i\|^2\|y_j\|^2-|\langle x_i,y_j\rangle|^2\right)
 =\sum_{S,i,j}\|x_i\wedge y_j\|^2 .
\]

Thus all 15 four-spin patterns together contribute exactly \(45b^6/32\) **from their two-triangle columns**. The full saving is at least this large both at half-spin cutoff and for the untruncated bare pair. Adding columns cannot cancel a nonnegative summand, and the bare Hilbert–Schmidt bound of row 1418 ensures convergence. In compact U(1) the *whole sum* is zero at fixed charges, regardless of its Wilson coefficients. For example, charges \((+1,-1,-1,+1)\) admit both pairings \((12)(34)\) and \((13)(24)\) on the very same one-dimensional invariant space.

**Value throughout the interval.** Write \(r_k=I_{k+1}/I_k\). GL3–GL4 give \(b=2r_1\), \(r_k=(2(k+1)/\beta+r_{k+1})^{-1}\), and \(r_k\le\beta/(2(k+1))\). Also \(b/2\) is the mean of the half-trace under the one-plaquette Wilson density. Its derivative is the strictly positive variance. At \(\beta=2\), \(r_4\le1/5\), \(r_3\ge5/21\), \(r_2\le21/68\), hence \(b\ge136/157\). On \(I=[2,513/256]\), \(r_3\le513/2048\) and \(r_2\ge 2048/6657\). Thus

\[
 \frac{136}{157}\le b\le
 \frac{2}{1024/513+2048/6657}<\frac{87}{100},\qquad
 \frac{3}{32}\left(\frac{136}{157}\right)^6
 \le \frac{3b^6}{32}<\frac{3}{32}\left(\frac{87}{100}\right)^6 .
\]

**Dimension of this pair calculation.** In dimension \(d\), four transverse signed directions have \(k=2\) allowed matchings if an opposite pair occurs and \(k=3\) otherwise. Of the \(\binom{2(d-1)}4\) patterns, \(16\binom{d-1}4\) have \(k=3\). For any two distinct matching lines the overlap has modulus \(1/2\), by permutation of the labels in (G8). In units \(u^8\) the squared pair norm is \(k+k(k-1)/4\), and the product bound is \(k^2\). The norm ratios are \(\sqrt{5/8}\) and \(1/\sqrt2\). All 15 patterns in 4D have the first ratio. In 5D there are 54 of the first kind and 16 of the second, giving total selected saving \((54\cdot3/2+16\cdot9/2)u^8=153b^6/16\). Multiplying the ratios formally by \(2^{d-4}\) would give \(\sqrt{5/8}\) in 4D and either \(\sqrt{5/2}\) or \(\sqrt2\) in 5D. That multiplication requires an identity relating a directional pair norm to a running coordinate of an isotropic block. The actual coordinate calculation below tests this point.

## Which channel operators the Wilson contraction supplies

**Class tested.** Cut one directed fine link. First fix its ordered plaquette spins, each zero or \(1/2\). An endpoint reduction is \(XDX^*\) on that link's invariant space, where \(X\) maps exterior coefficients to the open link. Allow any exterior form \(D\) and any Wilson weights for which the reduction commutes with reflection of each transverse axis whose two opposite occupied plaquettes occur. It suffices that \(D\) respects those reflections and \(X\) intertwines them. This includes the unconditioned Wilson site Gram of row 1418, sums over reflection orbits of its columns, and spin tails summed with reflection-invariant weights. Opposite ends can have different couplings or different such forms. The test fixes the pattern at the cut. A contraction that mixes two physical links or selects a single asymmetric exterior column can leave this class.

**Claim.** Every two such endpoint reductions on a common fixed pattern commute in 4D. In particular their spectral projections commute. This statement covers *all* 51 half-spin bond labels.

Orient each plaquette through the cut so that it traverses the directed link forwards. The Wilson character is invariant under inversion, and the dual bases on the two ends can be chosen compatibly. Reflection in a transverse coordinate fixes the directed link. It exchanges the two fundamental slots for its two opposite plaquettes and fixes the other occupied slots. Other changes of exterior basis cancel in \(XDX^*\). On the common invariant space the reduction therefore commutes with the transposition of those slots.

With zero or two occupied slots the invariant space has dimension one. Four occupied slots contain an opposite pair. Coupling that pair to spin zero or one gives the minus or plus eigenspace of its transposition. Each contains exactly one total singlet, because the remaining two fundamentals must have that same spin. Six occupied slots consist of three opposite pairs. Simultaneously diagonalize their three swaps. The tuple of pair spins \((j_1,j_2,j_3)\in\{0,1\}^3\) can give a singlet only for \((0,0,0)\), the three permutations of \((1,1,0)\), or \((1,1,1)\). Each supplies exactly one by the spin addition rule. Each such line has different swap eigenvalues. Odd occupancy has no invariant. This lists \(1+15+15\cdot2+5=51\) states across the fixed patterns. Every allowed reduction acts diagonally in the same lines on each pattern. The conclusion holds with arbitrary spectator spins at the other legs for which the reduction exists.

For the two-triangle columns the opposite-pair swap exchanges \(P=pp^*\) and \(Q=qq^*\). It changes the sign of \([P,Q]\), so the reflection average of the commutator vanishes. The actual endpoint Gram from these columns is \(u^4(P+Q)\). Before averaging, the two projectors obey \([P,Q]^2=-3I/16\) on their plane. Choose \(p=(1,0)\), \(q=(1/2,\sqrt3/2)\). Then \([P,Q]_{12}=\sqrt3/4=-[P,Q]_{21}\), and \(\operatorname{tr}(PQ)-\operatorname{tr}(PQPQ)=3/16\). The positive exterior-square saving above survives the symmetric sum. Charging an extra commutator of the two *summed* endpoint operators would count a term whose actual value is zero.

For the isotropic bare site in 5D, impose its full transverse signed-permutation symmetry. For a fixed occupancy of at most six, pair opposite slots first, then pair the remaining singletons. Each chosen pair can be swapped independently, using signed axis permutations for singletons. There are at most three such pairs, so the preceding spin-addition argument again leaves at most one singlet per joint swap character. Eight occupied slots give four opposite pairs. The only joint character with multiplicity greater than one has four spin-one pairs. Its singlet space has dimension three, by coupling two spin-one pairs through spin \(0,1,2\). In the vector realization of spin one its basis consists of the three delta pairings of four vector indices. They are independent by testing two equal indices of one value and two of another. The four axes permute the three pairings as the full symmetric group on three letters. A matrix commuting with this action has constant diagonal and constant off-diagonal entries in that basis, and all such matrices commute. Hence the actual commutator of isotropically reduced endpoint Grams is zero also in 5D, at weak coupling as well as on \(I\).

## The normalized four-direction test

Use the bare site tensor on \(B=\{0,1\}^d\), embedded with distinct boundary bonds as in the lattice or a torus with periods at least four. Contract all internal bonds, retaining the external fine bond labels in their coarse bundles. Denote the result by \(R_B\), its all-vacuum coefficient by \(z_B\), and the normalized tensor by \(R_B/z_B\). These are the result of pairing all coordinate directions, in any order. The following projection is taken **after** that exact map.

At each site \(x\) there is one outward fine bond in each coordinate direction. At every boundary bond allow nonzero spins only on plaquettes spanned at \(x\) by *two* outward bonds. Require every occupied corner of that kind to match its label at both bonds. Let \(c_x\) be the tensor obtained by contracting just those outward intertwiners and corner weights, with its vacuum coefficient one. On the indicated boundary subspace the exact identity is

\[
                    (R_B/z_B)_{\rm out}=\bigotimes_{x\in B}c_x.       \tag{1}
\]

To prove (1), classify fine plaquettes incident to \(B\). A plaquette with two outward directions meets \(B\) at the single site \(x\). One with one outward and one inward direction has its spin fixed to zero by a boundary slot. A plaquette using only internal bonds lies in \(B\) and has its full four corner weights. At each site the magnetic-index network therefore splits into an outward graph and the graph on its inward bonds. Their only connecting strands have dimension one. The internal bond labels and their contractions are precisely those occurring for vacuum external labels, for every choice of the outward intertwiners. No outward fine bond belongs to two sites of \(B\). This proves the product coefficient by coefficient. At fixed spin cutoff the argument is finite. For removal of the internal cutoff one can also expand the finite Wilson integral on the internal plaquettes directly. GL4 gives \(b_n\le(\beta/2)^n/n!\), and \(|\chi_{n/2}|\le n+1\), so the character products converge absolutely and uniformly on this finite graph. This retains every internal spin. Boundary coefficients selected by the projection are exactly those of the full bare input.

More explicitly \(z_B=\int\prod_{p\subset B}\big(e^{\beta q(U_p)}/A(\beta)\big)\,dU\), where \(q=\tfrac12\operatorname{tr}\), \(A(\beta)=\int e^{\beta q(U)}dU\), and the integrated links carry independent Haar measures. There are \(N_p=2^{d-2}\binom d2\) such plaquettes. Each unweighted \(q(U_p)\) has mean zero, so Jensen gives \(z_B\ge A(\beta)^{-N_p}\). Here \(A=2I_1(\beta)/\beta\) and its positive series gives \(A\le e^{\beta^2/8}<2\) on \(I\), using \((k+1)!\ge2^k\), \(\beta^2/8<2/3\), and \(e^2<8\). In 4D this is a lower vacuum denominator \(z_B>2^{-24}\) for the complete bare block.

At half spin the outward graph at a 4D site is \(K_4\). Every occupied vertex has even degree at most three. Its nonempty even subgraphs are exactly four triangles and three four-cycles, with a unique two-line intertwiner at each active leg. Their coefficient magnitudes are \(u=b^{3/4}/\sqrt2\) and \(s=b/2\), respectively, from the normalized cycle contraction. Thus (1) explicitly gives \(8^{16}\) orthogonal admissible coordinates. It gives \(u^2\) in magnitude for each pair of distinct-site triangles, and \(u^k s^\ell\) for any choice of \(k\) triangle sites and \(\ell\) square sites. The signs depend on the fixed bond conventions and are independent of \(\beta\). No four-strand projector occurs in this whole corner subspace. In 5D a \(K_5\) corner can itself have two triangles meeting a four-strand leg. A single outward triangle continues to have its same normalized coefficient.

**Failure of four-dimensional drift.** Fix the directed triangle on \(+1,+2,+3\). It can face outwards at \(2^{d-3}\) sites. Each of these distinct output coefficients equals the microscopic coefficient \(u(\beta)\) up to its fixed sign. The gain on a *single* such normalized coefficient is exactly zero for every \(\beta\in I\), including when all other plaquette spins in the block are summed. The conclusion holds at every finite positive coupling. For any two distinct \(\beta,\gamma\in I\), the Euclidean length of the change in those resolved output coordinates divided by the change in the corresponding single input coordinate is exactly \(2^{(d-3)/2}\). This gives the following test of the classical factor.

| Dimension | Per-copy response | Resolved Euclidean response | Classical \(2^{d-4}\) |
|---|---:|---:|---:|
| 4 | 1 | \(\sqrt2\) | 1 |
| 5 | 1 | \(2\) | 2 |

The table compares the same finite Wilson variation on both sides. Equivalently, calibrating inverse coupling by the strictly increasing \(u(\beta)\) gives back \(\beta\) on each of these output copies. In 4D the decrement against the classical value is zero. The signed reduction \(3b^6/32\) takes place on a different set of boundary labels. A matched pair of identical singlet lines also saturates Cauchy–Schwarz on its own four-strand coefficient. A strict debit uniform over the resolved labels cannot be assigned at the sewing step. Applying \(\sqrt{5/8}\) to every output sector would contradict (1). This extends the product-tensor derivative in row 1418 to finite bare Wilson inputs. The exposed-triangle argument in row 1341, (24), is the geometric precedent in its auxiliary-bond presentation.

### An interval obstruction for every fixed orthogonal basis

Let \(\beta_-=2,\ \beta_+=513/256\). Even an unrestricted centre \(C\) for the *normalized whole block* must obey

\[
 \max_{\beta=\beta_-,\beta_+}
       \|U(R_B(\beta)/z_B(\beta))-C\|_2
       >320(5/8)^{15}>\tfrac14 \qquad(d=4).                      \tag{2}
\]

Here \(U\) can be any common isometry, including one acting across a cut, with the vacuum covector transported when changing basis. Thus the estimate also applies to those fixed orthogonal rearrangements that preserve all closed contractions. It is independent of the rank of \(C\).

For the width of the coefficient, set \(r=A'/A=b/2\). The series of \(A\) gives \(A''+3A'/\beta=A\) by matching successive coefficients. Therefore \(b'=2(1-3r/\beta-r^2)\). Since \(r<87/200\) and \(\beta\ge2\), this gives \(b'>6331/20000>5/16\). Also \(b<1\), so \(u'=(3/(4\sqrt2))b^{-1/4}b'>5/32\). In particular \(u_+-u_->5/8192\), where \(u_\pm=u(\beta_\pm)\). The bound \(b>6/7\) gives \(u^4>54/343>(5/8)^4\).

Select one outward triangle at each of all sixteen sites independently. These \(4^{16}\) distinct orthonormal boundary coordinates have values \(\pm u^{16}\) by (1), with the same signs at both endpoints. The distance of the projected endpoints is \(2^{16}(u_+^{16}-u_-^{16})>640(5/8)^{15}\), by the factorization of the difference of the sixteenth powers. Every enclosing ball has radius at least half that distance. Finally \(5^{16}=152587890625>137438953472=2^{37}\) gives the last inequality in (2). The same projection argument restricted to the 64 single triangles and \(16\binom{16}{2}=1920\) distinct-site double triangles gives endpoint distances \(8(u_+-u_-)\) and \(\sqrt{1920}(u_+^2-u_-^2)\), respectively. No enumeration of the boundary tensor is needed.

For orthogonal sector radii in the unscaled output norm with fixed vacuum, (2) forces the Euclidean norm of the nonvacuum radius vector above \(1/4\). Row 1418 allows different scaled charts and does not stipulate this numerical ceiling on \(v\). Equation (2) is a necessary price for one fixed physical chart over \(I\). It supplies no impossibility theorem for a chart that absorbs the corner dependence analytically, changes the norm, or changes the input/output scale.

## A test that also allows mixed boundary plaquettes

One can specify a larger class directly in the *full* normalized block. For a compatible fixed exterior label \(\lambda\), let \(S_\lambda\) contain an internal edge \(e\) whenever a nontrivial mixed plaquette meets \(B\) along \(e\). Each such plaquette has two corners in \(B\). After extracting the boundary weight

\[
 a_\lambda=\prod_{p\ {\rm outward/outward}}b_{n_p}^{1/4}
             \prod_{p\ {\rm mixed}}b_{n_p}^{1/2},
\]

the coefficient of \(R_B/z_B\) equals \(a_\lambda\,\mathbb E_{\mu_B} F_\lambda(U|_{S_\lambda})\). Here \(\mu_B\) is the probability law with the complete internal Wilson density used to define \(z_B\). The function \(F_\lambda\) is obtained by contracting the fixed external intertwiners, the corner identifications, and one matrix of \(U_e\) in the oriented representation for each mixed plaquette at \(e\). To see the formula, undo the Haar spin sum on every internal link. Four internal corners reassemble each entire internal Wilson plaquette, while the two corners of a mixed plaquette leave exactly that one matrix on its internal edge. Outward/outward corners have no such matrix. Gauge actions at a vertex cancel at the corner identifications and act trivially on its fixed external invariant tensors. Thus \(F_\lambda\) is gauge invariant under independent gauges at the vertices of \(B\). The same uniform character bound used in (1) justifies the reassembly.

**Forest.** If \(S_\lambda\) is a forest, its marginal is product Haar for every gauge-invariant internal probability law, by Lemma FOREST. Consequently the Wilson interior contributes the same expectation as independent Haar. At half spin, an internal edge in \(B\) has only \(d-1\) mixed plaquettes available, one on the outward side of each transverse axis. In 4D it carries at most three active fundamentals in this expectation. Its Haar-invariant space has dimension zero or one. Thus no internal four-strand commutator can occur in *any* of these normalized forest readings. In 5D four mixed fundamentals are geometrically possible under the same rule. [Lemma FOREST, §3.4](gap-ps-disint-max.md) · [Its use under gluings](gap-blockstep2-check-opus.md)

**At most one independent cycle per connected component.** Choose a spanning forest of \(S_\lambda\). Vertex gauges set its links to one, leaving a single holonomy \(h_i\) on each remaining edge, one per cyclic component. The residual root gauges conjugate the \(h_i\) independently. The Wilson law of these holonomies is therefore invariant under the corresponding independent conjugations, even when their conjugacy classes are correlated. On remaining edge \(i\) put \(D_i=\bigotimes_{p\ {\rm reading}\ i}D^{(n_p/2)}\), using dual representations for opposite orientations. Resolve the tensor product as \(\bigoplus_j V_j\otimes M_{ij}\). Averaging over each root conjugation and using Schur's lemma gives the exact interior operator

\[
 \mathbb E_{\mu_B}\bigotimes_i D_i(h_i)
   =\sum_{\boldsymbol j}
       \mathbb E_{\mu_B}\!\left[\prod_i
           \frac{\chi_{j_i}(h_i)}{2j_i+1}\right]\,
       \bigotimes_i\Pi_{ij_i},                                      \tag{3}
\]

where \(\Pi_{ij}\) projects onto the whole \(V_j\otimes M_{ij}\). All dependence on the internal Wilson law is in the scalar expectations. For a fixed graph, forest and strand representations, (3) at different couplings, or for different gauge-invariant interior laws, consists of operators with common spectral blocks. Their commutator is zero, also when a spin occurs with multiplicity. Each holonomy based at the same vertex in a one-cycle component is a power of the same generator, so a group commutator of two such holonomies is the identity as well. The tree and conjugacy-class reductions themselves are prior work. The new application proves this limitation for every mixed boundary label with the indicated graph. [Sparse forest and cycle reductions](gap-solve45-astra62.md)

The fixed exterior contraction can still contain different recoupling projectors and the scalars in (3) can depend on the group. Formula (3) excludes a commutator **of the interior-dependent channel operators** in this class. Two noncommuting holonomies at a common base vertex need at least two independent cycles in its connected component. An asymmetric exterior contraction coupled to their joint law is a concrete way outside the obstruction.

## Disposition

The exact negative covers reflection-invariant one-link reductions on the fixed half-spin sectors, a uniform gain charged to the resolved raw triangles, and the interior commutator in (3). The determinant saving remains available in an estimate that distinguishes matched and mismatched columns. At four-dimensional block scale (1) fixes the normalized response of the exposed triangles to both bare endpoints, and (2) prices their effect even for an arbitrary common isometry. A general redistribution of interactions between neighbouring blocks, or a scale-dependent subtraction of an analytically transported reference, lies outside these conclusions. Row 1341 (25)–(27) already shows why such a reference must also carry its mixed boundary interactions.

I stopped at this failed drift test. The lower bound on \(z_B\) and the preserved boundary coefficients include the full bare spin tail. Entry into an invariant region of a new chart, a sector vector \(v\), the two inequalities for \(M_I\), and a four-direction inclusion in that chart remain open. The numerical work of a full verifier was never triggered, so there is no measured runtime for one. All displayed results are hand derivations. No computational assertion is used as a proof step, and there is no Lean-kernel receipt or independent check of the new arguments.

## Next two rows

1. **Test a connected two-cycle reading at the same normalization.** Use the two unit squares in the \(12\) and \(34\) planes meeting at the origin in \(\{0,1\}^4\). Freeze explicit compatible mixed-plaquette labels and two exterior routings. Divide by the same \(z_B\), keep their Wilson weights, and evaluate their joint matrix after subtracting the disconnected corner contribution. To pass, exhibit an actual signed contribution to a named normalized response that vanishes for each fixed U(1) charge assignment and gives a decrement in 4D with its five-dimensional classical comparison. If the two routings collapse to (3), or their signed term cancels in the proposed response, reject that reading. Noncommutation of test matrices alone cannot pass.
2. **Attempt the four-direction inclusion only for a surviving response.** Freeze a rearrangement across the cut, including its action on the mixed sector and the equality of all closed contractions, then fix input and output centres and scales. Accept a single interval certificate when it encloses the bare tails for all \(\beta\in I\), establishes a positive vacuum lower bound, and gives rational \(v>0\) and an outward \(M_I\) with \(M_I(0)\le v/16\) and \(M_I(v)-M_I(0)\le15v/16\) componentwise. Record measured cost, kernel replay and trusted base for any computed inequalities. A proved residual above its allowance rejects that chart. If the two-cycle test fails, this inclusion has no qualifying input.
