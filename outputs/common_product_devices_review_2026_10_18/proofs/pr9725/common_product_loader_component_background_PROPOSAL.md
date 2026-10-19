# A local-commutator interface for the isolated loader component

New author extension, requiring distinct review. The checked isolated square gadget admits a complete finite-time comparison in an arbitrary bounded background whose error depends on commutators at its four data terminals, not on the background's global norm or volume. No perturbative spectral gap for the full background-plus-gadget Hamiltonian is assumed. The bound is sufficient and can be very costly in time. For the actual router-strength matching it does not, as presently estimated, close the required operating budget. That failure of this upper-bound certificate is not an obstruction to every possible background-adapted gadget.

## 1. Checked component and the new background

Use exactly isolated source7e676: four data qubits with Hermitian unitary Pauli operators O_r on distinct sites, four ancillary square qubits, H0=Delta sum_edges(I-ZZ)/2, V=nu sum_r O_r X_b_r, and

    H_gad=4nu I+H0+V,
    alpha=nu/Delta<=1/64,
    Omega=O_1O_2O_3O_4,
    s=-2nu^2/Delta-nu^4/(2Delta^3),
    g=5nu^4/(2Delta^3),
    R6=Delta(32alpha)^6/[1-(32alpha)^2].                 (1)

The literal injection J tensors the data with the supplied ancillary cat+. Work in the reducing ancillary X_all=+ sector. The isolated checked proof constructs an isometry W=Pi J C into the exact low band, with

    ||W-J||<20alpha,
    H_gad W=W[4nu I+E],
    ||E-(sI-g Omega)||<=R6.                              (2)

Here Pi is the isolated real spectral projection, and C=(J^*Pi J)^(-1/2). All these maps act as identity on other data/environment degrees of freedom. Cat+ preparation and the arbitrary positive two-body block class remain premises.

Let B be ANY bounded self-adjoint background acting on the data and an arbitrary finite rest system, but not on the four new ancillas. It may contain distant interactions and need not commute with Omega or individual O_r. Its norm may grow with volume. Define the local commutator coefficient

    C_B=sum_(r=1)^4 ||[B,O_r]||.                         (3)

If B=sum_l B_l is a local decomposition, then ||[B,O_r]||<=sum_(l meeting data r)||[B_l,O_r]||; terms disjoint from the four terminals vanish exactly. This supplies a volume-independent ceiling when the terminal incidence strengths and degrees are uniformly bounded. Exact cancellations can give a better ceiling than this termwise triangle bound, as section4 demonstrates.

The compared total generators are

    H_tot=H_gad+B tensor I_anc,
    H_tar=B+(4nu+s)I-g Omega.                            (4)

The background in the target is the SAME physical B, not a quenched or time-averaged replacement. Other outputs and passive references are retained.

## 2. Resolvent commutator and complete dynamical bound

Use the isolated contour |z|=Delta/2. Since [B,H0]=0 and ||V||<=4nu,

    ||(z-H0-V)^(-1)||<=2/[Delta(1-8alpha)],
    ||[B,V]||<=nu C_B.

Commuting B through the contour resolvent gives

    ||[B,Pi]||
       <=(Delta/2)*4/[Delta^2(1-8alpha)^2] *nu C_B
       =2alpha C_B/(1-8alpha)^2.                        (5)

This is an identity/estimate for the isolated projection Pi, not a claim that the FULL H_tot has a separated low spectral band. It uses no smallness of ||B||.

Let X=J^*Pi J-I. From the isolated proof ||X||<=deltaPi<=1/7 and ||C||<1.081. Because B J=J B on the data/rest domain,

    ||[B,X]||<=||[B,Pi]||.

The absolutely convergent binomial series C=(I+X)^(-1/2) and the identity [B,X^n]=sum_(l=0)^(n-1)X^l[B,X]X^(n-1-l) give

    ||[B,C]||<= [1/(2(1-deltaPi)^(3/2))] ||[B,Pi]||
                                              <.64||[B,Pi]||.

