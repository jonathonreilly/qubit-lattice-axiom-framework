lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T16:52Z

# Check of row 1215 (`library/gap-solve23-astra62.md`), queue row 1221

Started 2026-11-20T04:52Z (date -u). Checker: Claude Opus 5.5, max effort, Mac mini Claude worker 2. The author of row 1215 is gpt-6.2-astra (another provider), so this check is cross-provider. Source checked: `library/gap-solve23-astra62.md` at commit 9be3e60ef (489 lines). Everything is checked by hand; no numeric run is a proof step here.

Verdict scale per statement: HOLDS, HOLDS AFTER CORRECTION, FAILS, each with the line of the source.

## Plan (at most eight steps)

1. Read the source in full; list its statements with line numbers and labels; read the cited earlier rows.
2. Check the coalescence of the periodic neutral levels at fixed spatial size.
3. Check the twisted neutral gap limit 4 arsinh sin(pi/(2n)).
4. Check the gapless comparison trajectory (14)-(15).
5. Check the monopole and low-energy weight bounds (26)-(29).
6. Check everything else, in source order.
7. Restatement search: grep `library/open-core.md` and the FINISH rows for each positive claim; read the cited earlier statements where a step depends on them.
8. Verdict table and RESULT line.

## Step results

(written step by step below)

### Step 1. Inventory of the source (done 2026-11-20)

The source has 489 lines. Its labelled statements, by line, with the equation each one asserts:

| Lines | Label in source | Content |
|---|---|---|
| 17-24 | PROVED | definitions (1): \(V_\eta\), \(M_\eta\), \(C_\beta\), \(F_{\beta,\eta}\); twist \(\eta_p=-1\) on the 12-faces at \(x_1=x_2=n-1\) |
| 26 | PROVED | gauge projection; flips commute with \(F\); Perron uniqueness; \(F\ge0\) |
| 28-40 | PROVED | (2) norm of the Gaussian kernel \(K_D\) |
| 42-61 | PROVED | (3) \(\lim_\beta\lambda_0=\max_{\rm flat}L(D_A)\): lower bound 50, localization 52-57, patch bounds 59-61 |
| 67-88 | PROVED | (4) evaluation; flat classification 80; curl symbol 82; \(S_n(\theta)>S_n(0)\) 84-88 |
| 90-96 | PROVED | (5) coalescence of periodic neutral levels at fixed \(n\) |
| 100-106 | PROVED | twisted sector: eigenvalues on \(\mathcal H_+\) converge to the Gaussian on \(L^2(N)^{H_A}\) |
| 108-114 | PROVED | (6) twisted neutral gap \(\to 2\mu_n=4\operatorname{arsinh}\sin(\pi/(2n))\) |
| 118-145 | PROVED | (7) \(\lim_\beta\mathcal E_m=c_m/n+O(n^{-3})\) |
| 147-159 | PROVED | (8) twisted neutral trace; multiplicity 20; \(t=\lfloor sn\rfloor\) limit; numbers at \(s=1/512,1/2\) |
| 165-211 | PROVED | factorization at fixed periodic \(n\): vacuum concentration 167, (9), (10), (11), moments 209-211 |
| 213-231 | PROVED | (12) plaquette covariance; (13) vanishing low-energy weight of one plaquette |
| 235-265 | PROVED | (14) comparison trajectory; (15) \(h^8C_u(h)\to\frac{3}{2\pi^4}(\int u)^2\) |
| 269-315 | PROVED | (16)-(19) joint range \(\beta\ge n^{32}\) |
| 317-329 | PROVED, given row 1145 | (20) vague limit of level counts |
| 333-354 | PROVED | (21) many large plaquette angles; failure of a global flat patch; converse given row 1211 (6) |
| 356 | ARGUED | infrared consequence |
| 358-371 | PROVED, given row 1211 (6) | (22) geometry of exceptional faces |
| 375-390 | PROVED | (23) vacuum response; \(0\le\mathcal E_m\le2bn\); pointwise sign counterexample |
| 392-417 | PROVED | (24)-(25) response formula; free-endpoint check |
| 423-435 | PROVED | (26) two-sign bound \(p_\beta=c_\varepsilon e^{-(E_*+\varepsilon)\beta}\) |
| 437-445 | PROVED | (27) sign Fourier coefficients; monopole count |
| 447-451 | PROVED, conditional in identification | one-loop slope \(b_*=11/(3\pi^2)\), \(b_*E_*<1\) |
| 453-470 | PROVED | (28) joint sign law; (29) vanishing low-energy weight; joint with straight transports |
| 472-474 | PROVED | monopole current size; reflection test |
| 478-485 | PROVED | (30) response gives the spectral edge |
| 487-489 | OPEN, RESULT | |

