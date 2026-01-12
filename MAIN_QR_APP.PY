import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import ImageTk, Image
import os

# Import the logic function from your QR_LOGIC.py file
try:
    from QR_LOGIC import create_qr_with_logo
except ImportError:
    messagebox.showerror("Module Error", "Could not find QR_LOGIC.py!")

def toggle_password():
    """Toggles the Wi-Fi password visibility between masked and plain text."""
    if show_pass_var.get():
        ent_wifi_pass.config(show="")
    else:
        ent_wifi_pass.config(show="*")

def update_input_fields(event=None):
    """Changes UI labels and inputs based on selected QR type."""
    choice = type_combo.get()
    
    # Reset standard entry
    ent_data.pack_forget()
    wifi_frame.pack_forget()
    
    if choice == "Link / Text":
        lbl_instruction.config(text="Enter URL or Message:")
        ent_data.pack(pady=5)
    elif choice == "Wi-Fi Network":
        lbl_instruction.config(text="Enter Wi-Fi Details:")
        wifi_frame.pack(pady=5)
    elif choice == "Contact (vCard)":
        lbl_instruction.config(text="Format: Name;Phone;Email")
        ent_data.pack(pady=5)
        if not ent_data.get():
            ent_data.insert(0, "John Doe;+123456789;john@email.com")

def on_logo_toggle():
    if logo_enabled_var.get():
        btn_browse.pack(after=check_logo, pady=5)
        lbl_logo_name.pack(after=btn_browse)
    else:
        btn_browse.pack_forget()
        lbl_logo_name.pack_forget()
        logo_path_var.set("")

def select_logo():
    path = filedialog.askopenfilename(title="Select Logo", filetypes=[("Images", "*.png *.jpg *.jpeg")])
    if path:
        logo_path_var.set(path)
        lbl_logo_name.config(text=f"Selected: {os.path.basename(path)}")

def generate():
    choice = type_combo.get()
    raw_data = ""

    if choice == "Link / Text":
        raw_data = ent_data.get()
    elif choice == "Wi-Fi Network":
        ssid = ent_wifi_ssid.get()
        password = ent_wifi_pass.get()
        raw_data = f"WIFI:S:{ssid};T:WPA;P:{password};;"
    elif choice == "Contact (vCard)":
        parts = ent_data.get().split(';')
        if len(parts) >= 3:
            raw_data = f"BEGIN:VCARD\nVERSION:3.0\nN:{parts[0]}\nTEL:{parts[1]}\nEMAIL:{parts[2]}\nEND:VCARD"
        else:
            messagebox.showerror("Error", "Use format: Name;Phone;Email")
            return

    if not raw_data:
        messagebox.showwarning("Input Error", "Input cannot be empty!")
        return
        
    save_path = filedialog.asksaveasfilename(defaultextension=".png", title="Save QR")
    if not save_path: return

    logo = logo_path_var.get() if logo_enabled_var.get() else None

    try:
        qr_obj = create_qr_with_logo(raw_data, logo, save_path)
        qr_preview = qr_obj.resize((250, 250), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(qr_preview)
        lbl_preview.config(image=img_tk, text="")
        lbl_preview.image = img_tk 
        messagebox.showinfo("Success", "QR Code Saved!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def refresh():
    ent_data.delete(0, tk.END)
    ent_wifi_ssid.delete(0, tk.END)
    ent_wifi_pass.delete(0, tk.END)
    show_pass_var.set(False)
    toggle_password()
    logo_enabled_var.set(False)
    on_logo_toggle()
    lbl_preview.config(image="", text="Your QR Code will appear here")

# --- UI Setup ---
root = tk.Tk()
root.title("Universal QR Pro")
root.geometry("450x850")

# 1. Type Selector
tk.Label(root, text="Select QR Type:", font=("Arial", 10, "bold")).pack(pady=10)
type_combo = ttk.Combobox(root, values=["Link / Text", "Wi-Fi Network", "Contact (vCard)"], state="readonly")
type_combo.current(0)
type_combo.pack()
type_combo.bind("<<ComboboxSelected>>", update_input_fields)

# 2. Input Section
lbl_instruction = tk.Label(root, text="Enter URL or Message:", font=("Arial", 9))
lbl_instruction.pack(pady=10)
ent_data = tk.Entry(root, width=45)
ent_data.pack()

# --- Wi-Fi Frame ---
wifi_frame = tk.Frame(root)
tk.Label(wifi_frame, text="Network Name (SSID):").pack()
ent_wifi_ssid = tk.Entry(wifi_frame, width=30)
ent_wifi_ssid.pack()

tk.Label(wifi_frame, text="Password:").pack(pady=(10,0))
ent_wifi_pass = tk.Entry(wifi_frame, width=30, show="*")
ent_wifi_pass.pack()

show_pass_var = tk.BooleanVar()
tk.Checkbutton(wifi_frame, text="Show Password", variable=show_pass_var, command=toggle_password).pack()

# 3. Logo Options
logo_enabled_var = tk.BooleanVar()
logo_path_var = tk.StringVar()
check_logo = tk.Checkbutton(root, text="Add a logo to the center?", variable=logo_enabled_var, command=on_logo_toggle)
check_logo.pack(pady=20)
btn_browse = tk.Button(root, text="📁 Select Logo", command=select_logo)
lbl_logo_name = tk.Label(root, text="No logo selected", fg="gray", font=("Arial", 8))

# 4. Action Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)
tk.Button(btn_frame, text="GENERATE", bg="#27ae60", fg="white", font=("Arial", 11, "bold"), command=generate, width=15).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="REFRESH", bg="#e67e22", fg="white", font=("Arial", 11), command=refresh, width=10).pack(side=tk.LEFT, padx=5)

lbl_preview = tk.Label(root, text="Your QR Code will appear here", bg="#f0f0f0", width=35, height=12, relief="sunken")
lbl_preview.pack(pady=10)

root.mainloop()
