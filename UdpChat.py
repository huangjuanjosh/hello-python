import socket
import threading


def send_message(udp):
    addr = input("enter destination ip:")
    port = int(input("enter destination port:"))
    while True:
        message = input("enter message to send：")
        udp.sendto(message.encode(), (addr, port))


def recv_message(udp):
    while True:
        recv_data = udp.recvfrom(1024)
        recv_message, (recv_ip, recv_addr) = recv_data
        print(recv_message.decode())


def main():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_port = int(input("enter your local port："))
    local_addr = ("", local_port)
    udp.bind(local_addr)  # bind local address to inform your address to the one you chat with
    thread1 = threading.Thread(target=send_message, args=(udp,))
    thread2 = threading.Thread(target=recv_message, args=(udp,))
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    main()
