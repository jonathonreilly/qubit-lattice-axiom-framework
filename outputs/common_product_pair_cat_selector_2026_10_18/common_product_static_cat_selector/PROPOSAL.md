# Permanently installed local cat selectors and a joint-state certificate

New source-exposed author theorem requiring distinct review. A real positive transverse-field selector on each existing ancillary square has a unique ground state close to the required signed cat, with an explicit fourth-order gap. A supplied small selector-energy excess certifies joint ancillary quality including retained environments. The fields can remain installed during the entire finite operation with their dynamical cost paid. This is not a preparation process, cooling theorem, or a claim about the ground state of the full operating Hamiltonian.

## 1. One square: exact signs and spectral statement

Let

    H0=Delta sum_(cycle edges)(I-Z_r Z_(r+1))/2,
    Hsel=H0+h sum_(r=1)^4(I-s_r X_r),
    r_h=h/Delta, 0<r_h<=r_*:=1/(4*32^3),
    s_r in{+1,-1}, product_r s_r=sigma.

All four added fields are positive real one-qubit blocks of norm2h; H0 is the existing positive square penalty, not an additional copy. Choose s_1=sigma and s_2=s_3=s_4=1, for definiteness. Conjugating by Z on sites with negative s_r converts this Hamiltonian to the all-positive-field selector and converts cat_sigma to cat_+. This is an exact mathematical sign relation. The installed fields themselves already have the stated signs; no physical gauge pulse is assumed.

Put Hc=Hsel-4hI=H0-h sum s_r X_r. It commutes with F=X_1X_2X_3X_4. At h=0, each F sector t=+-1 has precisely one zero vector cat_t and complementary gap2Delta. The checked isolated-square coefficient argument applies separately in each sector. Its data factors can here be scalar signs; its four-flip product is t*sigma. Single- and double-flip returns give the same scalar coefficients, while the all-four path acquires t*sigma. Thus the unique low eigenvalue in each sector satisfies

    E_t=-2h^2/Delta-h^4/(2Delta^3)
                       -(5/2)(h^4/Delta^3)t*sigma+R_t,
    |R_t|<=R6(h):=Delta(32r_h)^6/[1-(32r_h)^2].       (1)

This use of the isolated proof does not sum twelve interacting gadget energies; it is the exact isolated four-spin selector with scalar couplers. Sector t=-1 can alternatively be mapped to t=+1 by one Z, which also flips one field sign; hence the same analytic remainder applies. The literal low eigenvector in sector t, with its canonical positive-overlap phase, differs from cat_t in norm by less than20r_h.

At the chosen r_*, R6(h)/(h^4/Delta^3)<1/8. Consequently

    E_(-sigma)-E_sigma
       >=5h^4/Delta^3-2R6(h)>4h^4/Delta^3.             (2)

All other centered eigenvalues are at least2Delta-4h by Weyl's inequality, since ||h sum s_r X_r||<=4h. A cat trial vector has centered expectation0, so E_sigma<=0 (indeed it is negative). Thus all higher-state gaps above E_sigma exceed Delta on this domain. The other low eigenvalue is within4h of0 and E_sigma>=-4h, so its gap is at most8h<Delta. The global ground is therefore unique, lies in F=sigma, and the actual selector gap is the low-sector splitting, bounded below by

    g_sel:=4h^4/Delta^3,
    ||psi_sigma-cat_sigma||<20r_h.                    (3)

The exact ground energy is e_sel=4h+E_sigma. Equation(1) bounds it but a truncated expression is NOT substituted for e_sel in an energy certificate. An independently supplied certified upper bound on excess above this exact energy suffices; computing or measuring it is not a procedure specified here. The leading gap is5h^4/Delta^3 with the displayed bounded remainder, hence gap=Theta(h^4/Delta^3) as r_h tends to zero.

## 2. Twelve squares and a reference-safe energy certificate

Use the real-gauge pattern of1cc8: for EACH entrance the ordered(H,A) rows(XX,XY,XZ,YX,YY,YZ) require signs(+,-,+,-,+,-). Install the preceding fields on each corresponding square with that sigma. Squares are disjoint. Define

    A_sel=sum_(l=1)^12 Hsel,l,
    |Psi_sel>=tensor_l |psi_sigma_l>,
    |Cats>=tensor_l |cat_sigma_l>.

All single-square spectra are identical by the sign conjugation. Hence A_sel has a unique ground Psi_sel, exact energy12e_sel, and spectral gap at least g_sel. Telescoping the twelve normalized tensor factors, with the phases chosen in(3), gives

    ||Psi_sel-Cats||<240r_h,
    || |Psi_sel><Psi_sel|-|Cats><Cats| ||_1<480r_h.      (4)

Let omega be a normalized JOINT state on all rest qubits and a retained passive environment E, independent of the arbitrary logical/reference input. An assumed excess

    E_sel=Tr[(A_sel-12e_sel I)omega]>=0

implies q_sel:=Tr[(I-|Psi_sel><Psi_sel|)omega]<=E_sel/g_sel. This is a global statement on all48 ancillas, not a collection of marginal fidelities. Projection of a purification gives a normalized conditional environment/rest state and trace distance at most2sqrt(q_sel). The environment is retained, not manipulated or discarded.

