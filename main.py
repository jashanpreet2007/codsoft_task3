import customtkinter as ctk
import random
import string
from tkinter import messagebox

# ---------------- SETTINGS ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x700")
app.title("Jashanpreet's Advanced Password Generator")
app.resizable(False, False)

# ---------------- FUNCTIONS ---------------- #

def update_length(value):
    length_label.configure(
        text=f"Password Length: {int(value)} Characters"
    )


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak 🔴"
    elif score == 3:
        return "Medium 🟠"
    elif score == 4:
        return "Strong 🟢"
    else:
        return "Very Strong 🔥"


def generate_password():

    characters = ""

    if uppercase_var.get():
        characters += string.ascii_uppercase

    if lowercase_var.get():
        characters += string.ascii_lowercase

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror(
            "Error",
            "Please select at least one character type."
        )
        return

    length = int(slider.get())

    password = "".join(
        random.choice(characters)
        for _ in range(length)
    )

    password_entry.delete(0, "end")
    password_entry.insert(0, password)

    strength = check_strength(password)

    strength_label.configure(
        text=f"Password Strength: {strength}"
    )

    history_box.insert("0.0", password + "\n")


def copy_password():

    password = password_entry.get()

    if password:
        app.clipboard_clear()
        app.clipboard_append(password)

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )


# ---------------- TITLE ---------------- #

title = ctk.CTkLabel(
    app,
    text="🔐 ADVANCED PASSWORD GENERATOR",
    font=("Arial", 32, "bold")
)

title.pack(pady=15)

subtitle = ctk.CTkLabel(
    app,
    text="Generate Secure, Random & Strong Passwords",
    font=("Arial", 16)
)

subtitle.pack()

# ---------------- LENGTH ---------------- #

length_label = ctk.CTkLabel(
    app,
    text="Password Length: 12 Characters",
    font=("Arial", 18)
)

length_label.pack(pady=(20, 5))

slider = ctk.CTkSlider(
    app,
    from_=4,
    to=32,
    number_of_steps=28,
    width=450,
    command=update_length
)

slider.set(12)
slider.pack(pady=10)

# ---------------- OPTIONS ---------------- #

options_frame = ctk.CTkFrame(app)
options_frame.pack(pady=15)

uppercase_var = ctk.BooleanVar(value=True)
lowercase_var = ctk.BooleanVar(value=True)
numbers_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=True)

ctk.CTkCheckBox(
    options_frame,
    text="Uppercase",
    variable=uppercase_var
).grid(row=0, column=0, padx=15, pady=10)

ctk.CTkCheckBox(
    options_frame,
    text="Lowercase",
    variable=lowercase_var
).grid(row=0, column=1, padx=15, pady=10)

ctk.CTkCheckBox(
    options_frame,
    text="Numbers",
    variable=numbers_var
).grid(row=0, column=2, padx=15, pady=10)

ctk.CTkCheckBox(
    options_frame,
    text="Symbols",
    variable=symbols_var
).grid(row=0, column=3, padx=15, pady=10)

# ---------------- PASSWORD BOX ---------------- #

password_entry = ctk.CTkEntry(
    app,
    width=550,
    height=50,
    font=("Consolas", 18)
)

password_entry.pack(pady=15)

# ---------------- BUTTONS ---------------- #

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

generate_button = ctk.CTkButton(
    button_frame,
    text="Generate Password",
    width=180,
    command=generate_password
)

generate_button.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

copy_button = ctk.CTkButton(
    button_frame,
    text="Copy Password",
    width=150,
    command=copy_password
)

copy_button.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)

# ---------------- STRENGTH ---------------- #

strength_label = ctk.CTkLabel(
    app,
    text="Password Strength: -",
    font=("Arial", 18, "bold")
)

strength_label.pack(pady=10)

# ---------------- HISTORY ---------------- #

history_title = ctk.CTkLabel(
    app,
    text="Password History",
    font=("Arial", 20, "bold")
)

history_title.pack(pady=(15, 5))

history_box = ctk.CTkTextbox(
    app,
    width=650,
    height=180
)

history_box.pack(pady=10)

# ---------------- FOOTER ---------------- #

footer = ctk.CTkLabel(
    app,
    text="© 2026 Jashanpreet | Advanced Password Generator v1.0",
    font=("Arial", 12)
)

footer.pack(side="bottom", pady=10)

# Generate one password automatically
generate_password()

# Run App
app.mainloop()
