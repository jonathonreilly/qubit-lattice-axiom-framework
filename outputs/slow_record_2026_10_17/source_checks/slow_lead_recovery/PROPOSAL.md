# Slow-output attached device: complete local recovery difference

Status: authored conditional derivation, requiring distinct checking. The modified gate premise now has a distinct selective check; its underlying physical premises remain conditional. For the actual g=10^-6 output replacement, this derivation gives full-input background recovery L0=4e5 and sector difference

    ||Delta L|| <=4121+5.5e9 |delta|.                 (1)

The recovered range includes every finite source/cable/gate vertex and all slow CLOSED tails, excluding the propagating slow ray. The reduced constant 4121 comes from the actual forced gate column, not its whole inverse. The upstream slope uses the gate RETURN DIFFERENCE <=68u, not twice its individual reflection <=1540u. The emitter/core formula and spectral integral below remain conditional on NEW modified-device emitter and spectral estimates. No old emitter, mass, runtime or complete-output theorem is imported.

## Sources and prior exposure

Read completely the unchanged `../record_attached_recovery_sharp/PROPOSAL.md`, SHA256 `07320d9a2e7c4db6c7479be0c59064749dcd73209d0847db8327b1963465ef11`, and `../record_core_operator_difference/PROPOSAL.md`, SHA256 `69aa54015825bd6e240b1da5f856cb062157e2686d5403698592315fa4d529ac`. Their distinct checks are respectively `../record_attached_recovery_sharp_check/REVIEW.md` (cbd5dfd29fbe67ad36c3ffc97a896f55ea30b8a5af367930c48a080589523430) and `../record_core_operator_difference_check/REVIEW.md` (ad38a71087013fcee8f9ef7f00f62177d053c7ff03ba5573b524bbc3f9993357). Check-path labels are provenance, not substitutes for the arguments.

The changed local input is my `../slow_lead_gate_load/PROPOSAL.md`, SHA256 `c1e1fe95ca3c9d390df0fad468c80c93d4c1c2aa1e3fee4c93c4326f44b0e61d`, whose complete distinct check `../slow_lead_gate_load_check/REVIEW.md`, SHA256 `8fb22bfddeeda9dd8abd1f3c90bafe4fd34916ec385d47aa017c99b08b221a65`, was read before finalizing this proposal and supports its stated local scope. It uses the checked scalar slow-interface source a9795085bd36acbdaee9de8e46709f1a61c5065d5c6f0dadc37f8bb151f962e4/check ecec86951cdb2f36011e196fe8266bffec29f55a6d0ec8f67e4bfe5684a578fb and the actual attachment fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457. The unchanged local inverse premise is 3fb72f1629c0136531a41424683279a1b42f3a54bda4785359a367c018756c82/check cebb4153f1f1f75001614110ad7597fcf5b835ddad2ab15e0d57c1e089f0f67f.

I authored the sharp recovery, operator interface, slow-gate derivation and prior all-time synthesis; this is not independent verification. Root exposed the common-reflection cancellation and forced-column sharpening. Unchanged source/filter/finite-input premises are reused from sections 1–3 of the sharp recovery, whose canonical original-note dependency is SHA256 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff. Only downstream loading is changed here. All calibration, original inverse and supplied physical premises remain conditional. No solver, sweep, experiment, delegation, Git/W/publication/checkpoint/model/prompt changes occurred.

## 1. Unchanged upstream maps and changed boundary condition

Fix one selected real energy window, u=|q-pi/2|<=4e-6 and delta=E(q)-2j, with |delta|>=.0053u and |delta|<2.4e-8. Work in one parity with its full eight-dimensional fiber. P is the one open B channel at this energy and C=I-P. It is NOT a restriction of the prepared-input domain. The source is unchanged, including noncommuting contacts and K. Its input is capped exactly as before. The unloaded outgoing forcing B_e, terminated scattering S^D and recovery K_U on the 193 noncable upstream heads obey the unchanged upstream-only bounds

    ||P B_e||<400, ||B_e||<521,
    ||S^D||<2e8, ||S^D P||<3,
    |S^D_PP|=1, ||S^D_CP||<2,
    ||K_U P||<1000, ||K_U||<2e18.                 (2)