Earlier rows the source cites, with files: 1143 `gap-solve-astra62` (charged trial states, rectangle filling §1); 1145 `gap-solve2-astra62` ((1)-(3) straight holonomies, (5), (11)), its check 1146 `gap-solve2-check-opus`; 1149 `gap-solve4-astra62`; 1155 `gap-solve7-astra62` ((9), (20)-(22), coupling conversion); 1175 `gap-solve16-astra62` (change of time axis, selector); 1177 `gap-solve17-astra62`; 1211 `gap-solve22-astra62` ((6), (10), (18)-(20)); 1051 `gap-direction3-max` (Lemma K4); 678 `gap-ac-lat` (Lemma G); 898 `gap-next3-max` (C4).

The four positive claims named by row 1221 are (5) (lines 90-96), (6) (lines 100-114), (14)-(15) (lines 235-265) and (26)-(29) (lines 423-466). Each rests on lines 17-88 ((1)-(4)), so those are checked with them.

### Step 2. Foundations (1)-(4) and the periodic coalescence (5)

**(1), line 17-24. HOLDS.** \(C_\beta\) is convolution by a symmetric class-function probability density, so \(\|C_\beta\|=1\). \(F=M_\eta C_\beta M_\eta\) is the Osterwalder-Seiler/Lüscher transfer in temporal gauge with \(I_\beta^{|\mathcal E|}\) removed.

**Line 26. HOLDS.** \(V_\eta\) is gauge invariant (the signs are fixed and plaquettes transform by conjugation). The electric density is a class function, so \(C_\beta\) commutes with gauges. A flip of all \(i\)-edges crossing one cut changes each \(i\)-plaquette by \((-1)^2\) and each \(X_eY_e^{-1}\) by \((-1)^2\). The Perron argument is correct: \(F(X,Y)>0\) everywhere, \(\langle|f|,F|f|\rangle>\langle f,Ff\rangle\) for a real \(f\) of both signs, and the eigen-equation makes a nonnegative maximizer positive. \(F\ge0\): \(e^{\beta\operatorname{Re}g}=\sum_k\beta^k(\chi_{1/2}/2)^k/k!\) has nonnegative spin coefficients \(c_j\), and convolution by \(\chi_j\) is \(d_j^{-1}\) times the spin-\(j\) isotypic projection.

**(2), line 28-40. HOLDS.** In singular coordinates the kernel factorizes. For \(s=\sigma^2>0\) with \(A=1+s/2=\cosh\omega\), \(b=\sinh\omega\): the \(y\)-exponent is \(-\tfrac12(A+b)y^2+xy\), so \(e^{-by^2/2}\mapsto(A+b)^{-1/2}e^{-(A-1/(A+b))x^2/2}\) and \(A-1/(A+b)=b\) since \(A^2-b^2=1\). Eigenvalue \(e^{-\omega/2}\); the positive eigenfunction gives the Schur upper bound. \(\cosh\omega=1+s/2\) is \(\omega=2\operatorname{arsinh}(\sqrt s/2)\). At \(s=0\) the norm is \(\sup e^{-k^2/2}=1\). Tensor norms multiply for positive operators.

