from tkinter import *
from tkinter import messagebox
import random
import pandas as pd

# 전역 변수로 단어와 의미를 저장할 딕셔너리 선언
word_dict = {}

def main():
    # 메인 윈도우 생성
    window = Tk()
    window.title("단어장 프로그램")
    window.geometry("300x200")
    window.resizable(width=False, height=False)

    # 메인 화면 이미지 
    photo = PhotoImage(file ="image/main.gif")
    resized_photo = photo.subsample(2) # 사이즈 조정
    howto_label = Label(window, image = resized_photo)
    howto_label.pack()

    # 단어 외우기 메뉴 버튼
    word_button = Button(window, text="1. 단어 외우기", command=show_word_menu)
    word_button.pack()

    # 테스트 메뉴 버튼
    test_button = Button(window, text="2. 테스트", command=show_test_menu)
    test_button.pack()

    # 메인 루프 실행
    window.mainloop()


def show_word_menu():
    # 단어 외우기 메뉴 선택 시 호출
    # 윈도우 생성
    word_window = Tk()
    word_window.title("단어 외우기")
    word_window.geometry("300x500") 
    word_window.resizable(width=False, height=False)

    # 단어 목록 표시
    word_list_label = Label(word_window, text="단어 목록")
    word_list_label.pack()

    # 단어와 의미를 표시할 리스트 박스
    word_listbox = Listbox(word_window)
    word_listbox.pack()


    # 단어 딕셔너리의 키와 값을 리스트 박스에 추가
    for word, meaning in word_dict.items():
        item = f"{word} - {meaning}"
        word_listbox.insert(END, item)

    def delete_word():
        # 단어 삭제 버튼 선택 시 호출
        selected_word = word_entry.get()
        if selected_word in word_dict:
            del word_dict[selected_word]
            word_listbox.delete(0, END)
            meaning_entry.delete(0, END)
            for word, meaning in word_dict.items():
                item = f"{word} - {meaning}"
                word_listbox.insert(END, item) 
            word_entry.delete(0, END)
            messagebox.showinfo("안내", "단어가 삭제되었습니다.")
        else:
            messagebox.showinfo("안내", "존재하는 단어를 입력해주세요.")

    # 단어 삭제 버튼
    delete_button = Button(word_window, text="삭제", command=delete_word)
    delete_button.place(x=110, y= 300)


    
    
    def delete_all_words():
        # 전체 단어 삭제 버튼 선택시 호출
        word_dict.clear()
        word_listbox.delete(0, END)
        messagebox.showinfo("안내", "전체 단어가 삭제되었습니다.")
        word_entry.delete(0, END)
        meaning_entry.delete(0, END)

    delete_all_button = Button(word_window, text="전체 삭제", command=delete_all_words)
    delete_all_button.place(x=120, y=330)

    # 단어 입력 창
    word_entry_label = Label(word_window, text="단어:")
    word_entry_label.pack()
    word_entry = Entry(word_window)
    word_entry.pack()

    # 단어 뜻 입력 창
    meaning_entry_label = Label(word_window, text="단어 뜻:")
    meaning_entry_label.pack()
    meaning_entry = Entry(word_window)
    meaning_entry.pack()

    def add_word():
        # 단어 추가 버튼 클릭 시 호출되는 함수
        word = word_entry.get()
        meaning = meaning_entry.get()
        if word and meaning:
            word_dict[word] = meaning
            item = f"{word} - {meaning}"
            word_listbox.insert(END, item)

            word_entry.delete(0, END)
            meaning_entry.delete(0, END)
        else:
            messagebox.showinfo("안내", "단어와 뜻을 모두 입력해주세요.")

    # 단어 추가 버튼
    add_button = Button(word_window, text="추가", command=add_word)
    add_button.place(x=150, y=300)

    # 파일 불러오기 버튼
    def load_file():
        try:
            df = pd.read_excel("단어장.xlsx")
            for index, row in df.iterrows():
                word = row["단어"]
                meaning = row["뜻"]
                if word and meaning:
                    word_dict[word] = meaning
                    item = f"{word} - {meaning}"
                    word_listbox.insert(END, item)
            messagebox.showinfo("안내", "파일을 성공적으로 불러왔습니다.")
        except Exception:
            messagebox.showinfo("오류","파일을 불러오던 중 오류가 발생했습니다.")


    # 파일 불러오기 버튼
    load_button = Button(word_window, text="파일로 단어 불러오기", command=load_file)
    load_button.place(x=85, y=380)

    # 파일로 불러오는 법 버튼
    def open_instructions():
        image_window = Toplevel()
        image_window.title("파일로 불러오는 법")

        photo = PhotoImage(file ="image/Howto.gif")

        howto_label = Label(image_window, image = photo)
        howto_label.pack()

        image_window.mainloop()

    instructions_button = Button(word_window, text="파일로 불러오는 법", command=open_instructions)
    instructions_button.place(x=90, y=410)
    


    word_window.mainloop()
