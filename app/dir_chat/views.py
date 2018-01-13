"""___"""
import logging
from flask import render_template, request, flash
import random
import datetime as dt
from . import controller as cont
from . import chat

logger = logging.getLogger(__name__)

conversation_list = []

# conversation_list.append("chatbot: Hi, I am your chatbot")
# conversation_list.append("chatbot: Please talk to the chatbot..")
start_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
initial_tup = ("","chatbot: Hi, I am your chatbot",start_time)
conversation_list.append(initial_tup)
count_loop = 0

def get_chat_time():
     chat_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     return chat_time

@chat.route('/chat',methods = ['POST', 'GET'])
def result():
    
    global count_loop
    robot_data = ""
    global conversation_list
    tmp_list = []
    chat_counter = len(conversation_list)
    user_data = ""
    chat_time = get_chat_time()
    logger.debug("chat route")
    if request.method == 'POST':
        if request.form["action"] == "Chat":
            count_loop += 1
            tmp_res = request.form["chat_text"]
        
            robot_data = cont.conversation(tmp_res)
            logger.debug(tmp_res)
            user_data = tmp_res
            # conversation_list.append("user: " +user_data)
            # conversation_list.append("chatbot: " + robot_data)
            tmp_user = user_data #  + ". loop " + str(count_loop)
            tmp_robot = robot_data #  + ". loop " + str(count_loop)
            conversation_tup = (tmp_user, tmp_robot, get_chat_time())
            conversation_list.insert(0, conversation_tup)
        
       
            
            logger.debug(conversation_list)
        elif request.form["action"] == "Clear":
            conversation_list.clear()
            start_fresh_tup = ("","Ok, we start again, I am your chatbot. Learning, learning....",)
            conversation_list.append(start_fresh_tup)
        else:
            pass


        # conversation_list.reverse()
    else:
        # conversation_list.reverse()
        #is GET
        return render_template("chat/chat.html", conversation_list = conversation_list, chat_time = chat_time)
    return render_template("chat/chat.html", conversation_list = conversation_list, chat_time = chat_time)
