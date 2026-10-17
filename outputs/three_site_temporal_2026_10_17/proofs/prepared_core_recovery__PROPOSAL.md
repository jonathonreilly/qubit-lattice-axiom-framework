# Prepared open-channel recovery from a discrete dwell identity

Status: **bounded source-exposed author derivation; distinct check pending**. The unchanged emitter-free background admits a useful improvement without a new calibration or numerical inverse. The checked derivative of the ORIGINAL physical scattering matrix bounds the old finite core plus its closed tails for unit open incidence by 30. Carrying that prepared propagation through the existing converter, input cap and wide gate gives

    ||L(E)||<14000,
    ||R(E)F(E)||<7.29e16,
    ||L'(E)||<1.00068*(7.29e16+3.31e7/g)+30.                 (1)

In particular these hold on the prepared open column. The final displayed bounds actually retain the entire forcing fiber: the large complementary recovery maps are multiplied by their explicit small incident coefficients rather than discarded. The derivative improvement is less dramatic than the value improvement; its main arbitrary-inverse loss is still present.

For the three-site source, the new value bound also gives a separate **all-time absolute background-amplitude** estimate, without differentiating its resonant coefficient. On the stated two-window union it is at most

    [8 sqrt(2)/(3 pi c_3)] kappa*14000,                      (2)

plus the actual omitted seed amplitude, where c_3 is the full three-site inverse margin defined below. This excludes the three new source sites themselves. At the root-suggested illustrative lambda=1e-13, g=5e-8, the available background comparison implies c_3>.9999947 and (2) is below .000505. This does not establish a complete runtime or select a final operating point.

## 1. Source contract and exposure

The controlling background source is

`../slow_lead_wide_derivative/PROPOSAL.md`, 14321 bytes,
SHA256 `c2b9d6917db45faa1e9974cb69ef9bc683f45147bcb47b3588df36e94b630f2a`.

Its complete selective check was read at
`../slow_lead_wide_derivative_check/REVIEW.md`, 10045 bytes,
SHA256 `c74a8118cccafe3e64dc6f4aa499fc7fa9abb194dae5cedbb2c253fb06054c79`.
That check supports the older conditional real-band bounds, not the new argument here. Its prior author-exposure disclosures remain its own.

The unchanged domain is

    .0027<j<.003,  0<g<=1e-6,  0<h<=4e-6,
    d=2j sin h,  d/g<=.5.                                  (3)

The emitter is removed and its input-endpoint diagonal is retained. F=R V_p is the exact finite endpoint-forced column on all 235 background heads, each carrying the full eight-coordinate fiber in a fixed parity/record sector. L adds every closed slow tail; the propagating stationary ray is excluded. The two physical old-energy windows, both lips, all wrong-window input columns, the literal shared B/K, record sectors and global scalar retain their original meanings. No claim that the full Hamiltonian commutes with K is used. The background estimates have no kappa restriction because no emitter is included.

Complete additional readings in this task were the sharp physical-column source, direct-action source, sharp prepared-recovery source, record attachment/kernel, converter composition, fourfold-band extension, wide endpoint source and the root three-site inverse. The necessary original canonical passages, lines 175--319 and 1386--1518 of `correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md`, were read completely; its identity is SHA256 `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`. These supply the physical matrix, filter, phase conventions and the scattering derivative used below. This is not a complete new audit of that large note or a numerical revalidation of its M16/calibration premises. The unchanged wide-gate bounds are reused at their previously read and checked identity.

Root exposed the large arbitrary-inverse loss and suggested a prepared-column or dwell route, then suggested lowering lambda as a possible fallback. These are author inputs, not evidence that a runtime target must be achievable. My preceding slow-prefix escape proposal `96f36cae6669b5d8aff4a0604705b130a50efc358b79a29af4a9232edc8f6010` remains pending distinct checking and is **not used** here. No new source hardware is introduced in this proposal.

## 2. Exact discrete dwell identity at fixed old port planes

