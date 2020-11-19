import tkinter as tk
import numpy as np


# functions
expression = ""
tape_log = ""
after_equal = False


def numberpress(number):
    global expression, tape_log, after_equal
    if not after_equal:
        expression += str(number)
        tape_log += str(number)
    else:
        after_equal = False
        expression = str(number)
        tape_log += f"   {number}"
    readout.set(expression)
    tape.set(tape_log)


def operatorpress(operator):
    global expression, tape_log, after_equal
    if not after_equal:
        expression += str(operator)
        tape_log += str(operator)
    else:
        after_equal = False
        tape_log += f"   {expression}{operator}"
        expression = f"   {expression}{operator}"
    readout.set(expression)
    tape.set(tape_log)


def equalpress():
    try:
        global expression, tape_log, after_equal
        after_equal = True
        total = str(eval(expression))
        expression = total
        tape_log += f"={total}"
        readout.set(expression)
        tape.set(tape_log)
    except:
        readout.set("error")


def percentage():
    global expression, tape_log, after_equal
    if not after_equal:
        after_equal = True

        value = readout.get()
        flt_value = float(value)
        expression = str(flt_value/100)

        tape_log = tape_log.strip(value)
        tape_log += f"{value}/100={flt_value/100}"
    else:
        value = readout.get()
        flt_value = float(value)
        expression = str(flt_value/100)

        tape_log += f"   {value}/100={flt_value/100}"

    readout.set(expression)
    tape.set(tape_log)


def swap_sign():
    global expression, after_equal
    after_equal = True
    value = float(readout.get())
    expression = str(np.negative(value))
    readout.set(expression)


def square():
    global expression, after_equal
    after_equal = True
    value = float(readout.get())
    expression = str(np.power(value, 2))
    readout.set(expression)


def cube():
    global expression, after_equal
    after_equal = True
    value = float(readout.get())
    expression = str(np.power(value, 3))
    readout.set(expression)


def exponential():
    global expression, after_equal
    after_equal = True
    value = float(readout.get())
    expression = str(np.exp(value))
    readout.set(expression)


def power_of_ten():
    global expression, after_equal
    after_equal = True
    value = float(readout.get())
    expression = str(np.power(10, value))
    readout.set(expression)


def ln():
    global expression, after_equal
    after_equal = True
    value = float(readout.get())
    expression = str(np.log(value))
    readout.set(expression)


def log10():
    global expression, after_equal
    after_equal = True
    value = float(readout.get())
    expression = str(np.log10(value))
    readout.set(expression)


def clear():
    global expression, tape_log, after_equal
    after_equal = True
    expression = ""
    tape_log = ""

    readout.set(tape_log)
    tape.set(expression)


