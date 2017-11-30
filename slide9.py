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

# ウィンドウ作成
root = tkinter.Tk()
root.title("ダンジョン＆パイソン")
root.minsize(840, 454)
root.option_add("*font", ["メイリオ", 14])
# キャンバス作成
canvas = tkinter.Canvas(width=620, height=434)
canvas.place(x=10, y=10)
canvas.create_rectangle(0, 0, 620, 434, fill="gray")

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