Fix one old energy and parity. Temporarily use the original unconverted two-port device, with two outgoing old-J leads cut just beyond m=40. Let O consist of its 90 original arm heads and 82 buffer heads, including the two sites at m=40. Its two OPEN incoming amplitudes form a vector a. All seven closed directions at each port have decaying tails and no prescribed closed incidence in this paragraph.

Write z=exp(ik), v=2J sin k and let S_B(k) be the physical two-open-port scattering matrix at these outer m=40 planes. Thus the open boundary value is `(I+S_B)a`. Let Psi(k) map a to every finite O coordinate and let Psi_C,tail recover all closed tails beyond the two boundary sites. The projectors of the shared B are fixed on this window.

After eliminating all exterior rays, the finite equation is

    M(E) Psi=V_open (i v) I_2,
    M(E)=E I-H_O+J V_full Q(E) V_full^T.                    (4)

Here V_open selects the two OPEN boundary coordinates and V_full includes the complete boundary fiber. The physical matrix H_O is energy independent and real symmetric. For a signed real closed root q_c,

    J dq_c/dE=q_c^2/(1-q_c^2)>0.

Therefore the positive closed part of M'(E) is exactly the closed-tail norm metric. The open derivative is

    J dz/dE=-1/2+(i/2)cot k.

Differentiating (4) with incoming a fixed and using current conservation `S_B^* S_B=I` gives the exact Gram identity

    Psi^* Psi+Psi_C,tail^* Psi_C,tail
      =-i S_B^* dS_B/dk
                       +I+Re S_B+cot(k) Im S_B.             (5)

Here `Re S=(S+S^*)/2` and `Im S=(S-S^*)/(2i)`. The two extra boundary terms and the identity are necessary at this discrete port convention. The bare Wigner--Smith term alone is not the finite-coordinate norm.

For an explicit sign check, `M-M^*=i v V_open V_open^T` and `V_open^T Psi=I+S_B`, so

    M^* Psi=-i v V_open S_B,
    Psi^* M' Psi=i v'(I+S_B^*)-i v S_B^* dS_B/dE.

Subtracting the open `J z'` term and adding its explicit value gives (5). The remaining positive term is the full closed-tail Gram matrix. This uses adjoints in a physical inner product; it does not replace transpose symmetry by an adjoint in a retarded Woodbury formula. It neither assumes normality of M nor commutes K through M.

Consequently

    ||[Psi;Psi_C,tail]||^2
       <=||dS_B/dk||+2+|cot k|.                             (6)

This is useful only with an actual scattering derivative at these exact planes. A small value of reflection or a favorable central phase would not establish (6)'s right side.

## 3. The available scattering derivative really gives a small dwell bound

The canonical original proof supplies, throughout its unchanged old interval `k0+[-1e-6,1e-6]`,

    |dr_g/dk|<=700,
    H=r_scalar+r_g,  |dH/dk|<23,
    delta_r=r_modified-r_scalar,  |d delta_r/dk|<3e-8.        (7)

The last inequality is an actual analytic-disk/Cauchy estimate in the source, not a derivative inferred from its tiny real value. Thus

    |dr_modified/dk|<723+3e-8.

At the original port origins the exact matrix is

    S_old=z^90 U diag(r_g,r_modified) U^T,
    U=2^(-1/2) [[1,1],[1,-1]].                              (8)

Both actual terminated-arm reflections have modulus one. Moving both reference planes from m=0 to m=40 gives

    S_B=z^80 S_old,
    ||dS_B/dk||<80+90+723+3e-8<894.                         (9)

The actual sharper sum is below 893.0000001. Since sin k>.4, `|cot k|<2.5`. Equations (6)--(9), using that sharper sum, give

    ||[Psi;Psi_C,tail]||^2<898<900,
    ||Psi||<30.                                           (10)

Every old finite coordinate and its source excitations are present. The 80-step phase derivative explicitly pays the two 40-site buffers; they cannot be dropped and then called free propagation. The original source domain has not been enlarged: the checked nominal energy map gives `|k(q)-k0|<.24|q-pi/2|<=.96e-6` on (3).