For a complete operating-state certificate also let Pi_blank project every ORIGINAL rest head onto vacancy and shared R onto0, leaving old P and E untouched. It excludes the two emitter qubits which form the supplied input code. This projection commutes with the ancillary ground projection. If q_blank=Tr[(I-Pi_blank)omega], the joint bad weight obeys

    q_joint<=q_blank+E_sel/g_sel.

When the right side is below1, normalized projection onto both factors gives exactly

    |vac_other_heads,0_R><...| tensor
         |Psi_sel><Psi_sel| tensor sigma_PE

for some normalized sigma_PE, with all correlations to E retained. Combining purification projection with(4) yields the complete supplied-state comparison

    ||omega-|vac_other_heads,0_R><...|
                 tensor |Cats><Cats| tensor sigma_PE||_1
       <=2sqrt(q_blank+E_sel/g_sel)+480r_h.            (5)

Only the cat part is newly certified by the local selector energy. The blank-head/record quality and physical Q/dual-rail input remain supplied. Projection is a mathematical comparison, not a measurement or reset. If there are additional preparation-device outputs they must be included in E or another declared retained factor. A diagonal apparatus marginal would not justify replacing the square-root joint-state bound by a linear one.

The exact selector ground generally is NOT confined to the transformed gadget T_l=+ sectors of1cc8. Those sectors involve Y on rotated sites, whereas the selector uses real X fields. Being in F=sigma does not imply being in T_l=+ outside the two-dimensional penalty-zero space. We do not assume that invariance. The distance(4)--(5) pays this initial leakage relative to the exact signed-cat operating comparator.

## 3. Fields remain on throughout the operation

Let Hrun be the checked REAL, unpenalized b74d device, obtained from1cc8's exact ancillary gauge. It already contains H0 once per square, all48 data couplers and the scaled background. Define the actual new static runtime by adding only the48 fields:

    Hrun,sel=Hrun+48h I-h sum_(l,r) s_(l,r) X_(l,r).

The nonconstant sum has norm at most48h (in fact exactly48h on the full ancillary tensor space). Full-unitary Duhamel therefore gives, on the ENTIRE physical Hilbert space and all references,

    ||exp(-itHrun,sel)-exp(-i48ht)exp(-itHrun)||
       <=48h|t|.                                     (6)

There is no double-counted H0, no timed switch and no assumption that the selectors commute with the operating gadget. Equation(6) pays their actual induced sector leakage and all correlations throughout the horizon. The selector ground energy12e_sel is not a runtime scalar to be added: the exact identity scalar introduced by these installed fields is48h, and their remaining operator is paid by(6).

Thus if the parent complete vector error is d(t) and its absolute flag error is f(t), the new ideal-rest bounds are d(t)+48h|t| and f(t)+48h|t|, with identical target fields and an extra common phase exp(-i48ht). The final complete phase is

    exp{-it[48nu+s_joint+scale*cbar+48h]},
    cbar=8bbar+8(sqrt(2)-1)jbar.                        (7)

There is no original-head chemical potential and no separately appended bias or selector-ground phase. The q-dependent radial profile, its -i factor, incoming translation, positive finite normalization and unnormalized whole-horizon branch are unchanged.

## 4. Explicit simultaneous budgets, cap and counts

Choose0<epsilon<=1. Instantiate b74d's complete prescription at tau=epsilon/8 and simulation allowance epsilon_g=epsilon/16, including its finite T and all coefficients. It has final vector error<3tau/8+epsilon_g and whole-horizon flag vector error<tau/2+epsilon_g for the nominal signed-cat comparator. Select the positive field strength to be EXACTLY

    h=min{Delta/(4*32^3), Delta*epsilon/3840,
                                      epsilon/(768T)}. (8)

Then the selector spectral condition holds,480r_h<=epsilon/8 and48hT<=epsilon/16. A sufficient preparation-quality criterion is

    q_blank<=epsilon^2/512,
    E_sel<=g_sel*epsilon^2/512.                         (9)

Equations(5),(9) give epsilon_rest<=epsilon/4. These are supplied initial-state inequalities, not outputs of an assumed cooling dynamics. In particular (9) requires energy excess above the EXACT selector ground, not merely small energy relative to the unperturbed cat expectation4h per square.

Combining the state error, parent simulation and(6), on the final relative-width window the complete unhalved channel discrepancy is at most

    epsilon_rest+3tau/4+2epsilon_g+2(epsilon/16)
       <=19epsilon/32.

For every0<=t<=T the SAME absolute record-1 branch target has complete subnormalized channel discrepancy at most

    epsilon_rest+tau+2epsilon_g+2(epsilon/16)
       <=5epsilon/8.

Its ideal branch remains a contraction; there is no conditioning on a possibly rare flag. The final joint event (F support, R1, original non-F head vacancy, signed-cat comparator subspace) has probability at least

    1-(3tau/8+epsilon_g+epsilon/16)^2-epsilon_rest/2
       >=1-121epsilon^2/4096-epsilon/8.                (10)

