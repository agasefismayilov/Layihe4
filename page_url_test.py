import wikipedia

def test_page_url():
    try:
        # "Python (programming language)" səhifəsini əldə et
        page = wikipedia.page("Python (programming language)")

        # Gözlənilən URL
        expected_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

        # URL-i yoxlamaq
        assert page.url == expected_url, f"Expected URL '{expected_url}', but got '{page.url}'"
        print("Python page URL is correct")

        # "Artificial intelligence" səhifəsini düzgün şəkildə əldə et
        page_ai = wikipedia.page("Artificial intelligence")  # Dəyişdirilən səhifə adı

        # Gözlənilən URL
        expected_url_ai = "https://en.wikipedia.org/wiki/Artificial_intelligence"
        
        # URL-i yoxlamaq
        assert page_ai.url == expected_url_ai, f"Expected URL '{expected_url_ai}', but got '{page_ai.url}'"
        print("Artificial intelligence page URL is correct")
    
    except wikipedia.exceptions.PageError as e:
        print(f"Page not found: {e}")

# Test funksiyasını işə salmaq
test_page_url()

#python -m pytest --html=report.html