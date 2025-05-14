import numpy as np
import tensorflow as tf
import mss
import time
import pyautogui
import keyboard


model = tf.saved_model.load("model4/")
signature_keys = list(model.signatures.keys())
prediction_signature = model.signatures[signature_keys[0]]

sct = mss.mss()

team_offset = 0

pause = False
confidence_threshold = 0.9

def on_press(e):
    global pause
    global confidence_threshold
    global team_offset
    
    if(e.name == 'o'):
        if(team_offset == 0):
            print("Targetting terrorist side")
            team_offset = 3
        else: 
            print("Targetting counter-terrorist side")
            team_offset = 0

    if(e.name == '='): confidence_threshold+=0.0025;print(confidence_threshold)
    if(e.name == '-'): confidence_threshold-=0.0025;print(confidence_threshold)
    
    if(e.name == 'p'):
        pause = not pause
        if(pause): print("Paused")
        else: print("Unpaused")

keyboard.on_press(on_press)
pyautogui.FAILSAFE = False
print("Bot started")

while True:
    if(pause):
        time.sleep(20/1000) 
        continue
    
    img = sct.grab({
        "top":508,
        "left":928,
        "width":64,
        "height":64
    })

    image_rgb = np.frombuffer(img.rgb, dtype=np.uint8).reshape((64, 64, 3))
    image_rgb = image_rgb.astype(np.float32) / 255.0
    image_rgb = np.expand_dims(image_rgb, axis=0) # Shape (1, 64, 64, 3)

    out = prediction_signature(tf.constant(image_rgb))
    out = np.array(out["dense_1"])[0]

    if(out[team_offset] > confidence_threshold or out[team_offset + 1] > confidence_threshold):
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    
    time.sleep(0.005)


# Controls:
# "=" to increase confidence threshold
# "-" to decrease confidence threshold
# "o" to switch sides, "p" to pause