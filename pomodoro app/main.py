import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# PINK="#DA498D"
# RED="#8E1616"
#DARKGREEN="#3E7B27"
DARKGREEN="#638C6D"
PURPLE="#441752"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps=0
marks=""
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global marks
    global reps
    #print("Reset pressed!")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    heading=tkinter.Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
    heading.grid(column=1,row=0)
    marks=""
    reps=0
    check_mark=tkinter.Label(text=marks,fg=PURPLE,bg=YELLOW)
    check_mark.grid(column=1,row=3)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    WORK_SEC=WORK_MIN*60
    SHORT_BREAK_SEC=SHORT_BREAK_MIN*60
    LONG_BREAK_SEC=LONG_BREAK_MIN*60

    reps+=1

    rem=reps%8
    if (rem==1 or rem==3 or rem==5 or rem==7):
        heading=tkinter.Label(text=" WORK ",font=(FONT_NAME,50,"bold"),fg=DARKGREEN,bg=YELLOW,highlightthickness=0)#WORK in deep green
        heading.grid(column=1,row=0)
        count_down(WORK_SEC)
    elif rem==0:
        heading=tkinter.Label(text=" BREAK ",font=(FONT_NAME,50,"bold"),fg=RED,bg=YELLOW,highlightthickness=0)#LONG BREAK in deep read
        heading.grid(column=1,row=0)
        count_down(LONG_BREAK_SEC)
    elif  (rem==2 or rem==4 or rem==6):
        heading=tkinter.Label(text=" BREAK ",font=(FONT_NAME,50,"bold"),fg=PINK,bg=YELLOW,highlightthickness=0)#SHORT BREAK in pink
        heading.grid(column=1,row=0)
        count_down(SHORT_BREAK_SEC)
    



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def start_pressed():
    print("Start pressed!")



def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    #elif count_sec
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
        #print(count)
    else:
        global marks
        start_timer()
        marks=""
        work_session=math.floor(reps/2)
        for i in range(work_session):
            marks+="✔️"
        check_mark=tkinter.Label(text=marks,fg=PURPLE,bg=YELLOW)
        check_mark.grid(column=1,row=3)
# ---------------------------- UI SETUP ------------------------------- #



def do_something(thing):
    # canvas.create_text(115,130,text=f"{c}",fill="white",font=(FONT_NAME,35,"bold"))
    # c-=1
    # canvas.grid(column=1,row=1)
    print(thing)



global c
c=10
window=tkinter.Tk()
window.title("Pomodoro Timer")
#window.config(padx=100,pady=50)
window.config(padx=50,pady=50,bg=YELLOW)

#count_down(5)

######    The Heading
heading=tkinter.Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
heading.grid(column=1,row=0)


#######  Creating buttons
start_button=tkinter.Button(text="Start",command=start_timer,highlightthickness=0)
start_button.grid(column=0,row=3)



reset_button=tkinter.Button(text="Reset",command=reset_timer,highlightthickness=0)
reset_button.grid(column=2,row=3)



# check_mark=tkinter.Label(text="✔️",fg=GREEN,bg=YELLOW)
# check_mark.grid(column=1,row=3)



canvas=tkinter.Canvas(height=240,width=230,bg=YELLOW,highlightthickness=0)
tomato_img=tkinter.PhotoImage(file="day#28(The Pomodoro Timer App)\\tomato.png")
canvas.create_image(115,115,image=tomato_img)
timer_text=canvas.create_text(115,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

# count_down(5)

window.mainloop()