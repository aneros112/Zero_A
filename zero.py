import webbrowser
import tkinter as tk

url = "https://aneros112.github.io/Zero_A/"

# افتح الموقع في المتصفح الافتراضي
webbrowser.open(url)

# نافذة صغيرة فيها زر إغلاق
root = tk.Tk()
root.title("Zero Azrael Control")
root.geometry("200x100")
root.configure(bg="#1a1a1a")

btn = tk.Button(root, text="إغلاق ✖", command=root.destroy,
                bg="#d9363e", fg="white", font=("Arial", 12, "bold"),
                relief="flat", width=12, height=2)
btn.pack(pady=20)

root.mainloop()
