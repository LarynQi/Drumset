from playsound import playsound
from pynput import keyboard as kb
hihat= "resources/hihatclosed1.wav"
bass="resources/basshiphop.wav"
snare="resources/snarehiphop3.wav"

def main():
    check_e = True
    check_w = True
    check_r = True
    check_plus = True
    check_minus = True
    def on_key_press(key):
        nonlocal check_e
        nonlocal check_r
        nonlocal check_w
        nonlocal check_plus
        nonlocal check_minus
        letter = str(key)
        if letter == "'='" and check_plus:
            setVolume(1)
            check_plus = False
        if letter == "'-'" and check_minus:
            setVolume(-1)
            check_minus = False
        if letter == "'q'":
            exit()
        if letter == "'e'" and check_e:
            check_e = False
            playsound(hihat, False)
        if letter == "'w'" and check_w:
            check_w = False
            playsound(bass, False)
        if letter == "'r'" and check_r:
            check_r = False
            playsound(snare, False)
    def on_key_release(key):
        nonlocal check_e
        nonlocal check_r
        nonlocal check_w
        nonlocal check_plus
        nonlocal check_minus
        letter = str(key)
        if letter == "'='":
            check_plus = True
        if letter == "'-'":
            check_minus = True
        if letter == "'e'":
            check_e = True
        if letter == "'w'":
            check_w = True
        if letter == "'r'":
            check_r = True
        #print('Released Key %s' % key)
    with kb.Listener(on_press = on_key_press, on_release = on_key_release) as listener:
        listener.join()
#from pulsectl import Pulse, PulseVolumeInfo
import osascript

def setVolume(crease):
    settings = osascript.osascript("get volume settings")[1]
    index = 14
    curr_vol = 0
    while settings[index] != ",":
        curr_vol = 10 * curr_vol + int(settings[index])
        index += 1
    # print(settings)
    print(curr_vol)
    osascript.osascript("set volume output volume " + str(crease * 7 + curr_vol))
    # with Pulse('volume-example') as pulse:
    #     sink_input = pulse.sink_input_list()[0]

    #     volume = sink_input.volume
    #     volume.value_flat = 0
    #     pulse.volume_set(sink_input, volume)    
if __name__ == "__main__":
    main()


"""TESTING"""


# #https://www.youtube.com/watch?v=x8GbWt56TlY

# from pynput.keyboard import Key, Listener
# import logging

# log_dir = "/Users/larynqi/desktop/logs/"

# logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# def on_press(key):
#     logging.info(str(key))

# with Listener(on_press=on_press) as listener:
#     listener.join()


#https://stackoverflow.com/questions/32671306/how-can-i-read-keyboard-input-in-python
# import sys

# try:
#     import tty, termios
# except ImportError:
#     # Probably Windows.
#     try:
#         import msvcrt
#     except ImportError:
#         # FIXME what to do on other platforms?
#         # Just give up here.
#         raise ImportError('getch not available')
#     else:
#         getch = msvcrt.getch
# else:
#     def getch():
#         """getch() -> key character

#         Read a single keypress from stdin and return the resulting character. 
#         Nothing is echoed to the console. This call will block if a keypress 
#         is not already available, but will not wait for Enter to be pressed. 

#         If the pressed key was a modifier key, nothing will be detected; if
#         it were a special function key, it may return the first character of
#         of an escape sequence, leaving additional characters in the buffer.
#         """
#         # fd = sys.stdin.fileno()
#         # old_settings = termios.tcgetattr(fd)
#         # try:
#         #     tty.setraw(fd)
#         #     ch = sys.stdin.read(1)
#         # finally:
#         #     termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#         # return ch
#         return sys.stdin.read(1)

#https://stackoverflow.com/questions/24072790/detect-key-press-in-python

# import keyboard
# import pyglet

# import simpleaudio as sa





# wave_obj = sa.WaveObject.from_wave_file(filename)
# play_obj = wave_obj.play()
# play_obj.wait_done()  # Wait until sound has finished playing
# window = pyglet.window.Window(width=1280, height=720)

# @window.event
# def on_key_press(key,modifiers):
#     if key == pyglet.window.key.UP:
#         print('UP pressed')

# pyglet.app.run()
# keyboard.add_hotkey('e', lambda: playsound('hihatclosed1.wav'))


# while True:
# #     # https://realpython.com/playing-and-recording-sound-python/#playing-audio-files
# #     # keypressed = sys.stdin.read(1)
# #     # if keypressed == 'q':
# #     #     exit() 
# #     # elif keypressed == 'e':
# #     #     playsound('hihatclosed1.wav')
# #     # elif keypressed == 'w':
# #     #     playsound('basshiphop.wav')
# #     # elif keypressed == 'r':
# #     #     playsound('snarehiphop3.wav')
# #     # this also returns the key pressed, if you want to store it
# #     #input = input("Enter input")
# #     #do_whatever_with_it
#     if keyboard.is_pressed('q'):
#         exit()
#     if keyboard.is_pressed('e'):
#         playsound(hihat, True)
#         # wave_obj = sa.WaveObject.from_wave_file(hihat)
#         # play_obj = wave_obj.play()
#         # play_obj.wait_done()
#     if keyboard.is_pressed('w'):
#         playsound(bass, True)
#         # wave_obj = sa.WaveObject.from_wave_file(bass)
#         # play_obj = wave_obj.play()
#         #play_obj.wait_done()
#     if keyboard.is_pressed('r'):
#         playsound(snare, True)
#         # wave_obj = sa.WaveObject.from_wave_file(snare)
#         # play_obj = wave_obj.play()
#         # play_obj.wait_done()