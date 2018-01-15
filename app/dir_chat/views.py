"""___"""
import logging
from flask import render_template, request, flash, session
from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime
import random
import datetime as dt
from . import controller as cont
from .model import chatbot as chatbot
from .model import human as human
from . import chat

logger = logging.getLogger(__name__)

conversation_list = []

# conversation_list.append("chatbot: Hi, I am your chatbot")
# conversation_list.append("chatbot: Please talk to the chatbot..")
start_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
initial_tup = ("......","Hi, I am your chatbot, please say hi",start_time)
conversation_list.append(initial_tup)
count_loop = 0

username_ = " "

def get_chat_time():
     chat_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     return chat_time


def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
        
    return update_wrapper(no_cache, view)


@chat.route('/chat',methods = ['POST', 'GET'])
# @nocache
def result():
    reward = cont.get_response_reward()
    progress = cont.get_progress()
    global count_loop
    robot_data = ""
    global conversation_list
    tmp_list = []
    chat_counter = len(conversation_list)
    chat_time = get_chat_time()
    logger.debug("chat route")
    if request.method == 'POST':
        if request.form["action"] == "Chat":
            count_loop += 1 # for debug
            # user input
            tmp_user_data = request.form["chat_text"]
            user_data = str(tmp_user_data)
            # robot input based on user input
            tmp_state = cont.get_state()
            tmp_li = cont.conversation(user_data, tmp_state)
           
            logger.debug("check list")
            logger.debug(str(tmp_li))
            robot_data = tmp_li[0]
            tmp_state = tmp_li[1]
            # instances
            #if we nned the state for logging
            human_current = human.Human(user_data + " : (state:" + tmp_state + ")")
            #state is gone, just input
            # human_current = human.Human(user_data)
            chatbot_current = chatbot.ChatBot(robot_data)
            # tuple of current conversation
            conversation_tup = (human_current.statment, chatbot_current.statment, get_chat_time())
            # insert at the beginning of the list, to render that first
            conversation_list.insert(0, conversation_tup)
            # debug
            logger.debug(user_data)
            logger.debug("obj " + str(chatbot_current.statment))
            logger.debug(cont.get_state())
        
       
            
            logger.debug(conversation_list)
        elif request.form["action"] == "Clear":
            conversation_list = []
            start_fresh_tup = ("","Ok, we start again, I am your chatbot. Learning, learning. Please say Hi.",)
            conversation_list.append(start_fresh_tup)
            cont.set_state("start")
            cont.set_progress(5)
            cont.clear_response_reward()
            # global username_
            # session.pop("username", None)
        else:
            pass


        # conversation_list.reverse()
    else:
        # conversation_list.reverse()
        #is GET
        
        return render_template("chat/chat.html", conversation_list = conversation_list, chat_time = chat_time, progress = progress, reward = reward  )
    return render_template("chat/chat.html", conversation_list = conversation_list, chat_time = chat_time, progress = progress, reward = reward)