**(3), line 42-61. HOLDS.** Checked: \(I_\beta=(2\pi^2)^{-1}4\pi\int_0^\pi\sin^2u\,e^{-\beta(1-\cos u)}du=(2/\pi)\sqrt{\pi/2}\,\beta^{-3/2}(1+o(1))=(2\pi^2)^{-1}(2\pi/\beta)^{3/2}(1+o(1))\). Lower bound: \(\beta(1-\operatorname{Re}(e^{a}e^{-b}))=\beta(1-\cos\operatorname{dist}(e^a,e^b))\) with \(\operatorname{dist}=|a-b|(1+O(|a|^2+|b|^2))\); \(K_D\ge0\), so the sup of its Rayleigh quotient over a dense set is its norm. Upper bound: the IMS identity \(\sum_j\chi_j(X)F(X,Y)\chi_j(Y)=F(X,Y)(1-\tfrac12\sum_j|\chi_j(X)-\chi_j(Y)|^2)\) is exact; the normalized \(\chi_j\) are \(C_n/r\)-Lipschitz with \(C_n\) overlap, so the error kernel has Schur bound \(C_nr^{-2}\cdot O_n(\beta^{-1})=O_n(\beta^{-1/3})\). On a patch, \(|e|\le C_n\sqrt\beta r^2=C_n\beta^{-1/6}\); the cosine and chart-metric errors are relative \(O(r^2)\). The dilation gives the factor \(c_\beta^{-d/2}\to1\) at fixed \(d\). Centers with \(\beta V\le(\log\beta)^2\) accumulate only at flats, and \(L\) is continuous in \(D\).

