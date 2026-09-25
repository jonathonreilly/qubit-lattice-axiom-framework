# Blind PRE: original formation and a sum of Wilson-quadrature responses

For the full common matter/rotor law, the sum of the two normalized plaquette-quadrature impulse slopes is exactly a vacancy observable. Summing over elementary coordinate plaquettes on the even cubic torus gives
\[
\mathcal S(t)=48K\bigl(|V|-\langle N\rangle_t\bigr),\qquad
\mathcal S(s)-\mathcal S(t)=96K\,\mathbb E\,C_{[s,t]}.
\]
Here \(C_{[s,t]}\) is the actual number of original formation marks in that time interval of the unperturbed common-law evolution. The response is a derivative at zero lag, evaluated on the genuinely evolved preparation at time t. It is not a stationary spectral sum or a closed wave equation.

The derivative exists for every normal initial density, without an electric moment hypothesis. This follows from a bounded strong limit of the response commutator, proved below; it does not follow by differentiating an unbounded energy expectation. No microscopic derivative transfer is asserted.

There is a geometric qualification at \(L=4\). Elementary plaquettes and all simple graph four-cycles are different sets. If the latter are summed, the coefficients at \(L=4\) are \(60K\) per vacancy and \(120K\) per birth. Both conventions are made explicit; no elementary plaquette or winding contribution is silently counted twice.

## 1. Sources, supplied premises and independence

Only the following three complete science notes were read, at the exact indicated contents of main revision 60c5f194d940a7bbaf1cdd545296e31d74a02f1a:

| Note stem, all with _BOUNDED_THEOREM_NOTE_2026-09-24.md suffix | SHA256 |
|---|---|
| LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT | c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b |
| LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS | 7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a |
| FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES | 2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516 |

Live bytes were compared with these exact Git objects and copied into sources/. Previously fully read instructions and the physics-claim-reviewer skill are reused at unchanged hashes, recorded in the source manifest. Prior common-law and microscopic work is disclosed historical context. No other research packet was reopened, no author candidate was disclosed, and no historical scientific program was imported or executed.

Fix an equal even cubic torus of side \(L\ge4\), with its simple nearest-neighbor graph. Let \(A\) and \(B\) be the bipartition, \(n=|A|=|B|=L^3/2\). Orient links from A to B. The physical common P Hilbert space has \(q_a=\pm1\) on A, \(q_b=0,\pm1\) on B, integer link fields, and
\[
\operatorname{div}E=q-1_A .
\]
It retains all permitted colors, charges, fluxes and winding configurations. No flat-field or postbirth projection is made.

Write \(v_b=1-n_b\), \(N=nI+\sum_{b\in B}n_b\), and use exactly the supplied common generator
\[
\mathcal L\rho=-i[h,\rho]
+\sum_\mu\left(L_\mu\rho L_\mu^*
-\tfrac12\{L_\mu^*L_\mu,\rho\}\right),
\]
\[
h=KD+\delta H_4,\qquad
D=\sum_{a\to b}v_b E_{ab}(E_{ab}-q_a),\qquad
H_4=-2\sum_{\substack{a<c\\a,c\ {\rm share}\ B}}S_{ac}^*S_{ac}.
\]
Here \(S_{ac}=F_cF_aP\), \(L_{e,\sigma}=\sqrt\kappa\,Pj_{e,\sigma}F_aP\), and \(K,\delta,\kappa>0\) are fixed. The original alternative is the stipulated unnormalized coherent sum of the two signs on the same edge. All its channels are retained. No coherent sum across different edges, new reservoir or altered normalization is supplied.

The parents give self-adjoint h on the multiplication domain of D, bounded \(H_4,L_\mu\) at this fixed graph, and a trace-preserving completely positive semigroup \(\mathcal T_t\) on trace class. They also give, for every normal density and without electric moments,
\[
\langle N\rangle_t-\langle N\rangle_s
=2\int_s^t\operatorname{Tr}(\Gamma\rho_r)\,dr,\qquad
\Gamma=\sum_\mu L_\mu^*L_\mu,\quad \rho_r=\mathcal T_r\rho_0. \tag{1}
\]
Only the finite-graph portions of the sources are used. Their infinite-volume hypotheses and unlisted volume theorem are not imported.

## 2. What is being perturbed and measured

