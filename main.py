class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show_question(self, number):
        print()
        print("-" * 40)
        print(f"[문제 {number}]")
        print(f"자음: {self.question}")

        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer


def create_default_quizzes():
    return [
        Quiz(
            "ㄱㅅㅊ",
            ["괴물", "기생충", "명량", "극한직업"],
            2
        ),
        Quiz(
            "ㅂㅈㄷㅅ",
            ["부산행", "베테랑", "범죄도시", "신과함께"],
            3
        ),
        Quiz(
            "ㄱㅎㅈㅇ",
            ["인터스텔라", "극한직업", "기생충", "해운대"],
            2
        ),
        Quiz(
            "ㅁㄹ",
            ["암살", "명량", "도둑들", "관상"],
            2
        ),
        Quiz(
            "ㅇㅂㅈㅅ",
            ["인셉션", "아바타", "어벤져스", "알라딘"],
            3
        )
    ]


def show_menu():
    print()
    print("=" * 40)
    print("      영화 제목 자음 퀴즈")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


def get_menu_choice():
    while True:
        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "":
            print("입력값이 없습니다. 1부터 5까지 입력하세요.")
            continue

        try:
            choice = int(choice)
        except ValueError:
            print("숫자만 입력하세요.")
            continue

        if choice < 1 or choice > 5:
            print("1부터 5까지의 숫자를 입력하세요.")
            continue

        return choice


def show_quiz_list(quizzes):
    print()
    print(f"등록된 퀴즈 목록: 총 {len(quizzes)}개")

    for index, quiz in enumerate(quizzes, start=1):
        print(f"{index}. {quiz.question}")


def main():
    quizzes = create_default_quizzes()

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            print("퀴즈 풀기 기능은 다음 단계에서 만듭니다.")
        elif choice == 2:
            print("퀴즈 추가 기능은 다음 단계에서 만듭니다.")
        elif choice == 3:
            show_quiz_list(quizzes)
        elif choice == 4:
            print("점수 확인 기능은 다음 단계에서 만듭니다.")
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()