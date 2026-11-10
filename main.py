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


def main():
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            print("퀴즈 풀기 기능은 다음 단계에서 만듭니다.")
        elif choice == 2:
            print("퀴즈 추가 기능은 다음 단계에서 만듭니다.")
        elif choice == 3:
            print("퀴즈 목록 기능은 다음 단계에서 만듭니다.")
        elif choice == 4:
            print("점수 확인 기능은 다음 단계에서 만듭니다.")
        elif choice == 5:
            print("프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()