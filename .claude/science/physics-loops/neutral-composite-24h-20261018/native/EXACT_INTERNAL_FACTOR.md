# Exact internal dynamics behind the collective interaction

Status: exact-support for a coordinate identity in the supplied positive-parity tube; conditional-support for its low-energy interpretation.

Root derives a local unitary from three commuting Pauli pairs in the eight-state positive-parity rung. The protected pair is Zp=XXI and Xp=YIY in the previous three-coordinate basis. Internal pairs are Za=IIY,Xa=XIX and Zb=IXI,Xb=YYY. These are coordinates on four physical qubits with fixed parity, not extra physical qubits.

In this basis h=I_p tensor h_internal with

h_internal=-I Z-X I-Y Y-Z X.

The four original longitudinal operators become D0=Y_p tensor ZZ, D1=X_p tensor IY, D2=-Z_p tensor YZ, D3=-I_p tensor XY. Consequently the native longitudinal interaction remains exactly -Jz sum_a D_a(i)D_a(i+1), now with explicit protected and internal factors. This equality holds at every coupling ratio. It does not permit freezing the internal factors at strong coupling.

The internal Hamiltonian has energies -2sqrt2,0,0,+2sqrt2. Its unique ground projector is h_internal(h_internal-2sqrt2 I)/16. All four internal vertex expectations vanish. Each vertex sends that ground state exclusively into the zero-energy internal subspace. Thus direct first-order protected exchange vanishes, but correlated virtual excitation of two internal factors generates

K2=-(I+(Xp_i Xp_j+Zp_i Zp_j)/2)/sqrt2,

multiplying Jz²/Jperp. The denominator is exactly4sqrt2 Jperp. The independent exact projector contraction reproduces the previous XY interaction after relabeling collective axes. No new interaction, fluctuating coupling variable or chosen scalar field has been introduced. The unresolved equal-coupling problem is now explicitly a coupled protected/internal chain, rather than an assumed oscillator.

`neutral_exact_internal_factor.py` checks the unitary, each native operator, internal projector/transition identity and second-order contraction symbolically. An initial transcription used -YIY for the protected X coordinate; the vertex assertion caught it. Correct conversion of -X0X2Z0Z2 is +YIY. The corrected symbolic test passes.

Next: test internal excitation occupation and correlations in full-H stationary states, then investigate whether the exact coupled description supplies a controlled long-distance mode at equal strength. This identity does not establish the phase, a scalar pole, physical matter or cosmological coupling.


At equal coupling in the existing selected32site stationary eigenstate, exact local projector probabilities in the central rung are .4787583244 ground, .4252761926 middle and .0959654830 upper. Initial H residual2.06e-13; projector norm checks <3e-15. These quantify substantial internal admixture and invalidate treating the low-rung subspace as nearly exact there. The numerical occupation script consumes the existing frozen eigenvector; these diagnostics are separate from the self-contained symbolic factor certificate. No probability here is a real-particle abundance.