The old P/E information is still relocated to Q/E by the nominal entrance gauge, while the actual residual correlations are retained in these complete-output errors. The passive input and preparation references are acted on by identity.

No sites or two-body couplers are added. There are48 additional onsite positive blocks, so the total is175+4ell qubits and313+4ell listed blocks. Each ancillary load becomes2Delta+2nu+2h<Lambda under(8) and the parent's alpha<=1/(32K); all other loads are unchanged and belowLambda. Every selector field is real positive and onsite; it stays within the already enlarged arbitrary-positive two-body-or-less class and does not increase range35. Its coefficient h is an additional supplied magnitude, not a demonstrated native control.

The runtime T and ell are unchanged by(8), so their sufficient orders remain Lambda^-1 epsilon^-17 log^5(e/epsilon) and epsilon^-3 log(e/epsilon). As epsilon tends to zero, the third entry in(8) eventually dominates:

    h=Theta(Lambda epsilon^18/log^5(e/epsilon)),
    g_sel=Theta(Lambda epsilon^72/log^20(e/epsilon)).

The sufficient absolute energy-excess allowance in(9) consequently has order Lambda epsilon^74/log^20(e/epsilon). This large cost is explicit. It is not a cooling-time, measurement-precision or necessary-temperature theorem. The actual selector gap is of the same order by(1)--(3); even this fact refers to A_sel, not to Hrun,sel's spectrum.

## 5. What the certificate does and does not supply

The selectors are a permanently present local observable whose separately analyzed ground state selects the desired ancillary signs and approximates the runtime cats. The small-energy-excess assumption converts into a joint complete-state distance with reference retention, and the fields' runtime disturbance is paid uniformly. This replaces a direct cat-fidelity assumption by an optional quantitative local-energy assumption; it does not show that an arbitrary initial state attains it.

The full running Hamiltonian also contains data couplers and the router background. Its ground state need not be Psi_sel, and small total energy is not the same as small selector excess. No bath, thermalization, autonomous cooling, measurement, ground preparation, input loading, reset or timing mechanism is supplied. Blank R and original heads still need their own stated quality; their old Gibbs/head-gap certificates are not revived. The supplied dual-rail input, arbitrary positive finite-range real blocks, absent unwanted couplings, exact coefficient correlations and complete-output observation contract remain premises. No native realization, nearest-neighbor compilation, old literal processor transfer or permanent halt follows.

## 6. Exact sources and author exposure

Paths are relative to N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934.

- The isolated analytic coefficient, sector gap and normalized eigenvector interface come from common_product_loader_bond_realization/PROPOSAL.md7e6769927d3138b2812e0b4a0db62df1ef4d1d7096b10acfa2269a5ca8a98d39 and its fully read distinct reviewf71cdc4e4039f923f99c8ed1f2abab9baedee9f8f9456c1d77ed6a9978b9fd58. Their complete earlier reads are reused at the isolated-square scope. The specialization to two scalar-sign sectors and the gap/energy certificate here are new derivations.
- Real gauge common_product_real_two_body_gauge/PROPOSAL.md1cc8b14dabd52a73f90bedf0186d7c3c92d02a9608aa72ce01ff0303fa3fe1f3 and its distinct review603671b279be1867d9aabca527ac0142bee3e9d915eccf4ed050a2d9ae29db4a were fully read and hash verified here. Its exact signs, T sectors and all-output phase convention are retained.
- Unpenalized source common_product_two_body_runtime_penalty_removal/PROPOSAL.mdb74d8f05658f6718dfcb4d9a050c6ddca90a357eabeb9dfed9c042567b36d9bb was authored and fully read in the preceding task. Its complete distinct review common_product_two_body_runtime_penalty_removal_check/REVIEW.md64174ac689b6894ebfdf69369bdeb6816501ce15388cce6db5dd232d651b4337 was read and hash verified here, supporting the actual real-gauge combination, full-state norm/count/cap and finite contract. Its reported checked quadratic dependency388eb/review39e567 is used through that operating interface, not claimed as a new check here.

ROOT proposed a static signed transverse-field selector, requested a joint reference-safe certificate, and highlighted the need to keep the fields installed and pay their norm/time cost. This author derived the two-sector splitting margin, unique-ground conclusion, twelve-square projection inequality, transformed-sector caveat, exact scalar, simultaneous budgets and energy-allowance order after that exposure. This is same-model source-exposed author work requiring a distinct check, not independent confirmation or a preparation-success claim.

After this draft's union-bound certificate was written, ROOT also suggested either a combined diagnostic energy operator or the same commuting-projector union route. The present source retains(5); it does not install an additional blank-head penalty or identify any diagnostic energy with the actual runtime Hamiltonian.

The decisive check should challenge the sign/sector specialization of(1), remainder versus fourth-order splitting, uniqueness relative to all other states, joint environment projection, actual absence of T-sector invariance, selector-versus-runtime energy distinction, scalar48h, and every budget/count/cap in(8)--(10). Only this proposal was created. No scientific executable, numerical sweep, delegation, old source/W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred.
