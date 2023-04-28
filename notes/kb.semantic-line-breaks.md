---
id: i072yxnbanm19trtm8ct37n
title: Semantic Line Breaks
desc: ''
updated: 1682695292048
created: 1682695052578
tags:
  - kb
  - tool
---


> ## Semantic Line Breaks Specification (SemBr)
> The key words “must”, “must not”, “required”, “shall”, “shall not”, “should”, “should not”, “recommended”, “may”, and “optional” in this document are to be interpreted as described in RFC 2119.
> 
> Text written as plain text or a compatible markup language may use semantic line breaks.
> A semantic line break must not alter the final rendered output of the document.
> A semantic line break should not alter the intended meaning of the text.
> A semantic line break must occur after a sentence, as punctuated by a period (.), exclamation mark (!), or question mark (?).
> A semantic line break should occur after an independent clause as punctuated by a comma (,), semicolon (;), colon (:), or em dash (—).
> A semantic line break may occur after a dependent clause in order to clarify grammatical structure or satisfy line length constraints.
> A semantic line break is recommended before an enumerated or itemized list.
> A semantic line break may be used after one or more items in a list in order to logically group related items or satisfy line length constraints.
> A semantic line break must not occur within a hyphenated word.
> A semantic line break may occur before and after a hyperlink.
> A semantic line break may occur before inline markup.
> A maximum line length of 80 characters is recommended.
> A line may exceed the maximum line length if necessary, such as to accommodate hyperlinks, code elements, or other markup.

> ## One sentence per line
> When writing source documentation in a format such as Markdown, reStructuredText or AsciiDoc, I recommend you place every sentence on its own line and don’t use fixed-column word-wrapping.
> 
> ## Advantages
> * It prevents reflows (meaning a change early in the paragraph won’t cause the remaining lines in the paragraph to reposition), which ensures code diffs look more clean.
> * It lets you swap sentences more easily.
> * It lets you separate and join paragraphs more easily.
> * It lets you comment out sentences or add commentary to them.
> * You can spot sentences which are too long or sentences that vary widely in length.
> * You can spot redundant (and thus mundane) patterns in your writing.
> * You can easily apply bulk actions on sentences with editor macros, such as converting to list items by prepending a dash to each line.
> * It improves using GitHub’s “suggest changes” workflow, as it lets your reviewer start a new suggestion for each sentence instead of having to combine them.
> ## References
> * Rhodes, Brandon. “[Semantic Linefeeds](https://rhodesmill.org/brandon/2012/one-sentence-per-line/)” April 3, 2012
> * “[AsciiDoc Recommended Practices: One Sentence Per Line](https://asciidoctor.org/docs/asciidoc-recommended-practices/#one-sentence-per-line)”, Accessed January 22, 2021
> * “[Semantic Line Breaks](https://sembr.org/)” Accessed January 22, 2021

_Sources:_

  * [Semantic Linefeeds](https://rhodesmill.org/brandon/2012/one-sentence-per-line/)
  * [One sentence per line](https://nick.groenen.me/notes/one-sentence-per-line/)