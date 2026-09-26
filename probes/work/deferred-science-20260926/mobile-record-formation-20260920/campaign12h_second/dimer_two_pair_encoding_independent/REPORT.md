# Independent finite two-pair encoding check

The specified positive covariant preparation map exists and is injective
on the full fourteen-color probability simplex. No correction or unresolved
step was found in this finite claim. Its exact column rank is 14 and affine
rank is 13. This does not establish quantum dynamics or perfect label readout.

The complete primary construction was read at SHA-256
`ab657acc73902c4fe6ce42d0675fc77aeee977af63e4ff04a022238aff814e46`.
The independent calculation preceded all author checker/results access.

Stabilizers of e1 and (1,1,1) have sizes four and three. Their twirls are
invariant because a stabilizer action permutes the summands. Orbit
transporters therefore give the same matrix for each color regardless of
representative, and the family is covariant. All transporter choices and
all 336 rotation/color identities were checked with integer matrices.

Each seed is I plus positive vector outer products. Its conjugates dominate
I exactly. The two trace denominators are 1168 and 2125, giving strict
normalized eigenvalue lower bounds 1/1168 and 1/2125. Positivity here is
proved by the construction, without floating-point eigenvalue tests.

The independent checker assembles the unnormalized states as columns of a
256-by-14 integer matrix. A saved 14-by-14 minor has determinant **22325
modulo 65537**, with primality checked by trial division. This certifies a
nonzero integer determinant and therefore exact rational column rank14.
The complete minor and zero-based row-major operator indices are preserved
in INDEPENDENT_RESULTS.json. Nonzero column normalization preserves rank.
Since all density matrices have trace one, linear independence is equivalent
to affine independence; a separate modular difference calculation gives
affine rank13. No numerical rank tolerance or generic-randomness assertion
is used.

Exact character sums give alternating multiplicity zero in the dimension16
Hilbert representation and seven in its operator space. The constructed
cubic density operator is nonzero, transforms by that character, and has
Frobenius square 2516832/903125. These distinguish the two representation
spaces correctly. All states are full rank and overlap; the smallest
distinct-pair Hilbert-Schmidt overlap in this construction is
136474/4515625. Thus injectivity of probability mixtures does not mean
fourteen orthogonal states or perfect single-copy label discrimination.

The pre-comparison seal is
`468970742f7b834fa58a0a4bcb4df2a8adb933d66385fa2933751842dfa25e19`
(one source, seven artifacts). The complete author checker, result, both
streams and receipt were then read and authenticated. Checker SHA-256 is
`07e9dbd7aea660c5cf4bcd36da7dc448e02e479dea99d43c31140d056f5a5c0b`;
result SHA-256 is
`c2f750b6d59179f8024f509d89350f6c468ff11ee0fbc23691c460799a362fb9`.
Every reported mathematical value agrees with the independently sealed
integer/modular calculation. The author uses an exact rational rank routine;
this review did not rerun or import it. All source bindings, log/result
agreement and the successful receipt authenticate. No prose/code drift was
found. Both independent executions succeeded with empty stderr and no
discarded attempt. Full logs, scripts and pre-seal are preserved.

Only the preparation map is established. Injectivity gives a linear inverse
on its image, not a positive or completely positive inverse, a channel
implementing label-conditioned rates, or a local immutable-record protocol.
Geometry-change compatibility, preparation by births and quantum field
dynamics remain separate obligations. No framework primitive, publication,
formal audit or retention status was adopted. No primary sources were edited.
The bounded analysis and comparison were completed before the 00:23 UTC
stop; there are no further targets in this packet.
