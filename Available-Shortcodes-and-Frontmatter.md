# Not a Shortcode...

Ok, this first thing isn't unique to _Rootstalk_, but worth knowing anyway...  

**You can insert an attribute of `data-proofer-ignore` into any HTML tag (you'll most likely do this in our partials and shortcodes) to keep the `html-proofer` script from processing it.  See https://github.com/gjtorikian/html-proofer for details.**

Example: From `layouts/shortcodes/broken.html`

```
{{- $s := .Get 1 -}}
{{- $link := replaceRE "^https?://([^/]+)" "$1" $s -}}
{{- $dead := "dead" -}}
<a data-proofer-ignore href="/broken-external-link?{{- (querify $dead $link) | safeURL -}}" target="_blank">{{- .Get 0 -}}</a>
```
# Available Shortcodes with Examples

## {{% broken %}}

Used to deal with a broken external link in a content `.md` file.

**Example:**  From https://rootstalk.grinnell.edu/past-issues/volume-ii-issue-1/lahay/ 

```
According to information on the website for the {{% broken "American Society for the Prevention of Cruelty to Animals," "http://www.humanesociety.org/assets/pdfs/pets/puppy_mills/report-puppy-mills-then-now.pdf" %}} “puppy mills became more prevalent after World War II.
```

## {{% broken-endnote %}}

Used to deal with a broken "endnote" external link in a content `.md` file.

**Example:**  https://rootstalk.grinnell.edu/past-issues/volume-i-issue-1/ikerd/

```
{{% broken-endnote 7 "World Society for Protection of Animals, “What’s on Your Plate? The Hidden Costs of Industrial Animal Agriculture in Canada, 2012, page 136." "http://richarddagan.com/cafo-ilo/WSPA_WhatsonYourPlate_FullReport.pdf" %}}
```

## {{% dropcap %}}  

**Example:**  From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-viii-issue-1/buck/  

```
{{% dropcap %}}  
That fall, as the pasture grass grew thin,  
I climbed to the hay mow and threw down the bales.  
My husband knew then he was on his last fall-  
No doubt he was already thinking of sales!   
{{% /dropcap %}}  
```

## {{% pullquote %}}  

**Example:**  From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-viii-issue-1/burchit/  

```
{{% pullquote %}}
“[T]hrough the trial and error of these punk houses Rabalais refined his craft, learning things about the process that he could only learn by giving a lot of tattoos...” 
{{% /pullquote %}}
```

## {{% fixed_format %}}

**Example:** TBD

```
{{% fixed_format %}}
*do not come    too close to me*, he says, with strong brown eyes that   contain   the world.  
She stands atop  
packed black dirt,  
Facing me  
as I forget my self, forget my name, feel my breath, feel hers too

Shadows cast by the afternoon sun. reflecting their sacred bodies,  
moral behavior power survival entangled within their woolly dense fur  

the *tatanka*,"buffalo," are four-legged people{{% ref 6 %}},   
who hold a mystery of    sacred life,  
which travels  
   in dust  
formed playfully wallowing, rubbing their backs   
  with packs  
of Earth’s colorful skin.  
{{% /fixed_format %}}
```

## {{% indent %}}

**Example:** From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-viii-issue-1/taylor/

```
{{% indent 3 %}}  
I sit on a hill with wild carrot  
The white flowers turn their faces to the sky  
They play on this hill, layers and layers  
Swaying in the wind  
{{% /indent %}}  
```

## {{% attribution %}}

**Example:** From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-viii-issue-1/agpoon/  

```
{{% attribution 5 %}}  
*Mark Baechtel, Editor-in-chief*
{{% /attribution %}}  
```


## {{% indent-with-attribution %}}

**Example:** From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-viii-issue-1/agpoon/  

```
{{% indent-with-attribution 3 5 "*Mark Baechtel, Editor-in-chief*" %}}  
*Periodically, we like to allow one of our Associate Editors to take over the Editor’s column for an issue. We thought Hannah’s extraordinary re-imagining of the prairie’s changing seasonal colors deserved such a recognition.*    
{{% /indent-with-attribution %}}  
```

## {{% leaf-bug %}}

_This shortcode has no closing tag!  It marks the very end of an article's BODY text._

**Example:** From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-viii-issue-1/mcgary-adams-dubow-fay-stindt-schaefer/

```
abundance feels possible, coaxed 
by these tired hands. {{% leaf-bug %}}
```

## {{% figure_azure %}}

_This shortcode has no closing tag!  It's used to present an image from a JPG or PNG file._  

**Example:** From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-viii-issue-1/mcgary-adams-dubow-fay-stindt-schaefer/  

```
{{% figure_azure pid="Mustard-Seed-Farm-Flix-ep.-1-210930.png" caption="Open the first of four of Emma Kieran Schaefer's short videos on Mustard Seed Farm." alt="Some alt text" %}}  
```  

## {{% audio_azure %}}

_This shortcode has no closing tag!  It's used to present an audio playback widget for an MP3 file._

**Example:** From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-viii-issue-1/mcgary-adams-dubow-fay-stindt-schaefer/

```
{{% audio_azure pid="Mustard-Seed-Song-220317.mp3" caption="Use this player to hear Emma's recording of \"Miracle Seed\"" %}}
```

## {{% video_azure %}}

_This shortcode has no closing tag!  It's used to present a video playback widget for an MP4 file._  

**Example:** From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-viii-issue-1/mcgary-adams-dubow-fay-stindt-schaefer/  

```
{{% video_azure pid="Mustard-Seed-Farm-Flix-ep.-1-210930.mp4" caption="Open the first of four of Emma Kieran Schaefer's short videos on Mustard Seed Farm." %}}  
```  

## {{% ref %}}, {{% endnotes %}} and {{% endnote %}}

_These shortcodes have no closing tag!  They are used to create endnote references, heading and a list of endnotes at then end of an article._  

**Example:** From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-i-issue-1/ikerd/

```
3) “The clarity that the world changes through local communities taking action—that there is no power for change greater than a community taking its future into its own hands.”{{% ref 1 %}} 

...

Now that the sound-science has turned against them, the defenders of industrial agriculture have resorted to a multi-million dollar, nationwide propaganda campaign. {{% ref 2 %}}

...

{{% endnotes %}}
{{% endnote 1 "Margaret Wheatley, “The Big Learning Event,” Prepared for presentationat the University of Wisconsin, Madison, WI, June 2011." %}}
{{% endnote 2 "[Food Dialogues, U.S. Farmers and Ranchers Alliance.](http://www.fooddialogues.com/)" %}}
```  

&nbsp;  
&nbsp;  


# Available Frontmatter with Examples

## byline: 

An optional _article_ frontmatter element.  Used when there are no `contributors:`, or when the byline of an article needs an "override" value.  Note that the value should include the prefix `by`, or another appropriate opening verb.  Also, it may be wise to delete the `contributors:` element and subordinates from the frontmatter so that no _About..._ contributors block is generated.   

**Example:** From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-i-issue-1/andelson-note/ 

```
byline: by Jon Andelson
```

## no_leaf_bug: 

An optional _article_ frontmatter element.  Used to supress the automatic additon of a `leaf-bug` icon when an article has no body text.  

**Example:** From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-i-issue-1/editorial-staff/ 

```
no_leaf_bug: true
```