if __name__ == "__main__":
    window = tk.Tk()

    # window properties
    bg_color = "blue"
    window_color = "#252425"
    num_color = "blue"
    operator_color = "orange"

    window.title("Calculator")
    window.configure(bg=window_color)

    # configure window size
    window.rowconfigure(list(range(7)), minsize=50)
    window.columnconfigure(list(range(10)), minsize=50)

    # display
    readout = tk.StringVar()
    display_frame = tk.Frame(master=window, bg=window_color)
    display_frame.grid(row=0, column=0, rowspan=2,
                       columnspan=10, sticky="nsew")

    display = tk.Entry(master=display_frame, textvariable=readout, fg="white",
                       bg=window_color, relief="flat", font="Helvetica 37", justify="right")
    display.grid(row=1, column=0, ipadx=34)

    # ticker tape
    tape = tk.StringVar()
    display_tape = tk.Label(master=display_frame, textvariable=tape, fg="white",
                            bg=window_color, relief="flat", font="Helvetica 18 italic", justify="right", wraplength=500)
    display_tape.grid(row=0, column=0, sticky="e")

    # number keys
    zero = tk.Button(text="0", highlightthickness=0, font="Helvetica 20",
                     command=lambda: numberpress(0))
    one = tk.Button(text="1", highlightthickness=0, font="Helvetica 20",
                    command=lambda: numberpress(1))
    two = tk.Button(text="2", highlightthickness=0, font="Helvetica 20",
                    bg="black", command=lambda: numberpress(2))
    three = tk.Button(text="3", highlightthickness=0, font="Helvetica 20",
                      command=lambda: numberpress(3))
    four = tk.Button(text="4", highlightthickness=0, font="Helvetica 20",
                     command=lambda: numberpress(4))
    five = tk.Button(text="5", highlightthickness=0, font="Helvetica 20",
                     command=lambda: numberpress(5))
    six = tk.Button(text="6", highlightthickness=0, font="Helvetica 20",
                    command=lambda: numberpress(6))
    seven = tk.Button(text="7", highlightthickness=0, font="Helvetica 20",
                      command=lambda: numberpress(7))
    eight = tk.Button(text="8", highlightthickness=0, font="Helvetica 20",
                      command=lambda: numberpress(8))
    nine = tk.Button(text="9", highlightthickness=0, font="Helvetica 20",
                     command=lambda: numberpress(9))

    zero.grid(row=6, column=6, columnspan=2, padx=0.5, pady=0.5, sticky="nsew")
    one.grid(row=5, column=6, padx=0.5, pady=0.5, sticky="nsew")
    two.grid(row=5, column=7, padx=0.5, pady=0.5, sticky="nsew")
    three.grid(row=5, column=8, padx=0.5, pady=0.5, sticky="nsew")
    four.grid(row=4, column=6, padx=0.5, pady=0.5, sticky="nsew")
    five.grid(row=4, column=7, padx=0.5, pady=0.5, sticky="nsew")
    six.grid(row=4, column=8, padx=0.5, pady=0.5, sticky="nsew")
    seven.grid(row=3, column=6, padx=0.5, pady=0.5, sticky="nsew")
    eight.grid(row=3, column=7, padx=0.5, pady=0.5, sticky="nsew")
    nine.grid(row=3, column=8, padx=0.5, pady=0.5, sticky="nsew")

    # operators
    left_par = tk.Button(text="(", highlightthickness=0, font="Helvetica 20",
                         command=lambda: operatorpress('('))
    right_par = tk.Button(text=")", highlightthickness=0, font="Helvetica 20",
                          command=lambda: operatorpress(')'))
    decimal = tk.Button(text=".", highlightthickness=0, font="Helvetica 20",
                        command=lambda: operatorpress('.'))
    divide = tk.Button(text="÷", highlightthickness=0, font="Helvetica 20",
                       command=lambda: operatorpress("/"))
    multiply = tk.Button(text="x", highlightthickness=0, font="Helvetica 20",
                         command=lambda: operatorpress("*"))
    subtract = tk.Button(text="-", highlightthickness=0, font="Helvetica 20",
                         command=lambda: operatorpress("-"))
    add = tk.Button(text="+", highlightthickness=0, font="Helvetica 20",
                    command=lambda: operatorpress("+"))
    equals = tk.Button(text="=", highlightthickness=0, font="Helvetica 20",
                       command=lambda: equalpress())

    left_par.grid(row=2, column=4, padx=0.5, pady=0.5, sticky="nsew")
    right_par.grid(row=2, column=5, padx=0.5, pady=0.5, sticky="nsew")
    decimal.grid(row=6, column=8, padx=0.5, pady=0.5, sticky="nsew")
    divide.grid(row=2, column=9, padx=0.5, pady=0.5, sticky="nsew")
    multiply.grid(row=3, column=9, padx=0.5, pady=0.5, sticky="nsew")
    subtract.grid(row=4, column=9, padx=0.5, pady=0.5, sticky="nsew")
    add.grid(row=5, column=9, padx=0.5, pady=0.5, sticky="nsew")
    equals.grid(row=6, column=9, padx=0.5, pady=0.5, sticky="nsew")

    # function buttons
    all_clear = tk.Button(text="AC", highlightthickness=0, font="Helvetica 20",
                          command=lambda: clear())
    sign_change = tk.Button(text="+/-", highlightthickness=0, font="Helvetica 20",
                            command=lambda: swap_sign())
    to_percent = tk.Button(text="%", highlightthickness=0, font="Helvetica 20",
                           command=lambda: percentage())
    squared = tk.Button(text="x\u00B2", highlightthickness=0, font="Helvetica 20",
                        command=lambda: square())
    cubed = tk.Button(text="x\u00B3", highlightthickness=0, font="Helvetica 20",
                      command=lambda: cube())
    e_to_the = tk.Button(text="e\u207F", highlightthickness=0, font="Helvetica 20",
                         command=lambda: exponential())
    ten_to_the = tk.Button(text="10\u207F", highlightthickness=0, font="Helvetica 20",
                           command=lambda: power_of_ten())
    natural_log = tk.Button(text="ln", highlightthickness=0, font="Helvetica 20",
                            command=lambda: ln())
    log_10 = tk.Button(text="log", highlightthickness=0, font="Helvetica 20",
                       command=lambda: log10())

    all_clear.grid(row=2, column=6, padx=0.5, pady=0.5, sticky="nsew")
    sign_change.grid(row=2, column=7, padx=0.5, pady=0.5, sticky="nsew")
    to_percent.grid(row=2, column=8, padx=0.5, pady=0.5, sticky="nsew")
    squared.grid(row=3, column=1, padx=0.5, pady=0.5, sticky="nsew")
    cubed.grid(row=3, column=2, padx=0.5, pady=0.5, sticky="nsew")
    e_to_the.grid(row=3, column=4, padx=0.5, pady=0.5, sticky="nsew")
    ten_to_the.grid(row=3, column=5, padx=0.5, pady=0.5, sticky="nsew")
    natural_log.grid(row=4, column=4, padx=0.5, pady=0.5, sticky="nsew")
    log_10.grid(row=4, column=5, padx=0.5, pady=0.5, sticky="nsew")

    window.mainloop()
