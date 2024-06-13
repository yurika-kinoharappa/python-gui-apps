import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑
"""
1868年〜1912年　明治
1912年〜1926年　大正
1926年〜1989年　昭和
1989年〜2019年　平成
2019年〜2024年　令和
"""

# 出力ラベルの作成
label1 = tk.Label(window, text="西暦を入力してください", bg=bg_color, fg=fg_color)
label1.pack(pady=10)


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    num = int(entry1.get())  # 入力値を取得
    if num <= 1912:
        seireki = "明治" + str(num - 1867)
    elif 1913 <= num <= 1926:
        seireki = "大正" + str(num - 1912)
    elif 1927 <= num <= 1989:
        seireki = "昭和" + str(num - 1926)
    elif 1900 <= num <= 2019:
        seireki = "平成" + str(num - 1989)
    elif 2020 <= num <= 2024:
        seireki = "令和" + str(num - 2019)
    else:
        label2.config(text="")
    label2.config(text=f"西暦{num}年は、{seireki}年です")


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="変換", command=button_action)
button1.pack(pady=10)

label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
