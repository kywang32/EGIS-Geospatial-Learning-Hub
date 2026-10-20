# Public repository / private PDFs: pre-release checklist

- [ ] The public repo, public releases, and public Skill ZIP contain **zero** course PDFs or PPTX files.
- [ ] The public README, Skill and manifest all state the PDFs are **optional**, **request-only**, and **not CC BY 4.0**.
- [ ] Set a restricted Google Drive (or equivalent) link and insert it into the README **before** inviting requests. Check what request details the sharing provider displays.
- [ ] Keep the 14-PDF supplement ZIP outside the public repository and never add it to a public release.
- [ ] Make sure no previous public Git commit/release contains the PDFs; removing a file from the latest commit does not erase Git history, forks or downloaded copies.
- [ ] Review third-party maps, diagrams, screenshots, photos, datasets and institutional marks within course PDFs before distributing even privately.
- [ ] Check that student identities, private class links, tokens and unpublished confidential data are not disclosed within PDFs.
- [ ] Check the published access terms and any additional permission conditions against the author's intended policy.
- [ ] Test the public Skill with **no PDFs** installed. It must not invent lesson quotes or page citations.
- [ ] Test local PDF lookup after privately installing approved PDFs. PDF file names and counts must match `lookup/knowledge-index.json`.
- [ ] Confirm recipients understand that approval is an access control, not a technical guarantee against copying or onward sharing.

**Git caution:** `.gitignore` helps prevent accidental `git add` of untracked references but does not delete PDFs already tracked, cannot sanitize Git history and does not necessarily prevent web-upload operations. Never drag the 14-PDF directory into a public GitHub upload page.
