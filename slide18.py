import tkinter

# マップの描画
def draw_map():
    for y in range(0, MAX_HEIGHT):
        for x in range(0, MAX_WIDTH):
            p = map_data[y][x]
            canvas.create_image(x*62+31, y*62+31, image=images[p])

    # 主人公表示
    canvas.create_image(brave_x*62+31, brave_y*62+31,
        image=images[4], tag="brave")

def click_button_up():
    global brave_y
    brave_y = brave_y - 1
    canvas.coords("brave", brave_x*62+31, brave_y*62+31)

def click_button_down():
    global brave_y
    brave_y = brave_y + 1
    canvas.coords("brave", brave_x*62+31, brave_y*62+31)

def click_button_left():
    global brave_x
    brave_x = brave_x - 1
    canvas.coords("brave", brave_x*62+31, brave_y*62+31)

def click_button_right():
    global brave_x
    brave_x = brave_x + 1
    canvas.coords("brave", brave_x*62+31, brave_y*62+31)

# ウィンドウ作成
root = tkinter.Tk()
root.title("ダンジョン＆パイソン")
root.minsize(840, 454)
root.option_add("*font", ["メイリオ", 14])
# キャンバス作成
canvas = tkinter.Canvas(width=620, height=434)
canvas.place(x=10, y=10)
canvas.create_rectangle(0, 0, 620, 434, fill="gray")
# ボタン配置
button_up = tkinter.Button(text="↑")
button_up.place(x=720, y=150)
button_up["command"] = click_button_up
button_down = tkinter.Button(text="↓")
button_down.place(x=720, y=210)
button_down["command"] = click_button_down
button_left = tkinter.Button(text="←")
button_left.place(x=660, y=180)
button_left["command"] = click_button_left
button_right = tkinter.Button(text="→")
button_right.place(x=780, y=180)
button_right["command"] = click_button_right

# 画像データを読み込み
sample_path="12saipython/"
images = [tkinter.PhotoImage(file=(sample_path+"img6\chap6-mapfield.png")),
          tkinter.PhotoImage(file=(sample_path+"img6\chap6-mapwall.png")),
          tkinter.PhotoImage(file=(sample_path+"img6\chap6-mapgoal.png")),
          tkinter.PhotoImage(file=(sample_path+"img6\chap6-mapkey.png")),
          tkinter.PhotoImage(file=(sample_path+"img6\chap6-mapman.png"))]

# マップデータ
MAX_WIDTH = 10
MAX_HEIGHT = 7
map_data = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 2, 0, 0, 1, 3, 1],
            [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
# 主人公の位置
brave_x = 1
brave_y = 0
# 鍵取得フラグ
flag_key = False

draw_map()
root.mainloop()