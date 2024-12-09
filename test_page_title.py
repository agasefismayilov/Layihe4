import pytest
import wikipedia

# Keçərli bir Vikipediya səhifəsi fixture
@pytest.fixture
def valid_page():
    """Fixture: Keçərli bir Vikipediya səhifəsi."""
    return wikipedia.page("NASA")

# Keçərsiz bir Vikipediya səhifəsi fixture
@pytest.fixture
def invalid_page():
    """Fixture: Keçərsiz bir Vikipediya səhifəsi."""
    return "ThisPageDoesNotExist12345"

# Keçərli səhifənin başlığını yoxlayan test
def test_page_title_valid(valid_page):
    """
    Test: Keçərli bir Vikipediya səhifəsinin başlığını yoxla.
    """
    assert valid_page.title == "NASA", f"Expected 'NASA', but got {valid_page.title}"

# Keçərsiz səhifə üçün səhv mesajını yoxlayan test
def test_page_title_invalid(invalid_page):
    """
    Test: Keçərsiz bir səhifə üçün uyğun xəta mesajını yoxla.
    """
    with pytest.raises(wikipedia.exceptions.PageError):
        wikipedia.page(invalid_page)

# Ayırdetmə səhifəsi üçün səhv mesajını yoxlayan test
def test_page_title_disambiguation():
    """
    Test: Ayırdetmə səhifəsi üçün uyğun xəta mesajını yoxla.
    """
    with pytest.raises(wikipedia.exceptions.DisambiguationError):
        wikipedia.page("Mercury")  # "Mercury" ayırdetmə səhifəsidir.

 #python -m pytest tests/ --html=report.html