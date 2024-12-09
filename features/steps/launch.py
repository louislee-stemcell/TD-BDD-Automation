from behave import given, then
from features.pages.NavigatorBar import NavigatorBar

@given("I click the hamburger icon")
def step_impl(context):
    context.navigator_bar = NavigatorBar(context.driver)
    context.navigator_bar.click_hamburger_icon()

@then("I verify the Run Control button is displayed")
def step_impl(context):
    assert context.navigator_bar.is_run_control_screen_button_displayed(), "Run Control Screen is not displayed"
