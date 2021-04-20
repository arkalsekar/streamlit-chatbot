import streamlit as st 
from nltk.chat.util import Chat, reflections
from pyjokes import get_joke


pairs = [
    
         ['my name is (.*)', ['Hi! Hello %1 Sir. I am JARVIS. How may i Help You?']],
         ['hi', ['Hi Hello I am your JARVIS. How can I Help you?????']],
         ['What can you Do', ['Yes Sir, I can Do many Tasks.']],
        #  ['open (.*)', ['Sorry Sir, I cant open %1 .I am still a Chatbot. I cant automate things.', webbrowser.open('%1')]],
         ['do you think there is a creator', ['Yes, According to me there is creator of all this because even I have been created by Abdul Rehman']],
         ['about you', ['I am a ChatBot created by Prof Abdul Rehman']],
         ['Who am i', ['please try typing "my name is --"']],
         ['(Tell me a joke|Joke|joke|tell me jokes)', ['Hehe Do you know its Saturday Today, Elephant has two Teeths, We humans have Four legs']],
         ['Abd JOke', [get_joke(language='en', category='neutral') ]],
         ['Who created you?', ['Abdul Rehman has created me.']],
            
]


st.title("Rule based Chatbot")
st.subheader("This is a Rule based Chatbot made using NlTK and Python by Abdul Rehman ")


def main():
    st.write("Initialize the Chat bot By Typing Hi ")
    ref = st.text_input("Start your chat here")

    # a = st.text_input("Initialize your Conversation By Typing Hi")
    # chat.converse()
    chat = Chat(pairs, reflections)
    respo = chat.respond(ref)
    st.write(respo)

if __name__=="__main__":
    main()
