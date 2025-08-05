from playwright.sync_api import sync_playwright
import time

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        page = context.new_page()
        page.goto("https://www.tiktok.com/login")
        print("Silakan login manual di Railway terminal...")

        input("Tekan Enter setelah login...")

        context.storage_state(path="state.json")
        print("Login berhasil disimpan.")

        # Ganti dengan akun target
        page.goto("https://www.tiktok.com/@edistvasli")
        print("Berhasil buka akun target.")

        try:
            page.click("text=Report")
            print("Tombol report diklik.")
        except:
            print("Tombol report tidak ditemukan.")

        time.sleep(3)
        browser.close()

if __name__ == "__main__":
    main()
