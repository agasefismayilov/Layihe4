import pytest
import yaml
import io

# YAML məlumatlarını birbaşa daxil edirik
DEFAULT_CONFIG = """
wikipedia:
  base_url: "https://en.wikipedia.org/w/api.php"
  endpoint: "/w/api.php"
"""

# YAML məlumatını oxuyan fixture
@pytest.fixture(scope="session")
def config():
    # YAML məlumatını birbaşa daxil edilən `DEFAULT_CONFIG`-dən oxuyuruq
    return yaml.safe_load(io.StringIO(DEFAULT_CONFIG))

# Test verilənləri üçün fixture
@pytest.fixture(params=[
    {"input": "Pythn", "expected": "python"},
    {"input": "xyzabc123", "expected": None},
    {"input": "Python", "expected": None}
])
def suggest_data(request):
    return request.param

# Test funksiyası
def test_suggest(config, suggest_data):
    # Test verilənlərini fixture-dan götür
    input_data = suggest_data["input"]
    expected_output = suggest_data["expected"]

    # `base_url` və `endpoint`-dən URL qururuq
    base_url = config["wikipedia"]["base_url"]
    endpoint = config["wikipedia"]["endpoint"]
    
    # URL qurulması (endpoint artıq daxil olduğu üçün birləşdiririk)
    wikipedia_url = base_url + "?action=query&list=search&format=json&srsearch=" + input_data

    print(f"Testing Wikipedia URL: {wikipedia_url}")

    # Test üçün sadəcə giriş və gözlənilən nəticə ilə müqayisə aparırıq
    if input_data == "Pythn":
        actual_output = "Python"  # Simulyasiya edilmiş nəticə
    else:
        actual_output = None

    assert actual_output == expected_output, f"Expected {expected_output}, but got {actual_output}"

    #python -m pytest tests/ --html=report.html