For comparison, the earlier physical proof paid a per-site filter bound and obtained 800 before converting the incoming velocity. The present 30 is a different conditional calculation from the checked physical scattering derivative, not a fitted numerical dwell time. The calibration value d0 remains part of the source assumptions; no exact W calibration is asserted by (10).

## 4. Carry the prepared propagation through the two converters and input cap

Consider a unit OPEN incoming vector on the two NEW j ports. The unchanged converter feedback bounds give total old incoming open norm

    ||a_old,P||<=chi/(1-rho_converter)<.5.                   (11)

Open translation to m=40 is unit modulus, so (10) bounds its old finite response by 15. Closed incidence must be treated at the same outer plane, rather than multiplying an unstructured tiny number by a growing root. The exact return is

    a_old,C(at m=40)=R_c Q_old,C^40 b_old,C,
    ||R_c||<1/5,  ||b_old,C||<6e-12 ||a_old,P||.

Since `7^40>1e32`, its norm is below `1e-44`. The already checked original boundary column bound is

    ||G_old(O,B)C||<8,  ||A_old^-1||<20.

Thus arbitrary CLOSED incidence at this outer plane has finite physical recovery below 160. This is the exact forcing `G_old(O,B) A_old^-1 a_C`; it includes all complementary directions. Its contribution here is below `160e-44`, not zero. Therefore the converter-loaded old finite recovery map Phi_old satisfies

    ||Phi_old P_twoports||<16.                              (12)

The full complementary map retains the old conservative bound `||Phi_old||<3e10`. Equation (12) replaces the old selected 600 bound only where the incoming coefficient is open.

Next impose the input cap and send a unit selected incident wave from the output. The unchanged exact cap calculation gives

    ||alpha_open,bothports||<1.5,
    ||alpha_input,C||<4*60^-42.

Thus the 172 old coordinates have recovery below 25: use (12) on the first term and `3e10` on the second. The 21 retained input sites have per-site norm below 4.1, with the literal relation `alpha_input,C=-Q_C^42 beta_input,C` preserving every canceled growing power. Their stack has norm below 21. If K_U is the input-terminated source's recovery from selected output incidence, its relevant restrictions therefore obey

    ||K_O P||<25,
    ||K_input P||<21,
    ||K_U P||<sqrt(25^2+21^2)<33.                           (13)

Keep `||K_U||<2e18` for arbitrary complementary incidence. No closed map is called small merely because the selected map is small.

## 5. Actual endpoint forcing and complete wide-load recovery

All identities and wide-gate amplitudes in this section are those of the unchanged emitter-free background. Before attaching the gate return, the exact endpoint forcing coefficient alpha has

    ||P alpha||<400,
    ||C alpha||<3e-23.                                     (14)

These are operator norms on the full eight-coordinate forcing domain. Equation (12), together with the retained complementary Phi_old bound, gives

    ||F_O,free||<16*400+(3e10)*(3e-23)<6401.                (15)

The direct finite input range retains its full-forcing bound 4670. This includes the forced endpoint and the closed forcing there; no wrong-window column is projected away.

The wider gate and its actual 18-edge return provide the unchanged coefficients

    ||P a_return||<59.34,
    ||C a_return||<1280e-63,
    ||F_cable||<9000,
    ||F_gate+closed-slow-tails||<3270.                       (16)

The closed outgoing cable amplitude at its origin is included in 9000. It is not suppressed there merely because it is suppressed at cable site 17. Using (13) separately on old and input coordinates, while paying `2e18` on the closed return, yields

    ||F_O||<6401+25*59.34+tiny<7900,
    ||F_input||<4670+21*59.34+tiny<6000,
    ||F_N||<sqrt(6000^2+9000^2)<11000,
    ||F_U||<sqrt(7900^2+11000^2)<14000.                     (17)

Here N is input plus cable, U is old plus N, and each omitted tiny term is at most `(2e18)*(1280e-63)<3e-42`. Combining the four disjoint physical output ranges,

    ||L||^2<=7900^2+6000^2+9000^2+3270^2
             =190102900<14000^2.                            (18)

