# This is a sample Python script.
import socket
import threading
import time

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = "10.4.1.209"
PORT = 5051

client_socket.connect((IP,PORT))



def receive(ads):
    while True:
        reponse_du_serveur = client_socket.recv(2048).decode('utf-8')
        if reponse_du_serveur != "":
            print(f"Message du serveur: {reponse_du_serveur}")
        time.sleep(2)

thread_receive = threading.Thread(target=receive,args=(1,))
thread_receive.start()

while True:
    message = input("Saisissez un message (ou 'exit' pour quitter) : ")

    client_socket.send(message.encode('utf-8'))

    if message.lower() == 'exit':
        break


client_socket.close()


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
