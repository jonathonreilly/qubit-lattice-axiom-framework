# Released-source POST: selected original-mark energy power

The released author formula agrees with the sealed PRE for the declared compact vacuum and one-excitation inputs at each fixed even cubic side `L>=16`. The original instrument, occupied-B electric masks, all matter sectors of `H4`, gain, anticommutator and harmonic Haar fiber are retained. I find no coefficient or fixed-L limit correction needed. The author's additional finite plaquette certificate is exact; it gives the stated all-volume positive limiting vacuum baseline and hard-low-band bounds. Those additional implications were checked after release and are not discoveries attributed to my blind PRE.

There is one domain precision issue to resolve in presentation. The declared smooth packets support the energy derivative through the stronger electric-moment argument in PRE. The opening reference to arbitrary `psi in D(D)` should not be justified merely by saying that finite matter/field moves preserve a degenerate electric domain. The proposed restriction to these smooth packets is sufficient. This issue does **not** supply a counterexample to the fixed-packet theorem, nor even to well-definedness of the initial form for this particular original B: a separate monotone-occupancy argument below shows why this B preserves `D(D)`.

This is a scoped conditional comparison. It applies no audit verdict, changes no source, and supplies no microscopic initial-derivative, total-flux, reservoir heat, absorption or empirical claim.

## 1. Exact sources, provenance and coverage

The unchanged blind report is `PRE.md`, SHA256 `be47d27ab25dbf1853331b1bb8f02a2b67b3cc93c244b4a830fa86b810c71216`, under `PRE_SEAL.json`, SHA256 `a1cc8dc5b9af73952b55402902076e1b7b28b7bc7bbc2de4834c65dd8297031d`. All 65 PRE members, including initial code versions, the side-six correction and the failed first evidence-verifier run, remain unchanged.

The only new author packet read is `selected-mark-power-personal`, frozen under `post_sources/author/`. Its report is `ORIGINAL_SELECTED_MARK_ENERGY_POWER_ROOT.md`, SHA256 `dc34643135d5b31b627420ba6bc325b7d5b5dbf9095e6801d25b26d1dd8c66c6`; its `AUTHOR_SEAL.json` is `b0378a615fdaaca99e563a78e4e1361a19635976e114e2f04f5e5485ceb8a69c`, with 18 members. `POST_SOURCE_PINS.json` identifies all frozen bytes and the ten unchanged live origins reused from PRE. The three main scientific parents retain their authorized hashes at refreshed main `b47a67e3a08febd2aaf3545eae9a278b4901a72d`; exact git-byte checks are recorded by the final verifier. No changed scientific parent has been silently substituted.

I read the complete author note and all three programs, the complete certificate, source metadata, three execution receipts and author-review record. I parsed and compared every one of the 606 serialized words and 528 pair rows for the two signs, every one of the 67 coefficient rows, all 32 filling rows, and all 18 Fourier rows. The large polynomial output was checked in full against my earlier independent result rather than treated as read from a truncated display. The author-review record is author-reported process evidence, not another independent scientific check.

The author discloses prior geometry/algebra and Fourier-argument reuse in its metadata. I did not follow those references into other active packets. The released programs are self-contained, and none was imported or executed. My new `post_check.py` reads their JSON as data, compares it to the independent PRE coefficient, and checks the new certificate by a separately written A-to-B plaquette-walk construction. No author optimizer is run and no optimizer tolerance or optimality result is used.

## 2. Normalization, primitive and full-Hamiltonian correspondence

The author uses `v=sqrt(2) J_- phi`, represented by two coefficients `+1,-1`. My PRE uses the same unnormalized primitive pair, but stores **twice** the magnetic polynomial. In the author convention,

`C(A)=Q_j(A)=sum_(u<v) [-||S_uv Bv||^2 + Re <S_uv B*Bv,S_uv v>]`.

The factor `1/2` from the input normalization cancels the `-2` in `H4=-2 sum S_uv* S_uv`. In particular the anticommutator is the real form involving `B*Bv`; it is not the unselected input energy multiplied by the event probability. The author outward, inward, creation and adjoint shifts have the original exponents `-q,+q,sigma,-sigma`. Its matter matching retains equal-output interference. The selected signs give identical polynomials, matching the PRE's stronger fixed-g sign argument for this exact preparation.

After exact centering and orientation conversion, all 303 coefficients for each sign equal both my side-16 result and my infinite-local-lift result, divided by two. All 264 local pair rows per sign have the same term counts and zero-field values as PRE. Exactly 202 pairs contribute nonzero local polynomials. The ambient side-16 graph has 18432 unordered overlapping pairs, but disjoint terms cancel from the selected adjoint dissipator exactly; they are not numerically neglected.

