# TextContentGeneration
Generates Text Content from various sources such as YouTube Videos, Local Audio/Video Files, Webpages and PDF's.

Use the **_text_content_generation.generate()_** function to generate content from
four sources:
1. PDFS
2. Web Pages
3. YouTube Video Transcripts
4. Local Audio/Video Files

You can also individual modules if you need only specific functionality.
1. audio 
   1. audio_conv - converts files to wav format
   2. transcribe - whisper model to transcribe audio files
2. youtube
   1. yt_donwload - Download the yt video
   2. search_yt - Returns search titles based on search query
   3. search_and_download
   4. youtube_script - Gets transcript/captions content (EN)
3. summarize
   1. summarize_chunks - Summarizes content using BART
4. webpage
   1. read_pages - Scrapes a page
5. pdf
   1. pdf_read - Reads pdfs