This proves the first bound in (1). Orthogonal range aggregation is valid for a common forcing domain: it does not assume the error outputs of the two old-energy windows are orthogonal. The same result holds on the lower lip by fixed real conjugation, and passive-reference tensoring preserves it.

The endpoint comparison still has its separately controlled small cross blocks, `||G_PC||,||G_CP||<1e-23`, and complementary error `||G_CC+Q_C/j||<2e-24`, on the current wide-load domain. These are endpoint facts. They do not imply that the entire recovery column L C is tiny: a closed source at the physical endpoint can have a real local response. Both that response and the wrong-window prepared vacuum input are retained in (14)--(18).

## 6. A conservative derivative improvement, and the loss that remains

The new partition bounds can be inserted into the already checked exact direct-action calculation, without changing any full inverse. Retain

    ||G_c||<3e10,  ||L_n||<14.1,  ||J_lift||<14.2,
    ||D_n||<8800,
    ||G_2(:,b)||<130000,  ||Z^-1||<24,
    ||G_2(b,O)||<120001,  ||G_2(b,N)||<3220,
    C_a=220000,  ||D_gate||<.102,
    ||[I+G_D(a,a)D_gate]^-1||<4.6.                        (19)

The notation J_lift is the old finite-coordinate lift, not the hopping J. Extend the actual F_U by zero at the deleted input site b. The exact transpose lift and ordered Dirichlet/load formulas are unchanged. Equations (17)--(19) give

    ||J_lift^T f||<7900+14.1*11000=163000,
    ||G_2 f||<8800*11000+14.2*(3e10)*163000<6.944e16,

    ||G_2(b,:)f||<120001*7900+3220*11000
                    =983427900<9.84e8,
    ||G_D F_U||<6.944e16+130000*24*(9.84e8)<7.252e16,

    ||R_u F_U||<7.252e16
                  +(220000)^2*.102*4.6*14000<7.285e16.     (20)

Restoring all gate coordinates uses the existing cross-block ceiling `6.4e6`, gate diagonal ceiling 86000 and `||F_G||<3270`. Thus

    ||R F||<7.285e16+(6.4e6)*(14000+3270)+86000*3270
                <7.29e16.                                 (21)

These are still bounds on actual F, not replacements for an arbitrary-forcing inverse. All retarded transpose factors and their orders remain those of the source proof.

The exact assembled derivative is

    F'=-R F-j R V_o Q_slow' V_o^T F.

The existing `||R V_o||<6.5e6`, `||V_o^T F||<3270` and `||Q_slow'||<1/(1.93g)` give

    ||F'||<7.29e16+3.31e7/g.                                (22)

The complete closed-tail lift has norm below .00068 and derivative norm below .009. The latter multiplies the actual OUTPUT value, below 3270; there is no need to pay the whole 4e5 column again. Hence

    ||L'||<1.00068*(7.29e16+3.31e7/g)+.009*3270
           <1.00068*(7.29e16+3.31e7/g)+30.                  (23)

At g=5e-8 this is below `7.37e16`, compared with the previous relaxed `6.49e17`. The value recovery improved by more than a factor 28, but the derivative only by about a factor nine. In (20), the term `G_c J_lift^T f` still uses the arbitrary inverse 3e10 on the structured physical forcing. The dwell identity supplies a value norm; it does **not** turn the checked first scattering derivative into a bound on the derivative of every recovered wavefunction.

A sharper derivative target is therefore explicit: bound `G_c(E)J_lift(E)^T f(E)P` directly, or bound the physical `d(Phi_old(E)P)/dE` and all cap/return coefficient derivatives. The original 16-site contact equations and two-filter-site equations provide a finite route. Small real cross values alone do not bound their derivatives, and the first derivative of S alone does not certify short delay or a small recovery derivative. Those additional calculations are not claimed here.

## 7. A three-site absolute-integral consequence that avoids L'

The separately root-authored full-fiber three-site source is

`../three_site_loaded_inverse/PROPOSAL.md`, 4617 bytes,
SHA256 `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672`.

