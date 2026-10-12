# VERDICT: CONFIRMED WITH CORRECTIONS

The first-order completion, the gapped-edge floor, the light-literal-edge failure, and the one-mass removal of birefringence survive adversarial checking. The fixed campaign reading does not: TESTS.md explicitly requires a **second-order** Ward-complete pair stress, whereas the class used for the floor is only W1-complete. The correct FIXED reading is therefore **OPEN without pairing and OPEN with pairing**. The other material corrections are that W0 proves only that the axial TT blocks are empty under the two-point contracted Ward identity (not literally every possible higher identity), B2's no-go is conditional on W2 meaning the standard undeformed Dirac--Schwinger/HDA closure, the positive literal-edge floor is only established over the tested mass range, and the paired dD-M residue is $2\kappa_{\rm lat}m^2J_2$, not $4\kappa_{\rm lat}m^2J_2$.

## 1. Lemma P1: confirmed for a fixed positive gap, with locality scope

For $m>0$, W1 is algebraically solvable for every smooth spatial pair kernel:

\[
F^{0j}=\frac{D_iF^{ij}}{\omega},\qquad
F^{00}=\frac{D_iD_jF^{ij}}{\omega^2},\qquad \omega=\epsilon_1+\epsilon_2\ge 2m.
\]

Thus W1 imposes no further condition on the **spatial** pair kernel, although it does determine the time components. In the annihilation term of $T(-q)$, take $F_a=F_c^*$ and $\omega_a=-\omega$; since $D(-q)=-D(q)^*$, conjugating the creation equation gives the annihilation equation with the correct sign. This confirms the report's argument (R13-5_report.md:145-160) and the implementation (scripts/r135_w1_pair.py:58-64,80-84). The requested rerun reproduced creation residuals at $10^{-15}$, annihilation residuals at $10^{-15}$--$10^{-14}$, and the conjugation identity at $1.1\times10^{-15}$ (scripts/r135_w1_pair.out:2-13); a separate generic complex-kernel check did the same (R13-5_referee_checks.out:1). Hermiticity also requires the explicitly supplied conjugate annihilation term and the appropriate exchange symmetry/antisymmetry of the pair kernel; it is not a consequence of division by $\omega$ alone.

For fixed $m>0$, division by $\omega$ preserves $C^\infty$ regularity on the compact momentum torus, so the exact Fourier kernel is super-polynomially localized. This analytic fact, rather than five finite-distance coefficients, is the proof. It applies to exact U on G/L and M on L. M on G is nonlocal because sign$(k)\sqrt u$ jumps at the zone face (scripts/r135_w1_pair.py:32-38), consistently producing a power tail (scripts/r135_w1_pair.out:15-19). The numerical G profile itself uses a cubic spline (scripts/r99_profiles_copy.py:29-34,40-51), so that discretized runner is not by itself a $C^\infty$-locality certificate. The lemma does not cover a genuinely gapless channel, where $\omega$ can vanish and uniform locality can fail.

## 2. Lemma W0: contact terms vanish, but the conclusion must be narrowed

The $C_{4v}$ decomposition at axial $q$ is correct: $B_1=(xx-yy)$ and $B_2=xy$ are one-dimensional blocks, while every component hit by $q_\mu\Pi^{\mu\nu,\rho\sigma}$ lies in $A_1\oplus E$ (R13-5_report.md:186-198). The tadpole contacts do not rescue the identity. In a cubic vacuum $\bar T^{ij}=p\delta^{ij}$ and $\bar T^{0i}=0$; linearizing $\nabla_\mu T^{\mu\nu}=0$, every contact for an $xy$ or $xx-yy$ insertion either contains $q_x$ or $q_y$, or contracts $p\delta^{ij}$ with a traceless shear. It therefore vanishes for $q=(\omega,0,0,q_z)$. Equivalently, there is no little-group intertwiner from $B_{1,2}$ to the vector representations $A_1\oplus E$.

What follows is the narrower statement: the **two-point contracted Ward identity, including its cubic tadpole contacts, is empty on each axial TT block**, so transversality alone does not determine the TT pole function. The report's phrase “no Ward identity of any order” (R13-5_report.md:46-48,198) is stronger than its proof. Higher-point identities plus a specified local action, or a separate boost/Lorentz symmetry, can relate derivative coefficients; W0 only shows that this information is not present in the axial two-point contraction. The report itself correctly distinguishes the possible $q\to0$ contact constraints from the unfixed speed term (R13-5_report.md:200-207,340-349).

## 3. Lemma B2: the moment obstruction is valid for standard W2, not for every use of “Ward identity”

