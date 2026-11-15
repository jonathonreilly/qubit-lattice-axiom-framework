lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T12:33Z

# gap-detlemma-read-opus: locate the "determinant lemma" used by (TH)

FINISH row 986, port reading. Worktree pinned at afe5b3004. Quotes only; no proof attempt.

## Plan (at most eight steps)

1. Read row 981 and row 978 outputs: what (TH) and Corollary CU need, and the exact citations CA-II L141291, L141531.
2. Read CA-II around L141291 and L141531 (the quoted text of the citation and the constant asserted free of K).
3. Search CA-I, CA-II, CA-III, appendices, outline in the Sussman-Alpoge repository (local copy and latest default branch) for the determinant lemma.
4. Search Balaban's papers in ~/ym4d-papers for the torus-to-torus Gaussian normaliser comparison.
5. Classify: proved / cited / missing; quote with file and line.
6. State exactly the form (TH) needs; if missing, write the exact statement for a later proof row and say what kind of statement it is.
7. RESULT line.

## Step log

(filled in below as each step completes)

## Repo search (rule "Repo first")

- Row 981 (`library/gap-ladder-check-opus.md` Step 4, L119-131, L178, L208) found the phrase "determinant lemma" only at CA-II L141291 and L141531, and the one CA statement with "determinant" in its title (CA-I L105992, `4.24:prf-single-determinant`) is not a two-torus comparison. Row 877 (`library/gap-exit-check-astra.md` L490-492, gpt-6-astra) recorded the qualification of hypothesis (a). Row 981 named `library/b109.md` L132 and `library/hma.md` D5 as candidate local sources, unread. This row builds on those.
- `~/ym4d-papers` does **not exist on this machine** (Mac mini worker 3: `ls ~/ym4d-papers` gives "No such file or directory"). Balaban's papers could not be read here; Step 4 uses only the repository's own rebuilds and quotes of them. Reported as a skipped source.

## Step 1. Sources and what (TH) needs (00:45Z)

**Source.** Sussman and Alpoge, https://github.com/ethanwsussman/Yang--Mills-LLM-experiment, cloned 2026-11-15 into `/tmp/gapdet986/sa` (scratch, not committed). Default-branch HEAD `c7fef8b` (2026-11-10); 15 commits after `31a47c543775`. At HEAD the complete account lives at `YM4/Old/theorem_0_complete_account_raw_{I,II,III,master}.tex` (commit `ed82e1f`, "Move Theorem 0 sources into YM4/Old"), and the four blobs are **byte-identical** to those at `31a47c543775` (git blob ids equal: I `31898fb2`, II `f1e0aa13`, III `6012ff57`, master `ded00452`). So every CA line number below holds at both commits. New since 31a47: `YM4/{BA,CL,EM,FP,GI,LP,MB,RT,SI}/YM4_*.tex`, `YM4/YM4_1400.tex`, `YM4/YM4_sketch_500.tex`, `YM4/YM4_sketch_draft.tex`, YM3 files. These are searched in Step 3.

**What (TH) needs (from row 981, Step 4.3).** (TH) of Corollary CU (row 978, `library/gap-ladder-max.md` 5.2) is read from 1.1.5 (iii) of `library/gap-phys-seed.md`: Delta(n^4) <= (C_+ + C_- + delta) l^4 with V the full vacuum number, i.e. E_m of CA-II Definition 8.22 (L140913-140921, "Balaban's normalisation constant of the bare density rho_0 = exp[-x_0 A(U) - E_m] on T_m"), and delta = delta-bar_vac + c_det. The torus-independence lemma (CA-II L141283-141386) gives delta-bar_vac only for E_m **less** the Gaussian normalisers. So (TH) needs a separate bound on the difference of the per-volume Gaussian normalisers of two tori T_m, T_m', uniform in K.

## Step 2. The two citations, quoted (CA-II, blob f1e0aa13) (00:50Z)

