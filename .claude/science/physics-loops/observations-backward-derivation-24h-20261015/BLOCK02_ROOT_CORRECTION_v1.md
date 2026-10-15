# Root control-domain correction

The source specifies a smooth bump whose compact support lies strictly inside
(-1/2,1/2). The original author control used a flat smooth bump with support
[-1/2,1/2], so that particular test did not match the stricter support wording.
The analytic construction and inequalities were unaffected, but the test-domain
claim needed correction. This discrepancy was noticed when reading the focused
checker's corresponding domain correction; it was not an independent discovery.

The original check_block02_v1.py and BLOCK02_CONTROLS_v1.json are preserved.
The current runner uses psi(t)=2*phi(2t)/integral(phi), whose support is
[-1/4,1/4], and integrates in its actual support coordinates. It checks the
normalization and outside-support values and writes BLOCK02_CONTROLS_v2.json.
No scientific source equation or empirical data was changed. This is a corrected
control-domain mismatch, not a failed scalar theory or a new observation.
