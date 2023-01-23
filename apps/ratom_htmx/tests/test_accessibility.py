from django.shortcuts import reverse

import pytest
from axe_selenium_python import Axe
from selenium import webdriver


@pytest.mark.parametrize("page_name,page_url", [("homepage", reverse("home"))])
def test_accessibility_on_pages(
    live_server, django_db_serialized_rollback, settings, page_name, page_url
):
    """Run accessibility tests on pages of the site."""
    # Set STATICFILES_STORAGE to not use unique suffixes on static files, so they
    # can be found properly.
    settings.STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

    # Set driver to be a headless Firefox browser.
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    url = live_server.url + page_url
    driver.get(url)

    axe = Axe(driver)
    # Inject axe-core javascript into page.
    axe.inject()
    # Run axe accessibility checks.
    results = axe.run()

    # If there are violations, then write them to a file
    if len(results["violations"]) > 0:
        violations_filename = f"apps/ratom_htmx/tests/violations_{page_name}.json"
        axe.write_results(results["violations"], violations_filename)

    # Assert that there are no violations, or print out the titles
    # of each of the violations.
    violations_titles_list = [result["description"] for result in results["violations"]]
    violations_titles_str = "\n".join(
        [f"  {title}" for title in violations_titles_list]
    )
    error_msg = (
        f"\n\nAccessibility violations:\n{violations_titles_str}\n\n"
        f"Violation results have been written to {violations_filename}"
    )
    assert 0 == len(violations_titles_list), error_msg

    # Quit the browser.
    driver.quit()
