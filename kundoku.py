def katakana_to_hiragana(text):
    return ''.join(
        chr(ord(char) - 0x60) if 'ァ' <= char <= 'ン' else char
        for char in text
    )

def yomu(kanji,kaeri_ten,furigana,okurigana,okurigana_2):
    N = len(kanji)
    text = [''] * N
    result = ""
    for curr in range(N):
        if '再' in kaeri_ten[curr]:
            result += kanji[curr] + okurigana[curr]
            text[curr] = furigana[curr] + okurigana_2[curr]
        elif furigana[curr] != '_':
            text[curr] = furigana[curr] + okurigana[curr]
        else:
            text[curr] = kanji[curr] + okurigana[curr]
        if all([k not in kaeri_ten[curr] for k in ['レ','二','三','中','下','ー','再','置']]):
            result += text[curr]
            x = curr - 1
            while 'レ' in kaeri_ten[x]:
                result += text[x]
                x -= 1
            x += 1
            while '一' in kaeri_ten[x]:
                x -= 1
                while '二' not in kaeri_ten[x]:
                    x -= 1
                result += text[x]
                x -= 1
                y = x
                z = x + 2
                while z < N and 'ー' in kaeri_ten[z]:
                    result += text[z]
                    z += 1
                while y >= 0 and '三' not in kaeri_ten[y]:
                    y -= 1
                if y >= 0:
                    result += text[y]
                    x = y - 1
                while 'レ' in kaeri_ten[x]:
                    result += text[x]
                    x -= 1
                x += 1
            while '上' in kaeri_ten[x]:
                x -= 1
                y = x
                while y >= 0 and '中' not in kaeri_ten[y]:
                    y -= 1
                if y >= 0:
                    result += text[y]
                    x = y - 1
                while '下' not in kaeri_ten[x]:
                    x -= 1
                result += text[x]
                x -= 1
                while 'レ' in kaeri_ten[x]:
                    result += text[x]
                    x -= 1
                x += 1
    return result

if __name__ == '__main__':
    input_text = []
    with open('in', 'r') as file:
        for line in file:
            input_text.append(line.strip())
    for i in range(0,len(input_text),5):
        kanji = list(input_text[i])
        kaeri_ten = input_text[i+1].split()
        furigana = input_text[i+2].split()
        okurigana = ['' if o == '_' else katakana_to_hiragana(o) for o in input_text[i+3].split()]
        okurigana_2 = ['' if o == '_' else katakana_to_hiragana(o) for o in input_text[i+4].split()]
        result = yomu(kanji,kaeri_ten,furigana,okurigana,okurigana_2)
        print(result)