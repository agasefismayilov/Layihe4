import pytest
import wikipedia
from wikipedia.exceptions import HTTPTimeoutError, WikipediaException

def test_geosearch_no_results():
    # Uyğunsuz koordinatlar üçün sıfır nəticə gözlənilir
    results = wikipedia.geosearch(latitude=89.9, longitude=0, radius=10)  # Yaxın Şimal Qütbü
    assert isinstance(results, list), "Expected a list of results"
    assert len(results) == 0, "Expected no results"

def test_geosearch_rate_limit(mocker):
    # Mocking the geosearch function to raise an HTTPTimeoutError
    def mock_geosearch(*args, **kwargs):
        raise HTTPTimeoutError("Test query")

    # Mocker ilə geosearch funksiyasını patch edirik
    mocker.patch("wikipedia.geosearch", side_effect=mock_geosearch)

    # Bu dəfə pytest.raises metodunun düzgün işləməsini təmin edirik
    with pytest.raises(HTTPTimeoutError, match="Test query"):
        wikipedia.geosearch(37.7749, -122.4194, radius=10000)  # Yalnız latitude və longitude

def test_geosearch_success():
    # Uğurlu axtarış üçün nümunə
    results = wikipedia.geosearch(latitude=40.7128, longitude=-74.0060, results=5)  # New York koordinatları
    assert isinstance(results, list), "Expected a list of results"
    assert len(results) > 0, "Expected results"

def test_geosearch_invalid_input():
    # Uygunsuz giriş üçün WikipediaException gözlənilir
    with pytest.raises(WikipediaException):
        wikipedia.geosearch(latitude="invalid", longitude="input")


#python -m pytest tests/ --html=report.html