1. **Hypothesis (a) of Lemma `8.22:lem-vacuum-energy-density`** (L141283-141291): "(a) $E_{m''}$ denotes Ba{\l}aban's normalisation constant of the bare density on $\mathbb{T}_{m''}$, as in the normalisation of $\widetilde{Z}_{m''}$ in Definition~\ref{8.22:not-partition-sources-cells}, less the Gaussian normalisers of the $K$ steps, the Gaussian normaliser of step $j$ being the logarithm of the Gaussian integral of step $j$ at the trivial background; the Gaussian normalisers of the two tori are compared by the determinant lemma. This number is $E_{m''}=\sum_{j<K}E^{(j)}_{\mathrm{vac}}(\mathbb{T}_{m''},\mathbb{T}_{m''})$ ..."
2. **Remark after the lemma** (L141529-141534): "The determinant lemma, which compares the Gaussian normalisers of the steps excluded by hypothesis~(a), contributes a further constant, depending on $L$ and $\mathfrak{p}$ only (in particular not on $K$, $g_0$, $g$, $m$ or $m'$), to the zero-source comparison of the two tori."
3. **Why it is excluded** (proof, L141426-141432): "the one torus-wide number per level, the Gaussian normaliser of the step, is excluded by hypothesis~(a). Were hypothesis~(a) to admit even a bounded number of torus-wide numbers per level, they would contribute to $\delta_{\mathrm{vac}}$ a term of order $K(2L^{\min(m,m')})^{-4}$, which is not uniform in $K$ at fixed $m'$."
4. **Conclusion of the lemma** (L141374-141386): delta_vac := |E_m/(2L^m)^4 - E_m'/(2L^m')^4| <= delta-bar_vac := 2(E_0+1) K_* sum_{u>=0} L^{4u} exp[-(kappa/2)((1/2) L^11 L^u - 2)], "depends only on L and p; it does not depend on K, g_0, g, m or m'".

**A notational point the reader must hold (not a defect claim, a reading):** Definition 8.22 (L140913-140916) writes $E_m=\sum_{j<K}E^{(j)}_{\mathrm{vac}}(\mathbb{T}_m,\mathbb{T}_m)$ and calls it Balaban's normalisation constant of $\rho_0$; hypothesis (a) of the lemma (L141291-141292) writes the **same** sum and says it is that constant **less** the Gaussian normalisers. Read literally, both cannot hold unless the Gaussian normalisers are zero. Row 981 read Definition 8.22's E_m as the full constant (normalisers included) and the lemma's as the itemised sum (normalisers excluded). That reading is the one consistent with the remark at L141531 (the determinant lemma "contributes a further constant ... to the zero-source comparison of the two tori"), and it is the one used below.

## Step 3 (part 1). Search of the whole Sussman-Alpoge repository at HEAD c7fef8b (01:00Z)

Grep used (`git grep -n -i -E` on HEAD, all `.tex`/`.md`): `determinant lemma|gaussian normali[sz]er|normali[sz]er of the step|determinant.{0,40}two tori|two tori.{0,60}determinant`; then `vacuum.energy density|torus.independen|free.energy density|pressure.{0,30}(torus|tori)|(two|both) tori|density of .{0,30}normali[sz]` over `YM4/*.tex` (outside `Old/`) and `YM3/YM3_{I,II,main}.tex`.

**3.1 The phrase "determinant lemma".** In the whole repository at HEAD it occurs at CA-II L141291 and L141531 (the two citations) and at CA-I L103833 ("determinant lemma for the survivors, which forms det A_ss only", the survivors' block, row 981's `4.24:prf-single-determinant`). Nowhere else, in any file of YM3, YM4 (new parts), QED3, QCD3. **No statement of that name exists in the repository.**