Consequently the rectangular commutator satisfies

    ||B W-W B||
       <=(1.081+.64)||[B,Pi]||
       <=6alpha C_B.                                   (6)

The final ceiling follows from alpha<=1/64, so (1-8alpha)^2>=(7/8)^2. The conservative factor6 leaves margin.

Equations (2),(4),(6) give a residual on the WHOLE nominal input space,

    ||H_tot W-W H_tar||<=R6+6alpha C_B.                  (7)

Differentiate exp[-i(t-r)H_tot]W exp(-irH_tar) and integrate. Both evolutions are unitary, even though B need not preserve the isolated dressed subspace. Adding the literal-input and literal-output discrepancies from (2) proves, for every real t,

    ||exp(-itH_tot)J-J exp(-itH_tar)||
                      <=40alpha+|t|(R6+6alpha C_B).      (8)

This pays all actual ancillary leakage and all background-induced correlations. It is not a projected effective dynamics, postselection, or a claim of exact invariance. Arbitrary references tensor through the proof. The unhalved complete channel discrepancy is at most twice (8), capped at2. Supplied joint preparation trace error adds by full-unitary contraction, without discarding its environment.

If [B,O_r]=0 for every r, then C_B=0, B commutes with Pi,C,W and Omega, and (8) reduces exactly to the isolated bound for any background size or norm. This is an actual commuting-background transfer. The weaker condition [B,Omega]=0 alone is not sufficient to remove the additional issue; section6 gives a concrete counterexample to that inference.

## 3. A simultaneous sufficient prescription with a fixed horizon

For a chosen finite horizon T>0, chosen background ceiling C_B and error 0<epsilon<=1, the following is sufficient:

    Delta=Lambda/4,
    alpha<=min{1/64, epsilon/120,
                  [epsilon/(4Delta T*32^6)]^(1/6),
                  epsilon/(18T C_B)},                  (9)

with the last entry omitted if C_B=0. Then40alpha<=epsilon/3, TR6<=epsilon/3 and6alpha T C_B<=epsilon/3, so the complete vector error is at most epsilon on |t|<=T.

The new ancillary loads are at most2Delta+2nu<Lambda. Each data terminal receives an additional2nu<=Lambda/128. Thus (9) respects a fixed incident cap if the background has at least that stated terminal reserve; no claim is made for a background already saturating its cap. This is a volume-independent sufficient interface but it can make g=(5/2)Delta alpha^4 very small. It does not assert that a desired nontrivial gate angle gT or a prescribed router j is compatible with (9). Time, strength and accuracy must be matched together.

## 4. Actual XX(head)ZZ(program) commutators

Take one entrance's data operators

    O_1=X_i, O_2=X_j, O_3=Z_Q, O_4=Z_P,

where i=I0,1=(19,0,0), j=I0,0=(20,0,0), P=(21,1,0), and Q is the extra ordinary input program qubit. Use as B the original one-control finite router with this entrance's ordinary bond still present, optionally including mu N and the one kappa n_R. Q is idle in this background. This is a definite background test, not an assertion that six such components have already been assembled into a replacement bond.

The programmed mediator terms are diagonal in P, so [B,Z_P]=0 exactly, however large D0,D1 are. Also [B,Z_Q]=0. Record bias and distant writer/cable terms do not meet i,j and commute with their X operators. The following calculation is on the FULL head-occupation space, including double occupation, not just one-head row sums.

Using the exact positive-Q convention and the two endpoint vacancy cancellations, the part of B relevant to the i and j commutators has occupations

    (2j_strength+mu)n_i +(3j_strength+mu)n_j,

ordinary hopping of strength j_strength from i to j and from i to I0,2, and two hoppings of strength b from j to its two core mediators. Here j_strength is the router's coefficient j; this temporary name avoids confusion with the terminal label. Each hopping is -(a/2)(X_xX_y+Y_xY_y).

