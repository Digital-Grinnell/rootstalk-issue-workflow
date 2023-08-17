# Available Shortcodes with Examples

## {% dropcap %}  

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

## {{% indent-with-attribution %}}

**Example:** From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-viii-issue-1/agpoon/  

```
{{% indent-with-attribution 3 5 "*Mark Baechtel, Editor-in-chief*" %}}  
*Periodically, we like to allow one of our Associate Editors to take over the Editor’s column for an issue. We thought Hannah’s extraordinary re-imagining of the prairie’s changing seasonal colors deserved such a recognition.*    
{{% /indent-with-attribution %}}  
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

## {{% leaf-bug %}}

_This shortcode has no closing tag!  It marks the very end of an article's BODY text._

**Example:** From https://yellow-wave-0e513e510.3.azurestaticapps.net/past-issues/volume-viii-issue-1/mcgary-adams-dubow-fay-stindt-schaefer/

```
abundance feels possible, coaxed 
by these tired hands. {{% leaf-bug %}}
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