**(4), line 67-88. HOLDS.** Flat classification: in the open-cube tree gauge, faces crossing one seam make the \(n^2\) wrapping \(i\)-links equal to one \(h_i\). The corner face at \((n-1,n-1,x_3)\) is \(h_1h_2h_1^{-1}h_2^{-1}\), so \(\eta_p=-1\) gives \(h_1h_2=-h_2h_1\). Conjugacy to the negative forces zero trace; anticommuting imaginary units are orthogonal (\(uv+vu=-2u\cdot v\)); \(h_3\) is central. Linearization: the variation of \(U_1U_2U_3^{-1}U_4^{-1}\) at a flat is \(v_1+\operatorname{Ad}(U_1)v_2-\operatorname{Ad}(U_1U_2U_3^{-1})v_3-v_4\), the covariant curl. On a mode \(e^{iq\cdot x}\) it is \(v\mapsto w\wedge v\), \(w_j=e^{iq_j}-1\), and \(|w\wedge v|^2=|w|^2|v|^2-|\langle w,v\rangle|^2\), so the squared singular values are \(\ell(q),\ell(q),0\). Count: \(3\) colors \(\times n^3\) modes \(\times3=9n^3=d\). Twisted adjoint phases: \(\operatorname{Ad}i=\operatorname{diag}(1,-1,-1)\), \(\operatorname{Ad}j=\operatorname{diag}(-1,1,-1)\) on \((i,j,k)\) give \(\pi e_2,\pi e_1,\pi(e_1+e_2)\). Strict inequality: \(\omega'(s)=1/\sqrt{s(s+4)}\) is correct; \(s^{-1/2}=\int_0^\infty e^{-ts}(\pi t)^{-1/2}dt\); \(c(t)\to1\) as \(t\to0\) and \(c(t)\sim(4\pi t)^{-1/2}\) as \(t\to\infty\), so \(\int(1-e^{-ts})c(t)dt/t\) converges. The Poisson identity \(\sum_ke^{-t\ell((2\pi k+\theta)/n)}=n^3\sum_zp_t(nz)e^{i\theta\cdot z}\) is correct, and \(p_t(x)>0\) from \(e^{-6t}\exp(t\sum_j2\cos q_j)\). So \(S_n(\theta)+S_n(-\theta)+S_n(0)>3S_n(0)\) unless \(\theta\equiv0\), and the periodic maximum is at the eight central triples.

**(5), line 90-96. HOLDS.** Checked: flats \((e^{\phi_k\tau},1,1)\) with distinct small \(\phi_k>0\) have distinct gauge-and-flip orbits; \(L(D_A)\) is continuous in \(A\); \(K\)-invariant open \(\delta\)-neighborhoods \(U_k\) of the compact orbits have closures at positive distance (the product metric is \(K\)-invariant). The compression \(\mathbf 1_{U_k}F\mathbf 1_{U_k}\) has a kernel positive on all of \(U_k\times U_k\), so its top function is unique, positive, hence \(K\)-invariant (in \(\mathcal H_+\)); connectedness of \(U_k\) is not needed. Its top is bounded below by non-invariant packets near \(A_k\), which is legitimate because the top on \(L^2(U_k)\) equals the top on \(L^2(U_k)^K\). Cross terms: some edge has \(\operatorname{dist}(X_e,Y_e)\ge\delta_0/\sqrt{|\mathcal E|}\), so the kernel is \(\le I_\beta^{-|\mathcal E|}e^{-c\beta}\). Min-max on the \((j+1)\)-dimensional span gives \(\liminf\lambda^0_{j,+}\ge e^{-3S_n(0)}-\epsilon\). With \(\lambda^0_{j,+}\le\lambda^0_0\to e^{-3S_n(0)}\), (5) follows, and the excited trace at fixed \(t\) is at least \(J-o(1)\) for every \(J\). This is the lattice form of the flat abelian (toron) valley at fixed volume (Lüscher 1983; van Baal); the statement is only the weak-coupling limit at fixed \(n\), and it is correctly stated as such.

No earlier row is used in (1)-(5). The citations of row 1051 (Lemma K4), row 678 (Lemma G) and the Sussman-Alpoge outline at lines 26 and 65 are credit only; the source re-derives each step it uses.

### Step 3. The twisted sector: lines 100-159, (6), (7), (8)

**Lines 100-106 (eigenvalue convergence on \(L^2(N)^{H_A}\)). HOLDS.** Checked: the flat set is \(O=KA\) (the flip in direction 3 maps \(h_3=1\) to \(-1\); flips 1, 2 are absorbed by conjugation with \(j\), \(i\)). So \(O\) has two connected components, which the proof's "exponentially suppressed off a chart" step covers. All twisted phases are nonzero, so no mode has \(q\equiv0\): the gradient is injective, \(\ker D_A=T_AO\), \(g=3n^3\). Stabilizer: a gauge fixing the open-cube links is constant; \(gh_ig^{-1}=\epsilon_ih_i\) with \((h_i)=(i,j,1)\) gives \(g\in Q_8=\{\pm1,\pm i,\pm j,\pm k\}\) and \(\epsilon_3=+1\). The element \((g,\epsilon)\in H_A\) acts on left variations by \(v\mapsto\operatorname{Ad}(g)v\) (the flip leaves \(v\) unchanged). Normalization, checked: \((\beta/2\pi)^{d/2}\cdot\beta^{-(d-g)/2}\cdot\beta^{-g/2}\cdot(2\pi)^{g/2}=(2\pi)^{-(d-g)/2}\). The orbit displacement \(u\) is tangent and \(\xi,\zeta\in N\), so \(|\xi-\zeta-u|^2=|\xi-\zeta|^2+|u|^2\). For invariant \(f(k\exp_Av)=\tilde f(v)\), \(\|f\|^2=\operatorname{vol}(O)\int|\tilde f|^2j\,dv\) and the same factor appears in the form, so it cancels. \(L(D_A|_N)=L(D_A)\) because zero singular values contribute \(\omega(0)=0\) to (2).

**(6), line 108-114. HOLDS.** The one-dimensional Markov kernel \(k(x,y)\varphi(y)/(\lambda\varphi(x))\) has \(y\)-exponent \(-\tfrac12(A+b)y^2+xy\), so mean \(e^{-\omega}x\), variance \(e^{-\omega}\), stationary variance \(e^{-\omega}/(1-e^{-2\omega})=1/(2\sinh\omega)\), eigenvalues \(e^{-j\omega}\) with Hermite eigenvectors. \(H_A/\{\pm1\}\cong\mathbb Z_2^2\) acts on the colors \(i,j,k\) by \(\operatorname{Ad}i=\operatorname{diag}(1,-1,-1)\), \(\operatorname{Ad}j=\operatorname{diag}(-1,1,-1)\): the three distinct nontrivial characters, with \(\chi_k=\chi_i\chi_j\). A Hermite product with color occupations \((N_i,N_j,N_k)\) transforms by \(\chi_i^{N_i+N_k}\chi_j^{N_j+N_k}\), so it is invariant iff \(N_i\equiv N_j\equiv N_k\pmod 2\). Invariant excitations: some \(N_c\ge2\) (cost \(\ge2\omega_{\min}\)) or all \(N_c\) odd (cost \(\ge3\omega_{\min}\)). The minimum of \(\ell\) over the shifted grids is \(4\sin^2(\pi/(2n))\), at \(q=\pm(\pi/n)e_2\) for color \(i\) and \(\pm(\pi/n)e_1\) for color \(j\); color \(k\) has \(\ell\ge8\sin^2(\pi/(2n))\). So \(\omega_{\min}=2\operatorname{arsinh}\sin(\pi/(2n))=\mu_n\), and the neutral gap tends to \(2\mu_n=4\operatorname{arsinh}\sin(\pi/(2n))\). This is the lattice form of the known perturbative statement that a zero-electric-flux state in a twisted box needs two gluons (van Baal, cited in the source). Scope, stated correctly in the source: \(\beta\to\infty\) at fixed \(n\), lattice time units.

**(7), line 118-145. HOLDS.** \(\omega'(s)\sim s^{-1/2}\) and \(f(q)=|q|(1+O(|q|^2))\) with a smooth polar structure. The radial Fourier integral \((2\pi)^{-3}\int g(|q|)e^{-iv\cdot q}dq=(2\pi^2|v|)^{-1}\int_0^\infty g(\rho)\rho\sin(|v|\rho)d\rho\) is correct. Three integrations by parts of \(G=\rho^2\chi\): \(\int G\sin(k\rho)=-G''(0)/k^3-k^{-3}\int G'''\cos(k\rho)=-2/k^3+O(k^{-\infty})\). So \(\widehat f(v)=-1/(\pi^2|v|^4)+O(|v|^{-6})\), which agrees with the distribution transform \(\int_{\mathbb R^3}|q|e^{-iv\cdot q}dq=-8\pi/|v|^4\) divided by \((2\pi)^3\). The dyadic remainder bound with \(N=7\) sums to \(O(|v|^{-6})\). Poisson summation: \(S_n(\theta)=n^3\sum_z\widehat f(nz)e^{i\theta\cdot z}\), absolutely convergent. The numerator count: for \((z_1,z_2)\) = (odd, even), (even, odd), (odd, odd) the three terms \(1-\cos\) sum to \(2+0+2\), \(0+2+2\), \(2+2+0\); for (even, even) to 0. So (7) holds with the stated \(c_m\in(0,\infty)\). Also \(n\cdot4\operatorname{arsinh}\sin(\pi/(2n))\to2\pi\).

**(8), line 147-157. HOLDS.** \(\operatorname{Tr}_{\rm inv}=|G|^{-1}\sum_{g\in G}\operatorname{Tr}(g\,\cdot)\) with \(G=\mathbb Z_2^2\); the four elements have color signs \((\epsilon_1,\epsilon_2,\epsilon_3)\) with \(\epsilon_1\epsilon_2\epsilon_3=1\); each real oscillator gives \((1-\epsilon e^{-t\omega})^{-1}\), and two transverse polarizations per momentum give the exponent \(-2\) (real dimension \(2n^3\) per color, as counted in Step 2). Trace convergence for integer \(t\ge2\): the orbit-integrated kernel is dominated by \(C_ne^{-c_n(|\xi|^2+|\zeta|^2)}\), so Hilbert-Schmidt convergence follows by dominated convergence; the exterior part has HS norm \(O(\beta^{d/2}e^{-c\beta})\) against \(\lambda_0^m\to L(D_A)>0\); a product of two HS-convergent factors converges in trace norm.

**Line 159. HOLDS.** Multiplicity 20: per color \(i\) (and \(j\)) the minimal momenta \(\pm(\pi/n)e_2\) carry two transverse polarizations, four real coordinates; degree-two monomials in four variables number \(\binom52=10\); a mixed \(i\)-\(j\) pair has character \(\chi_k\ne1\); nothing else reaches \(2\mu_n\). The \(t=\lfloor sn\rfloor\) limit: \(f(q)\ge c\,|q|\) on the centered zone (\(\sin(x/2)\ge x/\pi\) and \(\operatorname{arsinh}(u)/u\ge\operatorname{arsinh}(\sqrt3)/\sqrt3\) on \([0,\sqrt3]\)), so dominated convergence applies; \(|2\pi k+\theta_\alpha|\ge\pi\) for twisted colors. The lower bound \(\liminf\ge20e^{-2\pi s}\) needs only the 20 states and \(\lfloor sn\rfloor\cdot2\mu_n\to2\pi s\). Numbers: \(20e^{-2\pi/512}\approx19.8>1/2\) and \(20e^{-\pi}\approx0.86>1/1650\). The thresholds \(1/2\) and \(1/1650\) are the "strict seed" margins of rows 1163-1177 (e.g. row 1163, `gap-solve10-astra62.md` (23); row 1165, `gap-solve11-astra62.md` line 64); the remark is correct in the stated order of limits (\(\beta\to\infty\) first).
