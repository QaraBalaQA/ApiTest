import ApiMethod
def test_checkformat():
    jsonformat = 'application/json; charset=utf-8'
    ApiMethod.CheckFormat()
    assert (ApiMethod.CheckFormat() == jsonformat)