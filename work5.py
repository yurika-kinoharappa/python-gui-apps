import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

str_list = [
    "今日はいい天気だ",
    "森に出かけよう",
    "はちみつを食べた",
    "クマに出会った",
    "クマがショックを受けている",
    "今のうちに帰ろう",
    "疲れて眠った",
]

label1 = tk.Label(window, text=str_list[0], bg=bg_color, fg=fg_color)
label1.pack(pady=10)


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    user_input = entry1.get()  # 入力値を取得
    if label1.cget("text") == user_input:
        import random

        num = random.randint(0, 4)
        label1.config(text=str_list[num])  # 画面に出力

    else:
        label2.config(text="")  # 画面に出力
    entry1.delete(0, tk.END)  # Entryの文字を削除


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="OK", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label0 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label0.pack(pady=10)

label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)
# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
