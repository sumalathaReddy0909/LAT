import tkinter as tk

class login (tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(fist_window)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class fist_window(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Log Analsys window",bd=8,bg="light blue",).pack(side="top", pady=50)
        tk.Button(self, text="ANALISE",fg="blue",
                  command=lambda: master.switch_frame(ANALISE)).pack()
        tk.Button(self, text="SEARCH",fg="blue",
                  command=lambda: master.switch_frame(SEARCH)).pack()
        tk.Button(self, text="OUTPUT",fg="blue",
                  command=lambda: master.switch_frame(OUTPUT)).pack()

class ANALISE(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="failure log file:").pack(side="top", pady=50)
        tk.Button(self, text="back", fg="green",
                  command=lambda: master.switch_frame(fist_window)).pack()

class SEARCH(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="erors:").pack(side="top",  pady=50)
        tk.Button(self, text="Back",fg="green",
                  command=lambda: master.switch_frame(fist_window)).pack()
class OUTPUT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="All log file:").pack(side="top", pady=50)
        tk.Button(self, text="Back",fg="green",
                  command=lambda: master.switch_frame(fist_window)).pack()
if __name__ == "__main__":
    app = login()
    app.mainloop()