import socket
import threading

class ChatServer:

    clients_list = []
    users = {"abhishek": "abhi", "user1": "abhi"}  # Add your username-password pairs here

    last_received_message = ""

    def __init__(self):
        self.server_socket = None
        self.create_listening_server()

    def create_listening_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        local_ip = ''
        local_port = 10319
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((socket.gethostname(), local_port))
        print("Listening for incoming messages..")
        self.server_socket.listen(5)
        self.receive_messages_in_a_new_thread()

    def receive_messages(self, so, username):
        while True:
            incoming_buffer = so.recv(256)
            if not incoming_buffer:
                break
            self.last_received_message = incoming_buffer.decode('utf-8')
            self.broadcast_to_all_clients(so, username)
        so.close()

    def broadcast_to_all_clients(self, senders_socket, username):
        for client in self.clients_list:
            socket, (ip, port), client_username = client
            if socket is not senders_socket:
                socket.sendall(f"{username}: {self.last_received_message}".encode('utf-8'))

    def receive_messages_in_a_new_thread(self):
        while True:
            client = so, (ip, port) = self.server_socket.accept()
            username, password = self.authenticate_client(so)
            if username and self.check_credentials(username, password):
                self.add_to_clients_list(client, username)
                print('Connected to', ip, ':', str(port), 'as', username)
                t = threading.Thread(target=self.receive_messages, args=(so, username))
                t.start()
            else:
                print('Invalid credentials. Connection refused.')

    def authenticate_client(self, so):
        so.sendall("Enter username: ".encode('utf-8'))
        username = so.recv(1024).decode('utf-8')
        so.sendall("Enter password: ".encode('utf-8'))
        password = so.recv(1024).decode('utf-8')
        return username, password

    def check_credentials(self, username, password):
        return username in self.users and self.users[username] == password

    def add_to_clients_list(self, client, username):
        if (client, username) not in self.clients_list:
            self.clients_list.append((client, username))


if __name__ == "__main__":
    ChatServer()
