from  bank import cherry
import pytest

def main():
    value()
    test_h()
    test_hello()
    test_remining()



def value():
    with pytest.raises(TypeError):
        cherry(1242523)

def test_h():
    assert cherry("Howdy") == "20$"


def test_hello():
    assert cherry("Hello") == "0$"



def test_remining():
    assert cherry("Waskjnaso nasdfo aslkd i?") == "100$"

# blah blah blah
# blah blah blah
# blah blah blah



if __name__ == "__main__":
    main()
# blah blah blah
# blah blah blah
# blah blah blah
# blah blah blah
# blah blah blah
