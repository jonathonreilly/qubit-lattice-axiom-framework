# Installed three-site product-source interface and one spectral operating point

ROOT author construction; distinct check pending. This is an installed seed-concentration and resolvent-conditioning milestone, NOT a complete output/runtime improvement.

Use the exact unchanged background and coordinate inventory of two_site_actual_attachment/PROPOSAL.md 2c0e8fe8dac3dd70f50fbc945aa0fd29a5eacbac63468ff5983cc7abd5343f49, whose distinct review is c047ecef01b5512e21555d7de4deeae38660ecb83b4c2c98ec4e7353e5c56b8e. The port is p=(40,63,1). Reuse old emitter as s2=(40,64,1), and install s1=(40,65,1),s0=(40,66,1). The two additional coordinates are checked vacant and adjacent only along this extension. Seed s0 is occupied; all other heads, including s1,s2, are blank, shared sources in supplied vacuum and record0, with arbitrary old/reference input.

For0<lambda<=1e-8 put a1=lambda/sqrt3,a2=lambda sqrt(8/3),kappa=sqrt(3jlambda). Replace the old two emitter blocks by SIX fullspace positive blocks:

 j(n_s2+n_p)-kappa exchange_(s2,p),
 Q_a2(s1,s2), Q_a1(s0,s1),
 (j-a2)n_s2, (2j-a1-a2)n_s1, (2j-a1)n_s0.

Here Q_a=a(n_x+n_y-exchange_xy). Since kappa<sqrt(9e-11)<j, a2<2e-8<j and a1+a2<3e-8<2j, all blocks are PSD. Diagonals are2j at each new source and at p. Compressing out all three source sites retains exactly j n_p from the structured port block and nothing from the other five. Thus the emitter-free background H_bg and its full8 kernel G are literally unchanged. Shared B, c_att, literal K/W, all downstream phases and original calibration premises stay fixed. No source-state-copying or vacancy scalar is introduced.

Relative to PR9679's M-site receiver inventory, add TWO heads and edges and FOUR unmerged blocks: heads M+238, total qubits M+243, head edges M+239, positive blocks2M+281. These count a possible finite installation, not a sufficient output length. The largest new source incident norm loads in this decomposition are3j+a2 at s2,2j+a1+a2 at s1,2j+a1 at s0; the previous background load at p stays unchanged.

The same semi-infinite background bound applies on d=2j sin h,0<h<=4e-6,0<g<=1e-6,d/g<=.5:

 ||G-G0||<a0+b0|delta|,
 a0=8e-18, b0=46000/.0053+290/g,
 G0=m_j(D), D=E-c_att-2j-B.

It retains full8/closedchannels and original exact matching assumptions. Full source Schur is precisely the three_site_loaded_inverse/PROPOSAL.md 7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672 source matrix; that source's distinct check is a dependency, not supplied by this geometry. The actual seed sixth moment and union bound are those of three_site_product_source/PROPOSAL.md a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823, also requiring its distinct check. In particular local moments do not infer actual escape from isolated source decay.

Consider the single nominal choice

 lambda=1e-11, g=5e-8, h=4e-6,
 d=2j sin h, with the original calibrated j enclosed by .0027<j<.003.

These are specified hardware changes, not a parameter sweep or calibration fit. The geometric source's largest new coupling is kappa<3e-7<j. The old g/h band is admissible: d<2.4e-8<g/2. The elementary sine inequality sin h>=h-h³/6 gives d>2.15e-8. Also b0<5.809e9, r=lambda/j<4e-9, and sqrt(1-3r)>.99999999. Therefore the inverse proposal's new condition obeys

 Theta3=(j a0+kappa²b0)/sqrt(1-3r)+6kappa²(a0+b0 d)
       <.000523.

For an elementary enclosure kappa²<9e-14, the main term is less than(.003*8e-18+9e-14*5.809e9)/.99999999; the second is below6*9e-14*(8e-18+5.809e9*2.4e-8)<7.53e-11. Their sum is below.000523. This establishes full source matching conditioning if the cited inverse proof is accepted, not a dynamical success probability.

The actual installed sixth moment, including arbitrary downstream load, is mu6=3lambda^6+(8/3)jlambda^5<8.00000003e-58. The common two-window omitted seed STATE norm is consequently

 ||E_H(I^c)V||<=sqrt(2mu6)/d³<4.1e-6.

A simple squared check is2mu6<1.600000006e-57, while(.0000041)^2*(2.15e-8)^6>1.65e-57. This concentration includes all outside spectral types and arbitrary old/reference superpositions. It does not prove absence of in-band trapped mass by itself. The separate complete matching/inverse conditions supply local seed regularity, but no quantitative escape rate.

For comparison with an old certificate, this operating point has a smaller proved omitted-state allowance than PR9679's .00125 prepared-mass allowance. That is a comparison of one error component for DIFFERENT sources. It does not preserve the old outgoing packet, full .00191 metric, T1e15, M250m or record guarantees, and does not establish a better complete apparatus. A new waveform, all local/source/core/closed-tail and incoming bounds, source-relative runtime and finite cut remain necessary. The isolated scalar critical pulse is a candidate comparison whose transfer must be proved.

Exact nominal couplings and their correlations, product seed, selective interaction installation, physical Hamiltonian/Record identification and all inherited conditional calibration premises remain supplied. No permanent halt, reset/reuse, native supplier, total precision improvement or practical time scale follows. No editable prompt/physical axiom/canonical file changed.
