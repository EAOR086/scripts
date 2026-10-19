"""词频统计 —— 统计文本中出现最多的单词。"""


def top_words(path, n=3):
    with open(path, encoding="utf-8") as f:
        text = f.read()

    counts = {}
    for w in text.split():
        if w in counts:
            counts[w] = counts[w] + 1
        else:
            counts[w] = 1

    items = list(counts.items())
    items.sort(key=lambda kv: kv[1], reverse=True)

    return items[:n]


if __name__ == "__main__":
    for word, count in top_words("sample.txt"):
        print(f"{word:10} {count}")