import textwrap


def solution_1():
    answer = textwrap.dedent(
        """
        print(max([(int(input()),x) for x in range(8)])[1])
        """
    )
    print(answer)


def solution_2():
    answer = textwrap.dedent(
        """
        print(max(range(8), key=lambda _: input()))
        """
    )
    print(answer)


def solution_2():
    answer = textwrap.dedent(
        """
        print(max(range(8), key=lambda _: input()))
        """
    )
    print(answer)

