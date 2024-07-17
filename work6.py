import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー　背景色
bg_color2 = "#000000"
fg_color = "#FFFFFF"  # 白　　　　　　文字色
fg_color2 = "#ffff00"
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

num = random.randint(1, 2)

if num == 1:
    mark = "×"
    label1 = tk.Label(window, text=f"あなたは {mark} です", bg=bg_color, fg=fg_color)
    label1.pack(pady=10)
elif num == 2:
    mark = "◯"
    label1 = tk.Label(window, text=f"あなたは {mark} です", bg=bg_color, fg=fg_color)
    label1.pack(pady=10)


num_table = [["", "", ""], ["", "", ""], ["", "", ""]]


def button_action():  # 関数の定義 ※ボタンが押されたときの動き 　　　リセット用
    button1.config(text="　")
    button2.config(text="　")
    button3.config(text="　")
    button4.config(text="　")
    button5.config(text="　")
    button6.config(text="　")
    button7.config(text="　")
    button8.config(text="　")
    button9.config(text="　")
    label2.config(text="　")
    num_table == [["", "", ""], ["", "", ""], ["", "", ""]]


def action(x, y):
    num_table[x][y] = mark
    # 勝利判定横ライン
    if num_table[0][0] == mark and num_table[0][1] == mark and num_table[0][2] == mark:
        label2.config(text="あなたの勝ちです")
    elif (
        num_table[1][0] == mark and num_table[1][1] == mark and num_table[1][2] == mark
    ):
        label2.config(text="あなたの勝ちです")
    elif (
        num_table[2][0] == mark and num_table[2][1] == mark and num_table[2][2] == mark
    ):
        label2.config(text="あなたの勝ちです")
    # 勝利判定縦ライン
    elif (
        num_table[0][0] == mark and num_table[1][0] == mark and num_table[2][0] == mark
    ):
        label2.config(text="あなたの勝ちです")
    elif (
        num_table[0][1] == mark and num_table[1][1] == mark and num_table[2][1] == mark
    ):
        label2.config(text="あなたの勝ちです")
    elif (
        num_table[0][2] == mark and num_table[1][2] == mark and num_table[2][2] == mark
    ):
        label2.config(text="あなたの勝ちです")
    # 勝利判定ななめライン
    elif (
        num_table[0][0] == mark and num_table[1][1] == mark and num_table[2][2] == mark
    ):
        label2.config(text="あなたの勝ちです")
    elif (
        num_table[0][2] == mark and num_table[1][1] == mark and num_table[2][0] == mark
    ):
        label2.config(text="あなたの勝ちです")


def button_action1():  # 関数の定義 ※ボタンが押されたときの動き
    button1.config(text=mark)
    action(0, 0)


def button_action2():  # 関数の定義 ※ボタンが押されたときの動き
    button2.config(text=mark)
    action(0, 1)


def button_action3():  # 関数の定義 ※ボタンが押されたときの動き
    button3.config(text=mark)
    action(0, 2)


def button_action4():  # 関数の定義 ※ボタンが押されたときの動き
    button4.config(text=mark)
    action(1, 0)


def button_action5():  # 関数の定義 ※ボタンが押されたときの動き
    button5.config(text=mark)
    action(1, 1)


def button_action6():  # 関数の定義 ※ボタンが押されたときの動き
    button6.config(text=mark)
    action(1, 2)


def button_action7():  # 関数の定義 ※ボタンが押されたときの動き
    button7.config(text=mark)
    action(2, 0)


def button_action8():  # 関数の定義 ※ボタンが押されたときの動き
    button8.config(text=mark)
    action(2, 1)


def button_action9():  # 関数の定義 ※ボタンが押されたときの動き
    button9.config(text=mark)
    action(2, 2)


# ボタンの作成
button = tk.Button(window, text="リセット", command=button_action)
button.place(x=257, y=68)

# ボタンの作成
button1 = tk.Button(window, text="　", command=button_action1)
button1.place(x=220, y=120)

# ボタンの作成
button2 = tk.Button(window, text="　", command=button_action2)
button2.place(x=280, y=120)

# ボタンの作成
button3 = tk.Button(window, text="　", command=button_action3)
button3.place(x=340, y=120)

# ボタンの作成
button4 = tk.Button(window, text="　", command=button_action4)
button4.place(x=220, y=160)

# ボタンの作成
button5 = tk.Button(window, text="　", command=button_action5)
button5.place(x=280, y=160)

# ボタンの作成
button6 = tk.Button(window, text="　", command=button_action6)
button6.place(x=340, y=160)

# ボタンの作成
button7 = tk.Button(window, text="　", command=button_action7)
button7.place(x=220, y=200)

# ボタンの作成
button8 = tk.Button(window, text="　", command=button_action8)
button8.place(x=280, y=200)

# ボタンの作成
button9 = tk.Button(window, text="　", command=button_action9)
button9.place(x=340, y=200)

# 出力ラベルの作成
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.place(x=250, y=300)

matrix_frame = tk.Frame(window)
matrix_frame.pack(pady=0)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
