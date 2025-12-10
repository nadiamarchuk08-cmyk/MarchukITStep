import sqlite3
import requests
from bs4 import BeautifulSoup

class DatabaseObj:
    def __init__(self):
        self.connection = sqlite3.connect("database.sl3")
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS sites (url TEXT);")
        self.connection.commit()

    def add_site(self, url_site):
        self.cur.execute("INSERT INTO sites (url) VALUES (?);", (url_site,))
        self.connection.commit()

    def get_sites(self):
        self.cur.execute("SELECT url FROM sites;")
        return self.cur.fetchall()

    def clear_table(self):
        self.cur.execute("DELETE FROM sites;")
        self.connection.commit()


class ParserObj:
    def parse(self, url, search_text):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, features="html.parser")

                paragraphs = soup.find_all("p")

                for p in paragraphs:
                    if search_text.lower() in p.text.lower():
                        return p.text.strip()

                return "Інформацію не знайдено."
            return "Сайт не відповідає."
        except:
            return "Помилка з'єднання."

class InterfaceObj:
    def __init__(self, db, parser):
        self.db = db
        self.parser = parser

    def start_search(self):
        sites_list = self.db.get_sites()
        print("\nПрограма для пошуку інформації про Білу Церкву")

        print("\n--- ДОСТУПНІ САЙТИ ---")
        for index, site_row in enumerate(sites_list):
            print(f"{index + 1}. {site_row[0]}")

        try:
            choice = input("\nВведіть номер сайту: ")
            site_number = int(choice)
            if 1 <= site_number <= len(sites_list):
                selected_url = sites_list[site_number - 1][0]
                word = input("Що шукаємо: ")
                print(f"\nОбробка запиту...")
                result = self.parser.parse(selected_url, word)

                print("-" * 50)
                print(f"РЕЗУЛЬТАТ:\n{result}")
                print("-" * 50)
            else:
                print("Помилка: Неправильний номер.")

        except ValueError:
            print("Помилка: Потрібно ввести число.")
def run():
    db = DatabaseObj()
    parser = ParserObj()
    ui = InterfaceObj(db, parser)

    db.clear_table()
    db.add_site("https://bc-rada.gov.ua/node")
    db.add_site("https://landmarks.in.ua/oblast/kyivska/bila-tserkva")

    ui.start_search()

if __name__ == "__main__":
    run()