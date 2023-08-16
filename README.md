# SortEmPics

v.1.2.1:
· Popup added, showing the numbers of each file type sorted.

---
v1.2.0:
· Videos and other type of files are processed and organized, by in a simple way. If any existed, they are put in a "videos" or "others" folder, in the output folder, without being sorted by date.
· As with images, if file names conflicted, they are renamed.

---
v1.1.0:
· Nested folders diving added.
· Duplicated files taken care of, depending on the configuration policy.

---
v1.0.0:
This application was designed and developed under external requirements, 
and tuned up with what I thought was best for it.
I have to admit there are some things that could be done better,
but it works, and it's free. Anyone is free to fork it and do
the best they can with it (just give credit! :>)

This app is made explicitly for Windows and not tested on Linux or Mac OS.

Files in the input folder cannot be in nested folders. They must all
be in the same root folder.

Some missing features I thought of that I (or anyone) could implement
in a future:

· Image and Video separated root folders (I've tried using Image to determine
the files formats, but seems quite broken, makes the app laggy and
I didn't think it was worth the effort digging any further)
· Avoding to take into account non-image files (like .config files and such,
specially from professional cameras) to sort.
· Better HUD.
· Test it work on Linux or Mac (may not work due to folder separating format)
· Sorting video files (unfortunately, Image will crash if given
a video file, so that's to be avoided)
· Dive into nested folders in the Input folder

I hope you can make the best use out of this!

-Relderf
