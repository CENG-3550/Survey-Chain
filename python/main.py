from web3 import Web3
import json
from participant.participant import Participant

# Web3 Settings
ganache_url = "#"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount = web3.eth.accounts[0]

# Contract Settings
abi = json.loads("#")
address = "#"
contract = web3.eth.contract(address=address, abi=abi)



def main():
    while True:
        print("""
        1- Kaç Kullanıcı Olduğunu Öğren
        2- Kullanıcı Oluştur
        0- Çıkış
        """)

        deger = int(input("Hangi işlemi yapmak istediğinizi seçin: "))

        if(deger == 0):
            break
            
        elif(deger == 1):
            participant = Participant(web3, contract)
            participant.participantCount()

        elif(deger == 2):
            name = input("Lütfen isminizi giriniz: ")
            age = int(input("Lütfen yaşınızı giriniz: "))
            participant = Participant(web3, contract)
            participant.createParticipant(name, age)

if "__main__" == __name__:
    main()







