# client.py
from tkinter import Tk, Frame, Scrollbar, Label, Entry, Text, Button, messagebox
import socket
import threading

class GUI:
    def __init__(self, master):
        self.root = master
        self.client_socket = None
        self.initialize_socket()
        self.initialize_gui()
        self.listen_for_incoming_messages_in_a_thread()

    def initialize_socket(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_ip = '127.0.0.1'
            remote_port = 10319
            self.client_socket.connect((socket.gethostname(), remote_port))
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to connect: {e}")
            self.root.destroy()

    def initialize_gui(self):
        self.root.title("Socket Chat")
        self.root.resizable(0, 0)
        self.display_chat_box()
        self.display_name_section()
        self.display_chat_entry_box()

    def listen_for_incoming_messages_in_a_thread(self):
        threading.Thread(target=self.receive_message_from_server, args=(self.client_socket,)).start()

    def receive_message_from_server(self, so):
        while True:
            try:
                buffer = so.recv(256)
                if not buffer:
                    break
                message = buffer.decode('utf-8')
                if "joined" in message:
                    user = message.split(":")[1]
                    message = user + " has joined"
                elif "authenticated" in message:
                    message = "Successfully authenticated"
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview('end')
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

        so.close()

    def display_name_section(self):
        frame = Frame()
        Label(frame, text='Enter your name:').pack(side='left', padx=10)
        self.name_widget = Entry(frame, width=20, borderwidth=2)
        self.name_widget.pack(side='left', anchor='e')
        Label(frame, text='Password:').pack(side='left', padx=10)
        self.password_widget = Entry(frame, width=20, show='*', borderwidth=2)
        self.password_widget.pack(side='left', anchor='e')
        self.join_button = Button(frame, text="Join", width=10, command=self.on_join)
        self.join_button.pack(side='left')
        frame.pack(side='top', anchor='nw')

    def display_chat_box(self):
        frame = Frame()
        Label(frame, text='Chat Box:').pack(side='top', anchor='w')
        self.chat_transcript_area = Text(frame, width=60, height=10)
        scrollbar = Scrollbar(frame, command=self.chat_transcript_area.yview, orient='vertical')
        self.chat_transcript_area.config(yscrollcommand=scrollbar.set)
        self.chat_transcript_area.bind('<KeyPress>', lambda e: 'break')
        self.chat_transcript_area.pack(side='left', padx=10)
        scrollbar.pack(side='right', fill='y')
        frame.pack(side='top')

    def display_chat_entry_box(self):
        frame = Frame()
        Label(frame, text='Enter message:').pack(side='top', anchor='w')
        self.enter_text_widget = Text(frame, width=60, height=3)
        self.enter_text_widget.pack(side='left', pady=15)
        self.enter_text_widget.bind('<Return>', self.on_enter_key_pressed)
        frame.pack(side='top')

    def on_join(self):
        if len(self.name_widget.get()) == 0:
            messagebox.showerror("Enter your name", "Enter your name to send a message")
            return
        password = self.password_widget.get()
        self.name_widget.config(state='disabled')
        self.password_widget.config(state='disabled')
        self.join_button.config(state='disabled')
        self.client_socket.send(f"joined:{self.name_widget.get()}:{password}".encode('utf-8'))

    def on_enter_key_pressed(self, event):
        if len(self.name_widget.get()) == 0:
            messagebox.showerror("Enter your name", "Enter your name to send a message")
            return
        self.send_chat()
        self.clear_text()

    def clear_text(self):
        self.enter_text_widget.delete(1.0, 'end')

    def send_chat(self):
        senders_name = self.name_widget.get().strip() + ": "
        data = self.enter_text_widget.get(1.0, 'end').strip()
        message = (senders_name + data).encode('utf-8')
        self.chat_transcript_area.insert('end', message.decode('utf-8') + '\n')
        self.chat_transcript_area.yview('end')
        self.client_socket.send(message)
        self.enter_text_widget.delete(1.0, 'end')
        return 'break'

    def on_close_window(self):
        if self.root:
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.client_socket.close()
                self.root.destroy()
                self.root = None
                exit(0)

if __name__ == '__main__':
    root = Tk()
    gui = GUI(root)
    root.protocol("WM_DELETE_WINDOW", gui.on_close_window)
    root.mainloop()
