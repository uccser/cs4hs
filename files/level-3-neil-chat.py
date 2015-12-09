"""
Python Chatbot based on javascript from:
        https://computationalthinkingcourse.withgoogle.com/unit?lesson=17&unit=7
"""
def main():
    print("Hello")
    chat()
    print("TTFN")
    
def chat():
    question = input().lower()
    while not("bye!" in  question):
        if 'who' in question:
            print('My name is StupidBot.')
        elif 'when' in question:
            print('I was born in 2015.')
        elif 'you are' in question:
            ans = "Why do you say I am {}?".format(question.split('you are')[-1])
            print(ans)
        else:
            print("I don't understand. Ask me another question.")
        question = input().lower()
