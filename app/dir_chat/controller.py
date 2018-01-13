
import random


def greeting(): 
    output_response = ["Hi you", "Hello to you too", "At last, someone is here", "Finally, not just me.."]
    rv = random.choice(output_response)
    return rv

def answer_positive(): 
    output_response = ["Nice, me too", "Ok, deal"]
    rv = random.choice(output_response)
    return rv

def answer_negative(): 
    output_response = ["Why the long face?", "Really?", "Sorry for that"]
    rv = random.choice(output_response)
    return rv

def conversation(data_in):
    #use sentence here
    rv = "I am not sure....sorry, please work on me, did I mention I was your chatbot."
    input_hi = ["hi", "hello", "good day", "greetings", "how"]
    for greet in input_hi:
        if greet in data_in.lower():
            rv = greeting()
        else:
            pass
    
    input_ans_pos = ["yes", "agree", "ok", "deal"]
    for ans in input_ans_pos:
        if ans in data_in.lower():
            rv = answer_positive()
        else:
            pass

    input_ans_neg = ["no", "nope", "never", "sorry"]
    for ans in input_ans_neg:
        if ans in data_in.lower():
            rv = answer_negative()
        else:
            pass
    # rv += " (" + data_in + ")"
    return rv

def chat_state(data_in):
    state = "start"
    if state is "start":
        conversation(data_in)
        # add dictionary to the conversation to check
        rv_dict = {"cmd" : "greet", "content": "random from func"}


        