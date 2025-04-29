import tkinter as tk
from autocorrector import AutoCorrector

def run_correction():
    input_text = text_input.get("1.0", tk.END)
    corrected_text = ""

    if correction_mode.get() == "Basic":
        corrected_text = corrector.basic_correct(input_text)
    else:
        corrected_text = corrector.context_correct(input_text)

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, corrected_text)

corrector = AutoCorrector()
root = tk.Tk()
root.title("AI Autocorrect Tool")
root.geometry("600x400")

tk.Label(root, text="Enter Text:").pack()
text_input = tk.Text(root, height=5)
text_input.pack()

correction_mode = tk.StringVar(value="Basic")
tk.Radiobutton(root, text="Basic (TextBlob)", variable=correction_mode, value="Basic").pack()
tk.Radiobutton(root, text="Context-Aware (BERT)", variable=correction_mode, value="Context").pack()

tk.Button(root, text="Correct Text", command=run_correction).pack()

tk.Label(root, text="Corrected Text:").pack()
text_output = tk.Text(root, height=5)
text_output.pack()

root.mainloop()