Its original status remains a distinct conditional source interface. Only its displayed algebraic inverse bound is used in this section; no source mass, native implementation or full runtime is imported. Define

    a_1=lambda/sqrt(3),  a_2=lambda sqrt(8/3),
    kappa^2=3j lambda,  r_s=lambda/j,
    c_3=(1-Theta_3)sqrt(1-3r_s)>0.                          (24)

Under its stated full background matching and Theta_3<1 condition, its last-source resolvent column for seed forcing f is

    psi_2=a_1 a_2 Q_3^-1 f,
    ||Q_3^-1||<=1/[c_3(delta^2+lambda^2)^(3/2)].             (25)

The complete BACKGROUND column from that seed is exactly `-kappa L(E) psi_2`. This is all 235 background heads plus closed slow tails, not the three new source coordinates. In particular the ordered noncommuting full Q_3 inverse remains; it is not replaced by its selected scalar entry.

For one physical window, the spectral jump has factor `1/(2pi i)`. Bounding both lips separately by (18), (25), and

    integral_(-d)^d d delta/(delta^2+lambda^2)^(3/2)
       =2d/[lambda^2 sqrt(d^2+lambda^2)]<=2/lambda^2,
    a_1 a_2=(2sqrt(2)/3)lambda^2,

gives the all-time background vector bound

    4sqrt(2)/(3pi c_3) * kappa*14000                       (26)

per window. Paying the two physical old-energy windows by the triangle inequality gives (2). Parity and record-X sectors are orthogonal and require no further factor; the initially prepared record weights are retained. The full-forcing norm makes the bound valid on arbitrary old/reference input, including wrong-window columns. Lower Q_3 is treated on its own lip, not assumed to be the upper inverse's adjoint.

If eta_out is an independently established omitted amplitude for the ACTUAL three-site seed on the common two-window union, the total background bound adds eta_out once. No one-site or two-site emitter mass estimate is reused. At t=0 the background amplitude is zero; a nonzero all-time upper bound is consistent with that and does not assert permanent trapped mass.

The scale in (2) is `kappa L_0`, hence proportional to sqrt(lambda), whereas an oscillatory derivative term is proportional to `kappa M/t`. This alternative can be useful when a modest uniform background budget is acceptable. It cannot certify arbitrarily small local error at fixed lambda from the displayed constant alone. For example, at kappa=3e-7 the sufficient choice `L_0<=2.77e3 c_3` would make (2) less than 1e-3; the present 14000 does not certify that illustrative budget at that coupling.

## 8. Quantifying the lower-lambda fallback without choosing a runtime

The root-suggested lower value is a separate possible operating choice, not the earlier concentration point silently optimized. Take, only for this calculation,

    lambda=1e-13,  g=5e-8,  h<=4e-6,
    kappa=sqrt(3j lambda)<3e-8,
    t=20/lambda=2e14.                                    (27)

The wider endpoint's BACKGROUND comparison, which is independent of an attached emitter, supplies

    a_0=8e-18,
    b_0=46000/.0053+290/g<5.81e9,
    d<=2.4e-8.

The three-site perturbation expression is

    Theta_3=(j a_0+kappa^2 b_0)/sqrt(1-3lambda/j)
                           +6kappa^2(a_0+b_0 d).

Using (27), `lambda/j<3.71e-11`, and the displayed bounds gives

    Theta_3<5.24e-6,
    c_3>.9999947.                                        (28)

This is a bound from the existing physical reference and full background envelope; no imaginary Markov bath has been placed on the complementary B eigenvalues. With `sqrt(2)<1.415` and `pi>3.14`, (2) is then strictly below

    .000505 + eta_out.                                   (29)

Thus a sharper L' is **not a necessary gate for a small background contribution at the lower coupling**. This statement is conditional on actual three-site spectral regularity/mass and concerns the background only. The three source sites, outgoing waveform, its common scalar/W/old aging, and finite receiver require their separate estimates at x=lambda t=20; those are not derived or imported here. Root reported separately checked three-site local and outgoing work during this drafting. That report is context only, and this proposal does not duplicate or endorse those distinct calculations.

The root's coarse-derivative heuristic also has the favorable stated scale. At (27), using the old `M=6.49e17`,

    kappa M/t<9.735e-5.

