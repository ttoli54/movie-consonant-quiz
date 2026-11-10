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
        Quiz("ㄱㅅㅊ", ["괴물", "기생충", "명량", "극한직업"], 2),
        Quiz("ㅂㅈㄷㅅ", ["부산행", "베테랑", "범죄도시", "신과함께"], 3),
        Quiz("ㄱㅎㅈㅇ", ["인터스텔라", "극한직업", "기생충", "해운대"], 2),
        Quiz("ㅁㄹ", ["암살", "명량", "도둑들", "관상"], 2),
        Quiz("ㅇㅂㅈㅅ", ["인셉션", "아바타", "어벤져스", "알라딘"], 3)
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


def get_number(prompt, min_value, max_value):
    while True:
        value = input(prompt).strip()

        if value == "":
            print("입력값이 없습니다.")
            continue

        try:
            number = int(value)
        except ValueError:
            print("숫자만 입력하세요.")
            continue

        if number < min_value or number > max_value:
            print(f"{min_value}부터 {max_value}까지 입력하세요.")
            continue

        return number


def get_menu_choice():
    return get_number("메뉴를 선택하세요: ", 1, 5)


def get_answer():
    while True:
        value = input("정답 번호를 입력하세요 (1-4, q: 나가기): ").strip().lower()

        if value == "q":
            return None

        if value == "":
            print("입력값이 없습니다.")
            continue

        try:
            answer = int(value)
        except ValueError:
            print("1부터 4까지의 숫자 또는 q를 입력하세요.")
            continue

        if answer < 1 or answer > 4:
            print("1부터 4까지의 숫자를 입력하세요.")
            continue

        return answer


def get_text(prompt):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("빈칸으로 입력할 수 없습니다.")
            continue

        return text


def play_quiz(quizzes):
    if len(quizzes) == 0:
        print("등록된 퀴즈가 없습니다.")
        return None

    score = 0

    print()
    print(f"퀴즈를 시작합니다! 총 {len(quizzes)}문제입니다.")

    for number, quiz in enumerate(quizzes, start=1):
        quiz.show_question(number)
        user_answer = get_answer()

        if user_answer is None:
            print("퀴즈를 종료하고 메뉴로 돌아갑니다.")
            return None

        if quiz.is_correct(user_answer):
            print("정답입니다!")
            score += 1
        else:
            correct_choice = quiz.choices[quiz.answer - 1]
            print(f"오답입니다. 정답은 {quiz.answer}번 {correct_choice}입니다.")

    print()
    print("=" * 40)
    print(f"결과: {len(quizzes)}문제 중 {score}문제 정답")
    print("=" * 40)

    return score


def add_quiz(quizzes):
    print()
    print("새로운 퀴즈를 추가합니다.")

    question = get_text("자음을 입력하세요: ")

    choices = []

    for number in range(1, 5):
        choice = get_text(f"선택지 {number}를 입력하세요: ")
        choices.append(choice)

    answer = get_number("정답 번호를 입력하세요 (1-4): ", 1, 4)

    new_quiz = Quiz(question, choices, answer)
    quizzes.append(new_quiz)

    print("퀴즈가 추가되었습니다!")


def show_quiz_list(quizzes):
    print()
    print(f"등록된 퀴즈 목록: 총 {len(quizzes)}개")

    for index, quiz in enumerate(quizzes, start=1):
        print(f"{index}. {quiz.question}")


def show_score(best_score):
    print()
    if best_score == 0:
        print("아직 퀴즈를 풀지 않았습니다.")
    else:
        print(f"최고 정답 수: {best_score}개")


def main():
    quizzes = create_default_quizzes()
    best_score = 0

    try:
        while True:
            show_menu()
            choice = get_menu_choice()

            if choice == 1:
                score = play_quiz(quizzes)

                if score is not None and score > best_score:
                    best_score = score
                    print("새로운 최고 점수입니다!")

            elif choice == 2:
                add_quiz(quizzes)

            elif choice == 3:
                show_quiz_list(quizzes)

            elif choice == 4:
                show_score(best_score)

            elif choice == 5:
                print("프로그램을 종료합니다.")
                break

    except (KeyboardInterrupt, EOFError):
        print()
        print("프로그램을 안전하게 종료합니다.")


if __name__ == "__main__":
    main()
