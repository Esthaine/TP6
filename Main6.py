Température = 0
Nombres = 0

def on_button_pressed_a():
    global Température
    Température = input.temperature()
    if Température < 10:
        basic.show_string("Place the plant in a warmer environment")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Température
    Luminosité = 0
    Température = input.light_level()
    if Luminosité < 120:
        basic.show_string("Plants needs more light")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    if Nombres < 60:
        basic.show_string("Watering the plant")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_every_interval():
    global Nombres
    Nombres = randint(0, 100)
    basic.show_number(Nombres)
loops.every_interval(120000, on_every_interval)