The author constant `2794`, coefficient sum `0`, absolute coefficient sum `6700` and maximal word length `8` all follow from the complete coefficient comparison. Every word has zero divergence, conjugate pairing and zero winding. Its looser bound `length<=10` is harmless. The radius-five primitive patch embeds in every stated `L>=16` torus without additional local identifications. Thus the local coefficient applies at every such L and all words survive the harmonic Haar average. This would not justify silently using it on side six: the preserved PRE explicitly found a different side-six coefficient after the correct Haar projection.

The author's positive-axis plaquette `c_p` is my `ell`, after changing edge orientation, with **no overall sign difference**. Its vector `t` equals my `r` on all 67 edges. The check independently rebuilds the Hessian from the full author polynomial in A-to-B coordinates and verifies all 7396 matrix entries on its 86-edge support:

`H=-sum_z C_z z z^T = ell r^T+r ell^T`,

`#nonzero H entries=520, ell^T H ell=49600, ell.r=6200`.

Consequently `C(A)=(ell.A)(r.A)+O(|A|^4)`. This is the same quadratic coefficient independently obtained from the five-word first-jet calculation in PRE, not a new fit to the author Fourier table.

With `tau=tau_*`, both reports therefore give

`P_0^lim = kappa/(4 tau) C_pt`,

`P_alpha^lim-P_0^lim = kappa/(2 tau) Re(conj(chi_p) chi_t)`,

where `d_z=Omega_L^(-1/2)z/sqrt(2)`, `chi_z=sum alpha_r d_zr`, and `C_pt=<d_p,d_t>`. The root tables express power in units `kappa/(4 tau)`; the PRE's displayed power tables use `kappa/tau`. The root side-16 covariance `1245.3524037745194` divided by four agrees with PRE `311.33810094362974` to rounding. Treating the two table conventions as equal would create a spurious factor-four discrepancy.

## 3. Electric masks, domain and the fixed-packet limit

The correct electric term is

`D(q,E)=sum_(x in A,y~x) 1_(q_y=0) E_xy(E_xy-q_x)`.

Each integer summand is nonnegative, but occupied B sites remove complete incident directions. Thus `D(D)` is not interchangeable with the domain of `N_E=1+sum E_e^2`. For example, in a physical matter word with the two B vertices of an elementary loop occupied, adding arbitrary integer circulation around that loop changes no included electric summand. A square-summable tail in that circulation may be in `D(D)` while lacking the corresponding `N_E` moment. Finite Wilson translation at fixed matter and a finite operation that changes those masks are distinct domain questions.

For the exact packets used here, no such ambiguity affects the theorem. The normalized compact transverse vacuum and finite one-excitation wavefunctions are smooth, have all electric moments, and are constant in the harmonic angles. Fixed Gauss strings and all finite shift sums in B, H4 and the loss operators preserve every `N_E` graph norm. The diagonal `K D` commutes with `N_E`. The interaction-picture bounded-perturbation/Dyson construction consequently preserves weighted trace spaces at fixed g; choosing one extra electric moment allows the derivative paired with `h_g`. This is the differentiability argument already supplied in PRE. It gives the actual selected contribution

`kappa [<B psi,h_g B psi>-Re <B psi,B h_g psi>]`

for the declared inputs, rather than merely assigning a formal quadratic expression to a generator. It uses no lower coercive estimate of D by `N_E`.

A separate observation prevents overstating the domain criticism. Consider one legal term of the **original** `B=P j_(a,b,sigma) F_a P`. It moves the original charge `q_a` from a to a vacant neighbor z, then creates at a,b. For a nonzero term, z and b are distinct and were both vacant. They are both occupied in the output, so the only shifted edges `(a,z)` and `(a,b)` are excluded from the output D. No previously occupied B site becomes vacant. On surviving summands only `q_a` may change to sigma. For integer E and q,sigma in `{+1,-1}`,

`E(E-sigma) <= 2 E(E-q)+2`.

If q=sigma, this follows from `E(E-q)>=0`. For `(q,sigma)=(1,-1)` the gap is `(E-1)(E-2)`; for `(-1,1)` it is `(E+1)(E+2)`. Both are nonnegative on the integers. Hence pathwise

`D_output <= 2 D_input+12`.

Each legal path is a bounded partial isometry with a fixed electric translation, so this bound shows that it maps `D(D)` into `D(D)` with controlled graph norm; the finite sum B does too. Thus the initial form is well defined for `psi in D(D)` for this particular B. This specific argument is absent from the root's short generic domain sentence. I do not infer that arbitrary finite matter moves or every intermediate adjoint operator preserves `D(D)`. The limited public precision repair proposed by root—state the declared all-`N_E` packets and the weighted derivative argument—is sufficient without importing a larger generic-domain theorem.

