import sys


def try_get(func, *args):
    print(f'{func}を試みます')
    try:
        func(*args)
        print(f'{func}が実行されました')
    except Exception as e:
        print(e)
        print(type(e))
        print('実行中にエラーになりました')
        print('手動で継続する場合、手動で調整した後yを、中止する場合はn(y以外)を入力してください')
        flg = input('"y"or"n":')
        if flg == 'y':
            print('継続します')
            return
        else:
            print('中止します')
            sys.exit()


def test_func(a, b):
    result = a / b
    print('test_funcが実行されます')
    print(result)


if __name__ == '__main__':
    try_get(test_func, 6, 0)
    try_get(test_func, 6, 3)
