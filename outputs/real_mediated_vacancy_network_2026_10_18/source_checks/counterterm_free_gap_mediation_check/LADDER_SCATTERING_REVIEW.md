> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# Distinct check of the positive ladder stationary solution

**Disposition: SUPPORT the exact stationary two-port result; no required correction found.** The stated positive coefficients give nonsingular elimination and zero reflection in both old-X sectors at k=π/2, with t_+=−(3+4i)/5 and t_−=−(3−4i)/5 in the declared port convention. Their ratio is the literal W relative phase. This is an on-shell scattering statement, not a normalized packet, launched finite device, released gate or halt theorem.

## 1. Source, dependencies and exposure

The complete frozen source is N/counterterm_free_gap_mediation/LADDER_SCATTERING_REDUCTION.md, SHA256 `4f22fdb84d7636a6caad536323e5f02f971fba04a22ae9e8292e3c4e234929cc`, where N is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`. I waited for the actual author freeze notice, then read the complete source and checked its hash. Reported formulas before that freeze were treated as design exposure, not evidence.

The geometry/decision source `d1e9fc151e85d3d525b06b066402dc0d4b0822aa3d7479a6e8171c260887a417` and its review `daa480ebe3188437eb04a5a3a748f3f499290885696db0d6f4737682d56d8236` were just read/checked. The compensated primitive source `de29d04e85e5479ef4c35969f079bd5727f846c59ba6225f79fc81405c7cf86e`, review `88169175decc90a4f706ea3a1168ae54bf763e5a0cb5d3cb516b749fd65b9066`, and exact mediator source `37e2cf2c776d6425c93b113b92bc114b8e478db779d1dc6f0d28cc33a925ca34`, review `80c09db471dea4542ccfe9b236b91ccd2cd285502ce4b091d59cbcfbfa7e1e70`, are reused at their unchanged finite-interface scopes. They do not prove scattering or justify an infinite-volume physical approximation.

ROOT proposed the ladder route; the author supplied the symmetric construction. I have shared campaign/design exposure and did not author this source. This is distinct same-model source-exposed analytical reconstruction, not blind, retained-audit, native-realization or publication certification. No coefficient scan or numerical confirmation was used.

## 2. Actual graph and positive diagonal bookkeeping

The six vertices and seven edges agree with the previously checked two-plaquette geometry. Ports L=a_- and R=b_+ have disjoint outward lead rays. The old and mediator sites are distinct; unlisted geometrically neighboring pairs carry no implicit interaction. The controlled edge A–B contributes only hopping −p in the compensated one-head target. It has no ordinary parallel edge and supplies no unlisted Laplacian diagonal.

For an ordinary weight q, the positive exchange block has one-head diagonal q at each endpoint and off-diagonal −q. Its full norm is 2q. The unit lead attachment gives port diagonal one and hopping −1; lead interior diagonal is two. Including all supplied onsite values therefore gives exactly

    dL=q1+q2+1+ηL−E, dR=q5+q6+1+ηR−E,
    dv=q1+q3+ηv−E, dw=q4+q6+ηw−E,
    dA=q2+q4+ηA−E, dB=q3+q5+ηB−E.

In particular dA and dB have not received a fictional +1 from the controlled sign edge. The physical repulsion/mediator/compensation inventory is separate from this effective one-head operator. It is not asserted that the five-qubit physical approximation extends to infinitely many lead qubits with a finite global norm budget.

## 3. Full Schur reconstruction

At energy with dv,dw≠0, elimination gives

    v=(q1 L+q3 B)/dv,
    w=(q4 A+q6 R)/dw.

It subtracts q1²/dv and q6²/dw from the port diagonals, q4²/dw and q3²/dv from A and B respectively, and creates hoppings −f from L to B and −h from A to R, where f=q1q3/dv, h=q4q6/dw. The remaining internal matrix and coupling vectors are

    M=[α −p; −p β],
    α=dA−q4²/dw, β=dB−q3²/dv,
    k_L=(q2,f), k_R=(h,q5).

Its determinant is D=αβ−1, and its inverse is D⁻¹[β p; p α]. Consequently the port Schur matrix has diagonals l0−k_L M⁻¹ k_Lᵀ and r0−k_R M⁻¹ k_Rᵀ, and off-diagonal −k_L M⁻¹ k_Rᵀ. Expanding these products gives all three formulas (1) in the source, with the stated signs of the p cross terms. The total internal determinant is dv dw D. This verifies the elimination rather than assuming an effective two-port matrix with desired entries.

## 4. Lead phase convention and reflectionless criterion

With coordinate n increasing outward, e^(−ikn) is incoming because dE/dk=2sin k>0, whereas e^(ikn) is outgoing. Thus the left port and first lead-neighbor values are 1+r and e^(−ik)+r e^(ik); on the right they are t and t e^(ik). Inserting these into the two port equations gives exactly

    ell(1+r)−h t−e^(−ik)−r e^(ik)=0,
    −h(1+r)+(rho−e^(ik))t=0.

At r=0 the second equation gives t=h/(rho−e^(ik)). The outgoing denominator cannot vanish for real rho and 0<k<π. Substitution into the first yields h²=(ell−e^(−ik))(rho−e^(ik)). Since ell,rho,h are real, the imaginary part is sin k·(rho−ell), so reflectionlessness requires ell=rho. Writing A=ell−cos k and y=sin k then gives h²=A²+y² and t=h/(A−iy). No extra propagation phase is inserted between the reference planes at the ports.

The left and right lead dispersions and contact weights are identical, so their flux velocities are equal. Therefore |t|=1 at r=0 is already unit transmission in flux normalization; no omitted velocity factor changes the phase ratio. At the center k=π/2 both velocities equal two.

## 5. Positive coefficients and exact center solution

Under q1=q6=a, q2=q5=b, q3=q4=c and matching onsite pairs, the actual Schur data obey dv=dw=d, f=h=ac/d, α=β=z and l0=r0. Direct substitution gives the two formulas (5) in the source. At z=l0=0, D=−1, these become

    ell_p=rho_p=2pbf,
    h_p=−p(b²+f²).

The center transparency equation is then (b²+f²)²−(2bf)²=1, equivalently (b²−f²)²=1. With f=1/√8, a=c=f/2 and b=3f, it holds exactly.

All six edge coefficients are positive. The smallest onsite coefficient is ηL=ηR=1−5f/2>0, since 5f/2=5/(4√2)<1. The other onsite values 2−5f/2 and 2−3f/4 are also positive. At E=2 the actual positive-block sums give

    dL=dR=f,
    dv=dw=f/4,
    dA=dB=f.

Then ac/d=f, c²/d=a²/d=f, so z=l0=0 exactly. The internal determinant dv dw D is −f²/16≠0. This tests the target values using the installed positive diagonals rather than treating them as independent freely flattened variables.

Since f²=1/8, the final port data are

    ell_p=rho_p=3p/4,
    h_p=−5p/4.

Thus h_p²=25/16=(3p/4)²+1 and both sectors are reflectionless. The transmission formula gives

    t_+=(-5/4)/(3/4−i)=−(3+4i)/5,
    t_-=(5/4)/(−3/4−i)=−(3−4i)/5.                (R1)

The outgoing two-port linear system is nonsingular as well: its determinant is (ell_p−i)²−h_p²=−2−2i ell_p, nonzero. For example the internal amplitudes can be reconstructed without any pole from port values L=1,R=t_p:

    A=−p(f+b t_p), B=−p(b+f t_p),
    v=2(1+B), w=2(A+t_p).

These formulas are finite and satisfy the sequentially eliminated internal equations. They verify regular matching at the center; no bound-state or global completeness conclusion is inferred from this local regularity.

## 6. Full on-shell sector phase and scope of coherence

Since (3+4i)/5=e^(iθ), equation (R1) gives t_+=−e^(iθ), t_-=−e^(−iθ). Therefore

    t_+/t_-=e^(2iθ),
    t_p=−e^(−iθ)w_p,
    w_+=e^(2iθ), w_-=1.

This retains the common scalar −e^(−iθ) exactly. Inversion of the graph exchanges L↔R, v↔w and A↔B and leaves all listed coefficients and the controlled edge invariant. The identical lead conventions therefore give zero right reflection and the same reverse transmission. Equivalently, reciprocity and that inversion give the full two-port matrix S_p=t_p X_ports at the center. Its unitarity follows directly from |t_p|=1 and X_ports unitary, consistent with lossless real matching.

Taking the orthogonal old-X direct sum gives the stationary channel-amplitude operation −e^(−iθ)W⊗X_ports and its passive extensions. This is coherent in old inputs; it is not a classical selection of p. It is also an on-shell scattering-fiber statement. Plane waves are not normalized states of the full infinite lead Hilbert space, so this does not by itself furnish a complete finite-time isometry, a normalizable common output profile or an error bound for wave packets. The source explicitly keeps those obligations open.

## 7. Inventory and unresolved transfer

The six core exchange weights sum to 2(a+b+c)=8f, so their full-norm sum is 16f. The six onsite coefficients sum to

    2(1−5f/2)+2(2−5f/2)+2(2−3f/4)
       =10−23f/2.

Thus the core background norm is bounded by their total 10+9f/2 as stated. This is a full-space triangle bound, not a restricted one-head norm. The core background has twelve listed positive blocks.

With M_I,M_O additional finite lead vertices, there are L=6+M_I+M_O clocks and q=12+M_I+M_O background blocks before endpoint repairs. Each finite chain contributes one bond per new vertex including attachment. The compensated primitive inventory then has L+3 qubits and L+4+q blocks. These counts are conditional inventory accounting only: a finite chain endpoint has different degree/diagonal from an infinite interior, and no source-launch or boundary repair was silently included.

The positive effective core solution removes the earlier missing center-energy algebraic solution. It does not settle a useful bandwidth, explicit derivative bounds, normalized packet construction, real product endpoint launch, localized amplitudes, finite cuts or a return-free output interval. Continuity suggests a nonsingular neighborhood from the nonzero denominators, but no quantitative packet budget follows without deriving its size and the maps' derivatives. Such a proof must preserve the relative sector phase/profile, not merely both transmission probabilities.

Any finite physical composition must also pay the actual network norm and horizon in the compensated-link approximation, including r(L−2). The stationary common phase is additional to the retained old elapsed K, physical scalar and effective mediator evolution. The infinite leads used for this scattering calculation do not authorize applying a finite-global-norm physical bound to an infinite apparatus.

## 8. Actual verification

I reconstructed the actual Schur complement, lead convention, nonsingular center matching, positive diagonal sums, exact amplitudes and phase ratio, full two-port normalization, core norm bound and finite inventory counts analytically. No coefficient scan, optimizer, numerical eigensolver, scientific executable, external search, delegation or model override was used. The full frozen source was read and hashed, and this report was read back completely.

Only LADDER_SCATTERING_REVIEW.md was written. Sources, earlier reports, Git, canonical/checkpoint files and editable prompts remain unchanged. This is scoped stationary mathematical evidence, not a finite launched/released gate, native supplier, capture, reset or permanent halt theorem, and not retained certification or an instruction to publish.
