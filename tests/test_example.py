import pytest, os, sys, re,json
from faker import Faker
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))
from playwright.sync_api import Page, expect
from models.contact_page import ContactPage
from models.nav_bar import NavBar
with open('tests/../resources/config/test_config.json', 'r') as file:
    config = json.load(file)
url = config['QA']['url']
fake = Faker()
form_vallidation_error = 'Enter a value for this field.'
def test_verify_the_page_comes_up_properly(page: Page):
    contact_page = ContactPage(page)
    contact_page.navigate(url)
    expect(page).to_have_title(re.compile("Giant Rocketship turbocharges MSP growth by automating helpdesk management in Autotask."))
    

def test_navigate_to_the_contact_us_form_via_the_top_menu(page: Page):
    contact_page = ContactPage(page)
    nav_bar = NavBar(page)
    contact_page.navigate(url)

    nav_bar.navigate_to_contact_us_page()
    expect(page).to_have_title(re.compile("Contact › Giant Rocketship, Inc."))
    expect(page.locator("h1")).to_contain_text("Contact")
    expect(page.locator("#content")).to_contain_text("Have a question about features, trials, pricing, a demo, or anything else?")

def form_submitted_with_name_only_should_fail(page: Page):
    nav_bar = NavBar(page)
    contact_page = ContactPage(page)
    contact_page.navigate(url)
    nav_bar.navigate_to_contact_us_page()
    contact_page.fill_first_name_contact_form("first_name")
    contact_page.submit_contact_form()
    
    expect(contact_page.validation_error_name_field()).to_contain_text(form_vallidation_error)
    expect(contact_page.validation_error_email_field()).to_contain_text(form_vallidation_error)
    expect(contact_page.validation_error_comment_field()).to_contain_text(form_vallidation_error)
    page.reload()
    
def form_submitted_with_name_and_email_only_should_fail(page: Page):
    nav_bar = NavBar(page)
    contact_page = ContactPage(page)
    contact_page.navigate(url)
    nav_bar.navigate_to_contact_us_page()
    contact_page.fill_first_name_contact_form(fake.first_name())
    contact_page.fill_last_name_contact_form(fake.last_name())
    contact_page.fill_email_contact_form(f"{fake.first_name()}@test.com")
    contact_page.submit_contact_form()
    expect(contact_page.validation_error_comment_field()).to_contain_text(form_vallidation_error)
    page.reload()
    
def form_submitted_with_name_comment_and_email_should_succeed(page: Page):
    nav_bar = NavBar(page)
    contact_page = ContactPage(page)
    contact_page.navigate(url)
    nav_bar.navigate_to_contact_us_page()
    contact_page.fill_first_name_contact_form(fake.name())
    contact_page.fill_last_name_contact_form(fake.name())
    contact_page.fill_email_contact_form(f"{fake.first_name()}@test.com")
    contact_page.fill_comment_contact_form(fake.sentence())
    contact_page.submit_contact_form()
    expect(page.locator("#content")).to_contain_text(contact_page.comment_submittion_message())
    page.wait_for_url(f'{url}/thank-you/')
