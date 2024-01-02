from robot.api.deco import keyword, not_keyword


@keyword('Login via user panel')
def login():
      print("decorator for robot keyword")


@not_keyword
def this_is_not_keyword():
    pass