An elementary plaquette means the coordinate square
\(x,x+\hat\mu,x+\hat\mu+\hat\nu,x+\hat\nu\), for one unordered pair
\(\mu<\nu\) and each base vertex x. These are \(3L^3\) distinct unoriented coordinate plaquettes for \(L\ge4\). Choose either orientation once. Its integer circulation \(\nu_p\) has four coefficients \(\pm1\) and zero divergence. The Wilson unitary shifts
\[
W_p|q,E\rangle=|q,E+\nu_p\rangle.
\]
It is unitary on the entire physical rotor P space. Define the normalized Hermitian quadratures
\[
X_p=\frac{W_p+W_p^*}{2},\qquad
Y_p=\frac{W_p-W_p^*}{2i}.
\]
They commute and satisfy \(X_p^2+Y_p^2=I\), with norms at most one.

At preparation time \(t\ge0\), the baseline state is the actual full state
\(\rho_t=\mathcal T_t\rho_0\). To define a response, give that state the bounded unitary kick \(e^{i\theta Q_\beta}\), where \(Q_X=X_p,Q_Y=Y_p\), and evolve for a further lag \(u\ge0\) under the same full generator. The sign convention is an external Hamiltonian impulse \(-\theta Q_\beta\delta(\text{time}-t)\), in the model's \(\hbar=1\) convention. Define
\[
\chi_{\alpha\leftarrow\beta}(t,u)
=\left.\frac{d}{d\theta}\right|_{\theta=0}
\operatorname{Tr}\!\left[
Q_\alpha\mathcal T_u
\bigl(e^{i\theta Q_\beta}\rho_t e^{-i\theta Q_\beta}\bigr)
\right].
\]
The kick is a mathematical probe of the supplied dynamics. It is not asserted to be an implemented photon source or laboratory coupling.

Because \(Q_\beta\) is bounded, the derivative exists in trace norm for every normal \(\rho_t\), and
\[
\chi_{\alpha\leftarrow\beta}(t,u)
=i\operatorname{Tr}\rho_t[
\mathcal T_u^*(Q_\alpha),Q_\beta],\qquad
\chi_{\alpha\leftarrow\beta}(t,0)=0. \tag{2}
\]
The lag-slope matrix is
\[
\mathsf R_{\alpha\beta}^{(p)}(t)
=\lim_{u\downarrow0}\frac{\chi_{\alpha\leftarrow\beta}(t,u)}u. \tag{3}
\]
The pulse derivative in (2) is taken first. Reversing the Hamiltonian-pulse sign reverses this response sign. Scaling either kick or readout multiplies the corresponding response by that scale; using the unnormalized \(W+W^*\) and \((W-W^*)/i\) for both doubles each quadrature and multiplies all displayed slope sums by four.

## 3. Wilson commutation and the exact core calculation

Every rotor shift commutes with every other rotor shift. A Wilson loop is field-only and therefore also commutes with each matter operator and vacancy gate. It follows on the full physical space, including intermediate primitive outputs, that W commutes with \(F_a,F_a^*,j_\mu,j_\mu^*\), and hence with \(H_4,L_\mu,L_\mu^*\). Thus
\[
i\delta[H_4,Q_\alpha]=0,\qquad
\sum_\mu\left(L_\mu^*Q_\alpha L_\mu
-\tfrac12\{L_\mu^*L_\mu,Q_\alpha\}\right)=0. \tag{4}
\]
This does not say that the complete later response is free: subsequent generator actions on the electric commutator need not commute with the magnetic and jump terms.

The finite-support physical basis span is invariant under D, W and the quadrature polynomials. It is a common core for the following algebra. Put
\[
A_p=\sum_{e\in p}v_{b(e)}\nu_{p,e}^2
=2(v_{b_1}+v_{b_2}),\qquad 0\le A_p\le4I, \tag{5}
\]
where \(b_1,b_2\) are the two B corners of the plaquette. These matter gates commute with W. The exact finite-difference identity is
\[
W_p^*DW_p+W_pDW_p^*-2D=2A_p. \tag{6}
\]
All linear charge terms cancel. In particular, replacing the gated electric term by \(\sum E^2\) after births would incorrectly replace \(A_p\) by \(4I\).

Expanding the nested commutators gives bounded operators:
\[
[X_p,[KD,X_p]]=2K A_pY_p^2,\qquad
[Y_p,[KD,Y_p]]=2K A_pX_p^2,
\]
\[
[Y_p,[KD,X_p]]=[X_p,[KD,Y_p]]
=-2K A_pX_pY_p. \tag{7}
\]
For a scalar angle representation these are the products of the derivatives of cosine and sine, but no gauge fixing or angle-fiber decomposition is needed for their operator proof.

