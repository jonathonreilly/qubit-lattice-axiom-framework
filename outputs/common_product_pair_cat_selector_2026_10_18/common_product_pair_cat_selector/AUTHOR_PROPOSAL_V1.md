# Two-body pair selector for supplied signed-cat quality

ROOT-authored new candidate requiring distinct verification. This is an optional local excess-energy certificate for the supplied joint rest state in PR9725, NOT a physical preparation process. It replaces the four single-site selector fields by two real positive pair terms per square. All exact runtime, blankness, input independence, reference retention and finite-window restrictions remain.

## Exact square and all sectors

Label a square cyclically1,2,3,4. Let

 H0=Delta sum_cycle (I-Z_i Z_j)/2,
 Hpair=H0+h[(I-X1 X2)+(I-sigma X3 X4)], sigma=+1 or-1,
 0<h<=Delta/64, r=h/Delta.

Each added term is positive, real, two-body, norm2h, and acts on an existing nearest-neighbor edge of the square. Their sum has the true identity scalar2h. Define pair parities p=Z1Z2,q=Z3Z4, and F=X1X2X3X4. All commute with Hpair. In p=q=+1, the zero-H0 states are0000,1111 and the other two states1100,0011 have H0 energy2Delta. Write

 cat_t=(0000+t1111)/sqrt2,
 chi_t=(1100+t0011)/sqrt2, t=+1,-1.

On span(cat_t,chi_t), Hpair-2hI is exactly

 [[0,-h(1+sigma*t)],[-h(1+sigma*t),2Delta]].

Thus in t=sigma its eigenvalues are Delta +/- sqrt(Delta^2+4h^2); in t=-sigma the energies are0,2Delta. (For t=sigma=-1 the above chi convention still gives X12 cat_t=chi_t and X34 cat_t=t chi_t, so the off-diagonal is-2h.) These are all four states in the p=q=+1 sector.

If p=q=-1, the two internal pair walls already give H0>=2Delta. If p and q differ, the two cross edges have opposite signs, so H0=2Delta I. Since the added pair terms are positive, EVERY state in these other twelve dimensions has full Hpair energy>=2Delta. No data fiber or parity subspace is omitted from the comparison.

Set R=sqrt(Delta^2+4h^2). The unique full ground has F=sigma and exact energy

 e_pair=2h+Delta-R=2h-4h^2/(R+Delta).

Its first full gap is EXACTLY

 gap_pair=R-Delta=4h^2/(R+Delta).

Indeed the other low-sector energy is2h, whereas all remaining p=q=+1 energies exceed2Delta, and every other sector has energy>=2Delta>2h. For h<=Delta/64, R+Delta<4Delta, so

 gap_pair >= g_pair:=h^2/Delta.

The exact ground is psi_sigma=cos(theta)cat_sigma+sin(theta)chi_sigma, tan(theta)=2h/(R+Delta)<=r, with canonical positive cat overlap. Consequently ||psi_sigma-cat_sigma||<=2r. This deliberately loose bound follows immediately from the mixing angle; no unbounded perturbation remainder is used. At h=0 uniqueness fails; it is excluded.

## Reference-safe joint rest certificate

Use twelve disjoint squares with their actual six plus/six minus signs from the real gauge1cc8. Define A_pair=sum twelve Hpair, exact ground product Psi and exact reference12e_pair. Its full gap is at least g_pair, its product ground differs from Cats by vector norm<=24r and trace distance<=48r, by telescoping and the pure-state trace bound.

For an arbitrary joint rest state omega, including retained passive E and old program P, but independent of the fresh physical logical/dual-rail boundary input, let

 E_pair=Tr[(A_pair-12e_pair I)omega],
 q_blank=Tr[(I-P_blank)omega].

P_blank requires noninput head vacuum and R=0 as in b58d, and excludes the two boundary input emitters. It commutes with the ancilla ground projector. The spectral gap bounds the joint ancilla-ground failure by E_pair/g_pair. Projecting the joint blank/ground subspace and using purification gives, for some retained state sigma_PE,

 ||omega-|blank,R0,Cats><blank,R0,Cats| tensor sigma_PE||_1
 <=2sqrt(q_blank+E_pair/g_pair)+48r.                 (1)

The square-root term requires its probability budget below1. It is a full joint bound, not a sum of marginal fidelities; no entropy/reference/old program is discarded. The energy reference is EXACT, including all12 copies of e_pair. The observable is not the full running Hamiltonian and its ground is not assumed to be the running ground. Ground F=sigma is not the real gadget's transformed T=+1 sector in general; the state difference in(1) and the runtime perturbation below pay this discrepancy.

## All-time runtime composition

Take the actual unpenalized real two-body runtime Hrun of b74d/1cc8, as published in PR9725, including its existing twelve H0 terms ONCE. Add ONLY the24 pair-selector terms, not another H0:

 Hrun,pair=Hrun+24hI-h sum_(24 pairs) sign_pair X_i X_j.

The full operator norm of the nonconstant difference is<=24h. Therefore on the full Hilbert space, without any F/T/head-number conservation assumption,

 ||exp(-it Hrun,pair)-exp(-i24ht)exp(-it Hrun)||<=24h|t|.

