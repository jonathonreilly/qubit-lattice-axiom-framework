# Precision of the complete native parity instrument

Final campaign derivation, 2026-09-13. Conditional input: the decoded native
parity instrument of PR8089 at0b00d351b4c6d4ef6fd737925f5ae403e086cc95.
The code, observable B, outcome identification and physical intertwiners
are fixed. This concerns supplied pulse precision, not a physical program
decoder or general off-code matrix noise. Proof written before the checker.

Work on a finite-dimensional incoming code. Let B=B†, B²=I and theta in[0,pi/2]. Put c_theta=cos(theta/2),
s_theta=sin(theta/2), and

    F_z(theta)=(c_theta I+z s_theta B)/sqrt(2), z=+1,-1.
    I_theta(rho)=direct_sum_z F_z(theta) rho F_z(theta).

The output keeps the classical outcome AND the quantum poststate. Use the
full diamond norm, whose maximum channel distance is2. If B has both signs,

    ||I_theta-I_phi||_diamond = 2 sin(|theta-phi|/2).               (1)

Proof of upper bound: the coherent flagged isometry
V_theta=sum_z |z> tensor F_z(theta) satisfies
V_theta† V_phi=cos((theta-phi)/2) I. For every pure input with an arbitrary
reference, the two pure output vectors have this same overlap. Their trace
distance is2 sin(|theta-phi|/2). Convexity extends the bound to mixed inputs;
dephasing the outcome flag contracts trace norm and gives the instrument.
The channel-discrimination characterization of the diamond norm permits
such state inputs with a reference for a difference of channels.

For equality choose a unit vector psi with <psi|B|psi>=0, possible by an
equal superposition of one vector from each B eigenspace. Each outcome then
has probability1/2 for either angle. Its normalized vectors are
c_theta psi+z s_theta B psi and c_phi psi+z s_phi B psi, with overlap
cos((theta-phi)/2). Each classical block contributes sin(|theta-phi|/2)
to the trace norm, and the two blocks add. The same native intertwiners
J_z preserve these norms, so the result applies on the fixed incoming code
to the physical Record outputs. A scalar-B restricted sector retains only
the upper bound; the stated saturation argument does not apply there.

Now compare N-step adaptive histories. The two processes use the same
outcome labels, observables B_j(h), code transitions, dwell channels and controller structure;
their only difference is theta_j(h) versus phi_j(h), with
|theta_j(h)-phi_j(h)|<=delta_j<=pi/2 uniformly in prior classical history h.
For the complete history channel, contractivity and telescoping give

    ||H_theta-H_phi||_diamond
       <= min(2, sum_j 2 sin(delta_j/2)).                         (2)

At each step the history-controlled instrument is a direct sum over h,
so its distance is bounded by the largest instrument distance in that
step. Other shared channels have diamond norm1. Classical history output
therefore has total variation at most min(1,sum_j sin(delta_j/2)).
This includes all failed/zero-outcome branches without dividing by branch
probabilities. It is not a uniform claim about normalized poststates
conditioned on a rare, separately selected history.

If the control is specified as contrast kappa=sin(theta), let
|kappa-lambda|<=epsilon<=1, with both in[0,1]. Convexity of arcsin means the
largest angle difference occurs at the upper endpoint, hence

    ||I_arcsin(kappa)-I_arcsin(lambda)||_diamond <= sqrt(2epsilon).
                                                                    (3)

Indeed the endpoint difference is arccos(1-epsilon), and(1) gives
2 sin(arccos(1-epsilon)/2)=sqrt(2epsilon). This bound is attained when
one contrast is1 and the other1-epsilon and B has both signs. If both
contrasts instead lie in[0,kappa_max] with kappa_max<1, the mean value
bound and2sin(x/2)<=x give the sharper Lipschitz estimate

    distance <= epsilon/sqrt(1-kappa_max²).                       (4)

Thus small changes in outcome effects near a projective endpoint can cost
the square root of that change in the complete instrument. This is a
precise calibration distinction, not a no-go for robust measurement. Angle
control itself has distance at most|theta-phi|. The scalar on-code data-law
precision theorem of PR8088 and its off-code discontinuity example concern
a different map and remain unchanged. No native preparation, law selection,
physical controller or causal calibration mechanism is supplied by(1)-(4).

Mathematical reference: [Watrous, The Theory of Quantum Information,
Theorem 3.51, printed pages 176–177](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=183).
The statement and proof were read on 2026-09-13. It applies because the
instrument difference is a Hermitian-preserving map between finite matrix
spaces. The native angle-distance and saturation arguments above are
derived here; the reference supplies the pure-state diamond characterization.
