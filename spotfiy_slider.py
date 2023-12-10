import tkinter as tk
from tkinter import ttk
import sys
import websockets
import multiprocessing

class TinkerApp(tk.Tk):
    def __init__(self):
        super().__init__(
            screenName="spotify_slider",
            baseName="spotify_slider"
        )
        self.title("Spotify music slider")

        # Slider
        self.slider = ttk.Scale(self, from_=0, to=100, orient="horizontal", command=self.slider_changed)
        self.slider.grid(columnspan=3, row=1, column=1)

        # Slider Indicator Label
        self.slider_label = tk.Label(self, text="Volume: 0%")
        self.slider_label.grid(row=2, column=1)

        # Pin/Unpin Button
        self.pin_button = tk.Button(self, text="Pin", command=self.toggle_pin)
        self.pin_button.grid(row=2, column=2, columnspan=3)

        # Initialize pinned state
        self.pinned = False
        
        # Setup the sizing
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=1)
        
    def slider_changed(self, value):
        # Update the slider indicator label
        vol_percent = int(float(value))
        self.slider_label.config(text=f"Volume: {vol_percent}%")

    def toggle_pin(self):
        if self.pinned:
            self.attributes('-topmost', 0)  # Unpin the window
            self.pin_button.config(text="Pin")
        else:
            self.attributes('-topmost', 1)  # Pin the window
            self.pin_button.config(text="Unpin")

        # Toggle pinned state
        self.pinned = not self.pinned
        

    def on_start(self):
        h = self.winfo_height(); w = self.winfo_width()
        inc_w = 2.5
        inc_h = 2
        self.minsize(w, h)
        h *= inc_h; w *= inc_w
        h = int(h); w = int(w)
        self.maxsize(w, h)


    def mainloop(self, n: int = 0) -> None:
        self.after(500, self.on_start)
        self.after_idle(self.ws_server_process)
        return super().mainloop(n)
    
    async def ws_server_process():
        
        pass

if __name__ == "__main__":
    argc, argv = (len(sys.argv), sys.argv)

    
    app = TinkerApp()
    app.mainloop()