The pair channel drops out exactly. P1 gives $F^{0j}_{\rm pair}=O(q)$ and $F^{00}_{\rm pair}=O(q^2)$, so its contribution to $H=T^{00}(0)$, $P_j=T^{0j}(0)$, and $K_i=i\partial_{q_i}T^{00}(q)|_{q=0}$ vanishes (R13-5_report.md:211-222; scripts/r135_moments.py:1-16). A diagonal improvement in the scattering boost also commutes with $P$, so it cannot repair the commutator. The surviving one-body identity is therefore Theorem E,

\[
[K_i,P_j]=i\,d\Gamma\!\left(\epsilon[\delta_{ij}+A_{ij}]\right),
\qquad A=\operatorname{Hess}(\epsilon^2/2)-I,
\]

and periodicity gives $\langle A\rangle=-I$, forcing a failure outside the exact box (C5_R8-2_referee_verdict.md:31-47).

The moment relation is a necessary condition if W2 means the standard undeformed Dirac--Schwinger/hypersurface-deformation algebra: integrating the local stress algebra against $1,x_i$ yields $[K_i,P_j]=i\delta_{ij}H$, and regular seagulls or field-dependent corrections that vanish at flat background cannot change these flat charges. On that definition, B2 proves a bounded no-go for the stated single periodic-band, fixed-leading-generator class. But the report expressly says the scalar W2-to-moment implication is recalled rather than independently established (R13-5_report.md:89-92,225-229), while the supplied R12-1 verdict confirms necessity only in its free number-conserving fixed-core class and leaves altered generators, auxiliary/multiband matter, and other completions open (C5_R12-1_referee_verdict.md:5,9,13-15). Hence B2 does not rule out every two-point Ward--Takahashi identity in a preferred-background or deformed-algebra theory. “Not Ward-protected” should likewise mean that the usual Nielsen/BRST protection theorem is unavailable; it does not constitute a calculation of nonzero gauge dependence.

**No-go discipline check.** N1: five materially distinct attacks are (i) pair charges repairing the moments, (ii) a scattering-kernel boost improvement, (iii) flat-background seagull/field-dependent corrections, (iv) a deformed or preferred-foliation constraint algebra, and (v) extra fields, bands, or an unfolded tower; (i)--(iii) fail in the stated standard-W2 class, while (iv)--(v) are genuine out-of-class escapes. N2: there is one load-bearing wall, failure of the flat Poincaré moment, not several independent walls. N3: the hidden premise is exactly the report's “RECALLED” W2-to-moment implication and has been promoted to the scope. N4: R12-1's witness has the same fixed-leading-charge residual only after the scalar one-body reduction above; its broader unfinished construction is not evidence. N5: “every member” is restricted to the stated single-band standard-W2 class. N6: no new-axiom claim is needed. N7: the strongest steelman is a deformed HDA/preferred background for which the Poincaré moment is not required. N8: the prior field-dependent-completion lane itself leaves altered leading generators, auxiliary/multiband matter, and towers open (TESTS.md:2267-2298). The gate therefore passes only for the bounded standard-W2 no-go and fails for the report's broader rhetorical variants.

## 4. The floor: G confirmed; L failure confirmed with a mass-range correction

Both requested runners reproduced (scripts/r135_xi_split.py:36-63; scripts/r135_floor_bprime.py:7-18). An independent tensor Gauss--Legendre quadrature gives, for $b'=2$:

- $m=1$: $\Xi_{T_2}=-1.7384\times10^{-4}$, $\Xi_E=-9.0444\times10^{-5}$;
- $m=0.3$: $\Xi_{T_2}=-2.1272\times10^{-4}$, $\Xi_E=-1.1295\times10^{-4}$;
- $m=0.01$: $\Xi_{T_2}=-2.1722\times10^{-4}$, $\Xi_E=-1.1560\times10^{-4}$.

These values (R13-5_referee_checks.out:2-4) agree with the fine worker run (scripts/r135_floor_bprime.out:1-3). Since $A_{zz}\le0$ pointwise on G and the free edge weight is nonnegative, every member of the **defined** class obeys $\Xi\le\Xi_{\rm box\perp}<0$ (R13-5_report.md:233-240). At $a=\ell_P$, the T2g floor over those three masses is $4.37\times10^{-3}$ to $5.46\times10^{-3}$, not uniformly “at least $5\times10^{-3}$”; the $5.3\times10^{-3}$ number is the light-mass value. The Eg floor is $2.27\times10^{-3}$ to $2.91\times10^{-3}$.

For L, the doubler asymptotic and sign reversal are real: $I(10^{-4})=-1.131\times10^4$, with the first zero near $7\times10^{-4}$ (scripts/r135_L_small_m.out:1-2; R13-5_referee_checks.out:12-14). Smooth symmetry-compatible edge bumps supported near doubler corners can therefore contribute with the opposite sign and, after scaling, pass through $\Xi=0$; the positive box part is not a class floor for sufficiently light L species. One further correction is needed: “L, $m\ge0.1$” is not an all-mass theorem. Since $\int A\,dk=-2\pi$, $I(B)<0$ again for sufficiently large $B$; the independent run finds $I(20)<0$ (R13-5_referee_checks.out:11,17-19). Positivity is established for the campaign's tested $m=0.1,0.3,1$ range, including the fixed $m=0.3,1$, not for arbitrary larger mass.

