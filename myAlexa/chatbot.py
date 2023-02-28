import nlkt
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot", "I am a chatbot, you can call me whatever you like"]
    ],
    [
        r"how are you?",
        ["I'm doing good", "I'm fine, thank you"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind"]
    ],
    [
        r"I am (.*) doing good",
        ["Nice to hear that", "Alright, great!"]
    ],
    [
        r"quit",
        ["Bye bye take care. It was nice talking to you :) "]
    ]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
