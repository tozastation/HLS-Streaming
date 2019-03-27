# HLS(HTTP Live Streaming)を試そう
## Setup
### ストリーミングのマニフェストファイルと分割ファイルを生成  
`mediafilesegmenter -f output/ -i canon-index.m3u8 -B canon- music/canon_in_d.mp3`
### ストリーミングサーバにアップロード
`python uploader.py`
## Check
`open -a 'QuickTime Player' 'http://127.0.0.1:9000/canon/canon-index.m3u8'`