from app import multiply 

nums = [1, 2, 3, 4, 5]

def test_app(a=nums) -> int:
    assert multiply(a) == 120