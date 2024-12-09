import wikipedia

def test_page_id():
    try:
        # Verilmiş başlığa malik səhifəni əldə et
        title = "Python (programming language)"
        page = wikipedia.page(title)

        # API-dən qaytarılan səhifə ID-sini al
        actual_page_id = page.pageid

        # Gözlənilən səhifə ID-si
        # (Burada səhifənin ID-sini əvvəlcədən bilmək lazımdır. Misal üçün, bu, sabit dəyərdir.)
        expected_page_id = 23862  # Bu dəyəri Wikipedia səhifəsindən yoxlayın.

        # ID-ləri yoxla
        assert actual_page_id == expected_page_id, (
            f"Expected page ID '{expected_page_id}', but got '{actual_page_id}'"
        )

        print(f"Page ID for '{title}' is correct: {actual_page_id}")
    except wikipedia.exceptions.PageError as e:
        print(f"Page not found: {e}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Testi işə sal
test_page_id()
