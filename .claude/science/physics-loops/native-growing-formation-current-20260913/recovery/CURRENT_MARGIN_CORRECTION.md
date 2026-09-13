# Current-margin correction

The first extracted baseline passed470 finite checks but omitted a predicate
for the prose half-current threshold. The source stated epsilon<=1/6912.
The covariance-to-current error is2t epsilon. The weakest current bound is
sqrt(3)t/3456 in the x direction, so its half-margin requires
epsilon<=sqrt(3)/13824. The old threshold leaves nonzero current but does
not guarantee that half-margin. No empirical tolerance or test was relaxed.

The corrected source uses epsilon<=1/8192. Squaring gives
(13824/8192)²<3, and all three half-current comparisons now have an exact
check. A separate predicate rejects the old constant. The original note,
helper and raw first baseline are preserved here; historical campaign
Block11 at a08a917065 also retains the old claim and its source.

This is an author-found mathematical bound correction. It does not change
the native instrument, current formula, front proof or existence statement.
