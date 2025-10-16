import allure
from allure import attachment_type
def test_attachments():
    allure.attach("Text content", name="Text", attachment_type=allure.attachment_type.TEXT)