The target runtime phase is exactly48nu+s_joint+scale*cbar+24h. The isolated reference12e_pair is NOT an extra runtime phase. No field is switched off or externally timed.

For 0<epsilon<=1, instantiate the reference/runtime theorem exactly at tau=epsilon/8, epsilon_g=epsilon/16. Use its unchanged alpha, scale, T, finite length, source policy and coefficients for these smaller budgets. Choose

 h=min{Delta/64, Delta*epsilon/384, epsilon/(384T)}.

Then48r<=epsilon/8 and24hT<=epsilon/16. Require

 q_blank<=epsilon^2/512,
 E_pair<=g_pair*epsilon^2/512.

The square-root term in(1) is<=epsilon/8, so the initial joint rest trace allowance is<=epsilon/4. For the exact blank/Cats input the reference finite-vector final error is<3tau/8=3epsilon/64; the gadget error is<=epsilon_g=epsilon/16; the added pair dynamics costs<=epsilon/16. The total final vector error is<=11epsilon/64. Converting to channel distance and adding the supplied joint rest trace gives

 full unhalved channel distance <= 19epsilon/32.

For the whole horizon, the base absolute unnormalized wrong-record branch norm is<=tau/2=epsilon/16. Adding the same two operation errors gives3epsilon/16. The corresponding unhalved subnormalized channel error and rest error give<=5epsilon/8 on the whole horizon. The final joint success event has probability at least

 1-121epsilon^2/4096-epsilon/8,

using the squared final vector bound and the event-probability trace-distance half bound for the joint rest error. Preserve all apparatus outputs and the common finite outgoing profile from the parent theorem. The observation window remains relative width1/6; neither infinite retention nor capture/reset follows.

## Resource and interpretation limits

Each existing ancilla belongs to exactly one new pair, so its added incident norm is2h. Its total load is2Delta+2nu+2h<Lambda on the parent's Delta=Lambda/4, alpha<=1/(32K),K=48 and h<=Delta/64. Other sites are unchanged. There are24 new positive blocks, no new qubits and no enlarged range:

 175+4ell qubits, 289+4ell positive blocks, Manhattan range<=35.

The selector pairs themselves have range1. Exact negative pair signs for sigma=-1 preserve positivity. All other real positive two-body blocks remain supplied.

The parent's sufficient scale is T=Theta(Lambda^-1 epsilon^-17 log(e/epsilon)^5) and ell=Theta(epsilon^-3 log(e/epsilon)); therefore the stated minimum gives

 h=Theta(Lambda epsilon^18/log(e/epsilon)^5),
 gap_pair=Theta(Lambda epsilon^36/log(e/epsilon)^10),
 allowed E_pair=Theta(Lambda epsilon^38/log(e/epsilon)^10).

This is a relaxation of the sufficient local energy accuracy versus the previous onsite selector's epsilon^74/log^20 allowance, within the supplied coefficient family. Runtime, device-size exponents and autonomous preparation are NOT improved. Accurate local expectation/reference subtraction is still a substantial unproved physical requirement. Exact rationalizations avoid arithmetic cancellation but do not supply an experiment or precision feasibility. This is not evidence of a cooler, a product-to-cat evolution, a native material implementation, a nearest-neighbor implementation of the full running device, or identification with the original literal processor.

## Sources, exposure and checks still needed

ROOT fully read the parent operation publication NOTE299339801b7f6714df652ab874a1a65ad504ceaf8ba934c08249dde458986899 and its source/review family at PR9725 head24daf0bc43bf9eb2844abd55b93d01f91670f4f6. In particular unpenalized operation b74d8f05658f6718dfcb4d9a050c6ddca90a357eabeb9dfed9c042567b36d9bb/review64174ac689b6894ebfdf69369bdeb6816501ce15388cce6db5dd232d651b4337 and real gauge1cc8b14dabd52a73f90bedf0186d7c3c92d02a9608aa72ce01ff0303fa3fe1f3/review603671b279be1867d9aabca527ac0142bee3e9d915eccf4ed050a2d9ae29db4a retain their full earlier reads.

The previous onsite selector ab894394a2b2bd76dcc59b591f5d39d2aa070d7c1c3aa62528b76c99c6cd8c18/reviewc34ef97e7ae4a3b96932e9904b79aacc18cae6b6ac0f8c999006395a2b1aa32a supplies the reference-safe projection/runtime budgeting pattern; its spectrum/gap is NOT imported for this pair selector. Exact onsite supplement0ef4a6cdf6b2f228bb93e39f244720db533c47c6df3f8cb531b48ce8c424714c/reviewa0f095998b28ff7ede8f637713eaaf2f5a5de7a907f83afdbf72063547e04d56 is historical comparison only. ROOT derived the new complete pair-sector spectrum, mixing angle, physical inventory and revised budgets above. A distinct check must verify all sectors, signed conventions, exact gap, joint reference argument, full runtime norm/phase and constants; do not count this author derivation as independent confirmation. No scientific executable or numerical experiment has been run for this candidate.