#***************************************************************************
#***************************************************************************



#테스트 버튼 선택 시 호출되는 함수
def show_test_menu():
    #테스트 윈도우
    test_window = Tk()
    test_window.title("테스트")
    test_window.geometry("300x350")
    test_window.resizable(width=False, height=False)

    #최대로 입력할 수 있는 문제 수 표시
    question_num_label = Label(test_window, text="{} 이하로 입력하세요.\n문제수:".format(len(word_dict)))
    question_num_label.pack() 
    #문제수 입력창
    question_num = Entry(test_window)
    question_num.pack()
    
    


    
    #뜻->단어 테스트 함수(korean to english)
    def kte_test():
        #question_num에서 입력받은 숫자 할당
        kr_question_num = int(question_num.get())

        #뜻->단어 테스트 윈도우
        kte_test_window = Tk()
        kte_test_window.title("뜻 보고 단어 맞추기")
        kte_test_window.geometry("300x350")
        #kte_test_window.resizable(width=False, height=False)

        #워드 딕셔너리의 밸류값을 리스트로 할당
        kr_values = list(word_dict.values())

        #밸류값 범위에서 입력받은 문제 수 만큼 랜덤으로 리스트에 할당
        kr_question_list = random.sample(kr_values, kr_question_num)



        #밸류값으로 키값을 구할 수 없음
        #딕셔너리의 키값과 밸류값을 바꾼 새 딕셔너리 만듦
        reverse_word_dict = dict(map(reversed, word_dict.items()))

        #답지에 해당하는 랜덤 밸류값의 리스트
        kr_values_list = []

        #뜻랜덤문제(키값)에 해당하는 밸류값을 얻어 밸류값 리스트에 추가
        for i in kr_question_list:
            kr_values = reverse_word_dict[i]
            kr_values_list.append(kr_values)



        #문제의 답을 입력받을 리스트 생성
        kte_answer_list = []

        #랜덤문제리스트에서 문제와 입력받을 창 출력
        for v in kr_question_list:
            kte_test_label = Label(kte_test_window, text=v)
            kte_test_label.pack()
            kte_test_answer = Entry(kte_test_window)
            kte_test_answer.pack()

            #엔트리 창에 입력된 답을 리스트에 추가
            #예시: 첫번째 문제의 엔트리 창에 입력될 답은 리스트의 첫번째로 넣는 것
            kte_answer_list.append(kte_test_answer)


        #완료 버튼
        #kte_answer_list를 매개변수로 kte_test_check에 넘겨줌
        kr_finish_button = Button(kte_test_window, text="완료", command=lambda: kte_test_check(kte_answer_list))
        kr_finish_button.pack()


        #정답을 확인하는 함수
        def kte_test_check(entry_answer):
            #입력받은 답을 answer_list에 최종적으로 할당
            answer_list = []
            for entry in entry_answer:
                answer = entry.get()
                answer_list.append(answer)

            #맞춘 정답 수를 할당할 변수
            correct_answer = 0

            #입력받은 값과 정답을 비교함
            for i in range(kr_question_num):
                if kr_values_list[i] == answer_list[i]:
                    correct_answer += 1

            
            #정답 결과를 알려줌
            messagebox.showinfo("결과", "{} 문제 중 {} 문제 맞췄습니다!".format(kr_question_num, correct_answer))




    #단어->뜻 테스트 함수(english to korean)
    def etk_test():
        #question_num에서 입력받은 숫자 할당
        en_question_num = int(question_num.get())
        
        #단어->뜻 테스트 윈도우
        etk_test_window = Tk()
        etk_test_window.title("단어 보고 뜻 맞추기")
        etk_test_window.geometry("300x350")
        #etk_test_window.resizable(width=False, height=False)

        #워드 딕셔너리의 키값을 리스트로 할당
        en_keys = list(word_dict.keys())

        #키값 범위에서 입력받은 문제 수 만큼 랜덤으로 리스트에 할당
        en_question_list = random.sample(en_keys, en_question_num)


        #답지에 해당하는 랜덤 밸류값의 리스트
        en_values_list = []

        #단어랜덤문제(키값)에 해당하는 밸류값을 얻어 밸류값 리스트에 추가
        for i in en_question_list:
            en_values = word_dict[i]
            en_values_list.append(en_values)


        #문제의 답을 입력받을 리스트 생성
        etk_answer_list = []

        #랜덤문제리스트에서 문제와 입력받을 창 출력
        for k in en_question_list:
            etk_test_label = Label(etk_test_window, text=k)
            etk_test_label.pack()
            etk_test_answer = Entry(etk_test_window)
            etk_test_answer.pack()

            #엔트리 창에 입력된 답을 리스트에 추가
            #예시: 첫번째 문제의 엔트리 창에 입력될 답은 리스트의 첫번째로 넣는 것
            etk_answer_list.append(etk_test_answer)
        

        #완료 버튼
        #etk_answer_list를 매개변수로 etk_test_check에 넘겨줌
        en_finish_button = Button(etk_test_window, text="완료", command=lambda: etk_test_check(etk_answer_list))
        en_finish_button.pack()


        #정답을 확인하는 함수
        def etk_test_check(entry_answer):
            #입력받은 답을 answer_list에 최종적으로 할당
            answer_list = []
            for entry in entry_answer:
                answer = entry.get()
                answer_list.append(answer)

            #맞춘 정답 수를 할당할 변수
            correct_answer = 0

            #입력받은 값과 정답을 비교함
            for i in range(en_question_num):
                if en_values_list[i] == answer_list[i]:
                    correct_answer += 1

            #정답 결과를 알려줌
            messagebox.showinfo("결과", "{} 문제 중 {} 문제 맞췄습니다!".format(en_question_num, correct_answer))




    
    #입력받은 문제 수와 딕셔너리에 있는 단어의 갯수를 비교하는 함수
    def question_num_check():
        #입력받은 숫자 할당
        get_question_number = int(question_num.get())

        #딕셔너리에 있는 전체 아이템 갯수 할당
        dict_num = len(word_dict)

        #입력받은 수가 전체 단어 수 이하일 때
        if get_question_number <= dict_num:
            #뜻 -> 단어 테스트 버튼
            #kte_test 함수 실행
            kte_button = Button(test_window, text="뜻 -> 단어 맞추기", command=kte_test)
            kte_button.pack()

            #단어-> 뜻 테스트 버튼
            #etk_test 함수 실행
            etk_button = Button(test_window, text="단어 -> 뜻 맞추기", command=etk_test)
            etk_button.pack()

        else:
            messagebox.showinfo("안내", "입력된 문제 수가 단어장에 있는 단어 수보다 많습니다.")
            

    #문제 수 입력 버튼
    #question_num_check 함수 실행
    done_button = Button(test_window, text="입력", command=question_num_check)
    done_button.pack()



    

    

#***************************************************************************




main()