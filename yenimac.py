import os
import sys
import random

os.system("apt-get install net-tools")
os.system("clear")

print("""
##############
#mac değişim #
#coder:Erlik #
##############
""")

os.system("ifconfig")

x = input("ağ kartını seçiniz:")

os.system("ifconfig {} down".format(x))

mac0 = random.randint(10,99)
print(mac0)
mac1 = random.randint(10,99)
print(mac0,mac1)
mac2 = random.randint(10,99)
print(mac0,mac1,mac2)
mac3 = random.randint(10,99)
print(mac0,mac1,mac2,mac3)
mac4 = random.randint(10,99)
print(mac0,mac1,mac2,mac3,mac4)
mac5 = random.randint(10,99)
print("Yeni mac adresiniz:",mac0,mac1,mac2,mac3,mac4,mac5)


os.system("ifconfig {} hw ether {}:{}:{}:{}:{}:{}".format(x,mac0,mac1,mac2,mac3,mac4,mac5))

os.system("ifconfig {} up".format(x))
