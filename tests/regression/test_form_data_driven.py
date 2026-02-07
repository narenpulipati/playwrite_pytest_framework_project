import pytest

@pytest.mark.parametrize(
    "name,email,address",
    [
        ("Narendra", "naren@test.com", "Hyderabad"),
        ("Rahul", "rahul@test.com", "Bangalore"),
        ("Anita", "anita@test.com", "Chennai"),
    ]
)
def test_form_with_multiple_data(form_pom, name, email, address):
    form_pom.open_form_page()
    form_pom.fill_name(name)
    form_pom.fill_email(email)
    form_pom.fill_address(address)
    form_pom.submit_form()