For those packets the exact output has a fixed unitary factor times `(W_p-1) phi_g/sqrt(2)`. Its norm is `O(g)`, its first electric derivatives are `O(1)`, and the input satisfies `||D psi_g||=O(g^-2)`. The first-derivative form gives

`<B psi_g,D B psi_g>=O(1)`;

the anticommutator is bounded by `||B psi_g|| ||B|| ||D psi_g||=O(g^-1)`. Multiplying by `K=g^2/(2 tau)` yields electric gain `O(g^2)` and anticommutator `O(g)`, so both vanish. The retained masks only remove derivative terms; bounded matter coefficients and fixed string derivatives cause no stronger divergence. Neither proof replaces D by the empty-B form after the mark.

The finite contractible Laurent expansion, evenness and compact Gaussian moments give an `O(g^4)` expectation remainder for C, hence `O(g^2)` after multiplication by `delta=1/(4 tau g^2)`. Cutoff errors remain exponentially small after these fixed inverse powers. Combining with the electric bound proves the common fixed-L limit and a safe `O(g)` remainder for the fixed packet. Constants may depend on L and the chosen packet. Neither trace-norm convergence nor a generic `O(g^2)` vector approximation alone transfers this unbounded energy derivative.

## 4. Independent exact check of the released plaquette filling

This section is a **POST-only verification of a newly released author construction**. My PRE had a rigorous coarse side-16 sign check but did not contain the following all-volume certificate.

Starting from my already sealed A-to-B r, `post_check.py` walks the four oriented sides of every supplied elementary face and sums its supplied integer coefficient. It verifies

`r-1550 ell = sum_(32 faces) b_q c_q`,

`sum |b_q|=646`.

All 525 link equations on the complete 375-face trial patch agree exactly in rational arithmetic. The result file records every one of the 32 faces and its separately generated four-edge boundary. Changing the first coefficient by one produces four nonzero residual edges, so the exact equality test detects an altered certificate. No optimization is performed or needed. The entire certificate lies in a fixed local patch and embeds in every L under consideration.

Translation and cubic symmetry of the reference `Omega_L` imply

`||d_q||^2=||d_p||^2=v_p`

for every elementary face, including those with different orientations. These are symmetries of the reference covariance; no symmetry of the charged full Hamiltonian is being assumed. Cauchy–Schwarz gives `|<d_p,d_q>|<=v_p`, and therefore

`|C_pt-1550 v_p|<=646 v_p`,

`904 v_p<=C_pt<=2196 v_p`.

The elementary plaquette is transverse and has zero harmonic component and squared Euclidean norm four. On the transverse space the cubic curl-square eigenvalues are at most 12, so `||Omega_L||<=sqrt(12)`. It follows that

`v_p=(1/2)<c_p,Omega_L^-1 c_p> >= 4/(2 sqrt(12))=1/sqrt(3)`.

For every fixed even `L>=16`,

`P_0^lim >= (226/sqrt(3)) kappa/tau >0`.

The constant is uniform across this family of **fixed-L limits**. This is not a uniform convergence theorem in g and L and does not permit a new joint limit. It concerns a supplied charged preparation of the reference vacuum, not a ground state of the full charged H and not an isolated system energy balance.

For the normalized unrestricted bright preparation `alpha=d_p/sqrt(v_p)`, the one-excitation covariance increment is `2 C_pt`. Thus the excess power is twice the reference vacuum power and the total is three times it. This agrees with the three author rows at epsilon 3.5, which cover the whole reference spectrum because `sqrt(12)<3.5`. It does not contradict PRE's proof that the **arbitrary-packet added-power quadratic form is indefinite**: that proof permits other normalized packets with negative excess and does not assert a negative vacuum baseline.

## 5. Independent derivation of the hard-low-band bound

Use centered integer momenta n with components in `[-L/2,L/2]`, taking one representative of each periodic momentum, and write `k=2 pi n/L`. For nonzero momentum,

`Omega(n)=2 sqrt(sum_mu sin^2(pi n_mu/L)) >= 4 ||n||_2/L`,

by `sin(theta)>=2 theta/pi` on `[0,pi/2]`. If `0<Omega<=epsilon<=2` is nonempty, `L epsilon>=4`. Every contributing coordinate satisfies `|n_mu|<=L epsilon/4`. Consequently the number of contributing momenta is at most

`(2 floor(L epsilon/4)+1)^3 <= 27 L^3 epsilon^3/64`.

Allowing the zero momentum and any duplicated boundary representatives only loosens this upper bound. Empty bands contribute zero; no normalized one-excitation packet can be supported in an empty band.

For the unit xy plaquette, its normalized Fourier edge-vector has squared norm

`[4 sin^2(k_x/2)+4 sin^2(k_y/2)]/L^3 <= Omega(n)^2/L^3`.

