class ContactPage:
    def __init__(self, page):
        self.page = page
        self.iframe_locator = page.locator("iframe")
        self.content_iframe_locator = page.locator("#content iframe")

    def navigate(self, url):
        self.page.goto(url)

    def fill_first_name_contact_form(self, first_name):
        self.iframe_locator.first.content_frame.get_by_label("First").fill(first_name)

    def fill_last_name_contact_form(self, last_name):
        self.iframe_locator.first.content_frame.get_by_label("Last").fill(last_name)

    def fill_email_contact_form(self, email):
        self.iframe_locator.first.content_frame.get_by_label("Email *").fill(email)
       
    def fill_comment_contact_form(self, comment):
            self.content_iframe_locator.first.content_frame.get_by_label("Comment or Message *").fill(comment)

    def submit_contact_form(self):
        self.iframe_locator.first.content_frame.get_by_role("button", name="Submit").click()

    def thank_you_page_content_area(self):
        return self.page.locator("#content")
    
    def comment_submittion_message(self):
        return "Your details have been submitted."
        
    def form_vallidation_error(self):
        return "Enter a value for this field."
    
    def validation_form_error_message(self, err_msg_locator):
        return self.iframe_locator.first.content_frame.locator(err_msg_locator)
    
    def validation_error_name_field(self):
        return self.validation_form_error_message("#error-Name")
    
    def validation_error_email_field(self):
        return self.validation_form_error_message("#error-Email")
    
    def validation_error_comment_field(self):
        return self.validation_form_error_message("#error-MultiLine")
    
    # def validation_error_comment_field(self):
    #     return self.validation_form_error_message("#error-MultiLine")
    #     page.locator("#content")