One has ||[n_x,X_x]||=1 and

    ||[-(a/2)(X_xX_y+Y_xY_y),X_x]||=a.

Therefore exact diagonal cancellation followed by triangle inequality gives

    ||[B,X_i]||<=4j_strength+mu,
    ||[B,X_j]||<=2b+4j_strength+mu,
    C_B<=2b+8j_strength+2mu=:C_router.                  (10)

The two source emitters are far away (ell>=1000), so their weak bonds do not meet these terminals. The same calculation holds at the other entrance. The large P-diagonal detuning terms drop out of (10); a global ||B|| estimate would miss that useful fact. If an entrance bond is removed or its coefficient reduced during a separately defined assembly, its contributions and positivity must be recomputed; (10) is not automatic for arbitrary added couplings.

Uniform head penalty is material: [N,X_i] is nonzero. One isolated XX component can change head number, even though the SUM defining the original SWAP hopping conserves it. Thus mu cannot be treated as a harmless scalar in this isolated-component background argument. The full one-head scalar identity of the original router does not apply to these virtual gadget excursions. Record bias commutes with these four O_r and contributes no term to (10).

## 5. The present certificate does not close the router time matching

To match this component to the selected summand of the entrance bond, require

    g=j_strength/4,
    j_strength=10Delta alpha^4.                         (11)

At Delta=Lambda/4 with the preparation penalty mu=Lambda/4, inserting C_router from (10) into (8) budgets at least the positive term6alpha T(2mu). Already for T>=1/j_strength this numerical allowance is at least

    12alpha mu/j_strength=(6mu/(5Delta))alpha^-3
                                         =(6/5)alpha^-3. (12)

It is far above a small error for alpha<=1/64. Equation (12) is a LOWER BOUND ON THIS CHOSEN SUFFICIENT ALLOWANCE, not a lower bound on the actual simulation error. Weakening nu further at fixed cap makes this particular matched-time allowance worse. Thus (9) cannot simultaneously certify that strength/time match with the included uniform penalty. It is incorrect to describe the local term as small and then silently ignore its multiplication by the very long operating T.

Even omitting mu does not immediately recover the old operation theorem. With b=j_strength/eta and T=U/j_strength, the chosen local allowance is

    6alpha T(2b+8j_strength)
                          =6alpha U(2/eta+8).           (13)

For the actual biased family's j_strength=Lambda tau^2/(8*10^12), eta=sqrt(tau)/1000 and Delta=Lambda/4, equation (11) fixes

    alpha=tau^(1/2)/(20*10^12)^(1/4),
    alpha/eta=1000/(20*10^12)^(1/4)>0,

a constant independent of tau. Hence the leading selected allowance in (13) grows with U, rather than becoming a small error on the large router horizon. This tests the actual coefficient matching, not an arbitrary independent alpha choice. No runtime order is inferred from an unchecked new resource family.

These failures leave a specific next calculation: a background-adapted dressing/counterterm analysis that controls the leading local corrections, or a gadget design preserving the relevant head-number structure so the uniform penalty does not shift virtual denominators. Such a calculation may improve the interface, but is not performed here. Increasing Delta without respecting incident cap, dropping mu while retaining its preparation theorem, or asserting cancellation between six independently analyzed components would not repair the current proof.

## 6. A concrete warning: commuting with the product is not enough

Consider the same isolated square with O=(X_1,X_2,Z_3,Z_4), and add B=J0 Z_1Z_2 with 0<J0<Delta/2. Adding the harmless scalar J0 makes the background block J0(I+Z_1Z_2) positive; data1 and2 are adjacent on the explicit upper square. This example fits arbitrary positive two-body backgrounds and preserves the ancillary X_all sector.

