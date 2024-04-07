from cmu_graphics import *
import copy, string, itertools, random
import random, itertools, string, copy
import tkinter as tk

def quizGame(app):
    quizGameStart(app)
    drawQuizGame(app)
    quizGameMousePress(app)
    
def quizGameStart(app): 
    app.width=1000
    app.height=800
    app.score_game_3_round_1_b1_add=0
    app.score_game_3_round_2_b2_add=0
    app.score_game_3_round_3_b3_add=0
    app.score_game_3_round_4_b4_add=0
    app.score_game_3=dict()

def drawQuizGame(app):
    drawLabel('Are You My Soulmate',500,100,size=28,font='monospace',fill='pink')
    drawRect(250-100,300,200,100,fill='pink')
    drawRect(750-100,300,200,100,fill='pink')
    drawRect(250-100,500,200,100,fill='pink')
    drawRect(750-100,500,200,100,fill='pink')
    drawLabel(f'Test 1:{app.score_game_3_round_1_b1_add}',250,350,size=20,font='monospace')
    drawLabel(f'Test 2:{app.score_game_3_round_2_b2_add}',750,350,size=20,font='monospace')
    drawLabel(f'Test 3:{app.score_game_3_round_3_b3_add}',250,550,size=20,font='monospace')
    drawLabel(f'Test 4:{app.score_game_3_round_4_b4_add}',750,550,size=20,font='monospace')
    pass
    

def quizGameMousePress(app,mouseX,mouseY):
    
    if (350>=mouseX>=150) and (400>=mouseY>=300):
        root = tk.Tk()
        game1 = CodeTracing(root)
        root.mainloop()
        app.score_game_3_round_1_b1_add=game1.score
    elif (850>=mouseX>=650) and (400>=mouseY>=300):
        root = tk.Tk()
        game2 = MathGame(root)
        root.mainloop()
        app.score_game_3_round_2_b2_add=game2.score
    elif (350>=mouseX>=150) and (600>=mouseY>=500):
        root = tk.Tk()
        game3 = GeographyGame(root)
        root.mainloop()
        app.score_game_3_round_3_b3_add=game3.score
    elif (850>=mouseX>=650) and (600>=mouseY>=500):
        root = tk.Tk()
        game4 = SportsTriviaGame(root)
        root.mainloop()
        app.score_game_3_round_4_b4_add=game4.score

    