**3.2 Other "Gaussian normaliser" passages in CA (not the lemma).**
- CA-I L3764-3778 (Definition `4.2:def-increment` (a)): the Gaussian normaliser enters as "log Z^(j-1)(U_j) - log Z^(j-1)(1)", i.e. **with its trivial-background value subtracted**. CA-I L3966-3985 (one-loop value): constants C_det(N), C_cmp(L,N) bound |B_k - B_k^ref| and |B_k^ref - (11 C_g/24 pi^2) log(1/eta)|, again for the reference functional "minus its value at the trivial background". CA-II L26797-26800 and L27525 (beta^0_l, "the coefficient, in the sense of [(1.22)]{B-CMP109}, of the Gaussian normaliser of step l"): a background coefficient. None of these touches log Z^(j)(1) itself, which is the number the lemma excludes. So C_det(N) of CA-I L3976 is **not** the determinant lemma's constant (different object: background-dependent coefficient vs trivial-background value).

**3.3 The 3D account does have the statement, in another form.** YM3_I (`YM3/YM3_I.tex`, HEAD), Subsection "Comparison of vacuum constants on two tori" (L65335-65508), Proposition `III-7-12` (L65356-65377):

> "Then $\left|\frac{E_{(K)}[\bar{\mathfrak w}_1]}{\ell_1^3}-\frac{E_{(K)}[\bar{\mathfrak w}_2]}{\ell_2^3}\right|\le2C_{\rm tt}C'_{\rm tt}E_0e^{-\kappa\ell_*/(5M)}$." (L65370-65374, with $C_{\rm tt}=2C_{E,0}$, $C_{E,0}=2048\sum_{n\ge0}e^{-n}$, $C'_{\rm tt}=2$.)

and its proof **includes the Gaussian normaliser**, by localising it, not by excluding it (L65403-65430):

> "The two vacuum families at level $j$ are $\mathsf{vl}^{(j)}_\iota(X,z)=E^{(j),\mathfrak w_\iota}(X,\mathbf1,z)$, $\mathsf{vn}^{(j)}_\iota(X,z)=\mathsf n^{(j),\mathfrak w_\iota}(X,z)$. They are real and each is bounded by $E_0e^{-\kappa d_j(X)}$; see Section~\ref{subsec:ymm1-62-1} and Proposition~\ref{II-192-21}. ... For $\mathsf{vn}^{(j)}$, use its local logarithm series and pivot term, \eqref{II-45-8} and the local-chart identity following \eqref{II-45-65}. ... All cubes, nonpivot bonds and tents in these definitions are carried by the common lift, so the Gaussian vacuum values agree as well."

and the torus-wide part of the Gaussian normaliser is a **counting term** with coefficients free of the torus (L65432-65445): "Write the full-torus contribution of step $j-1$ as $\mathsf N^{(j-1)}_\iota+\mathsf S^{(j)}_\iota$, where $\mathsf N$ is its counting term ... There are $3(L^3-1)$ positive nonpivot bonds per level-$j$ site. Thus $\ell_\iota^{-3}\mathsf N^{(j-1)}_\iota=L^{3(K-j)}[3(L^3-1)(\mathsf{co}^{\rm b}_{j-1}+\mathsf{co}^{\rm i}_{j-1})+\mathsf{co}^{\rm s}_{j-1}]$. The three coefficients in \eqref{II-192-10} depend on the common coupling sequence and fixed constants alone. Their contributions per volume therefore cancel."

So in three dimensions Sussman and Alpoge prove the two-torus comparison **with** the Gaussian vacuum values, by writing log of the Gaussian integral at the trivial background as an exactly extensive counting term plus a family n^(j)(X, z) of local terms with the same exponential bound as the effective-action terms. This is the form a four-dimensional "determinant lemma" would have to take, and it is credited to Sussman and Alpoge (YM3_I, HEAD c7fef8b). It is not a statement of the 4D account.

Still to do in Step 3: the definition (II-45-8) and Proposition II-192-21 of YM3_I (what the local Gaussian family is and how its bound is proved); the new YM4 files (YM4_1400, GI, EM, SI) passages on the Gaussian normaliser.

## Step 3 (part 2). How YM3_I localises the Gaussian normaliser at the trivial background (01:10Z)

Source: `YM3/YM3_I.tex` at HEAD c7fef8b (Sussman and Alpoge; credit them). Three-dimensional, SU(2), their own block RG (not Balaban's 4D step).

1. **Proposition `II-44-37`** (L40673-40713), Subsection "The Gaussian normalizer" (L40631). Statement, quoted in part: "There are $L$-dependent constants $a_N,\delta_N>0$, $M_N,E_b\ge1$, and $E_N=3L^3E_b$, such that the following holds when $M\ge M_N$. For every wall-connected coarse region $X$ there are local terms $N(X,b;P)$ ... Uniformly in the lattice, $k,X,P,b,z$, $|N(X,b;P)|\le E_b e^{-\delta_NM d_t(X)}$ ... $e^{2\Phi_t(P)}=\frac{\det\mathsf A(P_0)}{\det\mathsf A(P)}\prod_{c}(\det m_c(\mathbf1)/\det m_c(V))^2$ ... $\Phi_t(P)=\log Z_k[P]-\log Z_k[P_0]$." So the proposition itself is stated relative to the trivial background P_0.
2. **The trivial-background value is localised in its proof.** L40737-40755: for $b\in(Y_N^-)^+$, "$f_b(Y;P)=3\log c_N-\sum_{n\ge1}\frac1n\operatorname{tr}T_Y^n(b,b)$ converges normally and has modulus at most $F_N=3|\log c_N|+3\log(1/(1-q_N))$", with $T_Y=1-c_N^{-1}A_{Y,N}$, $\|T_Y\|\le q_N<1$ (spectrum of the compressed form in $[\gamma/2,B_a]$); and "$E^N(X;P,b)=\sum_{S_N(b)\subset Y\subset X}(-1)^{\#X-\#Y}f_b(Y;P|_Y)$" (Moebius inversion over coarse regions). These are defined at every P, **including P_0**.
3. **The vacuum family** (L60813-60846, Subsection "The constants of one step"): "$\mathsf n^{(j)}(X,b)=-\frac12E^N(X;P_0,b)$ for $b\in\mathfrak X^+$, $S_N(b)\subset X$; $6\log L$ for $b=b_0(c)$, $X=X(c)$; 0 otherwise", and "The proof of the normalizer gives $\mathsf n^{(j)}(X,z)\in\mathbb R$, $|\mathsf n^{(j)}(X,z)|\le E_Ne^{-\delta_NMd_j(X)}$." The Haar/averaging constants are the three **extensive coefficients** (II-192-10, L60870-60875): $\mathsf{co}^{\rm b}_j=\log\sigma_{\rm H}-\frac32y_j$, $\mathsf{co}^{\rm s}_j=-(L^3-1)\log\mathsf z(x_j,\varepsilon_j)$, $\mathsf{co}^{\rm i}_j=\frac32\log(2\pi)$, multiplied by lattice counts (II-97-4).
4. **Use on two tori.** Proposition `III-7-12` (Step 3 part 1 above) then treats $\mathsf{vn}^{(j)}=\mathsf n^{(j)}$ exactly as it treats the effective-action terms: equal on common (non-wrapping) lifts by the local-chart identity, exponentially small on non-common domains. **No separate determinant lemma is needed in 3D**, because the Gaussian normaliser is never treated as a torus-wide number there.

**Reading for the 4D account.** CA-II L141426-141432 calls the Gaussian normaliser "the one torus-wide number per level" and excludes it. YM3_I shows that, in Sussman and Alpoge's own 3D construction, the logarithm of the step's Gaussian integral at the trivial background is not torus-wide in the harmful sense: it is (counting term with torus-free coefficients) + (sum of local terms with exponential decay in d_j(X)), by a convergent log-series of a gapped positive form plus Moebius inversion. The 4D analogue of items 2-3 is what a "determinant lemma" with the asserted K-free constant would have to supply. Whether the 4D Balaban step has the inputs (spectral gap of the compressed form on every deep subregion, uniform in the level; local charts) is not settled by this reading; that is Step 4.

## Step 3 (part 3). The new 4D manuscript YM4_1400 (post-31a47) (01:20Z)

Source: `YM4/YM4_1400.tex` at HEAD c7fef8b (added after 31a47c543775, in commits af49e75..d07b5b7, 2026-11-09; Sussman and Alpoge). Grep over the new YM4 files (outside `Old/`): `tori\b|vacuum constant|per unit volume|exactly extensive|counting term|torus-wide`. No new YM4 file uses the phrase "determinant lemma" (Step 3.1).

1. **A two-torus vacuum-density criterion, stated as a conditional** (L102525-102580, paragraph "A local companion criterion for vacuum-density compatibility"): "Suppose the vacuum constant has the form $E_{\ell,K}=\sum_{j=0}^K[(\ell/a_j)^4c_{j,K}+\sum_{z}\sum_{D\in\mathcal D_{\ell,j}(z)}v_{\ell,j}(D,z)]$. The numbers $c_{j,K}$, the coupling sequence and every auxiliary choice are the same for all $\ell$. There is a translation-covariant infinite companion $v_{\infty,j}$ ... $|v_{\ell,j}(D,z)|,|v_{\infty,j}(D,z)|\le C_Ee^{-\kappa_E m}$ with $\kappa_E>\kappa_D$ ... Assume that rooted domains with $m<\ell/(C_0a_j)$ correspond bijectively to companion domains, with equal energy values." Conclusion (ET9-ET10): $|\ell^{-4}E_{\ell,K}-A_K|\le C\sum_{j}a_j^{-4}e^{-c\ell/a_j}\le C_{\ell_0}e^{-c\ell/2}$, "independently of $K$", and "two compatible tori obey the same bound with $2C_{\ell_0}e^{-c\min(\ell,\ell')/2}$". It adds (L102576-102580): "If the coupling sequence or local normalizer numbers differ between tori, or if nonwrapping compatibility has not been established for the actual formation rule, \eqref{...ET9} has not been proved for that construction."
2. **Its application to "the actual vacuum constants"** (L102645-102671): "$E_{\ell,K}=\sum_{j<K}[\mathsf E^{(j)}_{\mathrm I}+\sum_y\sum_{X\ni y}E^{(j+1)}(X,\mathbf1,y)+\sum_XR^{(j+1)}(X,\mathbf1)]$. In $\mathsf E^{(j)}_{\mathrm I}$, the Haar and Gaussian factor is one scalar per nonpivot bond and the gauge-fixing factor is one scalar per cell of the next lattice. The common coupling sequence and fixed choice of gauges give the same two scalars for the two tori, and both counts per unit volume are the same. ... Thus the common companion comparison applies to the vacuum constant in the sourced construction." Bound: $|E_{\ell,K}/\ell^4-E_{\ell_\star,K}/\ell_\star^4|\le C\sum_{u\ge0}L^{4u}e^{-c\ell_\star L^u/M}$.

**Reading.** Here the 4D vacuum constant is written with **no** torus-wide Gaussian normaliser: the "Gaussian factor" in E_I is a per-bond scalar (as YM3's $\mathsf{co}^{\rm i}_j=\frac32\log(2\pi)$), so the logarithm of the determinant of the step's quadratic form at the trivial background must sit inside the local terms $E^{(j+1)}(X,\mathbf1,y)$ or be absent. The passage asserts the decomposition; whether YM4_1400 proves that the log-determinant at $U=\mathbf1$ is localised (the 4D analogue of YM3_I `II-44-37` with its trivial-background value) is checked next (YM4_1400 L86260 "Vacuum constants and the interfaces used later", L86380, L86766).
