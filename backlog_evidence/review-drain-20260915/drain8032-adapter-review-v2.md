# PR8032 exact adapter confirmation

Capture authorized for the exact v2 adapter SHA-256 `39a96c89177b7d130dc5db09bfd13885ed5f72a9d23fcddf63a06b1c970cacd5`: primary then companion, serial, once each, 180 seconds and 256 MiB sampled aggregate RSS per attempt. Existing internal 180 MiB and all evidence-preservation guards remain.

The exact diff only binds cold clearance and adds the reviewed dual-main guard before and after capture. Actual guard-only invocation passes; wrong base and main pins fail. No scientific program was run. Source tree `d218c35f6ebdc84e6bb8ea8a8b2385ff9ed47ceb`, frozen base `e46c78efd91d00c8a96ea4f11ea8bc5a8e3ed0e6`, reviewed main `1bb8b7befb857852acaed93bcf2bb1e47925b013`. Any changed bound identity requires renewed affected review.
