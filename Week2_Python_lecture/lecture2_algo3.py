

def check_group(word):
    last_alphabet = ""
    alphabets = []
    for letter in word:
        if letter == last_alphabet:
            continue
        else:
            if letter in alphabets:
                return False
            alphabets.append(letter) #[a]
            last_alphabet = letter
    return True
count= int(input())
result = 0

for _ in range(count):
    word = input()

    #1.letter가연속적인가->aabb->직전알파벳이letter와같은지
    #2.이미나왔던단어인가
    #3.연속을깨트릴때이미나왔던알파벳인지검사->false면그룹단어가아님
    if check_group(word):
        result += 1

print(result)
