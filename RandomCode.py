import time
import random
import string

#------------------RENKLER---------------#
K = '\033[1;31m' #KIRMIZI
Y = '\033[2;32m' #YEŞİL
S = '\033[1;33m' #SARI
B = '\033[1;97m' #BEYAZ
by = 'Telegram: @Crosphp'
#------------------RENKLER---------------#

print(f"""{K}
⠀⠀⠀⡠⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⢡⠀⢄⠀⠀⠀
⠀⠀⣰⠃⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠘⣆⠀⠀
⠀⢀⡏⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹⡀⠀
⠀⣸⡇⠘⠷⢖⣒⡲⣤⣤⣤⣤⢖⣒⡲⠾⠃⢸⣇⠀
⠀⠻⠷⠚⠋⣩⡭⢭⣿⣿⣿⣿⡭⢭⣍⠙⠓⠾⠟⠀
⠀⠀⢀⣠⠞⢉⣴⠏⣽⣿⣿⣯⠹⣦⡍⠳⣄⡀⠀⠀
⣤⡴⠋⠁⠀⢸⣿⠀⢸⣿⣿⡏⠀⣿⡇⠀⠈⠙⢶⣤
⢹⡇⠀⠀⠀⢸⣿⠀⠈⣿⣿⠁⠀⣿⡇⠀⠀⠀⢸⡟
⠸⡇⠀⠀⠀⠀⣿⠀⠀⠘⠃⠀⠀⣿⠁⠀⠀⠀⢸⡇
⠀⢷⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⡾⠀
⠀⠘⡄⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢠⠃⠀
⠀⠀⠐⠀⠀⠀⠈⠇⠀⠀⠀⠀⢸⠁⠀⠀⠀⠂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠄⠀⠀⠠⠃⠀⠀⠀⠀⠀⠀⠀

━━━━━━━━━━━━━━━━━━━━━━
  {by} |
━━━━━━━━━━━━━━━━━━━━━━
""")
def type_slowly(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05) 
    print() 
def generate_play_codes(count, length=16):
    characters = string.ascii_uppercase + string.digits
    codes = []
    for _ in range(count):
        play_code = ''.join(random.choice(characters) for _ in range(length))
        codes.append(play_code)
    return codes

while True:
    type_slowly(f"Ne kadar Play Kod Üreteyim? Çıkmak için 'q' basın:{B} ")
    user_input = input()
    
    if user_input.lower() == 'q':
        print("Programdan çıkılıyor...")
        break
    
    try:
        num_codes = int(user_input)
        if num_codes <= 0:
            print("Lütfen pozitif bir sayı girin.")
            continue
        
        generated_codes = generate_play_codes(num_codes)
        print(f"\nÜretilen {num_codes} Play Kodları:{Y}")
        for code in generated_codes:
            print(code)
        print("\n")
        print(f"\n{B}İşlem Tamamlandı. {num_codes} adet Play Kod üretildi.")
        type_slowly("Tool'dan Çıkmak için 'N' Devam Etmek için 'Y' kullanın: ")
        next_action = input().strip().upper()

        if next_action == 'N':
            print("Tool'dan çıkılıyor...")
            break
        elif next_action == 'Y':
            print("Ana menüye dönülüyor...\n")
            continue
        else:
            print("Geçersiz giriş, ana menüye dönülüyor...\n")
            continue

    except ValueError:
        print("Lütfen geçerli bir sayı girin veya çıkmak için 'q' tuşuna basın.")
