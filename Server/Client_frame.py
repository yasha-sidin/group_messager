import threading
import time
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

import schedule as schedule

class Client_frame:
    def __init__(self, client):
        self._client = client
        self._send_frame = None
        self._textfield = None
        self._header_entry = None
        self._string_var_header = None

    def initialize(self):
        window = tk.Tk()
        window.title("Group's messager")
        window.minsize(950, 777)
        window.maxsize(950, 777)

        LISTBOX_FONT = tkFont.Font(family="Arial", size=14, slant="italic")
        BUTTON_FONT = tkFont.Font(family="Times New Roman", size=14, weight="bold", slant="italic")
        HEADER_FONT = tkFont.Font(family="Arial", size=14, slant="italic")

        style = ttk.Style()
        style.theme_use('alt')

        style.configure(
            "Vertical.TScrollbar",
            gripcount=0,
            background="#EBC8C1",
            darkcolor="#EBC8C1",
            lightcolor="#EBC8C1",
            troughcolor="#EBC8C1",
            bordercolor="#EBC8C1",
            arrowcolor="#B27355"
        )

        master_frame = tk.Frame(master=window, height=600, width=600, bg="#EBC8C1")
        master_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        text_frame = tk.Frame(master=master_frame, bg="#EBC8C1")
        text_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=6, pady=6, anchor=tk.N)

        text_field_frame = tk.Frame(master=text_frame, bg="#D5A8A0")
        text_field_frame.pack(fill=tk.BOTH, side=tk.TOP, padx=6, pady=6, expand=True)

        self._textfield = tk.Text(master=text_field_frame, relief="ridge", bg="#D5A8A0", background="#F4DBD6",
                                  height=26,
                                  highlightbackground="white", selectbackground="#FBEEE6", selectforeground="#E77A63",
                                  padx=15, pady=15, font=LISTBOX_FONT, width=65, undo=True, state='disabled')
        self._textfield.pack(fill=tk.BOTH, side=tk.LEFT, padx=6, pady=6, expand=True)

        scrollbar_vertical = ttk.Scrollbar(master=text_field_frame, orient=tk.VERTICAL, command=self._textfield.yview,
                                           cursor="arrow")
        scrollbar_vertical.pack(fill=tk.BOTH, side=tk.RIGHT)

        self._send_frame = tk.Frame(master=text_frame, bg="#EBC8C1")
        self._send_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=140, pady=6, anchor=tk.N)

        self._string_var_header = tk.StringVar(master_frame)
        self._header_entry = tk.Entry(master=self._send_frame, bg="#D5A8A0", font=HEADER_FONT, relief="ridge",
                                      justify=tk.LEFT, selectbackground="#FBEEE6", selectforeground="#E77A63", width=60, textvariable=self._string_var_header)
        self._header_entry.pack(side=tk.LEFT)

        button_clear = tk.Button(master=self._send_frame, text="Send", font=BUTTON_FONT, background="#D5A8A0",
                                 activebackground="#F4DBD6", command=self.__send_message)
        button_clear.pack(side=tk.LEFT)
        self.__refresh_messages()

        threading.Thread(target=self.__run).start()


        window.mainloop()

    def __refresh_messages(self):
        self._textfield['state'] = 'normal'
        data = list(map(lambda x: 'Message: ' + x + "\n", self._client.get_data()))
        string = ""
        for row in data:
            string += row
        if self._textfield.get("1.0", tk.END) == string:
            return
        self.__clear_text()
        self._textfield.insert("1.0", string)
        self._textfield['state'] = 'disabled'

    def __run(self):
        try:
            schedule.every(1).seconds.do(self.__refresh_messages)
            while True:
                time.sleep(1)
                schedule.run_pending()
        except Exception:
            exit(0)

    def __clear_text(self):
        self._textfield.delete("1.0", tk.END)

    def __send_message(self):
        if self._string_var_header.get() == "":
            return
        self._client.send_message(self._header_entry.get())
        self._header_entry.delete(0, tk.END)

    button_frame = property
    master = property
    textfield = property
    header_entry = property