## 5. Birefringence correction: confirmed

R11-1's referee inferred “at most one cone” from the unequal M/U rows (C5_R11-1_referee_verdict.md:19); that is valid for those vertices, not for the enlarged W1-complete class. Multiplying one polarization's edge squared-amplitude by the smooth positive factor $1+(c-1)\eta$ preserves box exactness and parity. On G-U, scaling Eg with $c=6.140189$ equalizes the two $\Xi$'s at $m=1$ (scripts/r135_xi_split.out:42-46). On L-U the analogous Eg coefficient is negative and inadmissible, but scaling T2g instead gives the valid positive coefficient $c=4.160499$ (R13-5_referee_checks.out:19-20). Thus birefringence is not class-wide even at one mass.

The all-mass characterization is also correct: after a Laplace representation, equality on a mass interval implies $F_A(t)F_{\Delta V}(t)=0$; because $F_A$ is analytic and $F_A(0)=-2\pi\ne0$, the pushforward of $|V_T|^2-|V_E|^2$ under $k_\perp\mapsto u_x+u_y$ must vanish, and the converse is immediate (R13-5_report.md:290-294). No smooth nonnegative member satisfying that condition for all masses was constructed, so the report correctly labels existence as suggested. The same pushforward kills the paramagnetic/CC-independent mass difference; arbitrary polarization-dependent seagulls remain separate law data.

## 6. Class fairness, the FIXED reading, and the paired factor

Hypothesis (ii) is mathematically fair as an explicit definition of a nonempty **auxiliary** class, but it is a strong additional law assumption, not a consequence of W1 or the fixed setting. Together with $k_z$-independence, it transports the continuum transverse vertex from an all-components box configuration to every edge $k_z$, precisely where the G anomaly has a fixed sign (R13-5_report.md:93-97). A $k_z$- or $q$-dependent vertex such as INV escapes, as the report admits (R13-5_report.md:109-117,412-417). Therefore the floor is class-wide over $\mathcal W_V$, not over all Ward-complete pair stresses.

Under the FIXED text, the reading is **OPEN**, not “SPLIT-PRESENT (scoped).” The registered setting demands a pair stress satisfying the **second-order** Ward identity (TESTS.md:4668-4673), and SPLIT-PRESENT requires nonzero physical pole splitting for every Ward-complete stress in the stated class (TESTS.md:4674-4677). The computed family is only W1-complete, while B2 says the standard-W2 subclass is empty; an empty-class universal statement cannot satisfy a reading that also asks for pole numbers. Moreover, the matter pole remains dD-M prescription-scoped, exactly the limitation already recorded for R11-1 (C5_R11-1_referee_verdict.md:11-21). Pairing is also OPEN: the TT response cancels in its stipulated matched model, but the only remaining matter result is not a W2-protected physical pole.

Finally, the paired residue has a factor-of-two prose error. The established normalization is

\[
c_m-c_T=\kappa_{\rm lat}(2J-\Xi),\qquad J=m^2J_2.
\]

Thus $\Xi=0$ leaves **$2\kappa_{\rm lat}m^2J_2$**, not $4\kappa_{\rm lat}m^2J_2$. This follows directly from the prior normalization (prior_scripts/r111_split_numbers.py:1-4,24-37). The worker's table and proton number actually use the correct $2\kappa J$ value, $-1.69\times10^{-39}$ on G, while only the printed formula is wrong (scripts/r135_xi_split.py:83-100; R13-5_referee_checks.out:21-22).

## Strongest correct statement

For a fixed massive free scalar and a smooth spatial pair kernel, W1 uniquely supplies smooth time components, with the conjugate annihilation channel restoring Hermiticity; in the standard undeformed Dirac--Schwinger/HDA interpretation of W2, those pair terms vanish from $H,P,K$, so the periodic-band boost anomaly gives a bounded obstruction to second-order closure for the fixed leading charges. Independently of that obstruction, in the explicitly narrower W1-only class $\mathcal W_V$, the gapped G profile has $\Xi\le\Xi_{\rm box\perp}<0$, giving a light-scalar dD-M split of order $2.3\times10^{-3}$ to $5.5\times10^{-3}$ per species at $a=\ell_P$; light L doublers destroy the class floor, and birefringence itself is removable by a smooth one-mass edge tuning. Matched TT pairing cancels the stipulated TT loop response and leaves the prescription-scoped scalar residue $2\kappa_{\rm lat}m^2J_2$, but because the campaign's fixed setting requires a second-order Ward-complete stress and gauge-invariant physical poles, the correct fixed reading is OPEN both without and with pairing.
