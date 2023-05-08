# 使い方
reformat_srt.pyをダウンロードして、適当な場所に保存します。
input_fileに、改行したい.srtファイルのパスを入力します。
output_fileに、改行後の.srtファイルを保存したい場所とファイル名を入力します。
max_charsに、1行に含めたい最大の文字数を入力します。
スクリプトを実行します。

```
python reformat_srt.py
```

# 注意事項
.srtファイルはUTF-8でエンコードされている必要があります。
max_charsで指定した文字数が、字幕表示領域を超えないようにしてください。
input_fileとoutput_fileのファイルパスは、適切に指定してください。
以上です。