class CodeTracing:
    def __init__(self, master):
        self.master = master
        self.master.title("Code Tracing")
        self.master.geometry("1000x800")

        self.score = 0
        self.current_question = 0
        self.questions = [
            {"definition": "def ct(t):\n    L = [ ]\n    for x,y in t:\n        L.append(x+y)\n    return tuple(L) + t[1]\nt = ((3, -4), (-5, 5), (3, 1))\nprint(ct(t))",
             "options": ["(-1, 1, -2, -4, -5, 1)", "(-1, 1, -2, 1, 2, 1)", "(2, 1, -2, 1, 1, 1)", "(-1, 1, 1, 2, -5, 1)"],
             "answer": "(-1, 1, -2, -4, -5, 1)"},
            {"definition": "def ct(L):\n    M = [ (L[i-1], L[i]) for i in range(1, len(L)) ]\n    t = tuple(M)\n    t += ((min(L), max(L)),)\n    return t\nprint(ct([5, -3, 5, -1]))",
             "options": ["((5, -3), (5, -1), (-3, 5), (5, 5), (-3, -1), (5, -1))", "((5, 5), (-3, -1), (5, -1), (5, 5), (-3, 5), (5, -3))", "((5, -3), (-1, 5), (-3, 5), (5, 5), (5, -1), (5, -3))", "((-3, 5), (-3, -1), (5, -3), (5, 5), (5, -1), (5, -3))"],
             "answer": "((5, -3), (5, -1), (-3, 5), (5, 5), (-3, -1), (5, -1))"},
            {"definition": "def ct(L):\n    M = list(range(len(L)))\n    for i in range(1, len(M)):\n        L[i] += M[i]\n        M[-i] += M[i]\n    return M\nL = [0, 4, 5, 3]\nprint(ct(L))\nprint(L)",
             "options": ["[0, 4, 5, 3]\n[0, 4, 5, 3]", "[0, 3, 5, 6]\n[0, 3, 5, 6]", "[0, 3, 5, 6]\n[0, 4, 5, 3]", "[0, 4, 5, 3]\n[0, 3, 5, 6]"],
             "answer": "[0, 3, 5, 6]\n[0, 4, 5, 3]"},
            {"definition": "import copy\ndef ct(L):\n    A = copy.deepcopy(L)\n    B = [A[0], L[1]]\n    B[1][0] = 1\n    A[0].pop()\n    A = A[1] + A[0]\n    B[1] = sorted(B[0])\n    print(A)\n    print(B)\nL = [[2, 1, 4], [5, 3]]\nct(L)\nprint(L)",
             "options": ["[1, 5, 3, 2, 1, 4]\n[[2, 1, 4], [1, 3]]\n[[2, 1, 4], [5, 3]]", "[1, 5, 3, 2, 1, 4]\n[[2, 1, 4], [1, 3]]\n[[1, 3], [2, 1, 4]]", "[1, 5, 3, 2, 1, 4]\n[[2, 1, 4], [2, 1, 4]]\n[[2, 1, 4], [5, 3]]", "[1, 5, 3, 2, 1, 4]\n[[2, 1, 4], [2, 1, 4]]\n[[1, 3], [2, 1, 4]]"],
             "answer": "[1, 5, 3, 2, 1, 4]\n[[2, 1, 4], [1, 3]]\n[[2, 1, 4], [5, 3]]"},
            {"definition": "import copy\ndef ct(L):\n    a = L\n    b = copy.copy(L)\n    c = copy.deepcopy(L)\n    a[0] = b[1]\n    b[1][1] = c[0]\n    c[1].append(b[1])\n    a[0][0] += (b[1].pop())[0]\n    return (a,b,c)",
             "options": ["([1, 3], [2, [2, 1, 4]])", "([1, 3], [[2, 1, 4], [2, 1, 4]])", "([2, [2, 1, 4]], [[2, 1, 4], [2, 1, 4]])", "([[2, 1, 4], [2, 1, 4]], [[1, 3], [2, [2, 1, 4]])"],
             "answer": "([1, 3], [2, [2, 1, 4]])"}
        ]

        self.question_label = tk.Label(master, text="", font=("Arial", 14), wraplength=800, justify="left")
        self.question_label.pack(pady=(20, 200))

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", font=("Arial", 12), width=80, wraplength=800, justify="left", command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=10)
            self.option_buttons.append(button)

        self.update_question()

    def update_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["definition"])
            options = question_data["options"]
            random.shuffle(options)
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
        else:
            self.show_score()
            self.master.update()  # 立即更新窗口
            self.master.after(1000, self.master.destroy)  # 等待3秒后关闭窗口

    def check_answer(self, idx):
        if self.option_buttons[idx].cget("text") == self.questions[self.current_question]["answer"]:
            self.score += 1
            
        self.current_question += 1
        self.update_question()

    def show_score(self):
        self.question_label.config(text=f"你的得分是: {self.score}/5")
        
        for button in self.option_buttons:
            button.pack_forget()
class MathGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Math Game")
        self.master.geometry("1000x800")

        self.questions = {
            "1. 5×6+9÷3−2 = ?": ["23", "24", "25", "26"],
            "2. 7×4−8÷2+3 = ?": ["29", "30", "31", "32"],
            "3. 10×2+12÷3−5 = ?": ["25", "26", "27", "28"],
            "4. 8×5−10÷2+6 = ?": ["39", "40", "41", "42"],
            "5. 5^6-9÷3+2 = ?": ["15616", "15617", "15618", "15619"]
        }

        self.current_question = None
        self.answers = None
        self.correct_answer = None
        self.score = 0
        self.question_count = 0

        self.create_widgets()
        self.ask_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.question_label.pack(pady=20)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.master, text="", font=("Helvetica", 16), width=20, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.answer_buttons.append(button)

        self.score_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.score_label.pack(pady=20)

    def ask_question(self):
        if self.question_count < 5:
            self.current_question, self.answers = random.choice(list(self.questions.items()))
            self.correct_answer = self.answers[0]
            random.shuffle(self.answers)

            self.question_label.config(text=self.current_question)
            for i in range(4):
                self.answer_buttons[i].config(text=self.answers[i])
        else:
            self.show_score()
            self.master.update()  # 立即更新窗口
            self.master.after(1000, self.master.destroy)  # 等待3秒后关闭窗口

    def check_answer(self, index):
        selected_answer = self.answers[index]
        if selected_answer == self.correct_answer:
            self.score += 1
        self.question_count += 1
        self.ask_question()

    def show_score(self):
        self.question_label.config(text="Game Over")
        for button in self.answer_buttons:
            button.pack_forget()
        self.score_label.config(text=f"Your score: {self.score}/5")
        self.score_label.pack(pady=20) 
        
class GeographyGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Geography Game")
        self.master.geometry("1000x800")

        self.questions = {
            "What is the capital of France?": ["Paris", "London", "Berlin", "Madrid"],
            "What is the currency of Japan?": ["Yen", "Dollar", "Euro", "Pound"],
            "What is the chemical symbol for water?": ["H2O", "CO2", "NaCl", "O2"],
            "What is the capital of China?": ["Beijing", "Shanghai", "Guangzhou", "Hong Kong"],
            "What is the capital of India?": ["New Delhi", "Mumbai", "Kolkata", "Chennai"]
        }

        self.current_question = None
        self.answers = None
        self.correct_answer = None
        self.score = 0
        self.question_count = 0

        self.create_widgets()
        self.ask_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.question_label.pack(pady=20)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.master, text="", font=("Helvetica", 16), width=20, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.answer_buttons.append(button)

        self.score_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.score_label.pack(pady=20)


    def ask_question(self):
        if self.question_count < 5:
            self.current_question, self.answers = random.choice(list(self.questions.items()))
            self.correct_answer = self.answers[0]
            random.shuffle(self.answers)

            self.question_label.config(text=self.current_question)
            for i in range(4):
                self.answer_buttons[i].config(text=self.answers[i])
        else:
            self.show_score()
            self.master.update()  # 立即更新窗口
            self.master.after(1000, self.master.destroy)  # 等待3秒后关闭窗口

    def check_answer(self, index):
        selected_answer = self.answers[index]
        if selected_answer == self.correct_answer:
            self.score += 1
        self.question_count += 1
        self.ask_question()

    def show_score(self):
        self.question_label.config(text="Game Over")
        for button in self.answer_buttons:
            button.pack_forget()
        self.score_label.config(text=f"Your score: {self.score}/5")
        self.score_label.pack(pady=20)

class SportsTriviaGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Sports Trivia Game")
        self.master.geometry("1000x800")

        self.questions = {
            "Who is the winner of the 18th World Cup?": ["France", "Brazil", "Germany", "Italy"],
            "Which country's player is Crowe?": ["Portugal", "Argentina", "Brazil", "Spain"],
            "Who is called 'The Lord of the Rings' in basketball NBA?": ["Russell", "Jordan", "Bryant", "LeBron"],
            "Who was MLB's MVP in '21?": ["Ohtani Shohei", "Mike Trout", "Bryce Harper", "Jacob deGrom"],
            "Who won the champion of figure skating in 2014 and 2018 Olympics?": ["Hanyu Yuzuru", "Nathan Chen", "Yuna Kim", "Evgenia Medvedeva"]
        }

        self.current_question = None
        self.answers = None
        self.correct_answer = None
        self.score = 0
        self.question_count = 0

        self.create_widgets()
        self.ask_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.question_label.pack(pady=20)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.master, text="", font=("Helvetica", 16), width=20, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.answer_buttons.append(button)

        self.score_label = tk.Label(self.master, text="", font=("Helvetica", 20))
        self.score_label.pack(pady=20)

    def ask_question(self):
        if self.question_count < 5:
            self.current_question, self.answers = random.choice(list(self.questions.items()))
            self.correct_answer = self.answers[0]
            random.shuffle(self.answers)

            self.question_label.config(text=self.current_question)
            for i in range(4):
                self.answer_buttons[i].config(text=self.answers[i])
        else:
            self.show_score()
            self.master.update()  # 立即更新窗口
            self.master.after(1000, self.master.destroy)  # 等待3秒后关闭窗口

    def check_answer(self, index):
        selected_answer = self.answers[index]
        if selected_answer == self.correct_answer:
            self.score += 1
        self.question_count += 1
        self.ask_question()

    def show_score(self):
        self.question_label.config(text="Game Over")
        for button in self.answer_buttons:
            button.pack_forget()
        self.score_label.config(text=f"Your score: {self.score}/5")
        self.score_label.pack(pady=20)

def main():
    runApp()

main()


