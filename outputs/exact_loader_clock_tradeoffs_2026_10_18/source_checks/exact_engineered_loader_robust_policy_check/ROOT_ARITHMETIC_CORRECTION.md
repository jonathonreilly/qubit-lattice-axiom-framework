# Narrow arithmetic correction to the robustness review

The frozen review040de776f54dd19c241837eef77338aec6e2480a4e25b3d3009c9341a1d8a460 section5 incorrectly states that delta0 is smaller than epsilon Lambda/[7680 pi(L+1)]. Publication drafting exposed this error and ROOT checked it directly. The source e69fa0e34d3fdb8d205cd1a8a5e26ea2efd3f3963a279b0d5edcf5d12ddbdc06 is unchanged.

The exact short-window ceiling is delta0=3 epsilon Lambda/[20480 pi(L+1)]. Its ratio to the cited comparison ceiling is 3*7680/20480=9/8, not less than1. The dwell ceiling is at most epsilon Lambda/[7680 pi(L+1)] and hence is smaller than delta0. With Jstar=Lambda/80 a valid common upper bound for BOTH policies is

    delta/Jstar <= 3 epsilon/[256 pi(L+1)].

For epsilon<=1,L>=296 this is at most3/[256 pi*297], strictly below3-sqrt(2). Thus the claimed fixed-form positive compensation remains positive. Bond/contact positivity uses the separate previously stated minimum-hopping ratios, unaffected by this comparison. All performance policies, full-support cap, complete-output and normalized-branch bounds are unchanged. The frozen review is retained as evidence, with this explicit correction required whenever that arithmetic is used.

This is a source-exposed ROOT analytical correction, not an additional retained audit or physical test. No scientific execution, source mutation or editable prompt change occurred.
