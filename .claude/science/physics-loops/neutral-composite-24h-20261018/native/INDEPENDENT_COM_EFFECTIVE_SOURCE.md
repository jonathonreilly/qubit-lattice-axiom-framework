# Independent nonzero-longitudinal-momentum effective-source check

Read `native/INDEPENDENT_FIXED_ORDER_SOURCE.md`, `/private/tmp/neutral_com_pole_root.md`, and the actual rows of `/private/tmp/neutral_bulk_second_boundary.json`. The proposed leading S-F vertex geometry and source limit are consistent. The limit remains conditional on the uniform outgoing fast-sector strip bounds; it is not a real-axis or full microscopic pole statement.

## Native endpoint mappings

For an axial-x slow interval [0,1] at separation (2,0), the JSON has exactly two shortening targets: the same two columns at layer 0 and at layer 1, each coefficient -1/2. These centers differ from the initial center 1/2 by +/-1/2. Their Fourier sum is -gamma, gamma=cos(p/2). The axial-y versions have raw +1/2; their transverse relative sign supplies precisely the d2 combination, consistent with the existing orientation gauge.

The same axial-x row has two adjacent-column ell=2 targets, [(0,0),(1,0)] and [(1,0),(2,0)], each coefficient -1/2. Both keep the longitudinal interval [0,1], so their center is unchanged. Axial-y has the analogous two targets, again -1/2. Thus the normalized scalar axial source A couples to the fast ell=2 arm endpoint e with the unchanged coefficient -1, whereas its shortening coupling to the fast same-layer d2 host is -gamma.

For diagonal slow separation (1,1), the row has four adjacent-column ell=2 targets at -1/2 each, all preserving [0,1], and no same-layer shortening targets. The normalized scalar diagonal source D therefore retains coefficient -2 to e, with no longitudinal phase. These are the same orientation-normalization factors as the verified zero-p calculation; longitudinal Fourier reduction changes only the center-shifting entries.

Consequently

v_A(p)=-gamma d2-e,    v_D(p)=-2e.

Other slow ell=2 separations cannot reach a nearest-column ell=2 fast state in two transverse flips: one whole-column transverse step only reaches such a state from axial-distance-two or diagonal separation. Two-edge shortening requires the two columns to have a two-edge connection; the diagonal mixed-XY contributions cancel as in the original zero-p calculation. No extra leading slow boundary component is introduced by Fourier phases, which are equal for the cancelling paths to the same endpoint configuration.

## Resolvent contraction

The uncorrected fast coefficient operator has

F0(p)d=-2d2-2gamma e.

The transverse host part is unchanged; only the adjacent-interval length link receives gamma. Therefore the correct identity is

v_A=(gamma/2)F0(p)d+(gamma^2-1)e.

It would be incorrect to keep the zero-p identity v_A=F0d/2 at nonzero p.

For fast host Green function G and confined-arm endpoint Green function g, the rank-one coupled expressions are

R_dd=G/(1-4gamma^2 gG),
R_ed=-2gamma g R_dd.

Under the established type of strip hypotheses, gamma stays positive, g stays bounded and bounded away from zero, and |G| grows logarithmically. Hence R_dd stays bounded and R_ed tends 1/(2gamma). Using R F_lambda=zR-I, with fixed-support correction (F_lambda-F0)d=O(lambda), gives

v_A^T R d -> -gamma/2+(gamma^2-1)/(2gamma)=-1/(2gamma),
v_D^T R d -> -1/gamma.

The vanishing correction requires the same local resolvent control as the zero-p proof, uniformly for p in the chosen neighborhood. No new assumption that the arm is unconfined is used.

## Original source

The physically normalized first dressed source is -sqrt(2) lambda cos p times d, as follows from the microscopic distance-two ZZ bond-center readout. Direct slow source remains zero through order lambda^2 by the same edge-counting argument, independent of Fourier phases. Combining the leading S-F vertex, physical fast resolvent factor, and first source thus gives

q_S,eff = lambda^2 [cos p/gamma] (A+2D)/sqrt(2) + o(lambda^2)

uniformly only where the required strip bounds are uniform. The sign agrees with the zero-p convention. Centering affects only the reference component.

This establishes the requested coefficient-model source limit conditional on the outgoing estimates. The endpoint coupling to the confined slow arm has an additional -gamma factor when assembling its final residue; it should not be omitted or counted twice. A complex outgoing residue uses the analytic transpose product, not a modulus-square. The result introduces no new source interaction and makes no empirical detector or cosmological identification.
