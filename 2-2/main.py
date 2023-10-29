# 파일에서 암호를 읽어오는 함수
def read_cipher_file(filename):
    try:
        with open(filename, 'r') as file:
            cipher_text = file.read().strip()
        return cipher_text
    except FileNotFoundError:
        print(f"파일 '{filename}'을 찾을 수 없습니다.")
        return None

# 카이사르 암호를 해독하는 함수
def caesar_cipher_decode(target_text, shift):
    decoded_text = ""
    for char in target_text:
        if char.isalpha():  # 알파벳인 경우만 처리
            is_upper = char.isupper()
            char = char.lower()
            decoded_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                decoded_char = decoded_char.upper()
        else:
            decoded_char = char
        decoded_text += decoded_char
    return decoded_text

# 암호 파일을 읽어옴
cipher_text = read_cipher_file('password.txt')

if cipher_text:
    # 자리수에 따라서 해독된 결과를 출력
    for shift in range(1, 27):
        decoded_text = caesar_cipher_decode(cipher_text, shift)
        print(f"Shift {shift}: {decoded_text}")

    # 몇 번째 자리수로 암호가 해독되는지 찾아냄
    for shift in range(1, 27):
        decoded_text = caesar_cipher_decode(cipher_text, shift)
        if cipher_text in decoded_text:
            print(f"암호가 Shift {shift}로 해독됩니다.")
            break

while(1):

    num=int(input("번호 입력: "))
    if num==shift:
        with open("result.text","w") as result:
            result.write((f"Shift {shift}: {decoded_text}"))
            print("result.text 생성 완료")
        break
    else:
        print("번호가 잘못되었습니다")
