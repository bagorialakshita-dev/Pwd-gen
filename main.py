import tkinter as tk
from tkinter import messagebox
import secrets
import string


def generate_password(length, groups):
    if not groups or length < len(groups):
        raise ValueError('Select at least one character type.')
    chars = [secrets.choice(group) for group in groups]
    chars += [secrets.choice(''.join(groups)) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return ''.join(chars)


def main():
    root = tk.Tk()
    root.title('PassGen | Password Generator')
    root.geometry('480x510')
    root.minsize(420, 490)
    root.configure(bg='#111827')
    bg = '#111827'
    fg = '#F3F4F6'
    tk.Label(root, text='PassGen', font=('Arial', 30, 'bold'), bg=bg, fg='#A78BFA').pack(pady=(24, 4))
    tk.Label(root, text='Create a strong random password', bg=bg, fg=fg).pack()
    result = tk.StringVar()
    tk.Entry(root, textvariable=result, state='readonly', readonlybackground='#243044', fg=fg, font=('Arial', 15), justify='center').pack(fill='x', padx=30, pady=20, ipady=10)
    length = tk.IntVar(value=16)
    tk.Label(root, text='Password length', bg=bg, fg=fg).pack()
    tk.Scale(root, from_=8, to=40, orient='horizontal', variable=length, bg=bg, fg=fg, highlightthickness=0, troughcolor='#374151').pack(fill='x', padx=30)
    options = [(name, chars, tk.BooleanVar(value=True)) for name, chars in [('Uppercase letters', string.ascii_uppercase), ('Lowercase letters', string.ascii_lowercase), ('Numbers', string.digits), ('Symbols', string.punctuation)]]
    for name, chars, enabled in options:
        tk.Checkbutton(root, text=name, variable=enabled, bg=bg, fg=fg, selectcolor='#374151', activebackground=bg, activeforeground=fg).pack(anchor='w', padx=30)
    status = tk.StringVar(value='Ready to generate')

    def generate():
        groups = [chars for _, chars, enabled in options if enabled.get()]
        try:
            result.set(generate_password(length.get(), groups))
            status.set('Password generated')
        except ValueError as error:
            messagebox.showwarning('PassGen', str(error))

    def copy():
        if result.get():
            root.clipboard_clear()
            root.clipboard_append(result.get())
            status.set('Copied to clipboard')

    tk.Button(root, text='Generate password', command=generate, bg='#7C3AED', fg='white', relief='flat').pack(fill='x', padx=30, pady=(15, 6), ipady=8)
    tk.Button(root, text='Copy password', command=copy, bg='#374151', fg='white', relief='flat').pack(fill='x', padx=30, ipady=6)
    tk.Label(root, textvariable=status, bg=bg, fg='#A78BFA').pack(pady=10)
    root.mainloop()


if __name__ == '__main__':
    main()
