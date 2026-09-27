# Conditional microscopic field correction for a rectangular two-junction SQUID

Construction/proof obligation, not native TOE confirmation. The already checked Krause2024 AppendixD notes that retaining field-independent harmonic ratios is an approximation. No reported fitted spectral/dispersion coefficient is imported here as an independent prediction.

Assume a short rectangular junction with width L, spatially uniform harmonic energy density v_m, negligible screening/self-field, and imposed linear phase phi(x)=phi_center+2pi(B/Bphi)x/L for x in[-L/2,L/2]. Direct integration gives

(1/L) integral cos[m phi(x)] dx = sinc(m B/Bphi) cos(m phi_center),

where sinc(z)=sin(pi z)/(pi z), including its sign and continuous value1 atzero. This is exact within these spatial assumptions. It is not justified for arbitrary nonuniform local transparencies/current density or a spatially varying field. Harmonics from series-inductance corrections instead carry products of the first-harmonic envelope (leading second harmonic proportional sinc²), a different mechanism.

For two arms with zero-field first-harmonic amplitudes Ja0,Jb0, common dimensionless zero-field harmonic ratios c_m(tau), common gap-suppression factor d(B), and externally imposed loop phase psi, define

A_m(B,psi)=d(B)c_m(tau)[Ja0 sinc(m B/Bphi,a)+Jb0 sinc(m B/Bphi,b) exp(i m psi)], c_1=1.

The effective potential is -Re sum_m A_m exp(i m phi). Do not replace individual signed sinc factors by absolute values. At bottom sweet spot psi=pi, odd harmonics subtract and even harmonics add; at top psi0 all add. In particular at zero field A_even/A_1=c_even*(Ja0+Jb0)/(Ja0-Jb0), whereas A_odd/A_1=c_odd. Away from sweet spots, rotate phase by arg(A_1) if desired, but all harmonics must rotate by m times that angle; a real first coefficient does not make the other coefficients real. In the charge basis retain conjugate hopping coefficients to preserve Hermiticity. Charge coupling is unchanged under this phase translation.

A common d(B) can be eliminated by calibrating an overall Josephson scale to a directly measured fundamental center at each field; this then predicts a different observable, not f01 or d(B). The arm ratio and field geometry must still be fixed independently. Unequal gap factors between arms, flux bias offset, finite inductance, junction inhomogeneity and microscopic changes of transparency are additional premises, not free corrections to fit evaluation residuals.

Independence ledger: AppendixD's Bphi,a≈.8T comes from high-field cavity modulation collapse. Its Bphi,b≈1.12T uses an arm-amplitude ratio inferred from joint spectral/dispersion fitting and cannot automatically be reused. A geometry-ratio alternative requires verified field orientation and actual penetrated AFM widths; the absolute and relative geometric uncertainty must remain explicit. Reported EC,Ja0,Jb0,c2,c3 and effectiveBc were fitted using the proposed dispersion targets. Raw flux/center-only data, if sufficient, must supply separate calibration or the empirical route remains conditional/unidentified. No local model outcome or target fit is claimed by this derivation.

Independent review domain clarification: phase rotation and ratios requireA1 nonzero (and for the zero-field bottom ratio,Ja0!=Jb0). The unnormalized finite potential remains defined at cancellation. At nonzero field even-arm contributions add algebraically with their signed sinc factors; this does not guarantee magnitude enhancement. Names top/bottom denotepsi0/pi in the usual first-harmonic regime, not proven global spectral extrema for arbitrary higher harmonics.