The formal response-slope matrix is therefore
\[
\mathsf R^{(p)}(t)
=2K\,\operatorname{Tr}\rho_t A_p
\begin{pmatrix}
Y_p^2&-X_pY_p\\
-X_pY_p&X_p^2
\end{pmatrix}. \tag{8}
\]
Here the trace applies entrywise to the displayed operator matrix. Each real quadratic form in its two indices is the expectation of
\(2KA_p(aY_p-bX_p)^2\), so the matrix is positive semidefinite. Both diagonal self-responses are nonnegative. Their sum is
\[
\mathsf R_{XX}^{(p)}(t)+\mathsf R_{YY}^{(p)}(t)
=2K\langle A_p\rangle_t
=4K\langle v_{b_1}+v_{b_2}\rangle_t. \tag{9}
\]
Individual entries retain field coherence, while their sum does not. None of these identities requires a diagonal density, zero winding, a prescribed matter word or translation invariance.

## 4. Why the lag derivative needs no electric moment

Using only the formal first derivative of \(\mathcal T_u^*Q\) would be insufficient: \([D,Q]\) is generally unbounded. The bounded nested commutator alone also would not justify exchanging limits. Here a direct bounded-commutator argument completes that step.

Let \(\mathcal U_u(A)=e^{iuKD}Ae^{-iuKD}\). For \(\varepsilon=\pm1\), define on the diagonal physical basis
\[
f_\varepsilon(q,E)=D(q,E+\varepsilon\nu_p)-D(q,E).
\]
It is a real diagonal multiplier, possibly unbounded, and
\[
f_\varepsilon(q,E+\tau\nu_p)
-f_\varepsilon(q,E)=2\varepsilon\tau A_p(q),
\qquad \tau=\pm1.
\]
The unitary-conjugation commutator is exactly
\[
[\mathcal U_u(W_p^\varepsilon),W_p^\tau]
=W_p^{\varepsilon+\tau}e^{iuKf_\varepsilon}
\bigl(e^{2iuK\varepsilon\tau A_p}-I\bigr). \tag{10}
\]
Consequently its norm is at most \(2K\|A_p\||u|\). Dividing by u gives uniformly bounded operators. Since \(e^{iuKf_\varepsilon}\to I\) strongly, the quotient has a strong limit. Combining the four shift terms for the quadratures proves
\[
\frac{i}{u}[\mathcal U_u(Q_\alpha),Q_\beta]
\ \longrightarrow\ [Q_\beta,[KD,Q_\alpha]]
\quad\hbox{strongly}, \tag{11}
\]
with norms at most \(2K\|A_p\|\le8K\).

It remains to retain the full actual generator. Write
\[
\mathcal L^*=\mathcal L_D^*+\mathcal V,\qquad
\mathcal L_D^*A=iK[D,A],
\]
where
\[
\mathcal V A=i\delta[H_4,A]
+\sum_\mu\left(L_\mu^*AL_\mu-\tfrac12\{L_\mu^*L_\mu,A\}\right).
\]
At fixed graph \(\mathcal V\) is a bounded normal map, strongly continuous on bounded sets, since it is a finite sum of left and right multiplications by bounded operators. One may take
\(M=2\delta\|H_4\|+2\sum_\mu\|L_\mu\|^2\) as a bound on its norm. Equation (4) gives \(\mathcal VQ_\alpha=0\).

The bounded-perturbation Dyson construction underlying the parent's common semigroup gives the dual Duhamel identity, interpreted in the strong operator topology,
\[
\mathcal T_u^*Q_\alpha-\mathcal U_uQ_\alpha
=\int_0^u
\mathcal U_{u-r}\bigl(\mathcal V\mathcal T_r^*Q_\alpha\bigr)\,dr. \tag{12}
\]
The left side has norm at most \(uM\), since \(\mathcal T_r^*\) is unital and contractive. It is strongly continuous at zero: unitary conjugation is strongly continuous and the remainder is \(O(u)\) in norm. Thus
\(\mathcal V\mathcal T_r^*Q_\alpha\to\mathcal VQ_\alpha=0\) strongly as \(r\downarrow0\). The integrands are uniformly bounded; conjugation by \(e^{i(u-r)KD}\) does not change their limit on a fixed vector as \(0\le r\le u\downarrow0\). Dividing (12) by u therefore gives a bounded family tending strongly to zero.

