from tkinter import *
from math import comb as choose

class OutsideRangeError(Exception):
    pass

class NError(Exception):
    pass

class UnsafeEvalError(Exception):
    pass

root = Tk()

root.geometry("648x400")
root.resizable(False, False)
root.configure(bg="#8D95EB")
root.title("Binomal Distribution Calculator")


def calculate():
    p_value = vetP()
    n_value = vetN()
    x_value = vetX(n_value)
    if None in (p_value,n_value,x_value):
        return
    q_value = 1 - p_value





def vetP():

    try:
        p = safeEval(p_field.get())
        if p == "invalid":
            raise UnsafeEvalError
        elif p == "":
            raise ValueError

        if p < 0 or p > 1:
            raise ValueError
    except UnsafeEvalError:
        p_error.configure(text="Invalid Expression!")
        return None
    except ValueError:
        p_error.configure(text="Must be a value between 0 and 1!")
        return None

    p_error.configure(text="")
    return p

def vetN():

    try:
        n = safeEval(n_field.get())
        if n == "invalid":
            raise UnsafeEvalError
        elif n == "":
            raise ValueError


        if n < 1 :
            raise OutsideRangeError
        elif n % 1 != 0:
            raise ValueError
    except UnsafeEvalError:
        n_error.configure(text="Invalid Expression!")
        return None
    except OutsideRangeError:
        n_error.configure(text="Must not be less than 1!")
        return None
    except ValueError:
        n_error.configure(text="Must be an integer value!")
        return None

    n_error.configure(text="")
    print("returning",n)
    return int(n)

def vetX(n):
    try:
        x = safeEval(x_field.get())
        if x == "invalid":
            raise UnsafeEvalError
        elif x == "":
            raise ValueError


        if x < 0:
            raise OutsideRangeError
        elif n != None and x > n:
            raise NError
        elif x % 1 != 0:
            raise ValueError
    except UnsafeEvalError:
        x_error.configure(text="Invalid Expression!")
        return None
    except NError:
        x_error.configure(text="Must not be greater than n value!")
        return None
    except OutsideRangeError:
        x_error.configure(text="Must not be less than 0!")
        return None
    except ValueError:
        x_error.configure(text="Must be an integer value!")
        return None

    x_error.configure(text="")
    return int(x)


def safeEval(input):
    new_input = ""
    if input == "":
        return input
    for i in input:
        if i not in "0123456789. */+-^()":
            return "invalid"
        elif i == "^":
            new_input += "**"
        else:
            new_input += i

    output = float(round(eval(new_input),26))
    print(output)
    try:
        return output
    except SyntaxError:
        return "invalid"

p_field = Entry(width=26, justify=CENTER, font=("Verdana", 12), relief=FLAT)
p_field.place(x=40, y=50)
p_text = Label(font=("Verdana", 10),text="Decimal probability of attempt succeeding(p)",bg="#8095EB", width=26, wraplength=150,justify=RIGHT)
p_text.place(x=172,y=29,anchor=CENTER)
p_error = Label(font=("Verdana", 10),bg="#8D95EB",fg="#852a16")
p_error.place(x=172,y=83,anchor=CENTER)

n_field = Entry(width=26, justify=CENTER, font=("Verdana", 12), relief=FLAT)
n_field.place(x=40, y=130)
n_text = Label(font=("Verdana", 10),text="Number of attempts(n)",bg="#8D95EB")
n_text.place(x=172,y=119,anchor=CENTER)
n_error = Label(font=("Verdana", 10),bg="#8D95EB",fg="#852a16")
n_error.place(x=172,y=163,anchor=CENTER)

x_field = Entry(width=26, justify=CENTER, font=("Verdana", 12), relief=FLAT)
x_field.place(x=40, y=210)
x_text = Label(font=("Verdana", 10),text="Number of successful attempts(x)",bg="#8D95EB")
x_text.place(x=172,y=199,anchor=CENTER)
x_error = Label(font=("Verdana", 10),bg="#8D95EB",fg="#852a16")
x_error.place(x=172,y=243,anchor=CENTER)

calc_button = Button(width=26, justify=CENTER, font=("Verdana", 12), text="Calculate", relief=FLAT, bg="#3E469E",
                     pady=0, fg="#12142e", activebackground="#3E469E", command = calculate)
calc_button.place(x=37, y=290)

exact_output = Label(width=26, justify=CENTER, font=("Verdana", 12), bg="#FFFFFF",pady=0)
exact_output.place(x=344,y=50)
exact_label = Label(font=("Verdana", 10),text="Chance of x successful attempts(X==x)",bg="#8D95EB")
exact_label.place(x=476,y=39,anchor=CENTER)

not_output = Label(width=26, justify=CENTER, font=("Verdana", 12), bg="#FFFFFF",pady=0)
not_output.place(x=344,y=130)
not_label = Label(font=("Verdana", 10),text="Chance of not getting\n x successful attempts(X!=x)",bg="#8D95EB")
not_label.place(x=476,y=109,anchor=CENTER)

gt_output = Label(width=26, justify=CENTER, font=("Verdana", 12), bg="#FFFFFF",pady=0)
gt_output.place(x=344,y=210)
gt_label = Label(font=("Verdana", 10),text="Chance of getting more than\n x successful attempts(X>x)",bg="#8D95EB")
gt_label.place(x=476,y=189,anchor=CENTER)

lt_output = Label(width=26, justify=CENTER, font=("Verdana", 12), bg="#FFFFFF",pady=0)
lt_output.place(x=344,y=290)
lt_label = Label(font=("Verdana", 10),text="Chance of getting less than\n x successful attempts(X<x)",bg="#8D95EB")
lt_label.place(x=476,y=269,anchor=CENTER)



root.mainloop()