It is transverse, and this vector norm already sums the two physical transverse polarizations. There is no further factor of two. The covariance weight per momentum is at most `Omega/(2 L^3)<=epsilon/(2 L^3)`. Hence the spectral projection onto the hard band gives

`v_(p,epsilon) <= 27 epsilon^4/128`.

Cubic symmetry and translation commute with this spectral projection. Thus every face in the exact filling has the same restricted norm as p. For a normalized alpha supported in this band,

`|chi_p|<=sqrt(v_(p,epsilon))`,

`|chi_t|<=2196 sqrt(v_(p,epsilon))`.

Combining these with the already proved power formula yields exactly

`|P_alpha^lim-P_0^lim| <= kappa/(4 tau) (2196*27/64) epsilon^4`,

`|P_alpha^lim-P_0^lim|/P_0^lim <= (2196/904)(27 sqrt(3)/64) epsilon^4`.

The author's constants are therefore valid without importing its earlier private Fourier argument. My bounded numerical control uses L16 only and separately forms the Fourier edge-vector. Across epsilon `.1,.2,.4,.7,1,2`, it checks empty/nonempty bands, the momentum enclosure, plaquette transversality, the per-momentum norm bound and equality of the restricted norms of all 32 certificate faces within floating roundoff. The maximum displayed face-norm difference is `2.78e-17`, and the transversality residual is `2.23e-16` or less. These floats are diagnostics, not the proof or interval enclosures.

The theorem requires a **hard spectral-support bound** on the initial reference packet. A mean-frequency ceiling is weaker; uncontrolled high-frequency tails cannot be assigned this epsilon-four suppression. The result does not make the band invariant under charged dynamics or produce a finite-g optical-scale error estimate. The epsilon 3.5 author rows are unrestricted bright controls, outside the stated `epsilon<=2` low-band theorem. The finite-g remainder was not shown uniform in shrinking epsilon, so no joint g/epsilon inference is added.

## 6. Author runtime correspondence and independent evidence limits

All 18 author members plus its seal agree with their frozen copies and the released hashes. All three receipt code hashes match the corresponding programs. Every stdout file is byte-identical to its named result JSON, and all three stderr files are empty. The spectral result names the exact polynomial-result hash; the filling result names the exact spectral-result hash. The root's code/prose/table relationships are consistent.

The recorded execution durations are `1.2106947919819504`, `0.4916321251075715` and `1.0414613340981305` seconds. Their internal calculation durations are respectively `1.1766735408455133`, `0.3904643750283867` and `0.014264250174164772` seconds. These are retained author records. The first two receipts bind code and exit/time but do not themselves name stdout bytes; that binding is supplied by the unchanged author seal and exact stdout/result equality. I neither reran nor restamped them.

All 18 Fourier rows were read. Stored totals equal baseline plus excess; reported mean frequencies lie within their specified bands; the low-band rows satisfy the analytic bounds; and the unrestricted bright rows have twice-baseline excess and three-times-baseline total. L16 agrees with the independently sealed PRE Fourier result. L32 and L64 are inspected author finite sums, not newly independently reproduced sums. The spectral output's historical “electric proof pending” wording is explicitly preserved: the later sealed note supplies that proof, and no old run has been rewritten to imply it already did so.

The new independent checker completed once with exit zero and empty stderr. Its complete code, stdout, result and execution receipt are retained. No author program, large parent control, unrelated source or active checker packet was run or read. The exact result comparison, filling check and analytic estimates establish correspondence within the stated scope; additional rows or a success label do not change provenance.

## 7. Preserved PRE contributions and surviving boundaries

The following remain identifiable PRE contributions rather than new author-result reproductions: the separately written five-word first-jet derivation of all 67 coefficients; the indefinite arbitrary-one-excitation added-power form; explicit full gain and anticommutator limits with their extensive cancellation; exact side-six winding and local-pair corrections; the all-electric-moment differentiability argument; and the warning that bare finite-spin `j_S P=0` gives zero initial selected microscopic power. Those facts prevent conflating this effective fixed-L initial power with conditional born energy or interchanging a microscopic limit with a time derivative.

The new all-volume filling/positivity and low-band proof survive the scoped POST check. The only proposed presentation repair concerns making the sufficient smooth-packet domain and derivative justification explicit; no numerical coefficient or stated packet limit needs repair. A generic extension beyond those packets would need its own full domain/evolution statement, not an appeal to finite-dimensional matter alone.

The original formation law and supplied charged preparation are maintained. Neither the PRE nor this POST shows that the dynamics selects or transports that preparation, sums all channel powers, supplies an energy-conserving reservoir realization, or models ideal photon absorption. No publication, audit status, axiom or existing evidence file has been changed.
