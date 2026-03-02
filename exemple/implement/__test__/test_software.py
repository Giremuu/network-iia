# An example from the professor B.ROSE
from implement.software import Software
import pytest

@pytest.fixture()
def create_software():
    return Software()

class TestSoftware:

    @pytest.mark.parametrize(
        "data, expected_output",
            [
                ("Bonjour", "message => Bonjour"),
                ("Bye", "message => Bye")
            ]    
        )
    def test_display_message(self,data,expected_output,create_software):
        output = create_software.display_message(data)
        assert output == expected_output
