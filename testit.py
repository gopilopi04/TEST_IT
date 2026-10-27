import pygame
from random import *
window=pygame.display.set_mode((500,700))
questions=[["Что делает оператор if?", '1.Повторяет команду', '2.Проверяет условие', '3.Завершает программу', '4.Создаёт переменную', 2],
['Для чего нужна переменная в программировании?','1.Для хранения данных', '2.Для удаления программы', '3.Для выключения компьютера', '4.Для открытия браузер',1],
['Какой оператор используется для цикла c условием в Python?', '1.print', '2.if', '3.while', '4.input',3],
['Что делает команда print() в Python?', '1.Вводит данные' , '2.Выводит данные на экран', '3.Создаёт цикл', '4.Проверяет условие',2],
['Какой тип данных используется для хранения целых чисел в Python?', '1.str', '2.bool', '3.int', '4.list',3],
['Для чего используется оператор else?', '1.Для выполнения действий, если условие if не выполнено', '2.Для создания переменной', '3.Для вывода текста', 
 '4.Для повторения цикла',1],
['Какая команда позволяет пользователю ввести данные в Python?', '1.print', '2.input', '3.if', '4.while',2]]
shuffle(questions)
index = 0
i=0
def ask():
    if question.index < len(questions) - 1:  # есть ли куда переключаться
        question.index += 1
        question.set_text(questions[question.index][0],25,(30,40,0)) # установить вопрос questions[index] в карточки
        for i in range(4):
            answers[i].set_text(questions[question.index][i + 1],25,(30,40,0))
            answers[i].set_color((0, 186, 241))
    else:
        print('Вопросы всё')
    
pygame.init()
class Text_area():
    
    def __init__(self,x,y,weight,height,color):
        self.rect=pygame.Rect(x,y,weight,height)
        self.fill_color=color
    
    def set_text(self,txt,f_size,txt_color):
        self.text=txt
        self.font1=pygame.font.Font(None,f_size)
        if len(txt) > 40:
            self.image1=self.font1.render(txt[:35],True,txt_color)
            self.image2=self.font1.render(txt[35:],True,txt_color)
        else:
            self.image1=self.font1.render(txt,True,txt_color)
            self.image2=self.font1.render('',True,txt_color)
    def fill(self):
        pygame.draw.rect(window,self.fill_color,self.rect)
    
    def set_color(self,color2):
        self.fill_color=color2
    
    def draw(self):
        pygame.draw.rect(window,self.fill_color,self.rect)
        window.blit(self.image1,(self.rect.x+35,self.rect.y+30))
        window.blit(self.image2,(self.rect.x+35,self.rect.y+60))
    
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
game=True
SPACING = 10
HEIGHT = 100
WIDTH = 400
clock=pygame.time.Clock()
window.fill((0, 90, 46))
question=Text_area(50,50,WIDTH,HEIGHT,(0, 186, 241))
question.set_text('ВОПРОС',75,(30,40,0))
question.index=-1
answers = list()
y = question.rect.bottom + SPACING
for i in range(4):
    answer=Text_area(50,y + (100 + SPACING) *i,WIDTH,HEIGHT,(0, 186, 241))
    answer.set_text('?',75,(30,40,0))
    answers.append(answer)

while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type==pygame.KEYDOWN and pygame.K_q:
            ask()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and question.index >=0:
            x, y= event.pos
            for i in range (len(answers)):
                if answers[i].collidepoint(x, y):
                    num = questions[question.index][-1]
                    if i ==num-1:
                        answers[i].set_color((0, 255, 51))
                    else:
                        answers[i].set_color((255, 0, 0))
                    answers[i].fill()
    question.draw()
    for answer in answers:
        answer.draw()
    pygame.display.update()
    clock.tick(40)
