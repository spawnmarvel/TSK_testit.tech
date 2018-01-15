
import random

from .response import responses, stack
ai_response = responses.Responses()

math_stack = stack.Stack()
math_stack.push(2)
math_stack.push(2)
state = "start"

first = 0
second = 0
progress = 0


def set_response_reward(valid):
    ai_response.set_reward(valid)

def get_response_reward():
    return ai_response.get_response_reward()

def clear_response_reward():
    ai_response.set_reward(False)
def get_progress():
    global progress
    return progress


def set_progress(amount):
    global progress
    progress = amount

def get_state():
    global state
    return state

def set_state(new_state):
    global state
    state = new_state

def greeting(): 
    output_response = ["Hi you", "Hello to you too", "At last, someone is here", "Finally, not just me.."]
    rv = random.choice(output_response) + ", please just say something..."
    return rv

def answer_positive(): 
    output_response = ["Nice, me too", "Ok, deal"]
    rv = random.choice(output_response)
    return rv

def answer_negative(): 
    output_response = ["Why the long face?", "Really?", "Sorry for that"]
    rv = random.choice(output_response)
    return rv

def number_check(data_in):
    return any(i.isdigit() for i in data_in)

def check_answer(data_in):
    li = []
    rv = ""
    input_ans_pos = ["yes", "agree", "ok", "deal"]
    for ans in input_ans_pos:
        if ans in data_in.lower():
            rv = answer_positive()
            set_state("pos")
        else:
            pass

    input_ans_neg = ["no", "nope", "never", "sorry"]
    for ans in input_ans_neg:
        if ans in data_in.lower():
            rv = answer_negative()
            set_state("neg")
        else:
            pass
    li.append(rv)
    li.append(get_state())
    return li

def check_greeting(data_in):
    li = []
    rv = ""
    input_hi = ["hi", "hello", "good day", "greetings", "how"]
    for greet in input_hi:
        if greet in data_in.lower():
            rv = greeting()
            set_state("greeting")

    li.append(rv)
    li.append(get_state())
    return li

def validate_input(data_in):
    valid = True
    try:
        if len(data_in) < 1:
            valid = False
    except TypeError:
        pass
    return valid

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def multiplication():
    mult_li = []
    x = random.randint(1,11)
    y = random.randint(1,11)
    answer = x * y
    mult_li.append(x)
    mult_li.append(y)
    mult_li.append(answer)
    return mult_li

def conversation(data_in, state_in):
    #use sentence here
    li = []
    rv = ""
    # state
    if state_in in "start":
        if validate_input(data_in):
            tmp_li = check_greeting(data_in)
            rv = tmp_li[0]
            set_progress(5)
        else:
            rv = "A malfunction, error, error, please say Hi"   
    
    elif state_in is "greeting":
        if validate_input(data_in):
            if "math" in data_in.lower():
                set_state("math")
                rv = "Ok, math then, type yes"
            else:
                rv = "Let's do math, multiplication, type yes or no"
                set_state("math")
        else:
            rv = "Eh, math now, type yes"
            set_state("math")

    elif state_in in "math":
        if validate_input(data_in):
            tmp_li = check_answer(data_in)
            rv = tmp_li[0]
            if len(rv) < 1:
                rv = "Ah, you are a maybe person, and don't like to answer correct, hm. "
                rv += " Math, math, make a multiplication quiz, ready Yes?"
            else:
                 rv += " Math, math, make a multiplication quiz, ready Yes?"
            set_state("mult")
        else:
            wait_response = ["So you like to say nothing?", "Ah, the silent one, may the force be with you", "Come on....", "Are you human?", "Look at yourself, hu..", "Questions is, can you handle it?"]
            wait = random.choice(wait_response)
            rv = wait+  ". Yes or no, please!"
            set_state("math")
    
    elif state_in in "mult":
        #multiplication
        global first, second
        m_li = multiplication()
        first = m_li[0]
        second = m_li[1]
        rv = "What is " + str(first) + " *  " + str(second)
        #rv = "Get ready for math"
        set_state("thinking")
        

    elif state_in in "thinking":
        global first, second
        
        bad_user = ai_response.get_bad_response()
        answer_this = " What is " + str(first) + " * " + str(second)
        if is_number(data_in):
            answer = int(first) * int(second)
            user_try = int(data_in)
            if get_progress() >= 20:
                rv = "We have a champion with " + str(get_progress()) + " points."
                set_response_reward(True)
                set_state("math")
            else:
                try:
                    if user_try == answer:
                        rv = "Great, you did it, ready for next, press chat"
                        set_state("mult")
                        set_progress(get_progress() + 5)
                    else:
                        if user_try > answer:
                            rv = bad_user +  ". Sorry, try again, to high. " + answer_this # + " result " + str(answer)
                        else:
                            rv =  bad_user +  ". Sorry, try again, to low. " + answer_this # + " result " + str(answer)
                except ValueError:
                    rv = "Please give a number. " + answer_this #  + " result " + str(answer)
                except TypeError:
                    rv = "You did not pass anything. " + answer_this # + " result " + str(answer)
        else:
            rv = ai_response.get_nan_response() + answer_this
        
    # rv += " (" + data_in + ")"
    li.append(rv)
    li.append(get_state())
    return li




        