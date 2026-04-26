from processor import Processor

def main():
    print("Hello World")
    user = input("Masukkan username: ")
    password = input("Masukkan password: ")
    limit = input("Masukkan limit: ")
    processor = Processor(user, password)
    processor.login()
    processor.scrapping_ig(user, limit)


if __name__ == "__main__":
    main()