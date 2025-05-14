import keyboard
import mouse
import mss
import mss.tools

i = int(open("last_index.txt","r").read())
print(i)

pause = False
def on_press(e):
    if(e.name != 'p'): return
    global pause
    pause = not pause
    if(pause): print("Paused data collection")
    else: print("Unpaused data collection")

def on_click():
    global i
    global pause
    sct = mss.mss()
    if(pause): return
    i+=1

    filename = f"raw_data/screenshot_{i}.png"

    img = sct.grab({
        "top":508,
        "left":928,
        "width":64,
        "height":64
    })
    mss.tools.to_png(img.rgb, img.size, output=filename)
    open("last_index.txt","w").write(str(i))

mouse.on_click(on_click)
keyboard.on_press(on_press)
keyboard.wait('[')

# Controls:
# "[" to capture data, "p" to pause