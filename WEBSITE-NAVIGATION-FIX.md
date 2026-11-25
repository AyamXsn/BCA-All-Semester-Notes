# Website navigation fix — files changed

The problem was that the homepage linked directly to `.md` files. GitHub Pages served those files as raw Markdown text instead of a formatted webpage.

## Changes made
- `index.html` — updated internal links from `.md` to the matching rendered `.html` pages.
- Every existing `.md` file — kept unchanged.
- A matching `.html` page was generated beside every Markdown file. This includes:
  - `Semester-01/README.html` through `Semester-08/README.html`
  - `Semester-01/<subject-folder>/README.html` and equivalent subject pages
  - `SUBJECT-LIST.html`
  - `README.html`
  - HTML versions of notes, references, resources, question folders and other Markdown documents.
- All generated pages use a consistent readable style and convert internal Markdown links to `.html` links.

## Upload
Upload the contents of this ZIP to the root of the existing GitHub repository and commit. Keep the folder structure. Do not upload the outer enclosing folder as an extra directory.

The original Markdown source files and all non-Markdown files are preserved. The new `.html` pages are additional browser-friendly versions.