Its commutator with \(Q_\beta\) also tends strongly to zero. Combining with (11),
\[
\frac{i}{u}[\mathcal T_u^*Q_\alpha,Q_\beta]
\ \longrightarrow\ [Q_\beta,[KD,Q_\alpha]]
\quad\hbox{strongly},\qquad
\left\|\frac{i}{u}[\mathcal T_u^*Q_\alpha,Q_\beta]\right\|
\le 8K+2M. \tag{13}
\]
Uniformly bounded strong convergence pairs with every trace-class density. This proves (3) and (8) for every normal \(\rho_t\), even when its D expectation is infinite. The proof never differentiates its mean energy or assumes \(\rho_t\) belongs to the trace-class generator domain.

For a fixed initial density and fixed preparation-time interval \([0,T]\), the lag limit also pairs uniformly with \(\{\rho_t:0\le t\le T\}\): this orbit is trace-norm compact, and a finite-net argument uses the uniform operator bound in (13). There is no operator-norm convergence assertion in (11) or (13), no uniform lag remainder over all densities, and no volume-uniform bound on M.

## 5. Summation and actual finite-time birth counts

Each vertex of the simple cubic torus belongs to twelve elementary coordinate plaquettes: four choices for each of three coordinate planes. Every plaquette has two B corners. Hence summing the bounded operator on the right of (9) gives
\[
\widehat{\mathcal S}
=\sum_{p\ {\rm elementary}}2KA_p
=48K\sum_{b\in B}v_b
=48K(|V|I-N). \tag{14}
\]
Equivalently each edge is in four plaquettes, every B has six edges, and the electric second difference contributes \(2K\) per vacant-edge incidence. Both counts give the same 48.

Define \(\mathcal S(t)\) as the sum of the two diagonal response slopes in (9), evaluated at the actual preparation time t. Equations (1) and (14) imply, for every \(0\le s\le t<\infty\),
\[
\boxed{\quad
\mathcal S(s)-\mathcal S(t)
=96K\int_s^t\operatorname{Tr}(\Gamma\rho_r)\,dr
=96K\,\mathbb E C_{[s,t]} .
\quad} \tag{15}
\]
The last equality is the original finite-graph labeled jump instrument's counting identity. Its bounded channels yield a nonexplosive count process, and the parent's bounded number balance applies with all channels included. Resolved and stipulated coherent-per-edge instruments obey the same equation, each with its own actual evolution and count law.

Equivalently, on the bounded number observable,
\[
\mathcal L^*\widehat{\mathcal S}=-96K\Gamma.
\]
Since \(\Gamma\) is bounded and \(\rho_t\) is trace-norm continuous,
\[
\mathcal S'(t)=-96K\operatorname{Tr}(\Gamma\rho_t).
\tag{16}
\]
This derivative is with respect to preparation time. It is distinct from the initial lag derivative used to define each response.

The response sum is nonincreasing and nonnegative. Equation (15) yields exactly the known capacity bound
\[
\mathbb E C_{[0,t]}\le
\frac{\mathcal S(0)}{96K}
=\frac{|V|-\langle N\rangle_0}{2}.
\]
It does not imply that this bound is attained, that \(\mathcal S(t)\) tends to zero, or that the instantaneous birth rate has a pointwise limit. For all B initially empty, \(\mathcal S(0)=48Kn=24KL^3\), independently of the initial field state.

The counts in (15) belong to the unperturbed baseline evolution \(\rho_t\). The impulse is used to diagnose response at that baseline state. This equation is not a law for a system subjected to repeated finite driving pulses or feedback.

## 6. The \(L=4\) geometry distinction

The general-graph magnetic parent sums all simple unoriented four-cycles when it expresses the initial-sector magnetic Hamiltonian. For \(L\ge6\), these are precisely the elementary coordinate plaquettes. For \(L=4\), there are also \(3L^2=48\) straight length-four loops winding around a periodic coordinate direction. They are physical Wilson unitaries on the full winding space but are not elementary coordinate squares.

The full common Hamiltonian in this PRE includes these extra contributions through the unchanged pair formula. They commute with every elementary \(W_p\), so none was omitted from the evolution in Sections 3–5.

If the response sum is instead defined over **all** simple graph four-cycles at \(L=4\), each B belongs to three additional cycles. Each extra cycle has two B vertices and has the same local second-difference calculation. Therefore
\[
\widehat{\mathcal S}_{\rm all\,4}=60K(|V|I-N),\qquad
\mathcal S_{\rm all\,4}(s)-\mathcal S_{\rm all\,4}(t)
=120K\,\mathbb E C_{[s,t]} \quad (L=4). \tag{17}
\]
This convention contains 240 loops at L=4, rather than 192 elementary plaquettes. The exact primitive geometry control independently enumerates them via the two A vertices and their two common B neighbors, and verifies that the 48 extras are exactly the straight winding loops. A length-four closed lift can acquire a nonzero periodic displacement at \(L=4\) only by taking all four steps along one axis, which also proves the classification. For \(L\ge6\), a length-four lift cannot wind.