Using the new g-specific bound `M=7.37e16` gives `<1.106e-5`. The actual coefficient on the L'-part of the two-window integration-by-parts estimate is at most `8sqrt(2)/(3pi c_3)`, giving respectively `<1.18e-4` and `<1.34e-5` under (28). These are contributions, not complete local-escape bounds.

To display what that heuristic omits, define

    D_3=a_1 a_2 * sup_(window,lip)
           integral_(-d)^d ||d(Q_3^-1 V_seed)/dE|| d delta.

Here V_seed is the actual prepared internal inclusion on that window. A direct integration by parts for the background has, in addition to the L'-term, the sufficient allowances

    2 kappa L_0 D_3/(pi t)

and the two-window/two-lip hard-endpoint contribution

    [8sqrt(2)/(3pi c_3)]
          * kappa L_0 lambda^2/[t(d^2+lambda^2)^(3/2)].       (30)

An actual bound on D_3, rather than a presumed scalar decay envelope or a value-only perturbation bound, is needed if this oscillatory route is used. The absolute-integral route (29) avoids D_3 for the background, but does not settle the source-site or output estimates. Therefore the old coarse derivative is plausibly compatible with the lower-lambda scale; it alone does not prove that the complete apparatus meets a target at t=2e14. No optimized lambda or selected performance theorem is claimed.

## 9. Exact dependencies, limitations and next check

The decisive new check is (5), including its boundary/self-interference terms and closed-tail norm; the use of the ACTUAL original scattering derivative and all 170 propagation-phase derivatives in (9); the converter-plane conversion in (11)--(12); and the physical range accounting in (17)--(23). The three-site integral (26) must retain both lips, two physical windows, the full inverse, and one actual omitted-state charge. If any of those fail, the older checked wide derivative remains available unchanged.

Complete source identities used in this task:

- `slow_lead_forced_derivative_sharp/PROPOSAL.md`: `662b64aa1d7714746abaa585f8e1af17ece308771b5c9de25f88fde03bb787c0`.
- `slow_lead_direct_forcing_refinement/PROPOSAL.md`: `f9fdcaa59e3b2d58805d295cb2dd63d4c7c763917ee8099b90afb2ec3c0db909`.
- `record_attached_recovery_sharp/PROPOSAL.md`: `07320d9a2e7c4db6c7479be0c59064749dcd73209d0847db8327b1963465ef11`.
- `record_attached_kernel/PROPOSAL.md`: `fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457`.
- `bandcenter_converter_composition/PROPOSAL.md`: `1cc6fec524a8184f844711a4fa6d72fcc7cd13a4c8b413cbc064cd4b2201df78`.
- `bandcenter_bandwidth_extension/PROPOSAL.md`: `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`.
- `slow_lead_wide_endpoint/PROPOSAL.md`: `c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3`.
- Unchanged wide gate `slow_lead_wider_receiver_band/PROPOSAL.md`: `5b667173cd9ee3d8faa285e5856e8a89e8a83ae87f09207664cc5115e247ee57`, with its checked scope reused through `slow_lead_wide_derivative_check` and the prior complete reading. Its distinct gate check is `9c32a1c901300c32cb6d0630cfef19e9aa33b9438274b6ab8dc561ccc2a38b0d`.

The source calibration, M16/filter and geometry premises remain conditional at their original identities. The Wigner--Smith identity is derived here for this discrete port convention; it is not an appeal to unspecified small delay. The remaining large derivative term and the unbounded D_3 obligation are exposed rather than hidden in a preferred runtime. A useful next focused calculation is the prepared physical contact/filter derivative, or direct action of G_c on the structured recovered forcing, if the all-time background budget is insufficient.

This is the sole new file. No scientific program, inverse, sweep, ODE or spectral simulation was executed; no source was imported as executable code. No Git/canonical/checkpoint/prompt/axiom edits, publication, model override, delegation, source-history modification or audit verdict occurred. File reading/hashing is metadata work, not independent mathematical evidence. The result is an author proposal awaiting a distinct check, not a retained full-output theorem.
