---
created: 2026-05-07
id: 60b0fb10-5dd0-440c-a8e6-5e8ca1a93222
tags:
  - misc
  - kb
---

# pandoc

## Convert a `docx` file to `md`

```shell
pandoc \
    --verbose \
    --from docx \
    --to markdown \
    --default-image-extension=png \
    --extract-media=images \
    'document.docx' -o document.md
```