These follow from physical selected incident waves, finite filter/buffer recovery and the EXACT endpoint forcing bracket in sharp recovery sections 1–3. In particular its full forcing coefficient has ||P alpha||<400 and ||C alpha||<3e-23. Growing closed factors on input sites are bounded using A_C Q_C^(20-n) C B_br, not by amplifying the latter tiny scalar bound. The unloaded finite arms/buffers cost <240001 and the 21 input sites cost <4670. These quantities are all defined BEFORE attaching any output return, so replacing that return does not change them.

At v0 the new diagonal return R_x has

    ||P R_x||<=1540u<r=.0062,
    ||P(R_+-R_-)||<=68u,
    ||C R_x||<e=10^-63.                            (3)

The open sector difference follows from the exact two-port denominator and signed transmission product, as proved in the slow gate note; the common leading reflection cancels. The cable plane multiplies open returns by w^36 of modulus one. For closed channels the stronger literal form |s|^36 |r_gate,x|<3*60^-36 is retained whenever a growing cable root occurs. These are actual load statements in both record-X sectors, not an assumption about emitter spectra.

Let b_x=S^D a_x+B_e and a_x=R_x b_x, as operators from the ENTIRE endpoint forcing fiber. Eliminating closed coefficients gives an effective selected source reflection differing from its unit-modulus value by <8e-47 and a selected forcing correction <3e-52. Thus

    ||P b_x|| < (400+3e-52)/[1-r(1+8e-47)] <403,
    ||C b_x|| <2(2*r*403+521)<1100,
    ||P a_x||<403r, ||C a_x||<1100e.              (4)

For clarity, the forcing correction follows directly from ||S_PC||<2e8, ||R_C||<e, closed inverse <2 and ||C B_e||<521. The source-reflection correction uses ||S_CP||<2. No modified emitter estimate is hidden in (4).

## 2. Difference feedback without paying the common reflection twice

Write A=||P(a_+-a_-)||. Since Delta b=S^D Delta a and ||C Delta a||<2200e, the exact identity

    Delta a=R_+ S^D Delta a+(R_+-R_-)b_-

gives

    A <= r A+r(2e8)(2200e)+(68u)403,
    A <=27600u+3e-54.                              (5)

The first coefficient uses |S_PP|=1. The noncommuting matrices have not been reordered: the selected diagonal return acts after S^D. A denominator 1-r=.9938 suffices. The numerical floor in (5) exceeds r(2e8)(2200e)/.9938. This bound is materially different from 2*403*1540u.

The upstream difference is therefore

    ||Delta L_U||
      <=1000 A+(2e18)(2200e)
      <2.76e7u+5e-42.                             (6)

For n=0,...,17 the cable field is Q^n b_x+Q^-n a_x. Its outgoing difference has norm at most 3A+(2e8)(2200e); its open incoming difference has norm A. For the closed incoming term use the literal returned field |s|^(36-n)r_gate,x b_C. At every retained site its two-sector bound is <6600*60^-19. Summing eighteen sites by sqrt(18)<5 gives

    ||Delta L_cable||<20A+1e-28.

Consequently a convenient safe envelope is

    ||Delta L_up||<=1e-24+2.9e7u.                 (7)

For absolute recovery, the closed outgoing coefficient at n=0 is NOT small: it costs its full <1100 in (4). Each cable site is bounded by 403+1100+403r+3300*60^-19<1506, and the cable norm is <7530. Upstream attachment costs <1000*403r+(2e18)*1100e<2499 in addition to 240001+4670. Thus ||L_up,x||<3e5 still follows for this NEW loading, rather than being inherited without recalculation.

## 3. Gate, closed tails and complete local recovery

At the last cable site n=17 the closed outgoing coefficient is suppressed by 60^-17. Equations (4) and the literal closed return give

    ||psi_x(v17)||<403+403r+1100*60^-17
                             +3300*60^-19<406.

The slow-gate proposal proves its actual forced-column map, including all gate sites and all seven slow closed tails, has norm <5.064. In particular the finite output port o is included; the slow propagating ray begins at the distinct first slow site. Hence each sector's gate-plus-closed-tail recovery is <406*5.064<2060, and its difference is <4120. No cancellation within these new local rows is assumed.

Combining orthogonal coordinate ranges, or simply adding their upper bounds, yields

    ||L_x||<4e5=L0,
    ||Delta L||<=4121+5.5e9|delta|.                (8)

The slope follows from 2.9e7/.0053<5.5e9; the constant 4121 pays 4120 and the upstream floor. Full B-channel norms are orthogonal direct sums, not eight times their largest block. The all-channel source maps in (2) and all endpoint input columns in (4) retain wrong-window input directions. The propagation ray itself is not in L: its generalized stationary wave is not square summable.

