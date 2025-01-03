def yomu(text,kaeri_ten):
    N = len(text)
    result = ""
    for curr in range(N):
        if 's' in kaeri_ten[curr]:
            result += text[curr]
        if all([k not in kaeri_ten[curr] for k in ['r','2','3','m','d','h']]):
            result += text[curr]
            x = curr - 1
            while 'r' in kaeri_ten[x]:
                result += text[x]
                x -= 1
            x += 1
            while '1' in kaeri_ten[x]:
                x -= 1
                while '2' not in kaeri_ten[x]:
                    x -= 1
                result += text[x]
                x -= 1
                y = x
                z = x + 2
                while z < N and 'h' in kaeri_ten[z]:
                    result += text[z]
                    z += 1
                while y >= 0 and '3' not in kaeri_ten[y]:
                    y -= 1
                if y >= 0:
                    result += text[y]
                    x = y - 1
                while 'r' in kaeri_ten[x]:
                    result += text[x]
                    x -= 1
                x += 1
            while 'u' in kaeri_ten[x]:
                x -= 1
                y = x
                while y >= 0 and 'm' not in kaeri_ten[y]:
                    y -= 1
                if y >= 0:
                    result += text[y]
                    x = y - 1
                while 'd' not in kaeri_ten[x]:
                    x -= 1
                result += text[x]
                x -= 1
                while 'r' in kaeri_ten[x]:
                    result += text[x]
                    x -= 1
                x += 1
    return result

if __name__ == '__main__':
    input_text = []
    with open('in', 'r') as file:
        for line in file:
            input_text.append(line.strip())
    text = input_text[0]
    kaeri_ten = input_text[1].split()
    result = yomu(text,kaeri_ten)
    print(result)