## 7. Counterexample to identifying nonzero response with activity

The positive value of \(\mathcal S\) does not force a positive instantaneous or future formation rate. This is a concrete statement about the same supplied finite model.

For any even \(L\ge4\), leave just the two B sites \((1,0,0)\) and \((3,2,2)\) vacant. Their torus graph distance is six. Put all A charges at plus and assign half the occupied B sites each sign. This is possible because \(n-2\) is even. The total charge minus the A background is zero; a spanning-tree integer flow supplies a physical electric basis word.

Every original birth needs two vacant B neighbors of one A, which these vacancies do not supply. Every retained \(S_{ac}\) requires two vacant B destinations whose distance is at most four, which they also do not supply. Thus all jumps and all magnetic pair terms annihilate every field word of this fixed charge pattern. A basis density is stationary under the remaining diagonal KD. Nevertheless
\[
\mathcal S(t)=96K>0,\qquad
\operatorname{Tr}(\Gamma\rho_t)=0,\qquad
\mathbb E C_{[s,t]}=0.
\]
This uses the finite-graph annihilation mechanism already supplied in the formation parent, with an explicit two-vacancy choice. It does not classify stationary states or claim accessibility from the all-B-empty preparation.

The summed response tracks vacancy capacity. Its decrease records formation. Individual plaquettes or individual quadratures need not decrease monotonically, because the full Hamiltonian redistributes matter and changes field coherences. A nonzero response sum is not a photon number, a positive absorption probability or evidence of a propagating photon mode.

## 8. Limits, failed routes and evidence

The result is a conditional common-law theorem. It retains the supplied compensation, Hamiltonian, tensor hard-core algebra and original mark choices. It establishes neither native physical selection nor an empirical match.

The order is fixed finite graph and fixed positive couplings; form the supplied common law under its parent resource limit if a microscopic interpretation is desired; then define the bounded kick derivative and the zero-lag response in that common law. Trace-density convergence at fixed positive times does not license interchanging the microscopic resource limit with this lag derivative. Finite-spin Wilson shifts are also not exact unitaries at their boundaries, so their quadrature-square identity cannot be imported without a separate estimate. No microscopic derivative theorem, joint volume/resource limit, field-only postbirth limit or physical clock identification is asserted.

A stationary response spectrum would need a stationary preparation, appropriate time-correlation hypotheses and a specified Fourier convention. Equation (15) concerns a zero-lag slope at possibly nonstationary preparation times. It does not provide such a spectrum, a damped-wave closure, a response bandwidth, photon decay or survival probability, source-to-detector propagation, or a photodetection calibration.

Three tempting routes are explicitly not used:

- Differentiating \(\operatorname{Tr}\rho[D,Q]\) for arbitrary normal \(\rho\). This is not justified without domain information; the bounded strong-commutator proof resolves the response derivative instead.
- Dropping vacancy gates or treating the postbirth field as if every B stayed empty. This loses the exact count relation.
- Identifying all graph four-cycles with coordinate plaquettes at L=4. The separate 60/120 coefficients preserve that distinction.

The independent response_primitive_control.py uses only exact Gaussian rational coefficients and integer physical paths. It checks three torus geometries, 21 core double-commutator groups, 63 real/imaginary field-coherence groups, 21 original resolved/coherent primitive and loss-balance groups, and seven total-response/number groups. Charge patterns include occupied and vacant B sites, negative A charges, nonzero electric flow and an added winding-three circulation. Core XX, YY and XY identities and matrix positivity are exact in these finite controls.

The first complete run succeeded. A second run added only the explicit L=4 all-four-cycle classification; its source diff and complete first evidence remain preserved. All earlier scientific entries are unchanged. No failed scientific execution occurred, no tolerance was loosened, and no author or historical program was run. The controls do not approximate the infinite rotor dynamics or prove the strong-limit argument by truncation.

The final control source SHA256 is 5566c18b555cb96ca73604a73a6eb1ea8de9d937ef7e8e59cacf184ace782f62. Its actual final execution took 0.5590087911114097 seconds, exit zero, empty stderr, and retained 24796 stdout bytes. All 115 scientific result groups were read, including every initial result row and the exact-equality check plus complete added geometry rows on the final run. Full source, both executions, logs, immutable source pins and a read-only evidence verifier accompany the PRE seal.
