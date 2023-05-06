import re


def split_text(text, n):
    text = text.replace("\n", " ")
    lines = [text[i:i + n] for i in range(0, len(text), n)]
    return "\n".join(lines)


def reformat_srt(input_file, output_file, max_chars):
    with open(input_file, "r", encoding="utf-8") as file_in:
        content = file_in.read()

    pattern = re.compile(r"(\d+)\s+([\d:,]+ --> [\d:,]+)\s+([\S\s]+?)(?=\n\n|\Z)", re.MULTILINE)
    matches = pattern.finditer(content)
    new_subs = []

    for match in matches:
        index, timecode, text = match.groups()
        text = split_text(text, max_chars)
        new_subs.append(f"{index}\n{timecode}\n{text}")

    with open(output_file, "w", encoding="utf-8") as file_out:
        file_out.write("\n\n".join(new_subs))


if __name__ == "__main__":
    input_file = "E:\\output\\temp_2_kaigyo.srt"
    output_file = "E:\\output\\temp_2_kaigyo_output.srt"
    max_chars = 18 #左の数字で何文字で改行するかを指定する。
    reformat_srt(input_file, output_file, max_chars)
