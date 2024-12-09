import wikipedia

def test_suggest(config, suggest_data):
    # Test verilənlərini fixture-dan götür
    input_data = suggest_data["input"]
    expected_output = suggest_data["expected"]

    # Test edilən saytın URL-i (yalnız göstərmək üçün istifadə edilə bilər)
    wikipedia_url = config["wikipedia"]["base_url"]
    print(f"Testing Wikipedia at {wikipedia_url}")

    # Suggest metodunu yoxlayırıq
    result = wikipedia.suggest(input_data)
    assert result == expected_output, f"Expected {expected_output}, got {result}"
