---
title: Backing up iPhoto images to an external destination using Carbon Copy Cloner
slug: backing-up-iphoto-images-only
author: Yoav
date: 2012-01-15T17:54:40+00:00
geo_latitude:
  - 32.412453
  - 32.412453
  - 32.412453
geo_longitude:
  - 34.823134
  - 34.823134
  - 34.823134
geo_accuracy:
  - 0
  - 0
  - 0
geo_address:
  - ישראל
  - ישראל
  - ישראל
geo_public:
  - 1
  - 1
  - 1
jabber_published:
  - 1326650081
  - 1326650081
  - 1326650081
email_notification:
  - 1326650083
  - 1326650083
  - 1326650083
twitter_cards_summary_img_size:
  - 'a:7:{i:0;i:374;i:1;i:330;i:2;i:2;i:3;s:24:"width="374" height="330"";s:4:"bits";i:8;s:8:"channels";i:3;s:4:"mime";s:10:"image/jpeg";}'
  - 'a:7:{i:0;i:374;i:1;i:330;i:2;i:2;i:3;s:24:"width="374" height="330"";s:4:"bits";i:8;s:8:"channels";i:3;s:4:"mime";s:10:"image/jpeg";}'
  - 'a:7:{i:0;i:374;i:1;i:330;i:2;i:2;i:3;s:24:"width="374" height="330"";s:4:"bits";i:8;s:8:"channels";i:3;s:4:"mime";s:10:"image/jpeg";}'
categories:
  - howto
tags:
  - backup
  - carbon copy cloner
  - ccc
  - iphoto

---
When I started using iPhoto, I didn&#8217;t realize my images are all enclosed inside a single package file. This is annoying because I&#8217;m used to having all my photos on a network share for easy access from PCs and other devices.

It turns out directly accessing images from iPhoto in the finder isn&#8217;t too difficult &#8211; you just need to &#8220;Show Package Contents&#8221; on the iPhoto library file, and navigate to the &#8220;Master&#8221; folder. However regularly backing up those images is a little more tricky.

If you&#8217;ve ever wanted to back up just the images from inside your iPhoto library to an external drive, a network share etc, then this is how you do it with the excellent Carbon Copy Cloner:

  1. In CCC&#8217;s main window, select &#8220;Choose a folder&#8221; from the source drop down. A folder navigation window will open.
  2. Ignore it for now and open a general finder window &#8211; navigate to your iPhoto library file location (usually under Pictures in your user account folder), and right-click on the iPhoto Library file and select on &#8220;Show Package Contents&#8221; from the pop-up menu.  
    <a href="images/spc.jpg"><img loading="lazy" decoding="async" class="aligncenter size-medium wp-image-900" title="" src="images/spc.jpg" alt="Show Package Contents" width="300" height="264" /></a>  
    [  
][1] 
  3. Now drag the &#8220;Masters&#8221; folder directly into CCC&#8217;s folder navigation window. That&#8217;s it &#8211; just select your destination and click on clone.  
    <a href="http://blog.yoavfarhi.com/2012/01/15/backing-up-iphoto-images-only/iphoto1/" rel="attachment wp-att-897"><img loading="lazy" decoding="async" class="aligncenter size-medium wp-image-897" title="" src="images/iphoto1.png" alt="Drag the masters folder into CCC" width="300" height="168"   /></a>  
    [  
][2] 

<div>
</div>

 [1]: images/iphoto1.png
 [2]: images/iphoto2.png