B COMMUTES with Omega=X_1X_2Z_3Z_4, but not with O_1 or O_2. In a data Z_1Z_2 eigenstate z=+-1, flipping ancillary1 or2 with its data X changes the background energy from J0 z to -J0 z. Its excitation denominator is therefore2Delta-2J0 z. Flips3 or4 keep denominator2Delta. Second-order perturbation about H0+B consequently gives the diagonal shift

    E2(z)=-nu^2/(Delta-J0 z)-nu^2/Delta
         =-2nu^2/Delta
          -nu^2 J0^2/[Delta(Delta^2-J0^2)]
          -[nu^2 J0/(Delta^2-J0^2)] z.                 (14)

The denominators stay bounded away from zero by the stated J0 condition. Returning to P at second order requires the same ancillary flip twice; no missing cross path changes this result. The last term in (14) is a NONSCALAR correction of order nu^2 J0/Delta^2. It is not in the isolated scalar s and is much larger than g=O(nu^4/Delta^3) at fixed J0/Delta and small alpha.

This explicitly refutes importing the unchanged isolated effective generator merely from [B,Omega]=0. It does not prove that the background cannot be compensated or simulated by another method. A scalar phase adjustment alone cannot remove the z-dependent shift. The example also explains why an improved background theorem needs to inspect intermediate virtual energies, not just the final product's commutator. The local residual theorem (8) remains valid for this example; its conservative cost pays the effect rather than declaring it absent.

## 7. Scope, exact evidence and required check

The extension proves a sufficient complete-output bound depending only on terminal commutators, an exact zero-extra-cost commuting-background transfer, an explicit actual-router commutator ceiling, and a counterexample to a weaker naive commuting criterion. It does NOT prove an exact block diagonalization of H_tot, a useful matched router simulation, simultaneous six-term packing, GHZ+ preparation, a licensed entrance-bond realization or an autonomous loader. All primitive, geometry, old-P/environment-retention, endpoint-injection and release obligations from the source remain.

Paths are under N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. The isolated source common_product_loader_bond_realization/PROPOSAL.md is7e6769927d3138b2812e0b4a0db62df1ef4d1d7096b10acfa2269a5ca8a98d39, authored and fully read in the immediately preceding task. Its distinct common_product_loader_bond_realization_check/REVIEW.md, f71cdc4e4039f923f99c8ed1f2abab9baedee9f8f9456c1d77ed6a9978b9fd58, was fully read and hash verified here; it supports only the isolated component, its cat+ premise, coefficients, analytic remainder and complete-output estimate. The review also records an exact characteristic-polynomial check by a different method; no code or numerical evidence was run by this author for the present extension.

The actual background inventory is common_product_single_control_router/PROPOSAL.md76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01 and common_product_biased_record_finite_seed/PROPOSAL.md532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123. Their complete reads/hashes in the preceding loader/outgoing tasks remain valid. The uniform-penalty/source conventions are common_product_energy_blank_interface/PROPOSAL.mde6df21d39a9673b7e396390b64986a9e0deb74223540c975c14675a7f6fec668 and common_product_biased_record_preparation/PROPOSAL.md9979b614d77b98bf8bc63b6b87b69305beb7cf7607adf5722ae57b759728627e, fully reread in the loader task. The conditional target remains c97bffbbd02d1703103b4f59131706cdd9be8a19a937ea17382b6621df1bd83e and is not made native or licensed by this analysis.

ROOT suggested the local-commutator direction and requested the actual time accumulation and background distinctions. This author derived the commutator/isometry residual, actual terminal cancellation and warning example after exposure to that suggestion. This is same-model author work, not independent checking. A distinct review must inspect the rectangular commutator estimate, actual all-head occupation cancellations, cap reserve, time/strength matching and the second-order denominator shift before this interface is composed elsewhere.

Only this proposal was created. No scientific executable, simulation/sweep, source/W/Git/checkpoint/axiom/editable-prompt/model change, publication or delegation occurred. No universal no-go, practical runtime, native coefficient/state supplier or permanent halt is inferred.
