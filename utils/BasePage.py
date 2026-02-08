from utils.logger import Logger

log=Logger().get_logger(__name__)

class BasePage:
    def __init__(self,page):
        self.page=page

    def _locate_element(self,stratergy: str,value: str, name: str=None):
        stratergy= stratergy.lower()
        try:
            if stratergy == "role":
                element=self.page.get_by_role(value, name=name)

            elif stratergy == "testid":
                element=self.page.get_by_test_id(value)

            elif stratergy == "text":
                element=self.page.get_by_text(value)

            elif stratergy == "css":
                element=self.page.locator(value)

            elif stratergy == "xpath":
                element=self.page.locator(value)

            else:
                raise ValueError(" Unsupported locator stratergy: %s",stratergy)

            return element

        except Exception as e:
            log.info("Unable to locate your element !! check the DOM again \n execption message: %s",e)
