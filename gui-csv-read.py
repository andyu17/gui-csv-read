import pandas as pd
import tkinter as tk
from tkinter import filedialog

# ファイルダイアログでCSVファイルを選択する
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# CSVファイルを読み込み、DataFrameに変換する
df = pd.read_csv(file_path)

# GUIで列を選択するためのウィンドウを作成する
window = tk.Tk()
window.title("Select Columns")

# チェックボックスで列の選択を行う
var_car_id = tk.BooleanVar()
var_speed = tk.BooleanVar()
var_datetime = tk.BooleanVar()

cb_car_id = tk.Checkbutton(window, text="car_id", variable=var_car_id)
cb_car_id.pack()

cb_speed = tk.Checkbutton(window, text="speed", variable=var_speed)
cb_speed.pack()

cb_datetime = tk.Checkbutton(window, text="datetime", variable=var_datetime)
cb_datetime.pack()

# OKボタンをクリックした場合、選択された列を抽出する
def ok_button_clicked():
    selected_columns = []
    if var_car_id.get():
        selected_columns.append("car_id")
    if var_speed.get():
        selected_columns.append("speed")
    if var_datetime.get():
        selected_columns.append("datetime")

    # 選択された列を抽出し、新しいDataFrameを作成する
    new_df = df[selected_columns]
    window.destroy()

# OKボタンを作成する
ok_button = tk.Button(window, text="OK", command=ok_button_clicked)
ok_button.pack()

# ウィンドウを表示する
window.mainloop()

# 選択された列を含む新しいDataFrameを表示する
print(new_df)