The infinite closed-tail range is legitimate in this extension of the core interface. On this compact band its geometric norm is uniformly bounded and norm-continuous, with ratio <1/160000. Thus its recovery column is a Hilbert-space-valued bounded continuous function whenever the finite Schur matrices are regular. The union of those seven channels is fixed on each selected window. A window-dependent closed-tail projection is used separately per window; its contribution is added by triangle inequality. This is a decomposition of represented spectral contributions, not one global time-independent closed-channel projection on the ray. The finite-site restriction itself is fixed. This does not project out any finite-site coordinates or initial-input directions.

## 4. Exact modified emitter/core column and both lips

Retain the actual common emitter block H_e, coupling -kappa V, and modified background sectors H_b,x. Define R_b,x=(z-H_b,x)^-1, G_x=V*R_b,x V, L_x=Q R_b,x V and T_x=(z-H_e-kappa^2 G_x)^-1. The exact full emitter/core column difference is

    F_+-F_- = [ kappa^2 T_+ DeltaG T_- ;
               -kappa DeltaL T_-
               -kappa^3 L_+ T_+ DeltaG T_- ].       (9)

This is the unchanged algebraic identity applied to the CHANGED operators. Its direct kappa DeltaL term survives. No old T, DeltaG, mass or density constants have been substituted. All matrices and coordinate embeddings are real in fixed conjugations, including the slow connector and record-X basis. The lower recovery columns are therefore conjugates of the upper columns and satisfy (8) as well, even for arbitrary complex input vectors. The actual jump remains (F_down-F_up)/(2pi i); it is not the entrywise imaginary part or adjoint of a rectangular upper column.

Assume separately actual seed spectral absolute continuity and Bochner jump synthesis on the selected windows, and omitted SEED amplitudes epsilon_x. These must be proved for the modified device. For closed tails the uniform geometric bound above supplies their Bochner range control once the finite boundary values and emitter inverses are supplied. It does not establish omitted mass or exclude unrepresented singular spectrum. Passive references preserve all operator norms, and shared K stays inside the actual blocks. No old-system evolution is commuted through recovery.

## 5. Explicit conditional all-time local integral

Suppose the new emitter derivation supplies, on BOTH lips and sectors,

    ||T_x||<=1/[c sqrt(delta^2+gamma^2)],
    ||DeltaG||<=a_G+b_G|delta|,
    gamma=kappa^2/j, kappa=10^-8, c>0.

Here c,a_G,b_G are new obligations, not old-device numbers. With d=2j sin(4e-6)<2.4e-8 define

    I_G=2a_G arctan(d/gamma)/gamma
                          +b_G log(1+d^2/gamma^2),
    I_L=8242 asinh(d/gamma)
                          +1.1e10(sqrt(d^2+gamma^2)-gamma).

For one selected window the all-time record-1 emitter and background integrals are bounded by

    Ecore<=kappa^2 I_G/(2pi c^2),
    Bcore<=kappa I_L/(2pi c)+kappa^3(4e5)I_G/(2pi c^2).

Because d/gamma<720000, asinh(d/gamma)<15 and sqrt(d^2+gamma^2)-gamma<=d,

    I_L<123894,
    Bcore<.000198/c + (4e-19)I_G/(2pi c^2),
    Ecore<=1e-16 I_G/(2pi c^2).                    (10)

The per-window local record map is at most sqrt(Ecore^2+Bcore^2), uniformly for every real time, conditional on actual synthesis. There are two physical old-energy windows per parity; add their error bounds, with no assumed orthogonality of their output errors. Orthogonal parity sectors combine by a maximum. The omitted seed term is then (epsilon_++epsilon_-)/2, charged once for the union of windows rather than once per local coordinate.

For scale only, the explicit sufficient NEW conditions c>=.98 and I_G<=10^10 would imply per-window <.000203 and two-window <.000406 before omitted amplitude. This is an implication, not a claim that the modified emitter satisfies those conditions. Equation (10) is the operative interface for whatever bounds its derivation actually proves.

These bounds concern the unnormalized absolute record-1 local/closed component. They supply neither a correct outgoing W profile nor a success lower bound, time of onset, normalized relative accuracy, finite-lead theorem or permanent record. The common physical scalar, literal K/W, all prepared input columns and native preparation/record-readout premises remain separate obligations of a complete theorem.
