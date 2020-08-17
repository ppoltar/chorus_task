import pytest, logging, time
from selenium.webdriver.common.keys import Keys


'''Bugs:
1 - Setting icon  ---> Recording Setting doesn't allow any action, 
    this is bug since there is a functionality that is not available and it's needed if any changes to the recording setting is required.
2 - View transcript is not identical to the video recording. 
    If the customer will relay on the transcript then it can cause potential problems because not all if the content is indicated. 
    Also the transcript does not properly indicate who is the entity saying the content
'''

@pytest.mark.usefixtures("chrome_driver")
class TestPage():

    @pytest.mark.open_url
    def test_open_url(self, url_path, title_name, certification):
        logging.info(f"Open test site : {url_path['login_page']}")
        self.driver.get(url_path['test_page'])
        assert self.driver.title == title_name["login_page"]
        assert self.driver.current_url == url_path['login_page']

        #not good way to find email button but I had problem with this and with class "login-button" it working
        email_button = self.driver.find_elements_by_class_name("login-button")[-1]
        email_button.click()
        email_input = self.driver.find_elements_by_id("chorus-input")[0]
        email_input.send_keys(certification["Username"])
        password_input = self.driver.find_elements_by_id("chorus-input")[1]
        password_input.send_keys(certification["Password"])
        log_in_button = self.driver.find_element_by_class_name("mat-button-wrapper")
        log_in_button.click()
        time.sleep(3)
        assert self.driver.title == title_name["test_page"]
        assert self.driver.current_url == url_path['test_page']
        time.sleep(5)
        logging.info(f"Test site : {url_path['login_page']} opened")

    @pytest.mark.navigation_items_name
    @pytest.mark.parametrize("navigation_bar_names", [(['Comments', 'Scorecards', 'Snippets'])])
    def test_navigation_items_name(self, navigation_bar_names):
        logging.info(f"Testing navigation bar items name: {navigation_bar_names}")
        navigation_items = self.driver.find_element_by_class_name("buttons.flex.align-items-baseline").text.split("\n")
        assert  navigation_bar_names == [x for x in navigation_items if not any(c.isdigit() for c in x)]

    @pytest.mark.setting_button
    def test_setting_button(self):
        logging.info(f"Testing setting button")
        setting_button = self.driver.find_element_by_class_name("icon.an.an-gear.size-16")
        setting_button.click()
        recording_setting_button = self.driver.find_element_by_class_name("mat-menu-content.ng-tns-c222-5")
        assert recording_setting_button.click() != None , "Bug, need to be with setting options to give option to set the right setting and not None"


    # I dont finish this function, dont have time ...:(
    @pytest.mark.comments
    @pytest.mark.parametrize("tag_name, text_box_text", [('button', 'This is Pashas test')])
    def test_comments(self, tag_name, text_box_text):
        logging.info(f"Testing comments bar")
        comments_button = self.driver.find_element_by_class_name("mat-button.mat-primary")
        assert comments_button.tag_name == tag_name
        with pytest.raises(Exception) as e_info:
            assert comments_button.tag_name == 'button 123'
        logging.info(f"Test that fail on purpose, to check that it is not false pass: {e_info.value}")
        comments_button.click()

        logging.info(f"Testing add new comment")
        number_of_comment_before = len(self.driver.find_elements_by_class_name("comment-block"))
        comments_text_box = self.driver.find_element_by_id("mat-input-1")
        comments_text_box.send_keys(text_box_text)
        comments_button = self.driver.find_element_by_class_name("mat-flat-button.mat-primary")
        comments_button.click()
        time.sleep(3)
        number_of_comment_after = len(self.driver.find_elements_by_class_name("comment-block"))
        assert number_of_comment_after - number_of_comment_before  == 1

