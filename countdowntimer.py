import time

seconds= input("geri sayım için dakikka giriniz :")

while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1

print("SÜRE BİTTİ!")
