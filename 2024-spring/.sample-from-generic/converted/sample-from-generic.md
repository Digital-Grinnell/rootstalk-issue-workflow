---
index: sample-from-generic
azure_dir: rootstalk-2024-spring
articleIndex: 3
title: This is the Article’s Primary-Title
subtitle: 
byline: by This is the Byline Naming the Author(s)
byline2: 
categories: 
  - This is the Article-Type
tags: 
  - 
header_image: 
  filename: sample-from-generic-1.png
  alt_text: 
contributors: 
  - role: author 
    name: 
    headshot: 
    caption: 
    bio: " "
description: 
date: '17/04/2024 09:57:57'
draft: false 
no_leaf_bug: false
---

_This is an "Emphasized-Paragraph" styled paragraph. It will appear in italics as you see
 here. Used primarily for introductory or editorial content, or comments about the piece, not "of" the piece. Lorem
 ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar
 ultricies, purus lectus malesuada libero, sit amet commodo magna eros quis urna. Nunc viverra imperdiet enim. Fusce
 est. Vivamus a tellus._

 This is a "Normal" paragraph. Use it for most of an article’s text where Emphasis or other specialized text treatment
 is NOT needed. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce
 posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna eros quis urna. Nunc
 viverra imperdiet enim. Fusce est. Vivamus a tellus. Pellentesque habitant morbi tristique senectus et netus et
 malesuada fames ac turpis egestas. Proin pharetra nonummy pede. Mauris et orci.




 This is a "Normal" paragraph with a named, embedded hyperlink in the last sentence. The hyperlink’s displayed text
 (optional) appears to the reader and clicking on that text opens the hyperlink’s associated address or URL.
 [Click
 this link to learn more about hyperinks](https://support.microsoft.com/en-us/office/embed-or-link-to-a-file-in-word-8d1a0ffd-956d-4368-887c-b374237b8d3a) 
 and note that the displayed text may be omitted in which case the
 address is displayed.



## This is a Title (Secondary) or Section Heading

 This is a "Normal" paragraph with two footnote (endnote) references
 {{% ref 1 %}}
 expressed using lowercase Roman numerals
 {{% ref 2 %}}
 like `i`, `ii`, `iii` `iv`, etc. All such refenced notes in
 *Rootstalk* 
 appear as "endnotes" at the end of the article, not as "footnotes" at the end of the page. Instructions for inserting
 endnote references into a Word document can be found here:
 [Insert
 footnotes and endnotes](https://support.microsoft.com/en-us/office/insert-footnotes-and-endnotes-61f3fb1a-4717-414c-9a8f-015a5f3ff4cb) 




 The next element is an image using the "Article-Image" style. The caption was added by right-clicking on the image in
 Word and choosing the "Insert Caption…" command. The numeral "1" which appears at the start of the caption was
 automatically inserted by Word. I could find no way to suppress that behavior, but don’t worry, it will be
 automatically removed later.




 1This image caption was inserted using a right-click on the image.

## Just Another Title (Secondary)

 The next element is the same image as above using the "Article-Image" style, but its caption was provided on a
 separate line of text below the image. That caption line uses the "Caption" style.




 This is the image caption styled using "Caption".


 A handful of "Normal" paragraphs full of "lorem ipsum" text. Following this first paragraph is a "Pull Quote", the
 style name is "Intense Quote", highlighting text extracted from an upcoming paragraph. Lorem ipsum dolor sit amet,
 consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus
 lectus malesuada libero, sit amet commodo magna eros quis urna.



{{% pullquote %}}
Proin pharetra nonummy pede. Mauris et orci. Aenean nec lorem. In porttitor. Donec laoreet
 nonummy augue!
{{% /pullquote %}}

 Nunc viverra imperdiet enim. Fusce est. Vivamus a tellus. Pellentesque habitant morbi tristique senectus et netus et
 malesuada fames ac turpis egestas. Proin pharetra nonummy pede. Mauris et orci. Aenean nec lorem. In porttitor. Donec
 laoreet nonummy augue.




 Suspendisse dui purus, scelerisque at, vulputate vitae, pretium mattis, nunc. Mauris eget neque at sem venenatis
 eleifend. Ut nonummy.



## Adding Media

 Word templating is available for adding media in the form of embedded audio or video playback. While this is a
 "Normal" paragraph, the elements you see below are 15-second samples of video (.m4v) and audio (.mp3) captured from my
 screen while editing this template. The visual "widgets" you see here are optional, I only put them here to remind me
 of where they fall in the article.




 The
 **critical** 
 elements here are the "video_azure…" and "audio_azure…" statements wrapped in
 double-curly-braces! Those are "
 [shortcode](https://gohugo.io/content-management/shortcodes/) 
 " elements
 that make the media work.



{{% video_azure pid="15-second-video-sample-with-audio.m4v" caption="This caption says 'Use this player to see 15 seconds of sample video'" %}}

 This is a "normal" paragraph situated between a "Video" styled widget and an "Audio" styled widget.



{{% audio_azure pid="15-second-audio-only.mp3" caption="Use this player to hear 15 seconds of sample audio" %}}




## Adding Poetry or Fixed-Format Text

 Word templating is available for adding fixed-format text like poetry. The following lorem-ipsum text uses whitespace
 and the "Fixed-Format" style to selectively position text.




```
Lorem ipsum dolor sit amet,    This line indented by 4 spaces…consectetuer adipiscing elit.        This line intented by 7 spaces…Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna    eros    quis urna.      This line indented by 6 spaces…Nunc viverra imperdiet enim.
```

## Interview or Transcript Text

**Interviewer** 
 : This is typical interview or transcript text in "Interview" style. It features a
 "speaker" identifier followed by a colon then normal text.




**Interviewee** 
 : Using personal names or even initials in place of "Interviewer:" and
 "Interviewee:" is recommended. This format can also be used for transcripts, especially where a "speaker" identifier
 is recommended.



## This is a "List Paragraph"

 I didn’t create the "List Paragraph" style, it must have come from Microsoft. I’m using it
 here just to see how it behaves. It’s basically just a "Normal" paragraph but indented by 0.5 inches throughout. Might
 come in handy for something?



{{% endnotes %}} 
{{% endnote 1 " This is endnote #1 referenced with the lowercase Roman numeral ‘i’. Like other text, an endnote may contain a
 link like <a href=\"https://support.microsoft.com/en-us/office/insert-footnotes-and-endnotes-61f3fb1a-4717-414c-9a8f-015a5f3ff4cb\">this
 one</a>. " %}} 
{{% endnote 2 " This is endnote #2. Endnotes typically refer to content supporting the article, generally gleaned from research
 conducted during the article’s creation. " %}}

