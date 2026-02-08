import pytest
from utils.BasePage import BasePage

class Test_check_locator_logic():
    
    @pytest.mark.unit
    def test_check_locator_logic_success(self,page):
        base_page=BasePage(page)
        base_page._locate_element(stratergy="Text",value="password")
    
    @pytest.mark.unit
    def test_check_locator_logic_name_missing(self,page):
        base_page=BasePage(page)
        base_page._locate_element(stratergy="Role",value="password")
    
    @pytest.mark.unit
    def test_check_locator_logic_failed(self,page):
        base_page=BasePage(page)
        base_page._locate_element(stratergy="Test",value="password")
