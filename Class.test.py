import Class
import pytest

class Test_Point_Fall_in_retangle:
    
    @pytest.fixture()
    def point(self):
        return Class.Point()
    

    def test_fall_in_retangle_1(self, point):
        point.fall_in_retangle(["201.100.244.168", "139.3.227.118"], "18.12.93.94")

